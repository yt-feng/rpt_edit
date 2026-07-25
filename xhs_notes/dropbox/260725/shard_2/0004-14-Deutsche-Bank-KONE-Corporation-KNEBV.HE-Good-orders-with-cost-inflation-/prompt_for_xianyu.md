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
# Company KONE Corporation

Rating Buy

Europe
Finland

Capital Goods
Engineering

Reuters
KNEBV.HE

Bloomberg
KNEBV FH

Exchange
HEX

ADR
KNYJY

Ticker
KNEBV

ISIN
US50048H1014

Date
23 July 2026

Forecast Change

Price at 22 Jul 2026 (EUR) 46.72
Price Target (EUR) 67.00
52-week range (EUR) 70.00 - 48.20

# Good orders with cost inflation starting to feature, new TP €67, BUY

Q2 results featured strong order growth with the market reaction tempered by a slight decline in backlog margin, limited group margin expansion and modernisation revenue growth. We see some of these concerns as time-and-place as we update our forecasts. KONE continues to execute well as its market leadership reflects in strong order growth. As we head into H2, the industry faces increased cost inflation with KONE putting through price increases to keep price cost stable with H2 margin expansion now expected at +40bps yr/yr versus +40bps delivered in H1 with DB forecasts slightly ahead on orders but in-line on revenues and adj EBIT vs consensus for the year. We maintain our BUY recommendation as we update our target price to €67.

## Colour on the quarter and revised forecasts

Q2 order intake grew +11% yr/yr in local fx with modernisation >15% with price up in all regions ex China to reflect increased costs with Chinese pricing stable. Management indicated there was a bigger lag between tenders to orders in the Q2 intake with a slight decline in margin. In Maintenance, we expect revenue growth to accelerate slightly as we lap the effects of portfolio management in China with mgmt. reiterating its +HSD growth target as we factor in less M&A. In Modernisation, 15%+ order growth in lc was strong while revenue growth of +7% in lc was weaker than normal. As we head into H2, we expect Modernisation revenue growth to reaccelerate to +LDD against weaker growth comps in the second half. In New Building Solutions (NBS), we make minimal changes to revenue estimates for the remainder of FY26. Management confident on price cost as stable despite increased cost inflation as all regions ex China featured price increases. KONE has locked in pricing on raw materials for the rest of year with cost-pass through provisions on logistics a feature on most contracts. That said, we expect margin expansion for H2 in-line with H1 levels at +c40bps yr/yr as price actions to mitigate cost inflation may lag slightly in terms of impact. We also factor in margin progression in backlog which is an incremental headwind to operational leverage going forward in the short-term.

## Changes to DB estimates as we remain slightly ahead on orders for FY26

Versus our previous estimates, we adjusted our FY26 forecasts as follows; no meaningful change to group orders €9.6bn (+5.5% yr/yr growth in lc), increased our group revenues by +1% now €11.8bn (+5.1% yr/yr growth in lc) and increased our adj. EBIT by +1% now €1.49bn (12.6% margin). Versus consensus, our FY26

## Valuation & Risks

John Kim
Research Analyst
+44-20-754-18699

Gael de-Bray, CFA
Research Analyst
+33-1-4495-6562

<table><tr><td colspan="4">Key changes</td></tr><tr><td>TP</td><td>66.00 to 67.00</td><td>↑</td><td>1.5%</td></tr><tr><td>DB EPS (EUR)</td><td>2.22 to 2.36</td><td>↑</td><td>6.3%</td></tr><tr><td>Revenue (EURm)</td><td>11,701 to 11,815</td><td>↑</td><td>1.0%</td></tr></table>

Source: DB

![](images/9276dbdb0816749af5b0f8f738cd2297274bfac509eba57b6ac1d316cb06eaa7.jpg)

<table><tr><td>Performance (%)</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Absolute</td><td>-1.7</td><td>-16.4</td><td>-12.0</td></tr><tr><td>DJ (.STOXXE)</td><td>-0.7</td><td>4.9</td><td>17.7</td></tr><tr><td colspan="4">Source: DB</td></tr></table>

<table><tr><td colspan="2">Key indicators (FY1)</td></tr><tr><td>ROE (%)</td><td>36.7</td></tr><tr><td>ROA (%)</td><td>11.3</td></tr><tr><td>Net debt/equity (%)</td><td>-40.5</td></tr><tr><td>Book value/share (EUR)</td><td>5.6</td></tr><tr><td>Price/book (x)</td><td>8.4</td></tr><tr><td>Net interest cover (x)</td><td>59.9</td></tr><tr><td>EBIT margin (%)</td><td>11.8</td></tr><tr><td colspan="2">Source: DB</td></tr></table>

estimates are +2% ahead on group orders and in-line on revenue, and adj. EBIT. For FY27, we forecast group orders of €10.2bn (+6% yr/yr in lc), revenue of €12.6bn (+6% yr/yr in lc), and adj. EBIT of €1.69bn (13.4% margin). Versus consensus, our FY27 estimates are +3% ahead on group orders, +1% on revenue, and +1% on adj. EBIT.

## Valuation, target price of €67, BUY

We value KONE as a stand-alone business for now and maintain a target price of €67 (was €66) and a BUY rating. We value KONE using a DCF analysis based on our forecasts through 2030 with a terminal value calculation as we roll forward our valuation. We use a CAPM framework to calculate an 8.2% WACC and a terminal value implying a c17x. Downside risks include potentially severe pricing headwinds, and an inability to drive operational improvements.

<table><tr><td colspan="6">Forecasts and ratios</td></tr><tr><td>Year End Dec 31</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenue (EURm)</td><td>11,098</td><td>11,245</td><td>11,815</td><td>12,628</td><td>13,406</td></tr><tr><td>EBITA (EURm)</td><td>1,296</td><td>1,389</td><td>1,441</td><td>1,740</td><td>1,868</td></tr><tr><td>DB EPS (EUR)</td><td>1.86</td><td>1.97</td><td>2.36</td><td>2.66</td><td>2.85</td></tr><tr><td>P/E (DB EPS) (x)</td><td>24.3</td><td>27.6</td><td>19.8</td><td>17.6</td><td>16.4</td></tr><tr><td>EV/EBITA (x)</td><td>17.8</td><td>19.7</td><td>16.1</td><td>13.0</td><td>11.9</td></tr><tr><td>DPS (EUR)</td><td>1.80</td><td>1.80</td><td>1.83</td><td>2.36</td><td>2.54</td></tr><tr><td>Yield (%)</td><td>4.0</td><td>3.3</td><td>3.9</td><td>5.1</td><td>5.4</td></tr><tr><td colspan="6">Source: DB estimates, company data</td></tr></table>

## Q2 26 - key charts

Figure 1: Qtly order intake and organic order growth  
![](images/2a9aec22c0ff4cdc2b541bc86a6bd6461c64f1a24ab0c7a109b985b4ab82c2b3.jpg)  
Source : DB, Company data

Figure 2: Qtly sales and organic sales growth  
![](images/128f6a61cb81926eaad6d6411a2a49477c90d87c0c296a39ab72f3840ceda6ff.jpg)  
Source : DB, Company data

Figure 3: Adj EBIT and Adj EBIT margin  
![](images/c127bf23ece7127b3888a45d88bacb566b5349b20ddd448c915a5aae528aab81.jpg)  
Source : DB, Company data

Figure 4: FCF (EUR, m)  
![](images/441c8fc9d1265ed5b981823fa6795d00c5b4f6811e2e81f2c4928a1abff21f43.jpg)  
Source : DB, Company data

Figure 5: Organic Sales Growth (YoY, %)  
![](images/f69546ad2ca85c8b0bb851b629d36b54e12715c4f5280a4e635332da6e6719b6.jpg)  
Source : DB, Company data

Figure 6: Adj EBIT Margin (%)  
![](images/d8f9f31e515e842b59363c6c8498b91fcca0ee104dc5939c69ed09c4fa466981.jpg)  
Source : DB, Company data

## Financials

Figure 7: Annual P&L

<table><tr><td>Profit &amp; Loss (EURm)</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Total sales</td><td>9,982</td><td>9,982</td><td>10,514</td><td>10,907</td><td>10,952</td><td>11,098</td><td>11,245</td><td>11,815</td><td>12,628</td><td>13,406</td></tr><tr><td>Growth</td><td>10.0%</td><td>0.0%</td><td>5.3%</td><td>3.7%</td><td>0.4%</td><td>1.3%</td><td>1.3%</td><td>5.1%</td><td>6.9%</td><td>6.2%</td></tr><tr><td>-of which constant fx</td><td>8.2%</td><td>0.6%</td><td>6.4%</td><td>-1.8%</td><td>5.0%</td><td>2.2%</td><td>4.0%</td><td>5.1%</td><td>6.1%</td><td>6.2%</td></tr><tr><td>-of which currency</td><td>1.8%</td><td>-0.6%</td><td>-1.1%</td><td>5.5%</td><td>-4.6%</td><td>-0.9%</td><td>-2.8%</td><td>0.0%</td><td>0.8%</td><td>0.0%</td></tr><tr><td>Cost Of Goods Sold</td><td>-4,022</td><td>-3,958</td><td>-4,297</td><td>-4,458</td><td>-4,168</td><td>-4,335</td><td>-4,180</td><td>-4,029</td><td>-4,386</td><td>-4,773</td></tr><tr><td>Other Expenses</td><td>-4,526</td><td>-4,572</td><td>-4,678</td><td>-5,158</td><td>-5,314</td><td>-5,223</td><td>-5,409</td><td>-6,056</td><td>-6,203</td><td>-6,447</td></tr><tr><td>EBITDA</td><td>1,434</td><td>1,452</td><td>1,539</td><td>1,291</td><td>1,470</td><td>1,541</td><td>1,656</td><td>1,730</td><td>2,039</td><td>2,186</td></tr><tr><td>Margin</td><td>14.4%</td><td>14.5%</td><td>14.6%</td><td>11.8%</td><td>13.4%</td><td>13.9%</td><td>14.7%</td><td>14.6%</td><td>16.1%</td><td>16.3%</td></tr><tr><td>Depreciation &amp; Amortisation</td><td>-242</td><td>-239</td><td>-244</td><td>-259</td><td>-269</td><td>-292</td><td>-320</td><td>-340</td><td>-349</td><td>-368</td></tr><tr><td>DB EBITA</td><td>1,234</td><td>1,247</td><td>1,346</td><td>1,116</td><td>1,295</td><td>1,350</td><td>1,422</td><td>1,540</td><td>1,740</td><td>1,868</td></tr><tr><td>Margin</td><td>12.4%</td><td>12.5%</td><td>12.8%</td><td>10.2%</td><td>11.8%</td><td>12.2%</td><td>12.6%</td><td>13.0%</td><td>13.8%</td><td>13.9%</td></tr><tr><td>Adj EBIT</td><td>1,237</td><td>1,251</td><td>1,310</td><td>1,077</td><td>1,248</td><td>1,303</td><td>1,369</td><td>1,488</td><td>1,690</td><td>1,818</td></tr><tr><td>Margin</td><td>12.4%</td><td>12.5%</td><td>12.5%</td><td>9.9%</td><td>11.4%</td><td>11.7%</td><td>12.2%</td><td>12.6%</td><td>13.4%</td><td>13.6%</td></tr><tr><td>Items affecting comparability</td><td>-45</td><td>-38</td><td>-15</td><td>-45</td><td>-48</td><td>-54</td><td>-33</td><td>-98</td><td>0</td><td>0</td></tr><tr><td>Reported EBIT</td><td>1,192</td><td>1,213</td><td>1,295</td><td>1,031</td><td>1,200</td><td>1,249</td><td>1,336</td><td>1,390</td><td>1,690</td><td>1,818</td></tr><tr><td>Margin</td><td>11.9%</td><td>12.2%</td><td>12.3%</td><td>9.5%</td><td>11.0%</td><td>11.3%</td><td>11.9%</td><td>11.8%</td><td>13.4%</td><td>13.6%</td></tr><tr><td>Associate income</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Extraordinary items</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Net financial items</td><td>-9</td><td>11</td><td>-9</td><td>-9</td><td>6</td><td>5</td><td>-8</td><td>-23</td><td>70</td><td>76</td></tr><tr><td>Pre-tax profit</td><td>1,184</td><td>1,224</td><td>1,287</td><td>1,023</td><td>1,206</td><td>1,254</td><td>1,327</td><td>1,367</td><td>1,760</td><td>1,894</td></tr><tr><td>DB Pre-tax profit</td><td>1,220</td><td>1,261</td><td>1,323</td><td>1,062</td><td>1,253</td><td>1,301</td><td>1,380</td><td>1,517</td><td>1,810</td><td>1,944</td></tr><tr><td>Taxes</td><td>-279</td><td>-277</td><td>-298</td><td>-244</td><td>-275</td><td>-293</td><td>-335</td><td>-317</td><td>-405</td><td>-436</td></tr><tr><td>Profit from discontinued operation</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Minority interests</td><td>-7</td><td>-8</td><td>-9</td><td>-10</td><td>-6</td><td>-10</td><td>-12</td><td>-13</td><td>-16</td><td>-17</td></tr><tr><td>Net profit</td><td>898</td><td>939</td><td>980</td><td>769</td><td>926</td><td>951</td><td>980</td><td>1,037</td><td>1,339</td><td>1,441</td></tr><tr><td>DB EPS (full dilution)</td><td>1.79</td><td>1.87</td><td>1.95</td><td>1.54</td><td>1.86</td><td>1.86</td><td>1.97</td><td>2.36</td><td>2.66</td><td>2.85</td></tr></table>

Source : DB, Company data

Figure 8: Annual cash flow statement

<table><tr><td>Cash flow statement (EURm)</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>EBIT</td><td>1,193</td><td>1,213</td><td>1,295</td><td>1,031</td><td>1,200</td><td>1,249</td><td>1,336</td><td>1,390</td><td>1,690</td><td>1,818</td></tr><tr><td>Depreciation &amp; amortisation</td><td>242</td><td>239</td><td>244</td><td>259</td><td>269</td><td>292</td><td>320</td><td>340</td><td>349</td><td>368</td></tr><tr><td>Chg in provisions/other adj</td><td>-16</td><td>-36</td><td>-119</td><td>58</td><td>24</td><td>-49</td><td>61</td><td>166</td><td>63</td><td>66</td></tr><tr><td>Change in working capital</td><td>116</td><td>456</td><td>246</td><td>-533</td><td>-68</td><td>122</td><td>91</td><td>13</td><td>-17</td><td>-16</td></tr><tr><td>Operating Cash Flow</td><td>1,534</td><td>1,872</td><td>1,667</td><td>816</td><td>1,425</td><td>1,614</td><td>1,808</td><td>1,908</td><td>2,085</td><td>2,235</td></tr><tr><td>Net interest</td><td>23</td><td>12</td><td>27</td><td>34</td><td>3</td><td>5</td><td>-8</td><td>-23</td><td>70</td><td>76</td></tr><tr><td>Tax paid</td><td>-287</td><td>-333</td><td>-328</td><td>-275</td><td>-304</td><td>-351</td><td>-441</td><td>-390</td><td>-405</td><td>-436</td></tr><tr><td>Cash Earnings</td><td>1,270</td><td>1,550</td><td>1,365</td><td>574</td><td>1,125</td><td>1,268</td><td>1,358</td><td>1,495</td><td>1,750</td><td>1,876</td></tr><tr><td>Net investments fixed assets</td><td>-98</td><td>-88</td><td>-97</td><td>-101</td><td>-148</td><td>-120</td><td>-120</td><td>-118</td><td>-126</td><td>-134</td></tr><tr><td>Free Cash Flow pre dividend</td><td>1,172</td><td>1,462</td><td>1,269</td><td>473</td><td>977</td><td>1,148</td><td>1,238</td><td>1,377</td><td>1,624</td><td>1,742</td></tr><tr><td>% of EBIT</td><td>98%</td><td>121%</td><td>98%</td><td>46%</td><td>81%</td><td>92%</td><td>93%</td><td>99%</td><td>96%</td><td>96%</td></tr><tr><td>Dividend</td><td>-852</td><td>-881</td><td>-1,166</td><td>-1,088</td><td>-905</td><td>-906</td><td>-932</td><td>-932</td><td>-948</td><td>-1,224</td></tr><tr><td>Free Cash Flow post div</td><td>320</td><td>582</td><td>102</td><td>-615</td><td>72</td><td>243</td><td>306</td><td>445</td><td>676</td><td>518</td></tr><tr><td>% of EBIT</td><td>27%</td><td>48%</td><td>8%</td><td>-60%</td><td>6%</td><td>19%</td><td>23%</td><td>32%</td><td>40%</td><td>28%</td></tr><tr><td>Acquisitions</td><td>-27</td><td>-27</td><td>-35</td><td>-32</td><td>-172</td><td>-167</td><td>-164</td><td>-50</td><td>-50</td><td>-50</td></tr><tr><td>Disposals</td><td>0</td><td>5</td><td>11</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Issue of share capital/buyback</td><td>34</td><td>-4</td><td>-47</td><td>-58</td><td>-1</td><td>-20</td><td>-6</td><td>24</td><td>0</td><td>0</td></tr><tr><td>Other</td><td>-317</td><td>-740</td><td>-249</td><td>755</td><td>45</td><td>112</td><td>-202</td><td>331</td><td>-50</td><td>-50</td></tr><tr><td>Currency movement on cash</td><td>16</td><td>-20</td><td>249</td><td>-46</td><td>-15</td><td>-17</td><td>-70</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Net cashflow</td><td>27</td><td>-205</td><td>32</td><td>5</td><td>-71</td><td>151</td><td>-136</td><td>749</td><td>576</td><td>418</td></tr><tr><td colspan="11"></td></tr><tr><td>Change in net debt</td><td>136</td><td>-407</td><td>-207</td><td>887</td><td>283</td><td>183</td><td>131</td><td>-343</td><td>-576</td><td>-418</td></tr><tr><td>Net debt (including pension)</td><td>-1,570</td><td>-1,977</td><td>-2,183</td><td>-1,297</td><td>-1,014</td><td>-831</td><td>-700</td><td>-1,043</td><td>-1,619</td><td>-2,037</td></tr></table>

Source : DB, Company data

<table><tr><td>Model updated: 22 July 2026</td></tr><tr><td>Running the numbers</td></tr><tr><td>Europe</td></tr><tr><td>Finland</td></tr><tr><td>Engineering</td></tr><tr><td>KONE Corporation</td></tr></table>

<table><tr><td>Price (22 Jul 26)</td><td>EUR 46.72</td></tr><tr><td>Target Price</td><td>EUR 67.00</td></tr><tr><td>52 Week range</td><td>EUR 48.20 - 70.00</td></tr><tr><td>Market cap (m)</td><td>EURm 24,214USDm 27,617</td></tr></table>

## Company Profile

KONE Oyj is an international engineering and service company employing 60,000+ people across c60 countries worldwide. It was founded in 1910 and is headquartered in Espoo near Helsinki, Finland. Kone builds and services moving walkways, automatic doors and gates, escalators and lifts

[中间内容因长度限制已省略]

ted performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South Tower,Singapore 048583TeL: +65 6423 8001</td></tr></table>

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

## International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
