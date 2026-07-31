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
CHINA INTERNET: AUTO CLASSIFIED

# 2Q26 Preview: Stepped-Up Growth Investments and Capital Returns Meet Tough Industry Backdrop; Stay Neutral on Tuhu/Autohome

We remain cautious on China Internet auto classified platforms ahead of the upcoming 1H26 results scheduled for late Aug. As discussed in our prior note, the increase in oil price (domestic price +8% YTD) has put incremental pressure on revenue growth for platforms with relatively high exposure to the traditional ICE market, and industry competition leads to a tougher trade-off between scale and profitability in the context of lower operating leverage. We see our covered companies stepping up investments for long-term revenue growth potential while enhancing shareholder returns; that said, ROI of such investments against this tough industry backdrop is critical to share performance, in our view.

## What's new

Industry wise, domestic passenger vehicle industry beta may improve around September, with a narrowing yoy decline and potentially turning positive by year-end (more details in GS Asia Mobility Tech Company Call Series). That said, the potential reversal from the temporary decline of NEV penetration to 54% in 1H26 (vs. 58% in 2H25) and auto technology advancements and service integration (e.g., Xiaomi SkyNomad joining Li Auto with extended-range powertrain requiring maintenance every 3 years or 30k km of operations after the first-time maintenance, which extends the maintenance cycle by 1.5-3x) may pressure TAM expansion of traditional auto media/leads and aftersales services.

Company wise, both Tuhu Car and Autohome appear to double down investments in the infrastructure and new initiatives that management expects may fuel platform growth in the longer term. We estimate c.900 Tuhu Car workshop net additions in 1H26E, further acceleration vs. c.330/800 net additions in 1H/2H25 and to $24\%$ workshop count yoy growth, as evidenced by the accelerating merchant app DAU yoy growth. Autohome against the persistent media/leads revenue pressure unveiled its offline new retail brand Jiajiahaoche in Jun, which aims to open 600 stores this year primarily in the lower-tier markets via the franchise model. Additionally, Autohome aims to ramp-up its used car export business from 2H26E against the large market potential opportunity (e.g., China's used car export volume is only $5\%$ of new car export volume in 1H26 as per CADA).

Timothy Zhao  
+852-2978-2673 |  
timothy.zhao@gs.com  
GS (Asia) L.L.C.

Ronald Keung, CFA
+852-2978-0856 |
ronald.keung@gs.com
GS (Asia) L.L.C.

Eunice Liu  
+852-2978-7472 | eunice.liu@gs.com  
GS (Asia) L.L.C.

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

## Forecast revisions and TP changes

Tuhu Car (9690.HK, Neutral): We raise 2026-28E revenue forecasts by 1%/5%/6% driven by strong workshop expansion, yet lower adj. net profit forecasts by 17% on average primarily due to lower GPM and higher sales and marketing expenses related to online traffic acquisition and offline workshop expansion. Our revised 12m target price is lowered to HK\$13 (vs. HK\$15 prior) as we reflect the lowered EPS, based on an unchanged target P/E multiple of 15x. Tuhu on Jun 29 announced the share repurchase and cancellation plan of no less than 50mn shares till Jul 2028 (6% of total shares outstanding), which we believe implies enhanced capital return commitment against its strong balance sheet (Rmb7bn net cash as of 2025, equivalent to 80%+ of market cap).

■ Autohome (ATHM/2518.HK, Neutral): We cut our 2026-28E revenue forecasts by 8% and adj. EPS forecasts by 10% on average, primarily as we lower leads generation and data products revenue on the weak ICE vehicle sales and tight budgets of traditional auto dealerships. That said, we are encouraged by the company's stepped-up capital returns to shareholders equivalent to 22% shareholder return yield this year; post execution on US\$200mn share repurchase program in Mar-Jul, the company announced a new US\$400mn share repurchase program in Jul 2026 over the next 12 months, in addition to its Rmb1.5bn annual cash dividend commitment. We raise our 12m target prices for ADR/H-share to US\$19/HK\$37.5 (vs. US\$17/HK\$33 prior), based on unchanged valuation methodology i.e., 1) an 85% weighting to fundamental value based on 13.5x target P/E applied to our 2027E non-GAAP EPS, which is based on the top-quartile of the 12m-fwd P/E multiples over the past year due to enhanced shareholder returns; and 2) a 15% weighting to a theoretical M&A value derived from the unchanged 15x 12m-fwd target P/E multiple.

Tuhu Car (9690.HK)

<table><tr><td>9690.HK</td><td>12m Price Target: HK$13</td><td colspan="2">Price: HK$11.68</td><td colspan="2">Upside: 11.3%</td></tr><tr><td rowspan="2">Neutral</td><td>GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: HK$9.5bn / $1.2bn</td><td>Revenue (Rmb mn) New</td><td>16,461.6</td><td>18,524.6</td><td>20,639.7</td><td>22,322.0</td></tr><tr><td>Enterprise value: HK$362.7mn / $46.3mn</td><td>Revenue (Rmb mn) Old</td><td>16,461.6</td><td>18,290.2</td><td>19,736.0</td><td>21,006.2</td></tr><tr><td>3m ADTV :HK$13.8mn/ $1.8mn</td><td>EBITDA (Rmb mn)</td><td>556.4</td><td>524.5</td><td>780.0</td><td>946.2</td></tr><tr><td>China</td><td>EPS (Rmb) New</td><td>0.84</td><td>0.65</td><td>0.84</td><td>1.00</td></tr><tr><td rowspan="2">China Internet Verticals</td><td>EPS (Rmb) Old</td><td>0.84</td><td>0.88</td><td>0.99</td><td>1.10</td></tr><tr><td>P/E (X)</td><td>19.8</td><td>15.4</td><td>12.1</td><td>10.1</td></tr><tr><td>M&amp;A Rank: 3</td><td>P/B (X)</td><td>2.7</td><td>1.5</td><td>1.4</td><td>1.2</td></tr><tr><td rowspan="4">Leases incl. in net debt &amp; EV?: Yes</td><td>Dividend yield (%)</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>CROCI (%)</td><td>21.4</td><td>21.2</td><td>29.6</td><td>34.1</td></tr><tr><td></td><td>6/25</td><td>12/25</td><td>6/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>0.49</td><td>0.35</td><td>0.26</td><td>0.39</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 29 Jul 2026 close.

Exhibit 1: Tuhu 1H26E results preview

<table><tr><td>Rmb mn</td><td>1H24</td><td>2H24</td><td>1H25</td><td>2H25</td><td>New 1H26E</td><td>HoH %</td><td>YoY %</td></tr><tr><td>Number of Tuhu workshops</td><td>6,311</td><td>6,874</td><td>7,205</td><td>8,008</td><td>8,908</td><td>11%</td><td>24%</td></tr><tr><td>Revenues</td><td>7,126</td><td>7,633</td><td>7,877</td><td>8,585</td><td>8,763</td><td>2%</td><td>11%</td></tr><tr><td>Automotive products and services</td><td>6,643</td><td>7,158</td><td>7,362</td><td>8,023</td><td>8,180</td><td>2%</td><td>11%</td></tr><tr><td>Advertising, franchise and other services</td><td>483</td><td>474</td><td>515</td><td>561</td><td>583</td><td>4%</td><td>13%</td></tr><tr><td>COGS</td><td>(5,280)</td><td>(5,732)</td><td>(5,895)</td><td>(6,599)</td><td>(6,733)</td><td>-2%</td><td>-14%</td></tr><tr><td>Gross profit</td><td>1,846</td><td>1,900</td><td>1,982</td><td>1,985</td><td>2,030</td><td>2%</td><td>2%</td></tr><tr><td>Sales and marketing</td><td>(908)</td><td>(1,008)</td><td>(1,022)</td><td>(1,003)</td><td>(1,083)</td><td>-8%</td><td>-6%</td></tr><tr><td>General and administrative</td><td>(186)</td><td>(169)</td><td>(194)</td><td>(206)</td><td>(206)</td><td>0%</td><td>-6%</td></tr><tr><td>Research and development</td><td>(302)</td><td>(338)</td><td>(344)</td><td>(420)</td><td>(409)</td><td>3%</td><td>-19%</td></tr><tr><td>Operations and support</td><td>(283)</td><td>(293)</td><td>(310)</td><td>(372)</td><td>(350)</td><td>6%</td><td>-13%</td></tr><tr><td>OPEX, adj.</td><td>1,606</td><td>1,740</td><td>1,765</td><td>1,824</td><td>1,968</td><td>8%</td><td>11%</td></tr><tr><td>Operating profit</td><td>212</td><td>119</td><td>222</td><td>30</td><td>46</td><td>52%</td><td>-79%</td></tr><tr><td>Operating profit, adj.</td><td>286</td><td>187</td><td>326</td><td>207</td><td>126</td><td>-39%</td><td>-61%</td></tr><tr><td>SBC</td><td>74</td><td>68</td><td>104</td><td>177</td><td>80</td><td>-55%</td><td>-23%</td></tr><tr><td>PBT</td><td>289</td><td>198</td><td>312</td><td>111</td><td>138</td><td>24%</td><td>-56%</td></tr><tr><td>Tax</td><td>(5)</td><td>(0)</td><td>(5)</td><td>2</td><td>(3)</td><td>NM</td><td>46%</td></tr><tr><td>Net profit</td><td>284</td><td>198</td><td>307</td><td>113</td><td>135</td><td>20%</td><td>-56%</td></tr><tr><td>Net profit, adj.</td><td>358</td><td>266</td><td>410</td><td>290</td><td>215</td><td>-26%</td><td>-48%</td></tr></table>

<table><tr><td rowspan="2">as % revenue</td><td rowspan="2">1H24</td><td rowspan="2">2H24</td><td rowspan="2">1H25</td><td rowspan="2">2H25</td><td colspan="3">New</td></tr><tr><td>1H26E</td><td>HoH (pp)</td><td>YoY (pp)</td></tr><tr><td>GPM</td><td>25.9%</td><td>24.9%</td><td>25.2%</td><td>23.1%</td><td>23.2%</td><td>0.0</td><td>(2.0)</td></tr><tr><td>Automotive products and services</td><td>23.7%</td><td>22.9%</td><td>22.8%</td><td>20.2%</td><td>20.2%</td><td>(0.0)</td><td>(2.6)</td></tr><tr><td>Advertising, franchise and other services</td><td>85.9%</td><td>88.0%</td><td>90.0%</td><td>90.7%</td><td>90.6%</td><td>(0.1)</td><td>0.6</td></tr><tr><td>Sales and marketing</td><td>-12.7%</td><td>-13.2%</td><td>-13.0%</td><td>-11.7%</td><td>-12.4%</td><td>(0.7)</td><td>0.6</td></tr><tr><td>General and administrative</td><td>-2.6%</td><td>-2.2%</td><td>-2.5%</td><td>-2.4%</td><td>-2.3%</td><td>0.0</td><td>0.1</td></tr><tr><td>Research and development</td><td>-4.2%</td><td>-4.4%</td><td>-4.4%</td><td>-4.9%</td><td>-4.7%</td><td>0.2</td><td>(0.3)</td></tr><tr><td>Operations and support</td><td>-4.0%</td><td>-3.8%</td><td>-3.9%</td><td>-4.3%</td><td>-4.0%</td><td>0.3</td><td>(0.1)</td></tr><tr><td>OPEX</td><td>23.6%</td><td>23.7%</td><td>23.7%</td><td>23.3%</td><td>23.4%</td><td>0.1</td><td>(0.4)</td></tr><tr><td>OPEX, adj.</td><td>22.5%</td><td>22.8%</td><td>22.4%</td><td>21.2%</td><td>22.5%</td><td>1.2</td><td>0.0</td></tr><tr><td>Operating profit</td><td>3.0%</td><td>1.6%</td><td>2.8%</td><td>0.4%</td><td>0.5%</td><td>0.2</td><td>(2.3)</td></tr><tr><td>Operating profit, adj.</td><td>4.0%</td><td>2.5%</td><td>4.1%</td><td>2.4%</td><td>1.4%</td><td>(1.0)</td><td>(2.7)</td></tr><tr><td>SBC</td><td>1.0%</td><td>0.9%</td><td>1.3%</td><td>2.1%</td><td>0.9%</td><td>(1.1)</td><td>(0.4)</td></tr><tr><td>Net profit</td><td>4.0%</td><td>2.6%</td><td>3.9%</td><td>1.3%</td><td>1.5%</td><td>0.2</td><td>(2.4)</td></tr><tr><td>Net profit, adj.</td><td>5.0%</td><td>3.5%</td><td>5.2%</td><td>3.4%</td><td>2.5%</td><td>(0.9)</td><td>(2.8)</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 2: We expect the number of Tuhu workshops to grow +22% yoy to 9.8k in 2026E and exceed 10k+ by 2027E Number of Tuhu workshops (year-end)  
![](images/23078ec66b738eecb801d22df39a3ad404d309bd336162b3bbebfdb1a775b16d.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 3: Tuhu Merchant DAU increased +12% yoy to c.66k in Jun (vs. +11% yoy in May)  
![](images/006a597210c6a437c4209ac7fd1fcd44a4f2d1d9e1aefede7d0761639d3b3464.jpg)  
Source: Questmobile, Data compiled by GS Global Investment Research

Exhibit 4: Tuhu DAU increased +14% yoy in Jun (vs. +12% yoy in May), while Tuhu DAU/Tuhu Merchant app DAU reached 26.4 in Jun (vs. 25.0 in May)  
![](images/159d7d19d9c5fd928f139844e2da561c713176caa609f7f1f8248e565e5ecdc2.jpg)  
Source: Questmobile, Data compiled by GS Global Investment Research

Exhibit 5: We expect Tuhu's LTM transacting user to grow +18% yoy to c.31.3mn in 1H26E  
![](images/b25922c1f22caaecc1ca6e0b571631f9303e77feae751a259b78bcbaed1ee721.jpg)  
Source: Company data, GS Global Investment Research

## Autohome (ATHM/2518.HK)

<table><tr><td>2518.HK</td><td>12m Price Target: HK$37.5</td><td colspan="2">Price: HK$44.16</td><td colspan="2">Downside: 15.1%</td></tr><tr><td>ATHM</td><td>12m Price Target: $19</td><td colspan="2">Price: $22.74</td><td colspan="2">Downside: 16.4%</td></tr><tr><td>Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: $2.7bn</td><td>Revenue (Rmb mn) New</td><td>6,452.0</td><td>4,789.2</td><td>4,953.2</td><td>5,021.5</td></tr><tr><td>Enterprise value: $2.5bn</td><td>Revenue (Rmb mn) Old</td><td>6,452.0</td><td>5,199.1</td><td>5,380.5</td><td>5,447.9</td></tr><tr><td>3m ADTV :$14.4mn</td><td>EBITDA (Rmb mn)</td><td>1,137.3</td><td>459.8</td><td>753.7</td><td>816.4</td></tr><tr><td>China</td><td>EPS (Rmb) New</td><td>13.60</td><td>7.94</td><td>9.38</td><td>9.04</td></tr><tr><td rowspan="2">China Internet Verticals</td><td>EPS (Rmb) Old</td><td>13.60</td><td>8.72</td><td>10.42</td><td>10.01</td></tr><tr><td>P/E (X)</td><td>14.2</td><td>19.4</td><td>16.4</td><td>17.0</td></tr><tr><td>M&amp;A Rank: 2</td><td>P/B (X)</td><td>0.9</td><td>0.7</td><td>0.8</td><td>0.8</td></tr><tr><td rowspan="4">Leases incl. in net debt &amp; EV?: Yes</td><td>Dividend yield (%)</td><td>6.5</td><td>8.7</td><td>8.2</td><td>8.8</td></tr><tr><td>CROCI (%)</td><td>5.1</td><td>0.9</td><td>2.7</td><td>3.7</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>1.54</td><td>2.07</td><td>2.02</td><td>2.33</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 29 Jul 2026 close.

Exhibit 6: Autohome 2Q26E results preview

<table><tr><td rowspan="2">Rmb mn</td><td rowspan="2">1Q25</td><td rowspan="2">2Q25</td><td rowspan="2">3Q25</td><td rowspan="2">4Q25</td><td rowspan="2">1Q26</td><td colspan="3">New</td></tr><tr><td>2Q26E</td><td>QoQ (%)</td><td>YoY (%)</td></tr><tr><td>Media services</td><td>242</td><td>279</td><td>298</td><td>334</td><td>163</td><td>262</td><td>61%</td><td>-6%</td></tr><tr><td>Lead generation services</td><td>645</td><td>733</td><td>664</td><td>668</td><td>503</td><td>531</td><td>6%</td><td>-27%</td></tr><tr><td>Online marketplace &amp; others</td><td>566</td><td>746</td><td>816</td><td>460</td><td>382</td><td>378</td><td>-1%</td><td>-49%</td></tr><tr><td>Total net revenues</td><td>1,454</td><td>1,758</td><td>1,778</td><td>1,462</td><td>1,048</td><td>1,171</td><td>12%</td><td>-33%</td></tr><tr><td>Cost of revenues</td><td>316</td><td>503</td><td>646</td><td>319</td><td>257</td><td>288</td><td>12%</td><td>-43%</td></tr><tr><td>Gross profit, GAAP</td><td>1,138</td><td>1,255</td><td>1,132</td><td>1,143</td><td>791</td><td>882</td><td>11%</td><td>-30%</td></tr><tr><td>Gross profit, non-GAAP</td><td>1,141</td><td>1,258</td><td>1,137</td><td>1,147</td><td>792</td><td>883</td><td>11%</td><td>-30%</td></tr><tr><td>Sales and marketing</td><td>544</td><td>630</td><td>620</td><td>739</td><td>506</td><td>513</td><td>1%</td><td>-18%</td></tr><tr><td>General and administrative</td><td>131</td><td>133</td><td>125</td><td>115</td><td>120</td><td>108</td><td>-10%</td><td>-18%</td></tr><tr><td>Product development</td><td>274</td><td>253</td><td>279</td><td>258</td><td>274</td><td>221</td><td>-19%</td><td>-13%</td></tr><tr><td>Total operating expenses, GAAP</td><td>949</td><td>1,016</td><td>1,024</td><td>1,112</td><td>900</td><td>843</td><td>-6%</td><td>-17%</td></tr><tr><td>Operating profit, GAAP</td><td>233</td><td

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
