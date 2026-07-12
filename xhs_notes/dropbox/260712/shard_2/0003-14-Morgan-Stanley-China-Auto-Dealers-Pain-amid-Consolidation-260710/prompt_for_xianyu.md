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
# Pain amid Consolidation

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Zhongsheng Group Holdings (0881.HK)</td><td>From</td><td>To</td></tr><tr><td>Rating</td><td>Overweight</td><td>Equal-weight</td></tr><tr><td>Price Target</td><td>HK$10.50</td><td>HK$5.50</td></tr><tr><td colspan="3">China Yongda Automobiles Services (3669.HK)</td></tr><tr><td>Rating</td><td>Equal-weight</td><td>Underweight</td></tr><tr><td>Price Target</td><td>HK$1.20</td><td>HK$0.60</td></tr><tr><td colspan="3">China MeiDong Auto Holdings Ltd (1268.HK)</td></tr><tr><td>Rating</td><td>Equal-weight</td><td>Underweight</td></tr><tr><td>Price Target</td><td>HK$1.50</td><td>HK$0.40</td></tr></table>

Luxury auto dealer earnings recovery has been slow, hindered by weak ICE demand, falling finance commission and store closures. Despite reduced market expectations, we stay sidelined and downgrade dealers, as pain continues amid dealer consolidation. We think it too early to bottom fish.

1H26 new car data weaker than expected: Both volume and prices of luxury ICEs were tracking behind market expectations. Volume for China ICE car retail sales fell 26% YoY in 1H26 due to cuts to government subsidies and high oil prices – Mercedes-Benz volume fell 28%, BMW JV dropped 18%, Audi JV declined 16% YoY, and Porsche was down 32% YoY. Despite cuts to MSRP (manufacturer's suggested retail price) since the beginning of the year, luxury auto dealers' new car margins remained suppressed due to falling auto finance commissions. Therefore, although fewer new car units could potentially lead to narrower total new car losses, as fundamental demand is unlikely to improve in the near term, investors do not appear convinced by dealer valuations despite 50-60% share price corrections YTD.

After-sales could be dragged by store closures: Dealers' after-sales services used to be resilient; for example, Zhongsheng's repair service revenue grew at a $10\%$ CAGR and gross profit at a $13\%$ CAGR in 2022-25. However, due to accelerated store closures this year, we are concerned that some customers might leave the dealer network for independent repair stores that may provide better value-for-money services. Weak consumption sentiment, as well as declining new car volumes, could also damper after-sales demand.

Stay on the sidelines: We downgrade Yongda (3669.HK) and Meidong (1268.HK) to UW, and Zhongsheng (0881.HK) to EW, as ongoing dealer industry consolidation should suppress new car prices. Even top dealer groups are not out of the woods yet. We look for likely earnings recovery in 2027 post consolidation. Zhongsheng appears better positioned than peers, as it can expand after-sales to non-existing customers via its independent repair centers, while Yongda and Meidong may find it more difficult to retain customers.

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Shelley Wang, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Shelley.Wang@morganstanley.com</td><td>+852 3963-0047</td></tr><tr><td colspan="2">Tim Hsiao</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Tim.Hsiao@morganstanley.com</td><td>+852 2848-1982</td></tr><tr><td colspan="2">Joey Xu, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Joey.Xu@morganstanley.com</td><td>+852 3963-0337</td></tr><tr><td colspan="2">Peggy Wang</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Peggy.Pc.Wang@morganstanley.com</td><td>+852 3963-3934</td></tr></table>

![](images/af4b7e8174d718b496deb9dbdcaf5620ed899dc9d988e5d8d01f9de4db8d1a61.jpg)

Industry View

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Investment Thesis

## New car data weaker than expected in 1H26

Steeper decreases in volume: In China, declines in luxury ICE car sales, for brands such as BMW, Mercedes-Benz and Audi (BBA), were steeper in 1H26 than in the previous year. China total auto retail sales volume fell 20% YoY, ICE car volume dropped 26%, and BBA volume fell 16-28% amid cuts to government subsidies and high oil prices. Sales volume for Porsche China fell 41% YoY in 2Q26 and 28% YoY in 1H26.

Fewer units, reduced loss? With new car sales loss-making, and new car volume down YoY in 1H26 and likely also down YoY for full-year 2026, there is a chance that aggregate new car losses could narrow and drive an earnings recovery. However, investor feedback suggests such a mathematical (i.e., not sustainable) earnings recovery will not be sufficient to drive a valuation re-rating.

Exhibit 1: BBA China retail volume continues to decline YoY  
![](images/ae595f7df82534c2b6d5910cbbf962bb69140e6c272c5c7a13a8b3a2e58096e6.jpg)  
JV retail sales volume only, excluding imported volume. Source: China Passenger Car Association, MS

Exhibit 2: BMW China market share (%)  
![](images/403f77f8e15fc6c88ddbc4510cbd136d434640aff98b239c9a7b45205b9930d0.jpg)  
Source: CPCA, Yiche, MS

Exhibit 3: Mercedes China market share (%)  
![](images/c7fcc3a3a37634610bc6bad5353e67b771c51eaf44da5278b9576c029e098663.jpg)  
Source: CPCA, Yiche, MS

Exhibit 4: Porsche China luxury market share (%)  
![](images/4e9816454ee49497bf025ae81bb7ca7b2fed95468d9ef34af1fe4fca3e17b2ba.jpg)  
Source: CPCA, Yiche, MS

Exhibit 5: China market share by origin of OEMs  
![](images/1b290308c1a1a4075a793c9396b27b9859d678b134f93935d7de07d484cbfaac.jpg)  
Source: CPCA, Yiche, MS

## After-sales could be dragged by store closures

Reversing trends: In the past, auto dealers' after-sales revenue growth was supported by a growing ICE car population, new store openings, and customer retention programs. However, trends are turning into the opposite way, as ICE car population should decline in a few years (as EV penetration keeps increasing), the number of dealer stores is declining, and customers are looking for cheaper alternatives amid consumption downgrades.

For Zhongsheng, its after-sales revenue fell 5% YoY to Rmb26.1bn in 2025, vs. 9% YoY growth in 2024. Excluding accessories, its "core" after-sales revenue, including maintenance, warranty, and collision, also saw growth deceleration, from 16% YoY in 2023 to 10% YoY in 2024 and 4% YoY in 2025 (Rmb22.9bn). That said, Zhongsheng's after-sales business is still the most resilient among the three dealer groups, as its independent repair centers can serve non-Zhongsheng brands such as BYD.

For Yongda, its after-sales revenue peaked at Rmb11.5bn in 2021, and then fell steadily to Rmb9.2bn in 2025 due mainly to store closures; Yongda's number of 4S dealer stores dropped from 179 by end-2020 to 137 by end-2025. Its store concentration in the Yangtze River Delta region also means it is affected most by rising EV penetration among the three dealer groups. Since Yongda plans to shut down more ICE stores, we expect it to continue to drag after-sales growth.

For Meidong, its after-sales revenue fell 11% YoY to Rmb3.9bn in 2025, as it booked "auto finance commissions" into after-sales. Due to the cancellation of "high interest, high commission" auto finance products, Meidong's after-sales revenue dropped 27% YoY in 2H25, and we think its after-sales revenue continued to decline sharply in 1H26 against a high base. In addition, its "single city, single store" strategy means that once it closes a store in one city, it is difficult to divert existing customers to its other stores.

## Other earnings risks

1. Increasing labor costs: China's social insurance contribution obligation is not something new, but enforcement has become stricter this year. Auto retailing is a labor-intensive business, as it requires sales persons and repair technicians. At the end of 2025, Zhongsheng, Yongda, and Meidong had 30,287, 13,243, and 3,763 employees, respectively.

Any tighter enforcement of employer social insurance contributions, e.g., from minimal-wage-based to actual-wage-based, would lead to higher labor costs from 2026. Together with ongoing operating losses, this could lead many auto dealers to reassess their business outlooks and consider shutdowns as options.

2. Zhongsheng's impairment cost: Goodwill accounted for 6.8% of Zhongsheng's total assets at end-2025, and intangible assets another 7.6% (thus 14.5% in total), much higher than Yongda's 6% and Meidong's 3%. If luxury ICE sales weaken further, we see risk of Zhongsheng booking additional impairment costs. Although impairment does not affect cash flow, it could reduce dividends if the payout ratio is linked to reported earnings.

Stock views and catalysts

<table><tr><td>Company</td><td>What&#x27;s priced in</td><td>What&#x27;s not priced in</td><td>Next catalysts</td></tr><tr><td rowspan="3">Zhongsheng (0881.HK, EW)</td><td>·Weak sales of Mercedes and Lexus in 1H26</td><td>·N/A</td><td>·Mercedes GLC BEV sales volume in July (just launched July 8)</td></tr><tr><td>·Ongoing stake disposal by shareholder Jardine Matheson</td><td></td><td>·Potential extra rebate from Mercedes</td></tr><tr><td>·Expansion of independent repair centers</td><td></td><td>·1H26 results release in late August</td></tr><tr><td rowspan="3">Yongda (3669.HK, UW)</td><td>·Weak sales of BMW and Porsche in 1H26</td><td>·After-sales revenue to decline due to store closures</td><td>·Potential extra rebate from Porsche</td></tr><tr><td>·Rmb8-9K per unit extra rebate offered by BMW for 1H26</td><td>·Earlier-than-peer negative impact from EV due to Yongda&#x27;s store concentration in the Yangtze River Delta region</td><td>·1H26 results release in late August</td></tr><tr><td>·Store openings of EV brands such as Huawei, Xpeng, Smart, etc.</td><td>·Higher-than-expected labor cost due to tighter enforcement of employer social insurance contributions</td><td></td></tr><tr><td rowspan="2">Meidong (1268.HK, UW)</td><td>·Weak sales of Porsche and BMW in 1H26</td><td>·After-sales revenue to decline due to store closures</td><td>·Potential extra rebate from Porsche</td></tr><tr><td>·Rmb8-9K per unit extra rebate offered by BMW for 1H26</td><td>·Faster-than-expected customer loss as Meidong&#x27;s &quot;single city, single store&quot; strategy means once the store is closed, it is difficult to retain customers in that city</td><td>·1H26 results release in late August</td></tr></table>

Income Statement

# Zhongsheng (0881.HK): Financial Summary

Exhibit 6: Zhongsheng's financial summary

<table><tr><td>Rmb Mn</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenue</td><td>168,124</td><td>164,403</td><td>160,364</td><td>159,696</td><td>163,871</td></tr><tr><td>COGS</td><td>157,452</td><td>155,566</td><td>149,523</td><td>146,889</td><td>150,473</td></tr><tr><td>Gross profit</td><td>10,672</td><td>8,838</td><td>10,841</td><td>12,807</td><td>13,398</td></tr><tr><td>Other income &amp; gains</td><td>4,784</td><td>3,067</td><td>1,764</td><td>1,757</td><td>1,803</td></tr><tr><td>Selling expenses</td><td>7,553</td><td>7,827</td><td>7,635</td><td>7,603</td><td>7,802</td></tr><tr><td>Administrative expenses</td><td>2,229</td><td>4,601</td><td>2,233</td><td>2,344</td><td>2,461</td></tr><tr><td>Operating profit</td><td>5,675</td><td>(522)</td><td>2,738</td><td>4,617</td><td>4,938</td></tr><tr><td>Finance costs</td><td>1,573</td><td>1,528</td><td>1,275</td><td>1,275</td><td>1,275</td></tr><tr><td>Share of profit of JCE</td><td>2</td><td>(8)</td><td>(10)</td><td>(12)</td><td>(14)</td></tr><tr><td>Profit before income tax</td><td>4,103</td><td>(2,058)</td><td>1,453</td><td>3,330</td><td>3,649</td></tr><tr><td>Income tax expense</td><td>1,033</td><td>(159)</td><td>363</td><td>832</td><td>912</td></tr><tr><td>Profit after tax</td><td>3,071</td><td>(1,900)</td><td>1,090</td><td>2,497</td><td>2,737</td></tr><tr><td>Minority interest</td><td>(141)</td><td>(226)</td><td>11</td><td>25</td><td>27</td></tr><tr><td>Net profit</td><td>3,212</td><td>(1,673)</td><td>1,079</td><td>2,472</td><td>2,709</td></tr><tr><td>EPS (Rmb)</td><td>1.31</td><td>(0.71)</td><td>0.46</td><td>1.04</td><td>1.14</td></tr></table>

<table><tr><td></td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="6">Growth (%)</td></tr><tr><td>Revenue</td><td>-6%</td><td>-2%</td><td>-2%</td><td>0%</td><td>3%</td></tr><tr><td>Operating profit</td><td>-32%</td><td>N/M</td><td>N/M</td><td>69%</td><td>7%</td></tr><tr><td>Net profit</td><td>-36%</td><td>N/M</td><td>N/M</td><td>129%</td><td>10%</td></tr><tr><td colspan="6">Margins (%)</td></tr><tr><td>GP margin</td><td>6.3%</td><td>5.4%</td><td>6.8%</td><td>8.0%</td><td>8.2%</td></tr><tr><td>OP margin</td><td>3.4%</td><td>-0.3%</td><td>1.7%</td><td>2.9%</td><td>3.0%</td></tr><tr><td>Net margin</td><td>1.9%</td><td>-1.0%</td><td>0.7%</td><td>1.5%</td><td>1.7%</td></tr><tr><td colspan="6">Return (%)</td></tr><tr><td>ROA</td><td>3.0%</td><td>-1.6%</td><td>1.0%</td><td>2.4%</td><td>2.6%</td></tr><tr><td>ROE</td><td>6.9%</td><td>-3.8%</td><td>2.4%</td><td>5.4%</td><td>5.7%</td></tr><tr><td colspan="6">Gearing (%)</td></tr><tr><td>Total liability/asset</td><td>57%</td><td>58%</td><td>57%</td><td>56%</td><td>56%</td></tr><tr><td>Total debt/equity</td><td>76%</td><td>68%</td><td>67%</td><td>64%</td><td>62%</td></tr><tr><td>Net debt/equity</td><td>26%</td><td>21%</td><td>20%</td><td>16%</td><td>13%</td></tr><tr><td colspan="6">Efficiency</td></tr><tr><td>Asset turnover (x)</td><td>1.6</td><td>1.5</td><td>1.5</td><td>1.5</td><td>1.5</td></tr><tr><td>Inventory days</td><td>40.4</td><td>42.7</td><td>43.6</td><td>43.7</td><td>42.6</td></tr><tr><td>Receivables days</td><td>49.3</td><td>51.9</td><td>51.2</td><td>50.7</td><td>50.0</td></tr><tr><td>Payable days</td><td>36.6</td><td>43.7</td><td>48.9</td><td>48.3</td><td>47.3</td></tr><tr><td>Cash days</td><td>53.1</td><td>50.9</td><td>46.0</td><td>46.0</td><td>45.2</td></tr></table>

Balance Sheet

<table><tr><td>Rmb Mn</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="6">Non-current assets</td></tr><tr><td>PPE</td><td>17,324</td><td>17,874</td><td>18,761</td><td>19,508</td><td>20,113</td></tr><tr><td>Intangible assets</td><td>21,302</td><td>18,681</td><td>18,220</td><td>17,756</td><td>17,292</td></tr><tr><td>Long-term investment</td><td>150</td><td>220</td><td>210</td><td>198</td><td>184</td></tr><tr><td>Long-term deferred assets</td><td>548</td><td>594</td><td>594</td><td>594</td><td>594</td></tr><tr><td>Non-current assets</td><td>44,591</td><td>42,422</td><td>42,838</td><td>43,109</td><td>43,236</td></tr><tr><td colspan="6">Current assets</td></tr><tr><td>Inventories</td><td>18,477</td><td>17,934</td><td>17,779</td><td>17,374</td><td>17,737</td></tr><tr><td>Trade receivables</td><td>4,654</td><td>2,963</td><td>2,888</td><td>2,875</td><td>2,953</td></tr><tr><td>Prepayment &amp; other receivable</td><td>19,313</td><td>19,833</td><td>19,346</td><td>19,265</td><td>19,769</td></tr><tr><td>Cash and cash equivalents</td><td>18,688</td><td>15,421</td><td>15,644</td><td>17,156</td><td>18,344</td></tr><tr><td>Other current assets</td><td>4,449</td><td>5,149</td><td>5,149</td><td>5,149</td><td>5,149</td></tr><tr><td>Current assets</td><td>65,580</td><td>61,301</td><td>60,805</td><td>61,820</td><td>63,952</td></tr><tr><td cols

[中间内容因长度限制已省略]

efully before investing.

INDUSTRY COVERAGE: China Autos & Shared Mobility

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/09/2026)</td></tr><tr><td colspan="3">Joey Xu, CFA</td></tr><tr><td>Anhui Jianghuai Automobile (600418.SS)</td><td>E (08/19/2023)</td><td>Rmb24.45</td></tr><tr><td>BAIC Motor (1958.HK)</td><td>E (10/02/2025)</td><td>HK$0.80</td></tr><tr><td>Brilliance China Automotive (1114.HK)</td><td>E (03/31/2025)</td><td>HK$1.98</td></tr><tr><td>Chongqing Changan Automobile (000625.SZ)</td><td>E (03/03/2026)</td><td>Rmb6.94</td></tr><tr><td>Guangzhou Automobile Group (601238.SS)</td><td>U (10/23/2019)</td><td>Rmb5.10</td></tr><tr><td>Guangzhou Automobile Group (2238.HK)</td><td>O (05/05/2020)</td><td>HK$2.16</td></tr><tr><td>Huayu Automotive (600741.SS)</td><td>O (09/08/2020)</td><td>Rmb15.79</td></tr><tr><td>Jiangsu Changshu Automotive Trim Group (603035.SS)</td><td>E (08/14/2023)</td><td>Rmb10.72</td></tr><tr><td>Ningbo Huaxiang Electronic Co., Ltd. (002048.SZ)</td><td>E (05/05/2026)</td><td>Rmb22.60</td></tr><tr><td>SAIC Motor Corp. Ltd. (600104.SS)</td><td>O (11/25/2021)</td><td>Rmb9.91</td></tr><tr><td>Voyah Automotive Technology Co. Ltd, (7489.HK)</td><td>O (03/31/2026)</td><td>HK$3.13</td></tr><tr><td>Zhengzhou Yutong Bus Co (600066.SS)</td><td>E (09/22/2023)</td><td>Rmb28.21</td></tr><tr><td colspan="3">Shelley Wang, CFA</td></tr><tr><td>Beijing Jingwei Hirain Technologies (688326.SS)</td><td>U (09/27/2024)</td><td>Rmb67.95</td></tr><tr><td>Bethel Automotive Safety Systems Co Ltd (603596.SS)</td><td>O (12/11/2023)</td><td>Rmb25.81</td></tr><tr><td>Changzhou Xingyu Automotive Lighting Sys (601799.SS)</td><td>O (09/27/2024)</td><td>Rmb94.93</td></tr><tr><td>China MeiDong Auto Holdings Ltd (1268.HK)</td><td>U (07/10/2026)</td><td>HK$0.51</td></tr><tr><td>China Yongda Automobiles Services (3669.HK)</td><td>U (07/10/2026)</td><td>HK$0.80</td></tr><tr><td>Foryou Corporation (002906.SZ)</td><td>O (03/06/2024)</td><td>Rmb24.70</td></tr><tr><td>Fuyao Glass Industry Group (600660.SS)</td><td>E (12/01/2016)</td><td>Rmb50.68</td></tr><tr><td>Fuyao Glass Industry Group (3606.HK)</td><td>E (12/01/2016)</td><td>HK$50.60</td></tr><tr><td>Huizhou Desay SV Automotive Co Ltd (002920.SZ)</td><td>O (02/28/2025)</td><td>Rmb88.38</td></tr><tr><td>Keboda (603786.SS)</td><td>O (01/17/2024)</td><td>Rmb41.44</td></tr><tr><td>Minth Group Limited (0425.HK)</td><td>O (08/24/2015)</td><td>HK$27.50</td></tr><tr><td>NavInfo Co Ltd (002405.SZ)</td><td>U (03/06/2024)</td><td>Rmb6.38</td></tr><tr><td>Nexteer Automotive Group (1316.HK)</td><td>E (02/28/2025)</td><td>HK$3.93</td></tr><tr><td>Ningbo Joyson Electronic Corp (600699.SS)</td><td>E (03/11/2026)</td><td>Rmb21.21</td></tr><tr><td>Ningbo Tuopu Group Co Ltd (601689.SS)</td><td>E (11/12/2025)</td><td>Rmb55.83</td></tr><tr><td>Ningbo Xusheng Group Co Ltd (603305.SS)</td><td>E (06/18/2025)</td><td>Rmb11.80</td></tr><tr><td>Suzhou Recodeal Interconnect System (688800.SS)</td><td>O (07/02/2026)</td><td>Rmb81.73</td></tr><tr><td>TUHU Car Inc (9690.HK)</td><td>O (07/29/2024)</td><td>HK$13.22</td></tr><tr><td>Zhejiang Sanhua Intelligent Controls (002050.SZ)</td><td>E (11/12/2025)</td><td>Rmb42.85</td></tr><tr><td>Zhongsheng Group Holdings (0881.HK)</td><td>E (07/10/2026)</td><td>HK$5.06</td></tr><tr><td colspan="3">Tim Hsiao</td></tr><tr><td>BAIC BluePark New Energy (600733.SS)</td><td>U (08/07/2024)</td><td>Rmb4.64</td></tr><tr><td>BYD Company Limited (002594.SZ)</td><td>O (04/14/2025)</td><td>Rmb86.87</td></tr><tr><td>BYD Company Limited (1211.HK)</td><td>O (04/14/2025)</td><td>HK$82.65</td></tr><tr><td>EHang Holdings Ltd (EH.O)</td><td>O (03/13/2025)</td><td>US$5.79</td></tr><tr><td>Geely Automobile Holdings (0175.HK)</td><td>O (06/26/2024)</td><td>HK$18.13</td></tr><tr><td>Great Wall Motor Company Limited (601633.SS)</td><td>U (03/16/2022)</td><td>Rmb15.06</td></tr><tr><td>Great Wall Motor Company Limited (2333.HK)</td><td>E (01/08/2024)</td><td>HK$8.49</td></tr><tr><td>Hesai Group (HSAI.O)</td><td>O (07/28/2025)</td><td>US$16.40</td></tr><tr><td>Horizon Robotics (9660.HK)</td><td>O (12/02/2024)</td><td>HK$4.36</td></tr><tr><td>Li Auto Inc. (LI.O)</td><td>O (08/24/2020)</td><td>US$11.91</td></tr><tr><td>Li Auto Inc. (2015.HK)</td><td>O (11/16/2021)</td><td>HK$46.76</td></tr><tr><td>NIO Inc. (9866.HK)</td><td>O (10/03/2022)</td><td>HK$38.04</td></tr><tr><td>NIO Inc. (NIO.N)</td><td>O (08/26/2020)</td><td>US$4.78</td></tr><tr><td>WeRide Inc (WRD.O)</td><td>O (11/19/2024)</td><td>US$5.55</td></tr><tr><td>XPeng Inc. (9868.HK)</td><td>O (11/16/2021)</td><td>HK$50.85</td></tr><tr><td>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$12.98</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
