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
## Korea Autos

2Q preview: HMC softer, Kia in-line; cost inflation elevated, divergence led by volumes

HMC delivered 2Q global retail sales of 999k (-4% y/y), while Kia's 2Q retail sales were robust at 837k (+6% y/y). We forecast OP of W2.9tn for both HMC/Kia (vs. BBGe W3.1tn/W2.8tn): HMC is likely to fall short of BBGe on lower UTR and input cost inflation, while Kia should be closer on resilient UTR. We estimate commodity inflation (aluminum/copper/plastics/DRAM) implies \~W0.35tn/\~W0.25tn OP impact in 2Q, partly offset by FX tailwinds of \~W0.5tn/\~W0.4tn per quarter, though inflation accelerated in 2Q and may not be fully offset in the following quarters. Investors are now focused on the next robotics catalysts, with Kia preferred on valuation (6x 2027E P/E) and >4% yield but HMC may offer greater upside sensitivity if robotics sentiment re-heats. We maintain Overweight on HMC/Kia, cut HMC's 2026-28E OP by 6-11% and tweak Kia -4% to +2% on input cost hike, and roll PTs to Dec-27 using 11x/9x target P/E for core auto business to derive W640,000 and W260,000 PTs.

\- HMC 2Q retail sales softer but likely to recoup in 2H on new models; Kia's sales momentum continued in 2Q. HMC reported 2Q global retail sales of 999k units (-4% y/y), with weakness concentrated in Korea and Europe amid an aging model cycle and supply chain disruptions. We expect HMC's sales to improve in 2H as new models launch across Korea, the US, and Europe. Kia delivered robust retail sales of 837k units (+6% y/y), and we expect momentum to continue with its current model lineup.

\- 2Q preview: HMC OP softer, Kia in-line with BBGe. We forecast 2Q OP of W2.9tn for both HMC/Kia (vs. BBGe W3.1tn/W2.8tn). For HMC, we see downside vs. BBGe driven by a slower UTR (\~85% vs. \~100% in 2Q25) and input cost inflation, while Kia should be closer to BBGe on resilient UTR (\~100%). We estimate cost inflation impact of \~W0.35tn/\~W0.25tn for HMC/Kia's OP in 2Q, following lingering effects of commodity cost inflation in 1Q (aluminium +13% q/q, copper +15% q/q, plastics +30% q/q, DRAM +72% q/q). FX tailwinds of \~W0.5tn/\~W0.4tn per quarter should offset a meaningful portion, but HMC's volume headwind and lower UTR are incremental pressures, whereas Kia's volume growth should support OP. We remain mindful that inflation accelerated in 2Q and may not be fully offset by FX.

\- Investor feedback from our Asia marketing (link). While investors broadly agree that the robotics upside is valid, the focus has shifted to what could reignite sentiment. In our view, key watch items include HMG's planned opening of the robotics training center this summer and expectations that the Group will finalize detailed investment plans and subsidiaries' role alignment within the robotics business by the year-end. Fundamentally, Kia is preferred on valuation (6x 2027E P/E based on our estimates) and dividend yield $(>4\%)$ , although investor interest could rotate towards HMC if the robotics narrative heats up again.

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev End Date</td><td></td></tr><tr><td>Hyundai Motor Company</td><td>005380 KS</td><td>80,541</td><td>KRW</td><td>473,000</td><td>OW</td><td>n/c</td><td>640,000</td><td>Dec-27</td><td>670,000</td><td>Dec-26</td></tr><tr><td>Kia Corp</td><td>000270 KS</td><td>39,276</td><td>KRW</td><td>152,500</td><td>OW</td><td>n/c</td><td>260,000</td><td>Dec-27</td><td>240,000</td><td>Dec-26</td></tr></table>

Korea Auto, EV battery, Nuclear and Utility

Sonny Lee AC
(82-2) 758 5716
sonny.lee@JPM.com

Equity Ratings and Price Targets

Seri Yoon

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 07 Jul 26.

(82-2) 758 5704

seri.yoon@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

See page 15 for analyst certification and important disclosures, including non-US analyst disclosures.

\- Maintain Overweight on HMC/Kia. We expect tangible progress in HMG's robotics and autonomous driving efforts to underpin our constructive stance on the OEMs. We lower our 2026-28 earnings estimates for HMC by $6 - 11\%$ and tweak Kia's estimates by $-4\%$ to $+2\%$ , mainly reflecting the adverse impact from cost inflation. We roll-over our PTs from Dec-26 to Dec-27 and refresh our fair values for the core auto businesses, maintaining target P/E multiples of $11x / 9x$ for HMC/Kia.

Table 1: HMC/Kia: 1H retail sales vs. Annual guidance k units

<table><tr><td></td><td>1H26 Actual</td><td>1H25</td><td>% y/y</td><td>2026 Annual guidance (wholesale)</td><td>Progress</td></tr><tr><td>HMC</td><td>1,948</td><td>1,999</td><td>-3%</td><td>4,158</td><td>47%</td></tr><tr><td>Korea</td><td>309</td><td>346</td><td>-11%</td><td>700</td><td>44%</td></tr><tr><td>Overseas</td><td>1,639</td><td>1,653</td><td>-1%</td><td>3,458</td><td>47%</td></tr><tr><td>Kia*</td><td>1,616</td><td>1,543</td><td>5%</td><td>3,340</td><td>48%</td></tr><tr><td>Korea</td><td>296</td><td>276</td><td>7%</td><td>565</td><td>52%</td></tr><tr><td>Overseas</td><td>1,320</td><td>1,267</td><td>4%</td><td>2,775</td><td>48%</td></tr></table>

\*Excluding special-purpose vehicles  
Source: Company data, JPM estimates

Table 2: HMC/Kia: 2Q retail sales

<table><tr><td></td><td>2Q26 Actual</td><td>2Q25</td><td>% y/y</td></tr><tr><td>HMC</td><td>999</td><td>1,043</td><td>-4%</td></tr><tr><td>Korea</td><td>154</td><td>184</td><td>-16%</td></tr><tr><td>Overseas</td><td>844</td><td>859</td><td>-2%</td></tr><tr><td>Kia*</td><td>837</td><td>791</td><td>6%</td></tr><tr><td>Korea</td><td>154</td><td>142</td><td>9%</td></tr><tr><td>Overseas</td><td>682</td><td>649</td><td>5%</td></tr></table>

\*Excluding special-purpose vehicles  
Source: Company data

Table 3: HMC/Kia: JPMe vs. BBGe  
Wbn, %

<table><tr><td colspan="10">HMC</td></tr><tr><td rowspan="2"></td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td></tr><tr><td>Revenue</td><td>196,232</td><td>194,103</td><td>1%</td><td>206,671</td><td>202,353</td><td>2%</td><td>212,153</td><td>214,294</td><td>-1%</td></tr><tr><td>OP</td><td>11,822</td><td>11,969</td><td>-1%</td><td>13,280</td><td>13,441</td><td>-1%</td><td>14,099</td><td>14,766</td><td>-5%</td></tr><tr><td colspan="7">Kia</td><td colspan="3"></td></tr><tr><td rowspan="2"></td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td></tr><tr><td>Revenue</td><td>123,860</td><td>124,141</td><td>0%</td><td>129,822</td><td>130,274</td><td>0%</td><td>131,456</td><td>134,495</td><td>-2%</td></tr><tr><td>OP</td><td>10,412</td><td>10,241</td><td>2%</td><td>10,920</td><td>11,335</td><td>-4%</td><td>11,583</td><td>11,941</td><td>-3%</td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates

Table 4: HMC: New model schedule

<table><tr><td>HMC</td><td>1H26</td><td>2H26</td><td>1H27</td><td>2H27</td><td>2028~</td></tr><tr><td rowspan="6">Korea</td><td>Staria EV</td><td>Avante (ICE/HEV)</td><td>Kona (ICE/HEV)</td><td>Kona (EV)</td><td>Nexo F/L</td></tr><tr><td>Grandeur F/L</td><td>Tucson (ICE/HEV)</td><td>GV70 (HEV)</td><td>Sonata F/L (ICE/HEV)</td><td>loniq 5</td></tr><tr><td></td><td>Santa Fe F/L</td><td>Commercial PBV (ICE, EV)</td><td>G90 Coupe</td><td>Palisade F/L (ICE/HEV)</td></tr><tr><td></td><td>GV80,G80 (HEV)</td><td></td><td>Avante N (ICE/HEV)</td><td>GV80</td></tr><tr><td></td><td>GV90</td><td></td><td>loniq 9 F/L</td><td></td></tr><tr><td></td><td>G90 F/L</td><td></td><td></td><td></td></tr><tr><td rowspan="6">US</td><td>Nexo F/L</td><td>Tucson (ICE)</td><td>Tucson (HEV)</td><td>Kona (ICE/HEV)</td><td>Kona EV</td></tr><tr><td>IONIQ 6 N F/L</td><td>GV80 (HEV)</td><td>Elantra (ICE/HEV)</td><td></td><td>Sonata F/L (ICE/HEV)</td></tr><tr><td></td><td>GV90</td><td>Santa Fe (EREV)</td><td></td><td>loniq 9 F/L</td></tr><tr><td></td><td></td><td>GV70 (EREV, HEV)</td><td></td><td>Avante N (ICE/HEV)</td></tr><tr><td></td><td></td><td>G80 (HEV)</td><td></td><td>Palisade F/L (ICE/HEV)</td></tr><tr><td></td><td></td><td>G90 F/L</td><td></td><td>GV80, G90 Coupe</td></tr><tr><td rowspan="4">Europe</td><td>Staria EV</td><td>i20 (ICE)</td><td>Santa Fe (ICE/HEV)</td><td>i20 (HEV)</td><td>loniq 9 F/L</td></tr><tr><td></td><td>IONIQ 3</td><td>GV70 (HEV)</td><td>Kona (EV/HEV)</td><td>b seg EV</td></tr><tr><td></td><td>Tucson (ICE/HEV)</td><td></td><td></td><td>GV80, GV80 Coupe</td></tr><tr><td></td><td>GV90</td><td></td><td></td><td></td></tr><tr><td rowspan="2">India</td><td>Exter F/L</td><td>1 model change</td><td colspan="3">2 new nameplates; 3 model changes</td></tr><tr><td>Accent F/L</td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data, EVs in blue; model change in bold.

Table 5: Kia: New model schedule

<table><tr><td>Kia</td><td>1H26</td><td>2H26</td><td>1H27</td><td>2H27</td><td>2028~</td></tr><tr><td rowspan="2">Korea</td><td>Seltos (ICE/HEV)</td><td></td><td>PBV7</td><td>Sportage (ICE/HEV)</td><td></td></tr><tr><td>Niro F/L</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">US</td><td>Telluride (HEV)</td><td>Niro HEV</td><td></td><td>K4 F/L</td><td>Sportage (ICE/HEV/PHEV)</td></tr><tr><td>Seltos (ICE)</td><td>Seltos (HEV)</td><td></td><td></td><td></td></tr><tr><td></td><td>EV3</td><td></td><td></td><td></td></tr><tr><td rowspan="4">Europe</td><td>Seltos (ICE)</td><td>Seltos (HEV)</td><td></td><td>PBV7</td><td></td></tr><tr><td>EV2</td><td></td><td></td><td>Sportage (ICE/HEV/PHEV)</td><td></td></tr><tr><td>Niro</td><td></td><td></td><td>a segment SDV</td><td></td></tr><tr><td>C&#x27;eed F/L</td><td></td><td></td><td></td><td></td></tr><tr><td>India</td><td>Syros EV</td><td>Sorento (ICE/HEV)</td><td>Sonnet</td><td>c segment EV</td><td></td></tr></table>

Source: Company data. EVs in blue; model change in bold.

## Overweight

005380.KS, 005380 KS
Price (07 Jul 26):W473,000

▼ Price Target (Dec-27):W640,000  
Prior (Dec-26):W670,000

## Korea Auto, EV battery, Nuclear and Utility

Sonny Lee AC
(82-2) 758 5716
sonny.lee@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

Key Changes (FYE Dec)

<table><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. EPS - 26E (W)</td><td>39,951</td><td>37,575</td><td>-5.9%</td></tr><tr><td>Adj. EPS - 27E (W)</td><td>50,453</td><td>42,181</td><td>-16.4%</td></tr></table>

<table><tr><td colspan="4">Quarterly Forecasts (FYE Dec)</td></tr><tr><td colspan="4">Adj. EPS (W)</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>12,130</td><td>8,908A</td><td>7,985</td></tr><tr><td>Q2</td><td>11,365</td><td>9,402</td><td>12,204</td></tr><tr><td>Q3</td><td>8,572</td><td>11,311</td><td>12,658</td></tr><tr><td>Q4</td><td>3,918</td><td>7,608</td><td>8,882</td></tr><tr><td>FY</td><td>35,964</td><td>37,575</td><td>42,181</td></tr></table>

Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>10</td><td>5</td><td>3</td><td>9</td><td>22</td></tr><tr><td>Growth</td><td>85</td><td>80</td><td>77</td><td>87</td><td>36</td></tr><tr><td>Momentum</td><td>22</td><td>61</td><td>71</td><td>23</td><td>62</td></tr><tr><td>Quality</td><td>53</td><td>49</td><td>48</td><td>56</td><td>65</td></tr><tr><td>Low Vol</td><td>54</td><td>24</td><td>27</td><td>9</td><td>61</td></tr><tr><td>ESGQ</td><td>97</td><td>100</td><td>99</td><td>98</td><td>99</td></tr></table>

## Hyundai Motor Company

## 2Q softer on lower UTR and cost inflation

We expect HMC to report a W2.9tn OP in 2Q, coming in below BBGe of W3.1tn. HMC's global retail sales were weighed down by weakness in Korea amid an aging model cycle and supply chain disruptions, while a slower UTR (\~85% vs. \~100% in 2Q25) pressured profitability. Input cost inflation, led by aluminum alongside copper, plastics, and DRAM, is estimated to have a meaningful negative impact on OP, and while FX tailwinds should offset a portion, volume headwinds and lower UTR would represent incremental drags. That said, we expect HMC's sales trajectory to improve from 2H onward as new models launch across Korea, the US, and Europe. We maintain Overweight, as tangible progress in HMG's robotics and autonomous driving efforts underpins our constructive stance. We lower our 2026-28E earnings estimates by 6-11% on cost inflation and set our Dec-27 PT at W640,000.

Table 6: HMC: 2Q26 preview  
Wbn, %

<table><tr><td rowspan="2"></td><td colspan="3">2Q26</td><td rowspan="2">2Q25</td><td rowspan="2">% y/y</td><td rowspan="2">1Q26</td><td rowspan="2">% q/q</td></tr><tr><td>JPMe</td><td>BBG</td><td>Diff.</td></tr><tr><td>Revenue</td><td>48,874</td><td>49,101</td><td>0%</td><td>48,287</td><td>1%</td><td>45,939</td><td>6%</td></tr><tr><td>OP</td><td>2,876</td><td>3,144</td><td>-9%</td><td>3,602</td><td>-20%</td><td>2,515</td><td>14%</td></tr><tr><td>OP margin</td><td>5.9%</td><td>6.4%</td><td></td><td>7.5%</td><td></td><td>5.5%</td><td></td></tr><tr><td>NP</td><td>2,697</td><td>2,674</td><td>1%</td><td>3,250</td><td>-17%</td><td>2,585</td><td>4%</td></tr><tr><td>NP margin</td><td>5.5%</td><td>5.4%</td><td></td><td>6.7%</td><td></td><td>5.6%</td><td></td></tr></table>

Source: Company data, JPM estimates.

Wbn, %  
Table 7: HMC: Estimate revisions

<table><tr><td rowspan="2"></td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Old</td><td>New</td><td>% chg</td><td>Old</td><td>New</td><td>% chg</td><td>Old</td><td>New</td><td>% chg</td></tr><tr><td>Sales</td><td>197,637</td><td>196,232</td><td>-1%</td><td>205,560</td><td>206,671</td><td>1%</td><td>211,429</td><td>212,153</td><td>0%</td></tr><tr><td>% y/y</td><td>6.1%</td><td>5.4%</td><td></td><td>4.0%</td><td>5.3%</td><td></td><td>2.9%</td><td>2.7%</td><td></td></tr><tr><td>OP</td><td>12,624</td><td>11,822</td><td>-6%</td><td>14,852</td><td>13,280</td><td>-11%</td><td>15,916</td><td>14,099</td><td>-11%</td></tr><tr><td>OP margin</td><td>6.4%</td><td>6.0%</td><td></td><td>7.2%</td><td>6.4%</td><td></td><td>7.5%</td><td>6.6%</td><td></td></tr><tr><td>NP</td><td>11,222</td><td>10,684</td><td>-5%</td><td>13,657</td><td>11,783</td><td>-14%</td><td>15,156</td><td>12,739</td><td>-16%</td></tr><tr><td>NP margin</td><td>5.7%</td><td>5.4%</td><td></td><td>6.6%</td><td>5.7%</td><td></td><td>7.2%</td><td>6.0%</td><td></td></tr><tr><td>NP to Parent</td><td>10,274</td><td>9,737</td><td>-5%</td><td>12,660</td><td>10,782</td><td>-15%</td><td>14,243</td><td>11,822</td><td>-17%</td></tr></table>

Source: JPM estimates.

Price Performance  
![](images/749b241dce2d7cdf2cd28822035fd6af16c9fd263a12187aa0eed534ee666c3d.jpg)

— 005380.KS Price (W) — KOSPI (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>59.3%</td><td>-31.4%</td><td>1.3%</td><td>126.9%</td></tr><tr><td>Rel</td><td>-22.4%</td><td>-25.3%</td><td>-38.1%</td><td>-23.4%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>260</td></tr><tr><td>52-week range (W)</td><td>787,000-204,500</td></tr><tr><td>Market cap ($ mn)</td><td>80,541</td></tr><tr><td>Exchange rate</td><td>1,528.65</td></tr><tr><td>Free float (%)</td><td>57.8%</td></tr><tr><td>3M ADV (mn)</td><td>3.55</td></tr><tr><td>3M ADV ($ mn)</td><td>1,423.3</td></tr><tr><td>Volatility (90 Day)</td><t

[中间内容因长度限制已省略]

al information is available upon request. The information in this material has been obtained from sources believed to be reliable. While all reasonable care has been taken to ensure that the facts stated in this material are accurate and that the forecasts, opinions and expectations contained herein are fair and reasonable, JPM Chase & Co. or its affiliates and/or subsidiaries (collectively JPM) make no representations or warranties whatsoever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or
"""
