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
# Taiwan PCB & Laminates

## ABF/BT Sector: GM/pricing Upcycle Underway; Buy with Higher TPs

## CITI'S TAKE

Both ABF and BT substrate demand are rising on AI applications. With rising AI GPU/ASIC/CPU demand, we expect the ABF supply tightness to continue throughout 2027 with continued price hikes. For BT, we also see improving S/D status, given peers' less willingness in BT production. T glass is likely to still be a constraint throughout 2027, if new capacity ramps slower than expected. We expect substrate makers to enjoy GM expansion cycle evidenced by recent monthly earnings release. We raise TPs of NYPCB (new TP NT\$1,550), Kinsus (new TP NT\$1,100) and Unimicron (new TP NT\$1,500) and reiterate our Buy ratings. In the short term, we prefer NYPCB and Kinsus on more aggressive pricing strategies. We open 30-day upside CWs for NYPCB and Kinsus on potential sales/GM upbeat on price hikes.

ABF substrate: tight supply evidenced by improving China UTR — Besides rapid recovery in UTR of non-China capacity, we observe UTR in China ABF capacity is improving with peers like Zhen Ding announcing further capacity expansion. To note that, China ABF capacity is the least favorable option to US customers given geopolitical risk. However, it seems US customers are adopting it given lack of choices. Meanwhile, domestic AI demand for China is also improving, competing for capacity as well. Unless there is any sign of loosening demand in China capacity, we are confident on the growth prospects of the ABF industry. We currently forecast 15-20% QoQ ABF price hike in 3Q26 considering higher willingness to pay in high season and followed by 10-15% QoQ in 4Q26 considering lower seasonality.

BT substrate: improving S/D with peers gradually cutting capacity — Our industry checks suggest some peers are showing less willingness to take BT orders or are planning to convert BT production lines into ABF lines given better profitability and visibility. This coupled with its guidance, Unimicron now targets to cut at least 15% of its total BT capacity by end-2026, likely mostly for WBCSP-related products in Taiwan plants. We think Unimicron won’t fully exit BT market in the mid-term given some of its major ABF customers like Apple and few key Chinese customers still have BT demand. Thus, we think its capacity in Suzhou’s BT plant might be kept operational. As per our calculation (see figure 2), Unimicron’s BT sales roughly account for 11% of BT sales from global major peers. We project Unimicron to cut 40-50% of its BT capacity in the mid-term, thereby gradually transferring BT orders to other Taiwanese peers.

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Ccy</td><td rowspan="2">Price</td><td rowspan="2">Mkt Cap (M)</td><td rowspan="2">Date &amp; Time</td><td colspan="2">Rating</td><td rowspan="2">Short-Term View</td><td colspan="2">Target Price</td><td rowspan="2">ESPR (%)</td><td rowspan="2">Div Yld (%)</td><td rowspan="2">ETR (%)</td><td rowspan="2">Last Rpt Yr</td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td><td colspan="2">EPS</td><td colspan="2">EPS</td></tr><tr><td>Kinsus Interconnect Technology</td><td>3189.TW</td><td>NT$</td><td>891.00</td><td>469,482</td><td>30 Jun 13:30</td><td>1</td><td>nc</td><td>Upside^</td><td>400.00</td><td>1,100.00</td><td>23.5</td><td>0.2</td><td>23.6</td><td>Dec-25</td><td>9.56</td><td>11.42</td><td>16.20</td><td>38.61</td></tr><tr><td>Nan Ya PCB</td><td>8046.TW</td><td>NT$</td><td>1,185.00</td><td>765,706</td><td>30 Jun 13:30</td><td>1</td><td>nc</td><td>Upside^</td><td>1,100.00</td><td>1,550.00</td><td>30.8</td><td>0.2</td><td>31.0</td><td>Dec-25</td><td>14.07</td><td>16.41</td><td>36.82</td><td>51.89</td></tr><tr><td>Unimicron Technology</td><td>3037.TW</td><td>NT$</td><td>1,070.00</td><td>1,700,094</td><td>30 Jun 13:30</td><td>1</td><td>nc</td><td>Upside^</td><td>1,080.00</td><td>1,500.00</td><td>40.2</td><td>0.2</td><td>40.4</td><td>Dec-25</td><td>17.71</td><td>21.12</td><td>35.94</td><td>50.49</td></tr><tr><td colspan="6">1 = Buy, 2 = Neutral, 3 = Sell, H = High Risk</td><td colspan="13">ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change</td></tr><tr><td colspan="6">Source: Citi</td><td colspan="13">^Catalyst Watch</td></tr></table>

Jack Chen AC

+886-2-8726-9091

jack1.chen@citi.com

Laura (Chia Yi) Chen

+886-2-8726-9090

laura.cy.chen@citi.com

Nicholas Lai

+886-2-8726-9093

nicholas.lai@citi.com

Earnings Estimates

<table><tr><td colspan="4"></td><td colspan="4">Last Reported Year</td><td></td><td colspan="4">Current Fiscal Year</td><td></td><td colspan="4">Next Fiscal Year</td><td></td></tr><tr><td>Company Name</td><td>Ticker</td><td>Last Rpt Year</td><td>Currency</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY0</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY1</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY2</td></tr><tr><td rowspan="2">Kinsus Interconnect Technology</td><td rowspan="2">3189.TW</td><td>Dec-25</td><td></td><td>0.61</td><td>0.74</td><td>0.75</td><td>1.41</td><td>3.51</td><td>1.17</td><td>2.50</td><td>3.45</td><td>4.08</td><td>11.42</td><td>6.97</td><td>8.74</td><td>10.37</td><td>12.53</td><td>38.61</td></tr><tr><td></td><td>NT$</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Old</td><td></td><td>Dec-25</td><td>NT$</td><td>0.61</td><td>0.74</td><td>0.75</td><td>1.41</td><td>3.51</td><td>1.69</td><td>1.74</td><td>2.80</td><td>3.24</td><td>9.56</td><td>3.22</td><td>3.59</td><td>4.77</td><td>4.62</td><td>16.20</td></tr><tr><td>Nan Ya PCB</td><td>8046.TW</td><td>Dec-25</td><td>NT$</td><td>0.32</td><td>-0.29</td><td>1.12</td><td>1.86</td><td>3.01</td><td>2.03</td><td>3.38</td><td>5.08</td><td>5.92</td><td>16.41</td><td>8.73</td><td>12.22</td><td>14.65</td><td>16.29</td><td>51.89</td></tr><tr><td>Old</td><td></td><td>Dec-25</td><td>NT$</td><td>0.32</td><td>-0.29</td><td>1.12</td><td>1.86</td><td>3.01</td><td>2.03</td><td>2.87</td><td>4.07</td><td>5.11</td><td>14.07</td><td>6.52</td><td>8.41</td><td>10.48</td><td>11.41</td><td>36.82</td></tr><tr><td>Unimicron Technology</td><td>3037.TW</td><td>Dec-25</td><td>NT$</td><td>0.60</td><td>0.02</td><td>1.44</td><td>2.32</td><td>4.38</td><td>3.28</td><td>6.29</td><td>5.03</td><td>6.52</td><td>21.12</td><td>8.08</td><td>9.78</td><td>14.04</td><td>18.58</td><td>50.49</td></tr><tr><td>Old</td><td></td><td>Dec-25</td><td>NT$</td><td>0.60</td><td>0.02</td><td>1.44</td><td>2.32</td><td>4.38</td><td>3.20</td><td>4.07</td><td>4.11</td><td>6.34</td><td>17.71</td><td>6.88</td><td>7.79</td><td>9.90</td><td>11.38</td><td>35.94</td></tr><tr><td colspan="19">Source: Citi</td></tr></table>

T glass: likely continued constraint throughout 2027 — With rising AI GPU/ASIC/CPU demand, we think T glass constraint will likely continue into 2027, given the qualification progress for new vendors seems to be slower than expected. Among all the new vendors, Taiwan Glass Industry takes the lead in thick glass, but its product quality still falls short of Nittobo's. End-customers/fabless currently are still trying to find new vendors or other kinds of new solutions, which is why EMC's ABF CCL, MGC's RS Resin solution, Nanya Plastics' T glass or other new unlisted vendors' T glass are considered yet without proven. In our view, Nittobo's capacity expansion plan remains the key to the supply, yet whether to initiate another price hike is up to Nittobo's willingness, which is addressed in our JP analyst Yuta Nishiyama's report. In our view, whether industrywide T glass supply is able to fulfill all the AI chips demand is less concerning as we think substrate makers would just hike the prices to achieve growth despite the unit shipments being constrained. We expect fabless in the queue eventually needs to pay premium for the shortage, unless there is any delay in their AI chip development.

NYPCB: aggressive ABF/BT pricing strategies — NYPCB is the key beneficiary to Broadcom's Tomahawk products for ABF. Besides switch ICs, the company would also supply some ASIC projects with minority share. For BT, the company sees strong demand from memory. NYPCB is reluctant to enter into long-term agreements with customers with high exposure to spot market. Based on the last cycle experience, we expect the company to be aggressive in both ABF and BT pricing strategies in the coming quarters. We expect price hikes and improving UTR to drive its GM profile in the coming quarters. Our 2027E profit forecast increases by \~40% to NT\$33.5bn given more aggressive pricing strategies.

Kinsus: Vera CPU key suppliers + improving BT S/D — The company is bullish on its market share in Vera CPU, which echoes our view of market share >50%. The upside to its market share in Vera CPU would hinge on its capacity expansion pace. For its BT demand, we expect Kinsus to benefit from outflowing orders from Unimicron, driving its UTR quarter after quarter. We expect Kinsus' both ABF and BT UTR to reach full levels by end 2026. To note that, we think BT GM would likely surpass 20% levels in this cycle vs historical levels of 5-15% range. Kinsus currently has 35-40% BT sales exposure. We forecast more than double our 2027E profit estimate to NT\$20.8bn given improvement in both ABF and BT GM.

Unimicron: more T glass supply + HDI upside — To note that, in the long term, we remain bullish on Unimicron. We understand investors' short-term preference to ABF names with higher spot-price exposure and earnings growth. However, we think Unimicron still sees meaningful earnings upside from 1) GM benefits from long-term agreements, 2) HDI GM improvement when mass production kicks off and 3) more sufficient T glass supply, which would give Unimicron more bargaining power with customers vs other ABF peers. To note that, we think current 2Q26 GM uptick is likely driven by rising ABF demand rather than by HDI UTR improvement. Our 2027E profit forecast increases by 37% to NT\$77.6bn given GM expansion on more AI GPU/ASIC demand and price hikes.

GM expansion/price hikes underway; NYPCB/Kinsus preferred in the S-T — We see improving monthly profitability (see figure 1) of three Taiwanese substrate makers, which we believe is driven by enhanced product mix, rising UTR and price hikes. Given material changes to our 2027E profit estimates driven by margin expansion, we raise TPs of Unimicron/NYPCB/Kinsus to NT\$1,500 (30x 2027E EPS)/ NT\$1,550 (30x 2027E EPS)/ NT\$1,100 (28x 2027E EPS). We believe the GM/pricing upcycle would justify the high PE multiple of \~30x for all the three companies. Reiterate our Buy ratings on three names. In the short term, we prefer

NYPCB/Kinsus given aggressive pricings and improving BT sentiment. In the long term, we still like Unimicron given its leadership position.

<table><tr><td colspan="7">Figure 1. Unaudited monthly results of Unimicron, NYPCB and Kinsus</td></tr><tr><td colspan="7">Unimicron</td></tr><tr><td>(NT$mn)</td><td>1Q26</td><td>Jan</td><td>Implied Feb</td><td>March</td><td>April</td><td>May</td></tr><tr><td>Sales</td><td>37,446</td><td>12,767</td><td>11,600</td><td>13,079</td><td>13,933</td><td>na</td></tr><tr><td>Pre-tax earnings</td><td>6,299</td><td>2,382</td><td>2,290</td><td>1,627</td><td>3,460</td><td>na</td></tr><tr><td>Pre-tax margin %</td><td>16.8%</td><td>18.7%</td><td>19.7%</td><td>12.4%</td><td>24.8%</td><td>na</td></tr><tr><td>EPS (NT$)</td><td>3.28</td><td>1.23</td><td>1.31</td><td>0.74</td><td>1.85</td><td>na</td></tr><tr><td>Gains on financial assets (liabilities) at fair value</td><td>2,507</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>% of total sales</td><td>6.7%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7">Share price performance of Unimicron&#x27;s financial assets (%)</td></tr><tr><td>Unimicron</td><td>92%</td><td>72%</td><td>27%</td><td>-8%</td><td>99%</td><td>19%</td></tr><tr><td>UMC</td><td>18%</td><td>27%</td><td>5%</td><td>-14%</td><td>37%</td><td>87%</td></tr><tr><td>TWSE Index</td><td>11%</td><td>11%</td><td>10%</td><td>-10%</td><td>23%</td><td>15%</td></tr><tr><td colspan="7">Share price diff. of Unimicron&#x27;s financial assets (NT$/share, except Index)</td></tr><tr><td>Unimicron</td><td>225</td><td>159</td><td>103</td><td>(37)</td><td>439</td><td>172</td></tr><tr><td>UMC</td><td>7</td><td>13</td><td>3</td><td>(9)</td><td>21</td><td>67</td></tr><tr><td>TWSE Index</td><td>2,759</td><td>3,100</td><td>3,351</td><td>(3,692)</td><td>7,204</td><td>5,806</td></tr><tr><td colspan="7">NYPCB</td></tr><tr><td>(NT$mn)</td><td>1Q26</td><td>Jan</td><td>Feb</td><td>Implied March</td><td>April</td><td>May</td></tr><tr><td>Sales</td><td>11,177</td><td>3,720</td><td>3,166</td><td>4,291</td><td>4,451</td><td>4,440</td></tr><tr><td>Pre-tax earnings</td><td>1,598</td><td>450</td><td>369</td><td>779</td><td>746</td><td>977</td></tr><tr><td>Pre-tax margin %</td><td>14.3%</td><td>12.1%</td><td>11.7%</td><td>18.2%</td><td>16.8%</td><td>22.0%</td></tr><tr><td>EPS (NT$)</td><td>2.03</td><td>0.56</td><td>0.46</td><td>1.01</td><td>0.92</td><td>1.21</td></tr><tr><td colspan="7">Kinsus</td></tr><tr><td>(NT$mn)</td><td>1Q26</td><td>Implied Jan</td><td>Feb</td><td>March</td><td>April</td><td>May</td></tr><tr><td>Sales</td><td>11,105</td><td>3,962</td><td>3,204</td><td>3,939</td><td>na</td><td>4,200</td></tr><tr><td>Pre-tax earnings</td><td>964</td><td>99</td><td>421</td><td>444</td><td>na</td><td>563</td></tr><tr><td>Pre-tax margin %</td><td>8.7%</td><td>2.5%</td><td>13.1%</td><td>11.3%</td><td>na</td><td>13.4%</td></tr><tr><td>EPS (NT$)</td><td>1.17</td><td>-0.09</td><td>0.68</td><td>0.58</td><td>na</td><td>0.91</td></tr></table>

Figure 2. BT estimated sales of major global peers in 2025

<table><tr><td></td><td>Market Share (%)</td><td>Sales (US$mn)</td></tr><tr><td colspan="3">Taiwan peers</td></tr><tr><td>Unimicron</td><td>11%</td><td>551</td></tr><tr><td>Kinsus</td><td>10%</td><td>460</td></tr><tr><td>Nanya PCB</td><td>8%</td><td>376</td></tr><tr><td>Zhen Ding</td><td>5%</td><td>260</td></tr><tr><td colspan="3">Chinese peers</td></tr><tr><td>Shennan Circuits</td><td>12%</td><td>577</td></tr><tr><td>Shenzhen Fastprint</td><td>4%</td><td>186</td></tr><tr><td colspan="3">Korea peers</td></tr><tr><td>Simmtech</td><td>16%</td><td>748</td></tr><tr><td>SEMCO</td><td>14%</td><td>657</td></tr><tr><td>Daeduck</td><td>10%</td><td>479</td></tr><tr><td>LG Innotek</td><td>7%</td><td>322</td></tr><tr><td>Other small peers</td><td>4%</td><td>205</td></tr><tr><td>Total</td><td>100%</td><td>4,820</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi Estimates, Bloomberg

Figure 3. NYCPB – Earnings Revision

<table><tr><td rowspan="2">(NT$mn)</td><td colspan="3">2Q26E</td><td colspan="3">3Q26E</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td></tr><tr><td>Sales</td><td>13,344</td><td>13,585</td><td>-2%</td><td>16,176</td><td>15,603</td><td>4%</td><td>58,517</td><td>57,230</td><td>2%</td><td>107,214</td><td>92,356</td><td>16%</td><td>164,586</td><td>130,620</td><td>26%</td></tr><tr><td>Sequential growth (%)</td><td>19%</td><td>22%</td><td></td><td>21%</td><td>15%</td><td></td><td>46%</td><td>42%</td><td></td><td>83%</td><td>61%</td><td></td><td>54%</td><td>41%</td><td></td></tr><tr><td>Gross profit</td><td>3,048</td><td>2,651</td><td>15%</td><td>4,486</td><td>3,655</td><td>23%</td><td>14,502</td><td>12,581</td><td>15%</td><

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
