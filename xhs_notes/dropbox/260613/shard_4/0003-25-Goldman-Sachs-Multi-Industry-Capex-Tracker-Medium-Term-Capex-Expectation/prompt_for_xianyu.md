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
## Multi-Industry Capex Tracker

## Medium Term Capex Expectations Continue to Improve

We reflect on the latest trends in a core piece of our Multis toolkit – the Capex Tracker – where we conduct a bottom-up analysis of capex expectations, capturing €3.4tn of capex and c.4k companies across 34 different end and sub-end markets.

## Daniela Costa

+44 20 7774-8354

daniela.costa@gs.com

GS International

## Aditya Agarwal

+1 212 934-7448

aditya.a.agarwal@gs.com

GS India SPL

## Ines Lefranc

+44 20 7051-8710

ines.lefranc@gs.com

GS International

## Christian Hinderaker, CFA

+44 20 7774-7366

christian.hinderaker@gs.com

GS International

## Meihan Yang

+44 20 7051-6601

meihan.x.yang@gs.com

GS International

## Ope Otaniyi

+44 20 7051 6955

ope.otaniyi@gs.com

GS International

## Hollie Cooper

+44 20 7051-0956

hollie.cooper@gs.com

GS International

## Susmita Saha

+1 332 245-7701

susmita.saha@gs.com

GS India SPL

## Aayush Kandpal

+1 332 245-6142

aayush.kandpal@gs.com

GS India SPL

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

Table of Contents

<table><tr><td>Medium-term capex forecasts revised higher again, driven by tech and utilities</td><td>6</td></tr><tr><td>GS Capex Tracker by End Market</td><td>13</td></tr><tr><td>Appendix: Stock OSG vs Weighted Capex (&gt;50% RSQ)</td><td>59</td></tr><tr><td>Disclosure Appendix</td><td>61</td></tr></table>

## Our Capex Tracker has seen sizable upgrades in medium-term forecasts (2026E capex forecasts c.2pp up since our last update in March), pointing to a robust investment environment driven primarily by the technology and utilities sectors.

Through our bottom-up analysis capturing €3.4tn of capex across approximately 4,000 companies and 34 different end and sub-end markets, we expect 2026 capex to end well above historical trend growth (c.13% vs historical median of c.2%), while 2027 figures are also increasing (now at 12% vs 8% at the start of the year). We continue to see a highly favorable capex environment in the medium term in Tech, particularly in Datacenters (Buy on Schneider (on CL)) and Semiconductors (Buy VAT), as well as Utilities, specifically in power grids (Buy on Prysmian and Nexans).

In this update, we observe robust and positive moves wherein Capex CAGR growth across 2025-29E at c.9%, led by Datacenters at c.35% (a 6.5 pp increase in May-26 vs. Mar-26), Semiconductors at 23% (a +6.8 pp delta), and Oil and Gas at c.4% (a+3.5pp delta). Conversely, the most significant downgrades and cuts in medium-term capex expectations have occurred in sectors such as Chemicals, which saw a decline of -4.1 pp, and Construction Equipment, which fell by -4.0 pp. In absolute terms, Airports is projected to experience a negative absolute CAGR of -4% over the 2025–29E period.

We also highlight an increasing concentration of growth in a few structural areas related to Datacenters, Semis and Utilities, which represent c.39% of total capex in 2026E, compared to only 22% just four years ago in 2022. While these structural growth areas continue to anchor the aggregate outlook, we remain mindful of cyclical variations across other end markets. Specifically, in sectors like Telecom and Consumer, key investment indicators (such as capex-to-sales and capacity utilization) are currently running below their historical medians, signaling potential cyclical headwinds compared to the structural strength seen in tech and utilities.

## Our toolkit for picking stocks in multi-industry: Barometers, Screens and Capex Tracker

![](images/71723d962e2d28f9ee86cd385c1df618d8b33229c9dbf60a41277d9dbff4bdc4.jpg)

## BAROMETERS (short term)

c.1000 high frequency indicators

<table><tr><td colspan="2">Stock (61) data points</td><td>Region</td><td>52 2006</td><td>2Q 2006</td><td>3Q 2006</td><td>4Q 2006</td><td>1Q 2007</td><td>2Q 2007</td><td>3Q 2007</td></tr><tr><td>Germany Heavy Truck Sales</td><td>Europe</td><td></td><td>-25.6%</td><td>-53.4%</td><td>-10.3%</td><td>8.5%</td><td>9.7%</td><td>41.5%</td><td>10.2%</td></tr><tr><td>France Heavy Truck Sales</td><td>Europe</td><td></td><td>-28.6%</td><td>-52.4%</td><td>-8.1%</td><td>-3.0%</td><td>17.5%</td><td>55.5%</td><td>-1.1%</td></tr><tr><td>Italy Heavy Truck Sales</td><td>Europe</td><td></td><td>-11.1%</td><td>-52.4%</td><td>30.3%</td><td>11.1%</td><td>33.4%</td><td>121.7%</td><td>5.0%</td></tr><tr><td>Spain Heavy Truck Sales</td><td>Europe</td><td></td><td>-17.1%</td><td>-50.5%</td><td>5.1%</td><td>1.7%</td><td>32.4%</td><td>90.1%</td><td>8.0%</td></tr><tr><td>UK Heavy Truck Sales</td><td>Europe</td><td></td><td>-20.8%</td><td>-75.8%</td><td>-13.9%</td><td>-17.3%</td><td>-2.1%</td><td>155.8%</td><td>1.4%</td></tr><tr><td>Europe Heavy Truck Sales</td><td>Europe</td><td></td><td>-27.8%</td><td>-59.5%</td><td>-6.5%</td><td>-1.8%</td><td>18.0%</td><td>73.9%</td><td>13.8%</td></tr><tr><td>Germany Light Truck Sales</td><td>Europe</td><td></td><td>-10.7%</td><td>-38.7%</td><td>-2.9%</td><td>7.6%</td><td>8.2%</td><td>45.9%</td><td>-14.2%</td></tr><tr><td>France Light Truck Sales</td><td>Europe</td><td></td><td>-23.7%</td><td>-56.3%</td><td>5.5%</td><td>3.4%</td><td>41.9%</td><td>164.0%</td><td>-17.4%</td></tr><tr><td>Italy Light Truck Sales</td><td>Europe</td><td></td><td>-25.4%</td><td>-53.7%</td><td>12.3%</td><td>3.0%</td><td>30.2%</td><td>342.7%</td><td>-13.2%</td></tr><tr><td>Spain Light Truck Sales</td><td>Europe</td><td></td><td>31.1%</td><td>-56.5%</td><td>-4.8%</td><td>-3.5%</td><td>39.9%</td><td>285.5%</td><td>-30.5%</td></tr><tr><td>UK Light Truck Sales</td><td>Europe</td><td></td><td>-18.5%</td><td>-61.7%</td><td>5.8%</td><td>7.5%</td><td>36.5%</td><td>367.5%</td><td>-4.4%</td></tr><tr><td>Europe Light Truck Sales</td><td>Europe</td><td></td><td>-24.4%</td><td>-63.0%</td><td>-0.5%</td><td>-0.0%</td><td>31.7%</td><td>104.3%</td><td>-12.7%</td></tr><tr><td>Germany Medium Truck Sales</td><td>Europe</td><td></td><td>-22.9%</td><td>-70.1%</td><td>-7.9%</td><td>2.0%</td><td>8.9%</td><td>35.5%</td><td>3.7%</td></tr><tr><td>France Medium Truck Sales</td><td>Europe</td><td></td><td>-25.1%</td><td>-51.1%</td><td>-2.6%</td><td>-1.8%</td><td>20.0%</td><td>58.5%</td><td>-3.6%</td></tr><tr><td>Italy Medium Truck Sales</td><td>Europe</td><td></td><td>-11.4%</td><td>-51.0%</td><td>28.7%</td><td>0.0%</td><td>30.7%</td><td>52.5%</td><td>-1.1%</td></tr><tr><td>Spain Medium Truck Sales</td><td>Europe</td><td></td><td>-19.3%</td><td>-64.4%</td><td>-4.3%</td><td>8.2%</td><td>21.4%</td><td>75.9%</td><td>-10.7%</td></tr><tr><td>UK Medium Truck Sales</td><td>Europe</td><td></td><td>-17.5%</td><td>-74.1%</td><td>-8.4%</td><td>-16.1%</td><td>-5.0%</td><td>135.6%</td><td>-7.1%</td></tr><tr><td>Europe Medium Truck Sales</td><td>Europe</td><td></td><td>-28.3%</td><td>-67.2%</td><td>-4.6%</td><td>-2.6%</td><td>12.6%</td><td>64.1%</td><td>7.7%</td></tr><tr><td>Eurodollar Truck Traffic (Nyto)</td><td>Europe</td><td></td><td>-11.8%</td><td>-24.8%</td><td>-3.3%</td><td>4.5%</td><td>-21.0%</td><td>24.7%</td><td>-5.0%</td></tr><tr><td>Michelin North America Truck Tire (DE Estimates) (Nyto)</td><td>Europe</td><td></td><td>-20.3%</td><td>-58.7%</td><td>-8.0%</td><td>11.3%</td><td>22.2%</td><td>152.2%</td><td>13.3%</td></tr><tr><td>Michelin Europe Truck Tire Replacement (Nyto)</td><td>Europe</td><td></td><td>-0.3%</td><td>-33.7%</td><td>-0.7%</td><td>1.2%</td><td>17.0%</td><td>38.7%</td><td>0.0%</td></tr><tr><td>German Truck Tail Mileage TIDEA Averaged Worthy</td><td>Europe</td><td></td><td>111.8</td><td>102.3</td><td>111.0</td><td>110.4</td><td>115.3</td><td>118.0</td><td>114.0</td></tr><tr><td>North America Heavy Truck Sales</td><td>Europe</td><td></td><td>-25.8%</td><td>-61.0%</td><td>-31.7%</td><td>-3.7%</td><td>17.9%</td><td>65.8%</td><td>10.7%</td></tr><tr><td>Casa Truck Limited Index</td><td>USA</td><td></td><td>138.7</td><td>106.1</td><td>131.8</td><td>138.5</td><td>141.2</td><td>146.5</td><td>246.2</td></tr><tr><td>US PPI Heavy Truck Freight Manufacturing</td><td>USA</td><td></td><td>0.06%</td><td>0.06%</td><td>0.39%</td><td>1.12%</td><td>0.70%</td><td>1.12%</td><td>0.36%</td></tr><tr><td>Trucking Equipment (Nyto)</td><td>USA</td><td></td><td>-0.1%</td><td>-6.70%</td><td>-6.73%</td><td>-3.79%</td><td>-2.70%</td><td>3.30%</td><td>3.83%</td></tr><tr><td>Active Truck Utilization (%)</td><td>USA</td><td></td><td>83.17%</td><td>84.52%</td><td>90.35%</td><td>87.42%</td><td>99.20%</td><td>99.96%</td><td>100.00%</td></tr><tr><td>ATX Truck Turnage Index (NA, Nyto)</td><td>USA</td><td></td><td>2.9%</td><td>-9.8%</td><td>-0.0%</td><td>-2.0%</td><td>-3.9%</td><td>3.4%</td><td>-3.7%</td></tr><tr><td>The Case Shipment Index (Nyto)</td><td>USA</td><td></td><td>-8.7%</td><td>-71.4%</td><td>-7.5%</td><td>3.5%</td><td>7.6%</td><td>29.9%</td><td>14.0%</td></tr><tr><td>US intermodal volumes 12w RA (Nyto)</td><td>USA</td><td></td><td>-23.3%</td><td>-24.8%</td><td>4.6%</td><td>16.3%</td><td>18.5%</td><td>29.7%</td><td>8.7%</td></tr><tr><td>DAIT leads-to-truck ratio (Nyto)</td><td>USA</td><td></td><td>232.3%</td><td>219.7%</td><td>505.3%</td><td>455.3%</td><td>589.3%</td><td>540.6%</td><td>813.5%</td></tr><tr><td>Michelin North America Truck Tire (DE Estimates) (Nyto)</td><td>USA</td><td></td><td>-22.2%</td><td>-88.7%</td><td>-20.1%</td><td>-1.0%</td><td>-12.2%</td><td>158.0%</td><td>16.1%</td></tr><tr><td>Michelin North America Truck Tire Replacement Index (Nyto)</td><td>USA</td><td></td><td>-3.0%</td><td>-13.3%</td><td>0.3%</td><td>12.2%</td><td>11.7%</td><td>55.5%</td><td>15.5%</td></tr><tr><td>NA Class B Backing (Nyto)</td><td>USA</td><td></td><td>59.1%</td><td>-87.4%</td><td>-37.0%</td><td>18.7%</td><td>193.2%</td><td>174.5%</td><td>195.1%</td></tr><tr><td>NA Class B Solid (Nyto)</td><td>USA</td><td></td><td>-31.2%</td><td>-75.2%</td><td>-33.7%</td><td>-3.7%</td><td>14.5%</td><td>337.9%</td><td>4.8%</td></tr></table>

![](images/faefd3f4dafb036e7b0e335dc4236b161181a3bba767c11efe7fbde0545b8703.jpg)  
GS Barometer

![](images/54e56c25f7da542489b4c918bddc4497f3ba2c70e53353e6dd6792f31084d56d.jpg)

<details>
<summary>line chart</summary>

| Quarter | Company X OSG | Company X Barometer |
| --- | --- | --- |
| 2Q 2009 | -25% | -25% |
| 4Q 2009 | 15% | 20% |
| 1Q 2010 | 20% | 25% |
| 2Q 2010 | 15% | 20% |
| 3Q 2010 | 10% | 15% |
| 4Q 2010 | 5% | 10% |
| 1Q 2011 | 0% | 5% |
| 2Q 2011 | -5% | -5% |
| 3Q 2011 | -10% | -5% |
| 4Q 2011 | -5% | 0% |
| 1Q 2012 | 0% | 5% |
| 2Q 2012 | 5% | 10% |
| 3Q 2012 | 10% | 15% |
| 4Q 2012 | 5% | 10% |
| 1Q 2013 | 0% | 5% |
| 2Q 2013 | -5% | -5% |
| 3Q 2013 | -10% | -5% |
| 4Q 2013 | -5% | 0% |
| 1Q 2014 | 0% | 5% |
| 2Q 2014 | 5% | 10% |
| 3Q 2014 | 10% | 15% |
| 4Q 2014 | 5% | 10% |
| 1Q 2015 | 0% | 5% |
| 2Q 2015 | -5% | -5% |
| 3Q 2015 | -10% | -5% |
| 4Q 2015 | -5% | 0% |
| 1Q 2016 | 0% | 5% |
| 2Q 2016 | 5% | 10% |
| 3Q 2016 | 10% | 15% |
| 4Q 2016 | 5% | 10% |
| 1Q 2017 | 0% | 5% |
| 2Q 2017 | -5% | -5% |
| 3Q 2017 | -10% | -5% |
| 4Q 2017 | -5% | 0% |
| 1Q 2018 | 0% | 5% |
| 2Q 2018 | 5% | 10% |
| 3Q 2018 | 10% | 15% |
| 4Q 2018 | 5% | 10% |
| 1Q 2019 | 0% | 5% |
| 2Q 2019 | -5% | -5% |
| 3Q 2019 | -10% | -5% |
| 4Q 2019 | -5% | 0% |
| 1Q 2020 | -10% | -5% |
| 2Q 2020 | -5% | -5% |
| 3Q 2020 | -10% | -5% |
| 4Q 2020 | -5% | -5% |
| 1Q 2021 | -10% | -5% |
| 2Q 2021 | -5% | -5% |
| 3Q 2021 | -10% | -5% |
| 4Q 2021 | -5% | -5% |
| Q1 2022 | -10% | -5% |
| Q2 2022 | -5% | -5% |
| Q3 2022 | -10% | -5% |
| Q4 2022 | -5% | -5% |
</details>

![](images/652a77194cc62bd4c106f076042ee8a76fe2e13369e1e69f545d8bc2a411cfd3.jpg)

## SCREENs (medium term)

## Screens on fundamentals, consensus, corporate actions, valuation and ESG

## Operational metrics

ROIC 2024

ROIC chg. 23-28

EPS CAGR 23-28

Cash returns 22-23

Avg. FCF/adj. EBIT 23-28

chg. WC days 24-26

## Valuation metrics

FCF yield 2024

Div. & Buyback yield 2024

PEG ratio

EV/EBIT vs 10y avg. prem./disc.

L12M price performance

RSI 30D

% of buy ratings

## GS vs consensus

2024 EBIT vs. Visible Alpha

consensus data

## Corporate actions

IRR under basic LBO

assumptions

SOTP valuations

## Screen on ESG

Governance Rank - Global

Operational Headline E&S Rank

Operational E&S Momentum Rank

Total E&S Disclosure %

Headline Controversy Rank

Governance Rank - Global

## Bull/Bear/Normalization scenarios

Peak/trough/normalized EV/Sales

Peak/trough/normalized EV/EBIT

Peak/trough/normalized P/B

![](images/a60a72702700cbe3c24110a8574175be8c02591642fec900e895a39b39c3a20c.jpg)  
Screens

<table><tr><td>Company</td><td>Ticker</td><td>Price</td><td>Closing Price</td><td>Day Chg</td><td>High</td><td>Low</td><td>Yld</td><td>P/E</td><td>MCap m</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>S&amp;P Global</td><td>276.91</td><td>234.71</td><td>-0.58</td><td>276.74</td><td>276.71</td><td>-0.58</td><td>-0.58</td><td>-0.58</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>MitsubishiUFJ</td><td>374.79</td><td>339.26</td><td>-0.58</td><td>374.79</td><td>374.79</td><td>-0.58</td><td>-0.58</td><td>-0.58</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Nasdaq</td><td>162.06</td><td>146.24</td><td>-0.58</td><td>162.06</td><td>162.06</td><td>-0.58</td><td>-0.58</td><td>-0.58</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>China Mobile</td><td>394.72</td><td>376.42</td><td>-0.58</td><td>394.72</td><td>394.72</td><td>-0.58</td><td>-0.58</td><td>-0.58</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>Shanghai Hong Kong</td><td>164.23</td><td>139.26</td><td>-0.58</td><td>164.23</td><td>164.23</td><td>-0.58</td><td>-0.58</td><td>-0.58</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>Tencent Holdings</td><td>164.23</td><td>139.26</td><td>-0.58</td><td>164.23</td><td>164.23</td><td>-0.58</td><td>-0.58</td><td>-0.58</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>Daimler WWI</td><td>164.23</td><td>139.26</td><td>-0.58</td><td>164.23</td><td>164.23</td><td>-0.58</td><td>-0.58</td><td>-0.58</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>Haitai Froude SA</td><td>164.23</td><td>139.26</td><td>-0.58</td><td>164.23</td><td>164.23</td><td>-0.58</td><td>-0.58</td><td>-0.58</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="9">9</td><td rowspan="9">Suresa China Ltd. (HK)</td><td rowspan="9">164.23</td><td rowspan="9">139.26</td><td rowspan="9">-0.58</td><td rowspan="9">164.23</td><td rowspan="9">164.23</td><td rowspan="9">-0.58</td><td rowspan="9">-0.58</td><td rowspan="9">-0.58</td><td rowspan="9"></td><td rowspan="9"></td><td rowspan="7"></td><td rowspan="7"></td><td rowspan="7"></td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td></tr><tr></tr><tr><td>10</td><td colspan="14">China Mobile Limited (HK) (US$)</td></tr><tr><td>11</td><td colspan="14">China Mobile Limited (HK) (US$)</td></tr><tr><td>12</td><td colspan="14">China Mobile Limited (HK) (US$)</td></tr><tr><td>13</td><td colspan="14">China Mobile Limited (HK) (US$)</td></tr><tr><td>14</td><td colspan="14">China Mobile Limited (HK) (US$)</td></tr><tr><td>15</td><td colspan="14">China Mobile Limited (HK) (US$)</td></tr><tr><td>16</td><td colspan="14">China Mobile Limited (HK) (US$)</td></tr><tr><td>17</td><td

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
