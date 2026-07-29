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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# Zhejiang Supor - A

## A reset in earnings and dividend; downgrade to Neutral

We downgrade Supor to Neutral as we are less confident in its ability to cushion cost inflation via captive OEM export demand. Supor's preliminary 2Q results (our first take) came as a disappointment, and the analyst briefing gave us little confidence in the company's near-term earnings recovery. After the revision, our FY26-27E EPS suggests $6 - 9\%$ downside to consensus; the bigger risk, in our view, is dividend disappointment, where we see $20\%$ downside to Street DPS expectations - our FY26E DPS is Rmb2.01 or $4.7\%$ yield, vs. consensus at Rmb2.51 or $5.8\%$ . We cut our target multiple to 16x, placing it near 1 STD below historical average (old: 19x, in line with historical average), producing a Jun-27 price target of Rmb45 that only suggests $5\%$ potential upside. Downgrade to Neutral.

\- Downside to 2H revenue expectations. Revenue turned to negative $3\%$ YoY in 2Q, missing our expectation of $4\%$ YoY. The culprit was export. SEB, Supor's $83\%$ -owned parent-co and the source of $90\%$ of its export revenue, seems to be controlling inventory, and it appears that inventory adjustment may continue into 2H, hurting shipment cadence visibility. Domestic business has proven resilient but is not enough to offset the export weakness. We now expect 2H revenue to grow at $3\%$ (old: $4\%$ ) due to lower assumptions for export $(+4\%,$ vs $+7\%$ previously). This compares to Bloomberg consensus of $+7\%$ YoY (FY-1H), suggesting earnings downgrades could continue into 2H.

\- OP momentum disrupted by ongoing commodity cost pressure. GPM likely turned negative 1ppt YoY in 2Q, vs 1.2ppt expansion in 1Q, with export GPM the main drag. Supor locked in commodity prices in Apr-May, but seemingly after the petrochemical cost increase had already materialized. As a result, the lock-in didn't close the gap versus the cost markup pricing agreed with SEB before inflation picked up. Domestic GPM improved YoY on ASP hikes and SG&A was well controlled (-2% YoY), but this was not enough to offset export margin pressure. OP declined 16% YoY in 2Q, deteriorating from +3% in 1Q. Given persistent cost inflation, we now expect 2H OP to decline 3% YoY (old: +6%), despite lapping an easier base, due to lower GPM assumptions for export (16.3%, vs 19% previously).

\- PT and estimate change; Downgrade to Neutral. Supor remains a high-quality operator with solid domestic execution, product innovation and free cash flow generation. The issue is not structural relevance, but near-term earnings risk: export uncertainty, cost pressure, and limited operating leverage now make the prior premium harder to justify. We cut our FY26-27E EPS by 5-9% due to export revenue and GPM cuts, and cut FY26E DPS by 27% due to EPS cuts/lower payout assumption. We also reduce our target multiple by 15% to 16x. Our price target falls by 18% to RMB 45. Supor trades at 16x FY27 P/E on revised JPMe, still at a premium to small appliance peers due to relative stability. Key upside risks include: a more favorable export order recovery, renegotiation of export pricing, and a clearer dividend commitment.

## Neutral

Previous: Overweight

002032.SZ, 002032 CH
Price (27 Jul 26):Rmb42.83

▼Price Target (Jun-27):Rmb45.00  
Prior (Jun-27):Rmb55.00

Co-Head of Asia Pacific Consumer Research and Head of Asia Gaming/Leisure Research

DS Kim AC (852) 2800-8597 ds.kim@JPM.com

Yibo Wu  
(852) 2800-8559  
yibo.wu@JPM.com  
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Key Changes (FYE Dec)

<table><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. EPS - 26E (Rmb)</td><td>2.76</td><td>2.51</td><td>-8.9%</td></tr><tr><td>Adj. EPS - 27E (Rmb)</td><td>2.89</td><td>2.74</td><td>-5.2%</td></tr></table>

Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>64</td><td>58</td><td>66</td><td>60</td><td>52</td></tr><tr><td>Growth</td><td>17</td><td>57</td><td>24</td><td>39</td><td>35</td></tr><tr><td>Momentum</td><td>49</td><td>82</td><td>57</td><td>42</td><td>85</td></tr><tr><td>Quality</td><td>1</td><td>4</td><td>1</td><td>5</td><td>5</td></tr><tr><td>Low Vol</td><td>10</td><td>4</td><td>10</td><td>22</td><td>10</td></tr></table>

Price Performance  
![](images/871781478043f7947f16156352b95f45ae930a5fd0aa0097b6ec9b1f53ef16d1.jpg)  
— 002032.SZ Price (Rmb) — SHEN.B (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>-2.8%</td><td>8.0%</td><td>-9.1%</td><td>-17.2%</td></tr><tr><td>Rel</td><td>6.6%</td><td>5.0%</td><td>-5.0%</td><td>-5.3%</td></tr></table>

<table><tr><td colspan="2">Company Data</td></tr><tr><td>Shares O/S (mn)</td><td>797</td></tr><tr><td>52-week range (Rmb)</td><td>52.75-38.63</td></tr><tr><td>Market cap ($ mn)</td><td>5,039</td></tr><tr><td>Exchange rate</td><td>6.77</td></tr><tr><td>Free float (%)</td><td>16.0%</td></tr><tr><td>3M ADV (mn)</td><td>2.02</td></tr><tr><td>3M ADV ($ mn)</td><td>13.4</td></tr><tr><td>Volatility (90 Day)</td><td>31</td></tr><tr><td>Index</td><td>SZBSHR</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>15|3|1</td></tr></table>

Key Metrics (FYE Dec)

<table><tr><td>Rmb in millions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="5">Financial Estimates</td></tr><tr><td>Revenue</td><td>22,772</td><td>23,035</td><td>23,795</td><td>24,428</td></tr><tr><td>Adj. EBITDA</td><td>2,782</td><td>2,693</td><td>2,889</td><td>3,075</td></tr><tr><td>Adj. EBIT</td><td>2,572</td><td>2,486</td><td>2,681</td><td>2,866</td></tr><tr><td>Adj. net income</td><td>2,097</td><td>2,004</td><td>2,182</td><td>2,340</td></tr><tr><td>Adj. EPS</td><td>2.63</td><td>2.51</td><td>2.74</td><td>2.94</td></tr><tr><td>BBG EPS</td><td>2.69</td><td>2.75</td><td>2.94</td><td>3.06</td></tr><tr><td>Cashflow from operations</td><td>2,649</td><td>2,120</td><td>2,333</td><td>2,483</td></tr><tr><td>FCFF</td><td>2,435</td><td>1,968</td><td>2,162</td><td>2,304</td></tr><tr><td colspan="5">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>1.5%</td><td>1.2%</td><td>3.3%</td><td>2.7%</td></tr><tr><td>Gross margin</td><td>24.9%</td><td>24.4%</td><td>24.8%</td><td>25.1%</td></tr><tr><td>EBITDA margin</td><td>12.2%</td><td>11.7%</td><td>12.1%</td><td>12.6%</td></tr><tr><td>EBIT margin</td><td>11.3%</td><td>10.8%</td><td>11.3%</td><td>11.7%</td></tr><tr><td>Adj. EPS growth</td><td>(6.1%)</td><td>(4.4%)</td><td>8.9%</td><td>7.2%</td></tr><tr><td colspan="5">Ratios</td></tr><tr><td>Adj. tax rate</td><td>19.1%</td><td>19.1%</td><td>19.0%</td><td>19.0%</td></tr><tr><td>Interest cover</td><td>NM</td><td>226.9</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROCE</td><td>32.8%</td><td>32.2%</td><td>33.5%</td><td>32.8%</td></tr><tr><td>ROE</td><td>33.0%</td><td>32.1%</td><td>33.7%</td><td>33.1%</td></tr><tr><td colspan="5">Valuation</td></tr><tr><td>FCFF yield</td><td>7.1%</td><td>5.8%</td><td>6.3%</td><td>6.8%</td></tr><tr><td>Dividend yield</td><td>6.1%</td><td>4.7%</td><td>5.1%</td><td>5.5%</td></tr><tr><td>EV/Revenue</td><td>1.3</td><td>1.3</td><td>1.2</td><td>1.2</td></tr><tr><td>EV/EBITDA</td><td>10.5</td><td>10.9</td><td>10.0</td><td>9.2</td></tr><tr><td>Adj. P/E</td><td>16.3</td><td>17.0</td><td>15.6</td><td>14.6</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

We are Neutral on Supor. Supor remains a high-quality small appliance name in our coverage, supported by resilient domestic execution and solid free cash flow generation. The domestic business remains relatively defensive versus large appliances, with product innovation supporting ASP and margin improvement. However, the export business, about one-third of sales, faces lower order visibility from parent SEB and margin pressure from commodity inflation under pre-agreed OEM pricing. At 16x FY27E P/E with a 4.7% FY26E dividend yield, we see fair risk-reward, as relative stability is balanced by near-term earnings and dividend reset risks. Key upside risks are export recovery and OEM export pricing renegotiation.

## Valuation

We assign a 16x FY27E P/E to Supor, placing it near 1x std below historical average, and arrive at our Jun-27 PT of Rmb45.

![](images/dc73d9684058641b55416734b152e57ca0fa0708db8f510bf925e52672e38195.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Asia Pac ex JP</td><td>-0.03</td><td>0.01</td></tr><tr><td>Region: China</td><td>-0.14</td><td>-0.12</td></tr><tr><td colspan="3">Macro:</td></tr><tr><td>Generic 1st &#x27;CO&#x27; Future</td><td>-0.08</td><td>-0.33</td></tr><tr><td>Markit EM Composite PMI SA</td><td>-0.45</td><td>-0.29</td></tr><tr><td>JPM China A-shares Sentiment</td><td>0.26</td><td>0.24</td></tr><tr><td colspan="3">Quant Styles:</td></tr><tr><td>Value</td><td>-0.13</td><td>-0.09</td></tr><tr><td>Growth</td><td>0.11</td><td>0.07</td></tr><tr><td>Size</td><td>0.00</td><td>0.07</td></tr></table>

## Earnings forecasts

Based on 1H26 preliminary results announcement and analyst briefing, we forecast 2Q26 revenue to decline 3% YoY (China up 2% and overseas down 14%), group GPM to decline 1ppt YoY to 22.3% (China up 0.2ppt to 28.1%; overseas down 6.3ppt to 6.4%), group opex dollars to decline 2% YoY, and NPM to decline 1.2ppt to 6.6%.

Table 1: Supor - Summary of quarterly P&L

<table><tr><td>(Rmb mn, FYE Dec 31)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td>P&amp;L</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>5,786</td><td>5,691</td><td>5,420</td><td>5,874</td><td>5,882</td><td>5,528</td><td>5,581</td><td>6,044</td></tr><tr><td>YoY%</td><td>8%</td><td>2%</td><td>(2%)</td><td>(1%)</td><td>2%</td><td>(3%)</td><td>3%</td><td>3%</td></tr><tr><td>China</td><td>3,793</td><td>3,968</td><td>3,661</td><td>3,912</td><td>3,869</td><td>4,047</td><td>3,734</td><td>4,021</td></tr><tr><td>YoY%</td><td>3%</td><td>4%</td><td>2%</td><td>2%</td><td>2%</td><td>2%</td><td>2%</td><td>3%</td></tr><tr><td>Overseas</td><td>1,993</td><td>1,723</td><td>1,759</td><td>1,963</td><td>2,013</td><td>1,481</td><td>1,847</td><td>2,023</td></tr><tr><td>YoY%</td><td>18%</td><td>(2%)</td><td>(10%)</td><td>(6%)</td><td>1%</td><td>(14%)</td><td>5%</td><td>3%</td></tr><tr><td>(COGS)</td><td>(4,403)</td><td>(4,365)</td><td>(4,123)</td><td>(4,218)</td><td>(4,408)</td><td>(4,296)</td><td>(4,351)</td><td>(4,367)</td></tr><tr><td>GROSS PROFIT</td><td>1,383</td><td>1,326</td><td>1,297</td><td>1,657</td><td>1,474</td><td>1,231</td><td>1,230</td><td>1,677</td></tr><tr><td>GPM%</td><td>23.9%</td><td>23.3%</td><td>23.9%</td><td>28.2%</td><td>25.1%</td><td>22.3%</td><td>22.0%</td><td>27.7%</td></tr><tr><td>China</td><td>1,045</td><td>1,107</td><td>998</td><td>1,235</td><td>1,132</td><td>1,137</td><td>1,008</td><td>1,267</td></tr><tr><td>GPM%</td><td>27.5%</td><td>27.9%</td><td>27.2%</td><td>31.6%</td><td>29.3%</td><td>28.1%</td><td>27.0%</td><td>31.5%</td></tr><tr><td>Overseas</td><td>339</td><td>219</td><td>299</td><td>421</td><td>342</td><td>94</td><td>222</td><td>409</td></tr><tr><td>GPM%</td><td>17.0%</td><td>12.7%</td><td>17.0%</td><td>21.5%</td><td>17.0%</td><td>6.4%</td><td>12.0%</td><td>20.2%</td></tr><tr><td>(OPEX)</td><td>(812)</td><td>(814)</td><td>(809)</td><td>(988)</td><td>(859)</td><td>(797)</td><td>(814)</td><td>(992)</td></tr><tr><td>(Selling expense)</td><td>(581)</td><td>(571)</td><td>(563)</td><td>(694)</td><td>(646)</td><td>(553)</td><td>(569)</td><td>(697)</td></tr><tr><td>(Admin expense)</td><td>(93)</td><td>(105)</td><td>(88)</td><td>(113)</td><td>(87)</td><td>(99)</td><td>(84)</td><td>(110)</td></tr><tr><td>(R&amp;D expense)</td><td>(103)</td><td>(108)</td><td>(127)</td><td>(139)</td><td>(97)</td><td>(116)</td><td>(128)</td><td>(142)</td></tr><tr><td>(Business taxes and surcharges)</td><td>(35)</td><td>(30)</td><td>(31)</td><td>(43)</td><td>(29)</td><td>(29)</td><td>(32)</td><td>(44)</td></tr><tr><td>YoY%</td><td>5%</td><td>7%</td><td>8%</td><td>8%</td><td>6%</td><td>(2%)</td><td>1%</td><td>0%</td></tr><tr><td>(Selling expense)</td><td>5%</td><td>11%</td><td>15%</td><td>12%</td><td>11%</td><td>(3%)</td><td>1%</td><td>0%</td></tr><tr><td>(Admin expense)</td><td>1%</td><td>3%</td><td>(12%)</td><td>11%</td><td>(7%)</td><td>(6%)</td><td>(5%)</td><td>(3%)</td></tr><tr><td>(R&amp;D expense)</td><td>9%</td><td>(2%)</td><td>3%</td><td>(2%)</td><td>(5%)</td><td>8%</td><td>1%</td><td>2%</td></tr><tr><td>(Business taxes and surcharges)</td><td>27%</td><td>(16%)</td><td>(18%)</td><td>(9%)</td><td>(17%)</td><td>(3%)</td><td>3%</td><td>2%</td></tr><tr><td>OPERATING PROFIT (Non-GAAP)</td><td>571</td><td>512</td><td>487</td><td>668</td><td>615</td><td>434</td><td>416</td><td>685</td></tr><tr><td>YoY%</td><td>12%</td><td>(9%)</td><td>(15%)</td><td>(2%)</td><td>8%</td><td>(15%)</td><td>(15%)</td><td>2%</td></tr><tr><td>OPM%</td><td>9.9%</td><td>9.0%</td><td>9.0%</td><td>11.4%</td><td>10.5%</td><td>7.9%</td><td>7.5%</td><td>11.3%</td></tr><tr><td>Other income/(expenses)</td><td>42</td><td>33</td><td>38</td><td>220</td><td>31</td><td>35</td><td>42</td><td>228</td></tr><tr><td>Finance income/(expense)</td><td>7</td><td>7</td><td>5</td><td>(2)</td><td>(8)</td><td>(5)</td><td>1</td><td>0</td></tr><tr><td>OPERATING PROFIT (Reported)</td><td>619</td><td>552</td><td>530</td><td>886</td><td>638</td><td>464</td><td>460</td><td>913</td></tr><tr><td>YoY%</td><td>6%</td><td>(6%)</td><td>(14%)</td><td>(7%)</td><td>3%</td><td>(16%)</td><td>(13%)</td><td>3%</td></tr><tr><td>OPM%</td><td>10.7%</td><td>9.7%</td><td>9.8%</td><td>15.1%</td><td>10.8%</td><td>8.4%</td><td>8.2%</td><td>15.1%</td></tr><tr><td>Non-operating income</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>-</td><td>1</td><td>2</td></tr><tr><td>(Non-operating expenses)</td><td>(1)</td><td>(1)</td><td>(1)</td><td>(2)</td><td>(1)</td><td>(1)</td><td>(1)</td><td>(2)</td></tr><tr><td>Profit before tax</td><td>620</td><td>552</td><td>530</td><td>886</td><td>638</td><td>462</td><td>460</td><td>913</td></tr><tr><td>(Income tax expense)</td><td>(124)</td><td>(110)</td><td>(104)</td><td>(156)</td><td>(133)</td><td>(101)</td><td>(87)</td><td>(152)</td></tr><tr><td>Tax rate %</td><td>(20.1%)</td><td>(19.9%)</td><td>(19.6%)</td><td>(17.6%)</td><td>(20.8%)</td><td>(21.8%)</td><td>(19.0%)</td><td>(16.6%)</td></tr><tr><td>(Minority interest)</td><td>2</td><td>1</td><td>(0)</td><td>0</td><td>(0)</td><td>1</td><td>(0)</td><td>2</td></tr><tr><td>Net profit</td><td>497</td><td>443</td><td>426</td><td>731</td><td>505</td><td>362</td><td>372</td><td>764</td></tr><tr><td>YoY%</td><td>6%</td><td>(6%)</td><td>(13%)</td><td>(10%)</td><td>2%</td><td>(18%)</td><td>(13%)</td><td>5%</td></tr><tr><td>NPM%</td><td>8.6%</td><td>7.8%</td><td>7.9%</td><td>12.4%</td><td>8.6%</td><td>6.6%</td><td>6.7%</td><td>12.6%</td></tr></table>

Source: Company data, JPM estimates

We cut our FY26/27E EPS by 9%/5%, mainly due to export revenue and GPM cuts (Table 2). Post earnings forecast revision, we forecast FY26 sales to grow 1% YoY and net profit to decline 4% YoY, with a net margin of 8.7%. Over FY26-28, we forecast sales/net profit to

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
