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
§ = Consensus data is provided by Refinitiv Estimates

\*\* = Based on consensus methodology

ASMPT Ltd | Asia Pacific

# 2Q26 Preview: OSAT and PCB – Dual Growth Engines

ASMPT Ltd (0522.HK, 522 HK)

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>HK$188.00</td><td>HK$248.00</td></tr></table>

Strong capital spending plans by both OSAT and PCB companies in 2026 should support continued growth in ASMPT's semiconductor solutions and SMT businesses. We raise our price target to HK\$248 and reiterate our OW rating.

Strong OSAT and PCB capex momentum: Our bottom-up analysis shows OSAT capex is now likely to grow by another 45% in 2026 (Exhibit 5), compared with 34% in our 1Q26 preview note (link). Moreover, OSAT pricing is on an up-trend on the back of high utilization and strong demand. Recently, ASE raised advanced packaging quotes by more than 20% (link) and China OSATs also raised prices by 5-10% in general. As for ASMPT's SMT business, sales growth has historically shown a strong correlation with PCB companies' capex (Exhibit 6). This year, PCB companies are also expanding capex aggressively by around 69%, driven by increased AI demand. We expect ASMPT's semi solutions and SMT businesses to record strong sales growth on the back of its customers' strong capex trend.

A mixed TCB picture; logic remains strong, while some slowdown in HBM: We expect TSMC's CoWoS capacity to grow to 200kwpm by the end of 2027 (link), and that ASMPT will benefit as the sole supplier of CoWoS-L on-substrate TCB. While HBM production uses TCB, we see slower order momentum for related equipment. One potential reason is that memory manufacturers currently generate higher profitability by allocating DRAM dies to server DRAM production rather than HBM.

Key focus areas for the results: (1) TCB order wins in both HBM and logic, particularly TCB for chip-to-wafer (C2W) process; (2) photonics order momentum and visibility into orders for CPO-related tools; (3) organizational updates, including the new CEO appointment and planned business divestitures; (4) progress in hybrid bonding; and (5) demand trends from auto and industrial customers for SMT equipment.

Raise PT to HK\$248, OW: We adjust our model and raise our 2026-28e EPS by 7%, 10%, and 10%, respectively, reflecting stronger growth in both the semi solutions and SMT segments. We expect ASMPT to benefit from ongoing semi capacity expansion and robust AI-related demand. We find valuation attractive at 30x 2027e P/E, below its peers Besi at 35x and Hanmi at 43x.

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Daisy Dai, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Daisy.Dai@morganstanley.com</td><td>+852 2848-7310</td></tr><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Charlie Chan</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Charlie.Chan@morganstanley.com</td><td>+886 2 2730-1725</td></tr><tr><td colspan="2">Daniel Yen, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Daniel.Yen@morganstanley.com</td><td>+886 2 2730-2863</td></tr><tr><td colspan="2">Tiffany Yeh</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Tiffany.Yeh@morganstanley.com</td><td>+886 2 7712-3032</td></tr><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Ethan Jia</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Ethan.Jia@morganstanley.com</td><td>+852 3963-2287</td></tr></table>

![](images/42751228d6c06e2b7f35be207bf8faf0b512b298b949bc65ab858a887c3d32ca.jpg)

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>HK$248.00</td></tr><tr><td>Up/downside to price target (%)</td><td>21</td></tr><tr><td>Shr price, close (Jul 3, 2026)</td><td>HK$204.80</td></tr><tr><td>52-Week Range</td><td>HK$244.40-56.79</td></tr><tr><td>Sh out, dil, curr (mn)</td><td>398</td></tr><tr><td>Mkt cap, curr (mn)</td><td>HK$81,430</td></tr><tr><td>EV, curr (mn)</td><td>HK$73,755</td></tr><tr><td>Avg daily trading value (mn)</td><td>HK$332</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS (HK$)**</td><td>2.17</td><td>3.94</td><td>6.76</td><td>9.41</td></tr><tr><td>Prior EPS (HK$)**</td><td>-</td><td>3.67</td><td>6.14</td><td>8.58</td></tr><tr><td>EPS (HK$)§</td><td>1.40</td><td>3.79</td><td>5.71</td><td>7.11</td></tr><tr><td>Revenue, net (HK$ mn)</td><td>14,521</td><td>18,293</td><td>21,822</td><td>25,482</td></tr><tr><td>EBITDA (HK$ mn)</td><td>1,937</td><td>3,081</td><td>4,764</td><td>6,418</td></tr><tr><td>ModelWare net inc (HK $ mn)</td><td>902</td><td>1,648</td><td>2,827</td><td>3,936</td></tr><tr><td>P/E</td><td>35.5</td><td>52.0</td><td>30.3</td><td>21.8</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Preview to earnings

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">ASMPT Ltd 0522.HK</td></tr><tr><td>B/B ratio</td><td>↑ Likely upside surprise</td><td>↑ Modest revision higher</td></tr></table>

\- For 3Q26, we expect ASMPT's revenue growth momentum to continue and revenue to rise $9\%$ QoQ and $34\%$ YoY.

• We expect ASMPT to benefit from higher utilization and strong capex by OSAT and PCB companies.

\- We expect logic TCB orders to remain strong, while demand for HBM TCB orders are likely to be slow.

\*Likely impact to consensus EPS is for the next 12 months

Source: Company data, MS

# 2Q26 Preview and 3Q26 Outlook

Exhibit 1: ASMPT: 2Q26 preview

<table><tr><td>(HK$ mn)</td><td>2Q26</td><td>Q/Q</td><td>Y/Y</td><td>2Q26 guidance</td><td>Cons 2Q26e</td><td>Diff.</td></tr><tr><td>Net sales</td><td>4,498</td><td>10%</td><td>32%</td><td>~US$570mn at mid-point</td><td>4,442</td><td>1%</td></tr><tr><td>Gross profit</td><td>1,820</td><td>14%</td><td>35%</td><td></td><td>1,755</td><td>4%</td></tr><tr><td>Operating profit</td><td>519</td><td>52%</td><td>206%</td><td></td><td>456</td><td>14%</td></tr><tr><td>Pretax Income</td><td>540</td><td>34%</td><td>392%</td><td></td><td>463</td><td>17%</td></tr><tr><td>Net income</td><td>405</td><td>60%</td><td>202%</td><td></td><td>344</td><td>18%</td></tr><tr><td>Reported EPS</td><td>0.97</td><td></td><td></td><td></td><td>0.82</td><td>18%</td></tr><tr><td colspan="7">Margins</td></tr><tr><td>Gross margin</td><td>40.5%</td><td>1.3ppt</td><td>0.8ppt</td><td></td><td>39.5%</td><td>1.0ppt</td></tr><tr><td>Operating margin</td><td>11.5%</td><td>3.1ppt</td><td>6.6ppt</td><td></td><td>10.3%</td><td>1.3ppt</td></tr><tr><td>Net margin</td><td>9.0%</td><td>2.8ppt</td><td>5.1ppt</td><td></td><td>7.7%</td><td>1.3ppt</td></tr></table>

Source: Company data, Bloomberg, MS estimates.

Exhibit 2: ASMPT: 3Q26 outlook

<table><tr><td>(HK$ mn)</td><td>3Q26</td><td>Q/Q</td><td>Y/Y</td><td>Cons 3Q26e</td><td>Diff</td></tr><tr><td>Net sales</td><td>4,921</td><td>9%</td><td>34%</td><td>4,712</td><td>4%</td></tr><tr><td>Gross profit</td><td>2,024</td><td>11%</td><td>55%</td><td>1,835</td><td>10%</td></tr><tr><td>Operating profit</td><td>653</td><td>26%</td><td>1194%</td><td>526</td><td>24%</td></tr><tr><td>Pretax Income</td><td>674</td><td>25%</td><td>-405%</td><td>462</td><td>46%</td></tr><tr><td>Net income</td><td>507</td><td>25%</td><td>-289%</td><td>401</td><td>26%</td></tr><tr><td>Reported EPS</td><td>1.21</td><td></td><td></td><td>0.99</td><td></td></tr><tr><td colspan="6">Margins</td></tr><tr><td>Gross margin</td><td>41.1%</td><td>0.7ppt</td><td>5.5ppt</td><td>38.9%</td><td>2.2ppt</td></tr><tr><td>Operating margin</td><td>13.3%</td><td>1.7ppt</td><td>11.9ppt</td><td>11.2%</td><td>2.1ppt</td></tr><tr><td>Net margin</td><td>10.3%</td><td>1.3ppt</td><td>17.6ppt</td><td>8.5%</td><td>1.8ppt</td></tr></table>

Source: Company data, FactSet, MS estimates.

## Key Cycle Charts to Watch

Exhibit 3: The assembly (back-end) market is typically strongly correlated to semi-unit growth; we expect double-digit growth in 2026  
![](images/fb68a6694871276e0e236497631511eb9ea4661e06821d68d769d3d9e5d94c59.jpg)  
Source: WSTS, Bloomberg, e = MS estimates.

Exhibit 4: OSAT utilization at high levels in 1Q26  
![](images/4bef950400fd1b08fb2c09bfe5059f453062cd36311a8bc41ff30c1a762333d4.jpg)  
Source: Company data, MS.

Exhibit 5: OSAT capex is likely to grow 45% in 2026, marking the 3rd consecutive year of capex increase  
![](images/85d5d8cc896fbee01cf6f014a698285bef6f1c32d93c64d7e4d537fb9a443b2f.jpg)  
Source: Company data, Bloomberg, MS (E) estimates.

Exhibit 6: ASMPT's SMT revenue growth is correlated with PCB  
![](images/54759581a0d7a75dd791e938072721a7402e6bf4784139dc533ed8fef061e0e3.jpg)  
Source: Company data, Bloomberg, MS (E) estimates.

Exhibit 7: Besi B/B ratio well above 1  
![](images/24d0988f939cf362d7e85f1495dd4a976e236ada135500752778464b3a921679.jpg)  
Source: Company data, MS.

Exhibit 8: ASMPT quarterly orders reached its highest level in the past 4 years  
![](images/ffb2c8cdcf1cd500571ad4432d7ed47572cdb780885ab2f1b1adc502d85538be.jpg)  
Source: Company data, MS.

Estimate Revisions

We raise our 2026/27/28e EPS by 7%/10%/10%: On the back of stronger OSAT and PCB capex, we raise our sales forecasts for the semi solutions and SMT businesses, which we now expect to grow by 30% and 27% YoY, respectively. We expect the revenue growth momentum in 1H26 to continue in 2027 and 2028. Our margin assumptions are slightly up, mainly reflecting the higher mix of semi solutions, which carries a higher margin.

Exhibit 9: ASMPT: Summary of estimate changes

<table><tr><td>(HK$ mn)</td><td>New 2026e</td><td>Last published 2026e</td><td>Diff.</td><td>New 2027e</td><td>Last published 2027e</td><td>Diff.</td><td>New 2028e</td><td>Last published 2028e</td><td>Diff.</td></tr><tr><td>Net sales</td><td>18,293</td><td>18,089</td><td>1%</td><td>21,822</td><td>20,840</td><td>5%</td><td>25,482</td><td>24,187</td><td>5%</td></tr><tr><td>Gross profit</td><td>7,442</td><td>7,272</td><td>2%</td><td>9,273</td><td>8,830</td><td>5%</td><td>10,979</td><td>10,399</td><td>6%</td></tr><tr><td>Operating profit</td><td>2,134</td><td>1,984</td><td>8%</td><td>3,718</td><td>3,371</td><td>10%</td><td>5,198</td><td>4,732</td><td>10%</td></tr><tr><td>Pretax Income</td><td>2,256</td><td>2,106</td><td>7%</td><td>3,761</td><td>3,414</td><td>10%</td><td>5,240</td><td>4,775</td><td>10%</td></tr><tr><td>Net income</td><td>1,648</td><td>1,536</td><td>7%</td><td>2,827</td><td>2,567</td><td>10%</td><td>3,936</td><td>3,587</td><td>10%</td></tr><tr><td>Reported EPS</td><td>3.94</td><td>3.67</td><td>7%</td><td>6.76</td><td>6.14</td><td>10%</td><td>9.41</td><td>8.58</td><td>10%</td></tr><tr><td colspan="10">Margins</td></tr><tr><td>Gross margin</td><td>40.7%</td><td>40.2%</td><td></td><td>42.5%</td><td>42.4%</td><td></td><td>43.1%</td><td>43.0%</td><td></td></tr><tr><td>Operating margin</td><td>11.7%</td><td>11.0%</td><td></td><td>17.0%</td><td>16.2%</td><td></td><td>20.4%</td><td>19.6%</td><td></td></tr><tr><td>Net margin</td><td>9.0%</td><td>8.5%</td><td></td><td>13.0%</td><td>12.3%</td><td></td><td>15.4%</td><td>14.8%</td><td></td></tr></table>

Source: MS (e) estimates.

Exhibit 10: ASMPT: Semi-annual financials

<table><tr><td>(HK$ mn)</td><td>1H25</td><td>2H25</td><td>1H26e</td><td>2H26e</td><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td></tr><tr><td>Revenue</td><td>6,526</td><td>7,995</td><td>8,464</td><td>9,721</td><td>14,521</td><td>18,293</td><td>21,822</td><td>25,482</td></tr><tr><td>Semiconductor Solutions (SEMI)</td><td>4,000</td><td>3,692</td><td>4,545</td><td>5,467</td><td>7,692</td><td>10,011</td><td>12,583</td><td>14,921</td></tr><tr><td>SMT</td><td>2,526</td><td>3,928</td><td>3,920</td><td>4,254</td><td>6,454</td><td>8,174</td><td>9,239</td><td>10,561</td></tr><tr><td>Seq %</td><td>-3.3%</td><td>22.5%</td><td>5.9%</td><td>14.8%</td><td></td><td></td><td></td><td></td></tr><tr><td>Y/Y %</td><td>0.7%</td><td>18.5%</td><td>29.7%</td><td>21.6%</td><td>9.8%</td><td>26.0%</td><td>19.3%</td><td>16.8%</td></tr><tr><td>Cost of Goods (inc. depreciation)</td><td>3,897</td><td>5,173</td><td>5,050</td><td>5,693</td><td>9,070</td><td>10,850</td><td>12,548</td><td>14,503</td></tr><tr><td>Percent of Revenues</td><td>59.7%</td><td>64.7%</td><td>59.7%</td><td>58.6%</td><td>62.5%</td><td>59.3%</td><td>57.5%</td><td>56.9%</td></tr><tr><td>Gross Profit</td><td>2,630</td><td>2,822</td><td>3,414</td><td>4,028</td><td>5,451</td><td>7,442</td><td>9,273</td><td>10,979</td></tr><tr><td>Gross margin</td><td>40.3%</td><td>35.3%</td><td>40.3%</td><td>41.4%</td><td>37.5%</td><td>40.7%</td><td>42.5%</td><td>43.1%</td></tr><tr><td>Other Revenue (Interest Income)</td><td>80</td><td>110</td><td>87</td><td>120</td><td>190</td><td>207</td><td>200</td><td>200</td></tr><tr><td>Selling Expense</td><td>756</td><td>829</td><td>872</td><td>988</td><td>1,584</td><td>1,861</td><td>2,141</td><td>2,247</td></tr><tr><td>Percent of Revenues</td><td>11.6%</td><td>10.4%</td><td>10.3%</td><td>10.2%</td><td>10.9%</td><td>10.2%</td><td>9.8%</td><td>8.8%</td></tr><tr><td>General Administrative Expenses</td><td>527</td><td>671</td><td>602</td><td>622</td><td>1,197</td><td>1,224</td><td>1,010</td><td>1,010</td></tr><tr><td>Percent of Revenues</td><td>8.1%</td><td>8.4%</td><td>7.1%</td><td>6.4%</td><td>8.2%</td><td>6.7%</td><td>4.6%</td><td>4.0%</td></tr><tr><td>Net R &amp; D Expenses</td><td>1,017</td><td>1,038</td><td>1,080</td><td>1,145</td><td>2,056</td><td>2,224</td><td>2,404</td><td>2,524</td></tr><tr><td>Percent of Revenues</td><td>15.6%</td><td>13.0%</td><td>12.8%</td><td>11.8%</td><td>14.2%</td><td>12.2%</td><td>11.0%</td><td>9.9%</td></tr><tr><td>Operating Profit</td><td>330</td><td>285</td><td>861</td><td>1,273</td><td>614</td><td>2,134</td><td>3,718</td><td>5,198</td></tr><tr><td>Percent of Revenues</td><td>5%</td><td>4%</td><td>10%</td><td>13%</td><td>4.2%</td><td>11.7%</td><td>17.0%</td><td>20.4%</td></tr><tr><td>Finance Costs</td><td>90</td><td>79</td><td>78</td><td>79</td><td>169</td><td>157</td><td>157</td><td>157</td></tr><tr><td>Profit Before Tax</td><td>216</td><td>1,047</td><td>942</td><td>1,314</td><td>1,263</td><td>2,256</td><td>3,761</td><td>5,240</td></tr><tr><td>Taxes</td><td>(4)</td><td>364</td><td>286</td><td>328</td><td>361</td><td>615</td><td>940</td><td>1,310</td></tr><tr><td>Tax Rate %</td><td>-2%</td><td>35%</td><td>30%</td><td>25%</td><td>28.6%</td><td>27.2%</td><td>25.0%</td><td>25.0%</td></tr><tr><td>Minority</td><td>2</td><td>(2)</td><td>(3)</td><td>(3)</td><td>(0)</td><td>(6)</td><td>(6)</td><td>(6)</td></tr><tr><td>Net Profit</td><td>218</td><td>684</td><td>659</td><td>989</td><td>902</td><td>1,648</td><td>2,827</td><td>3,936</td></tr><tr><td>Percent of Revenues</td><td>3%</td><td>9%</td><td>8%</td><td>10%</td><td>6.2%</td><td>9.0%</td><td>13.0%</td><td>15.4%</td></tr><tr><td>Y/Y %</td><td>-30.9%</td><td>2159.2%</td><td>202.9%</td><td>44.5%</td><td>161.2%</td><td>82.7%</td><td>71.6%</td><td>3

[中间内容因长度限制已省略]

gy Co., Ltd. (688041.SS)</td><td>O (07/03/2026)</td><td>Rmb339.00</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$56.80</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb95.09</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$31.50</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb141.41</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb126.71</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb83.20</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb29.65</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb131.44</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$954.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,520.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$16,270.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$118.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb115.64</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb654.29</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$144.50</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$372.00</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb268.68</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$538.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$174.00</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$639.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$72.60</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$769.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb57.15</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$183.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$110.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$219.00</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb174.77</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb681.80</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,035.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$574.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$13.15</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,800.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$6,855.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$300.71</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$8,915.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

INDUSTRY COVERAGE: Technology - European Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/03/2026)</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>ASML Holding NV (ASML.AS)</td><td>O (09/22/2025)</td><td>€1,634.40</td></tr><tr><td>Infineon Technologies AG (IFXGn.DE)</td><td>O (02/06/2025)</td><td>€77.38</td></tr><tr><td>STMicroelectronics NV (STMPA.PA)</td><td>O (03/26/2026)</td><td>€62.78</td></tr><tr><td colspan="3">Nigel van Putten</td></tr><tr><td>Aixtron SE (AIXGn.DE)</td><td>E (05/25/2023)</td><td>€49.28</td></tr><tr><td>ASM International NV (ASMI.AS)</td><td>O (06/19/2024)</td><td>€975.60</td></tr><tr><td>BE Semiconductor Industries NV (BESI.AS)</td><td>O (11/07/2022)</td><td>€273.10</td></tr><tr><td>Melexis N.V. (MLXS.BR)</td><td>E (02/05/2026)</td><td>€78.55</td></tr><tr><td>Nordic Semiconductor ASA (NOD.OL)</td><td>E (02/10/2025)</td><td>NKr 182.20</td></tr><tr><td>Soitec SA (SOIT.PA)</td><td>O (03/26/2026)</td><td>€117.30</td></tr><tr><td>VAT Group AG (VACN.S)</td><td>E (03/21/2025)</td><td>SFr 709.40</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
