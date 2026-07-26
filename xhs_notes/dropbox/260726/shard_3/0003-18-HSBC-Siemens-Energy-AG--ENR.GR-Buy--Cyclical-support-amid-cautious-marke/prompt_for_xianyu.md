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
# Siemens Energy AG (ENR GR)

## Buy: Cyclical support amid cautious market mood

Expected rise in GW commitments for GS in H2 underlines ongoing market backdrop strength for gas turbines

\- Structural drivers for GT look robust and Gamesa’s march towards profitability in H2 can provide relief

◆ Lift TP to EUR205 (from EUR190) on higher peer multiple and estimates; weak share price run helps derisk Q3 results

## An eventful Q3 results in store

With shares -19% since 24 April 2026 highs (vs. FTSE World Industrials +1%), we believe upcoming Q3 FY26 results for Siemens Energy (ENR) on 5 August are to an extent derisked. We see potential for further guidance increases, particularly on FCF, given the strong demand backdrop.

## Gas Services (GS): debate is about the cycle

Judging from Q2-26 results from main peer GE Vernova (GEV US, USD985.03, TP USD1,040, Hold), the key debates in gas power are around the pace of turbine order growth in H2-26 and 2027 and demand-supply balance in 2030 and beyond (see Q2 earnings miss with cyclical reassurance, 23 July 2026). Both GEV and ENR have indicated further growth in overall GW commitments (ENR to 90-100GW by FY26 and GEV to 125GW by YE-26) with pace of conversion of slot reservation agreements (SRA) driving strong firm backlog growth (see p. 3). ENR sees strong market demand in Q3 FY26 and expects a strong start to FY27 after a weaker Q4, based on a 110-120GW sustained annual market for gas turbines (including combined-cycle) for the coming years. This contrasts with more conservative guidance from MHI (7011 JT, JPY3,892, n/c) issued in May of falling y-o-y orders and 70-100GW of global demand for gas turbines in 2026.

## Grid Technologies (GT): a more structural story

We see more resilient order intake for grid equipment, driven by broader electrification trends and refurbishment / expansion needs for legacy grids. High market growth is driving positive pricing in US, with pricing more stable in Europe.

## Siemens Gamesa: inching towards profitability in H2

We expect Gamesa to reach profitability in H2 FY26 after years of losses (see p. 3) thanks to high volume deliveries in offshore. We note a wider debate about offshore delivery fading in 2028-29 from current high levels but believe that rising auction volumes and better visibility post 2030 in Europe can allay shorter-term headwinds.

## Maintain Buy and raise TP to EUR205 from EUR190

We marginally adjust top-line estimates and our more positive view of margin growth for GT and GS to FY28 leads to an overall 10-30bps margin increase in FY26e/28e. Based on an unchanged $15\%$ discount to GEV's 2028e EV/EBITDA multiple, we derive a new TP of EUR205 (up from EUR190). With implied upside of $35\%$ , we retain Buy on ENR.

## Equities

Energy Equipment & Services

Germany

![](images/4237ad22318bb04ec6b72e721bc275928b304f88aa2d202296f9841e7e014d0a.jpg)

## MAINTAIN BUY

TARGET PRICE (EUR)

205.00

PREVIOUS TARGET (EUR)

190.00

SHARE PRICE (EUR) UPSIDE/DOWNSIDE

152.32 +34.6%

(as of 22 Jul 2026)

## MARKET DATA

<table><tr><td>Market cap (EURm)</td><td>131,164</td></tr><tr><td>Market cap (USDm)</td><td>149,677</td></tr><tr><td>3m ADTV (USDm)</td><td>576</td></tr></table>

<table><tr><td>Free float</td><td>72%</td></tr><tr><td>BBG</td><td>ENR GR</td></tr><tr><td>RIC</td><td>ENR1n.BE</td></tr></table>

FINANCIALS AND RATIOS (EUR)

<table><tr><td>Year to</td><td>09/2025a</td><td>09/2026e</td><td>09/2027e</td><td>09/2028e</td></tr><tr><td>HSBC EPS</td><td>1.60</td><td>4.04</td><td>5.94</td><td>7.67</td></tr><tr><td>HSBC EPS (prev)</td><td>1.60</td><td>4.45</td><td>5.80</td><td>7.41</td></tr><tr><td>Change (%)</td><td>0.0</td><td>-9.0</td><td>2.5</td><td>3.5</td></tr><tr><td>Consensus EPS</td><td>1.58</td><td>4.41</td><td>6.07</td><td>7.84</td></tr><tr><td>PE (x)</td><td>95.3</td><td>37.7</td><td>25.6</td><td>19.9</td></tr><tr><td>Dividend yield (%)</td><td>0.5</td><td>1.2</td><td>1.7</td><td>2.3</td></tr><tr><td>EV/EBITDA (x)</td><td>36.8</td><td>19.9</td><td>15.4</td><td>12.1</td></tr><tr><td>ROE (%)</td><td>14.1</td><td>33.6</td><td>48.3</td><td>54.2</td></tr></table>

52-WEEK PRICE (EUR)  
![](images/ba9033b18bd78514896870cafaae645cf5fb6bc677313ce8aa5ebedac6ab25f9.jpg)  
Source: LSEG IBES, HSBC estimates

## Sean McLoughlin\*

Senior Global Industrials Analyst

HSBC Bank plc

sean.mcloughlin@hsbcib.com

+44 20 7991 3464

## Stacey Sun\*

Global Industrials Analyst

HSBC Bank plc

stacey.sun@hsbc.com

+44 203 2685810

## Shashi Mishra\*

Associate

Bangalore

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

Financials & valuation: Siemens Energy AG  
Financial statements

<table><tr><td>Year to</td><td>09/2025a</td><td>09/2026e</td><td>09/2027e</td><td>09/2028e</td></tr><tr><td colspan="5">Profit &amp; loss summary (EURm)</td></tr><tr><td>Revenue</td><td>39,077</td><td>43,619</td><td>49,569</td><td>55,995</td></tr><tr><td>EBITDA</td><td>3,350</td><td>6,071</td><td>7,824</td><td>9,798</td></tr><tr><td>Depreciation &amp; amortisation</td><td>-1,781</td><td>-1,559</td><td>-1,431</td><td>-1,321</td></tr><tr><td>Operating profit/EBIT</td><td>1,569</td><td>4,512</td><td>6,393</td><td>8,477</td></tr><tr><td>Net interest</td><td>-28</td><td>40</td><td>65</td><td>110</td></tr><tr><td>PBT</td><td>2,213</td><td>4,690</td><td>6,538</td><td>8,677</td></tr><tr><td>HSBC PBT</td><td>2,208</td><td>4,990</td><td>6,668</td><td>8,807</td></tr><tr><td>Taxation</td><td>-527</td><td>-1,055</td><td>-1,308</td><td>-2,082</td></tr><tr><td>Net profit</td><td>1,415</td><td>3,355</td><td>4,941</td><td>6,294</td></tr><tr><td>HSBC net profit</td><td>1,414</td><td>3,436</td><td>4,976</td><td>6,330</td></tr><tr><td colspan="5">Cash flow summary (EURm)</td></tr><tr><td>Cash flow from operations</td><td>5,820</td><td>9,089</td><td>7,766</td><td>9,305</td></tr><tr><td>Capex</td><td>-1,663</td><td>-2,289</td><td>-2,590</td><td>-2,915</td></tr><tr><td>Cash flow from investment</td><td>-1,618</td><td>-2,289</td><td>-2,590</td><td>-2,915</td></tr><tr><td>Dividends</td><td>-612</td><td>-1,510</td><td>-2,223</td><td>-2,833</td></tr><tr><td>Change in net debt</td><td>-2,793</td><td>-2,030</td><td>-793</td><td>-1,468</td></tr><tr><td>FCF equity</td><td>4,157</td><td>6,800</td><td>5,177</td><td>6,391</td></tr><tr><td colspan="5">Balance sheet summary (EURm)</td></tr><tr><td>Intangible fixed assets</td><td>11,487</td><td>11,487</td><td>11,487</td><td>11,487</td></tr><tr><td>Tangible fixed assets</td><td>7,559</td><td>8,290</td><td>9,448</td><td>11,042</td></tr><tr><td>Current assets</td><td>34,452</td><td>39,184</td><td>42,873</td><td>47,493</td></tr><tr><td>Cash &amp; others</td><td>9,162</td><td>10,402</td><td>10,581</td><td>11,409</td></tr><tr><td>Total assets</td><td>56,637</td><td>62,225</td><td>67,049</td><td>73,208</td></tr><tr><td>Operating liabilities</td><td>37,891</td><td>45,344</td><td>49,975</td><td>55,213</td></tr><tr><td>Gross debt</td><td>4,372</td><td>3,582</td><td>2,967</td><td>2,327</td></tr><tr><td>Net debt</td><td>-4,790</td><td>-6,820</td><td>-7,614</td><td>-9,082</td></tr><tr><td>Shareholders&#x27; funds</td><td>10,675</td><td>9,800</td><td>10,808</td><td>12,570</td></tr><tr><td>Invested capital</td><td>6,445</td><td>3,215</td><td>3,252</td><td>3,400</td></tr></table>

Ratio, growth and per share analysis

<table><tr><td>Year to</td><td>09/2025a</td><td>09/2026e</td><td>09/2027e</td><td>09/2028e</td></tr><tr><td colspan="5">Y-o-y % change</td></tr><tr><td>Revenue</td><td>13.4</td><td>11.6</td><td>13.6</td><td>13.0</td></tr><tr><td>EBITDA</td><td>135.1</td><td>81.2</td><td>28.9</td><td>25.2</td></tr><tr><td>Operating profit</td><td></td><td>187.6</td><td>41.7</td><td>32.6</td></tr><tr><td>PBT</td><td>21.5</td><td>111.9</td><td>39.4</td><td>32.7</td></tr><tr><td>HSBC EPS</td><td>123.8</td><td>153.1</td><td>47.0</td><td>29.0</td></tr><tr><td colspan="5">Ratios (%)</td></tr><tr><td>Revenue/IC (x)</td><td>5.2</td><td>9.0</td><td>15.3</td><td>16.8</td></tr><tr><td>ROIC</td><td>15.8</td><td>72.4</td><td>158.2</td><td>193.7</td></tr><tr><td>ROE</td><td>14.1</td><td>33.6</td><td>48.3</td><td>54.2</td></tr><tr><td>ROA</td><td>3.6</td><td>6.4</td><td>8.4</td><td>9.7</td></tr><tr><td>EBITDA margin</td><td>8.6</td><td>13.9</td><td>15.8</td><td>17.5</td></tr><tr><td>Operating profit margin</td><td>4.0</td><td>10.3</td><td>12.9</td><td>15.1</td></tr><tr><td>EBITDA/net interest (x)</td><td>119.6</td><td></td><td></td><td></td></tr><tr><td>Net debt/equity</td><td>-44.9</td><td>-69.6</td><td>-70.4</td><td>-72.3</td></tr><tr><td>Net debt/EBITDA (x)</td><td>-1.4</td><td>-1.1</td><td>-1.0</td><td>-0.9</td></tr><tr><td colspan="5">CF from operations/net debt</td></tr><tr><td colspan="5">Per share data (EUR)</td></tr><tr><td>EPS Rep (diluted)</td><td>1.60</td><td>3.95</td><td>5.90</td><td>7.63</td></tr><tr><td>HSBC EPS (diluted)</td><td>1.60</td><td>4.04</td><td>5.94</td><td>7.67</td></tr><tr><td>DPS</td><td>0.70</td><td>1.78</td><td>2.66</td><td>3.44</td></tr><tr><td>Book value</td><td>12.20</td><td>11.45</td><td>12.81</td><td>15.13</td></tr></table>

Valuation data

Buy

<table><tr><td>Year to</td><td>09/2025a</td><td>09/2026e</td><td>09/2027e</td><td>09/2028e</td></tr><tr><td>EV/sales</td><td>3.2</td><td>2.8</td><td>2.4</td><td>2.1</td></tr><tr><td>EV/EBITDA</td><td>36.8</td><td>19.9</td><td>15.4</td><td>12.1</td></tr><tr><td>EV/IC</td><td>19.1</td><td>37.7</td><td>37.0</td><td>35.0</td></tr><tr><td>PE*</td><td>95.3</td><td>37.7</td><td>25.6</td><td>19.9</td></tr><tr><td>PB</td><td>12.5</td><td>13.3</td><td>11.9</td><td>10.1</td></tr><tr><td>FCF yield (%)</td><td>3.2</td><td>5.2</td><td>3.9</td><td>4.9</td></tr><tr><td>Dividend yield (%)</td><td>0.5</td><td>1.2</td><td>1.7</td><td>2.3</td></tr></table>

\* Based on HSBC EPS (diluted)

ESG metrics

<table><tr><td>Environmental Indicators</td><td>09/2025a</td><td>Governance Indicators</td><td>09/2025a</td></tr><tr><td>GHG emission intensity*</td><td>4.5</td><td>No. of board members</td><td>20</td></tr><tr><td>Energy intensity*</td><td>37.4</td><td>Average board tenure (years)</td><td>4.1</td></tr><tr><td>CO2reduction policy</td><td>Yes</td><td>Female board members (%)</td><td>45</td></tr><tr><td>Social Indicators</td><td>09/2025a</td><td>Board members independence (%)</td><td>45</td></tr><tr><td>Employee costs as % of revenues</td><td>26.7</td><td></td><td></td></tr><tr><td>Employee turnover (%)</td><td>7.4</td><td></td><td></td></tr><tr><td>Diversity policy</td><td>Yes</td><td></td><td></td></tr></table>

Source: Company data, HSBC  
\* GHG intensity and energy intensity are measured in kg and kWh respectively against revenue in USD '000s

<table><tr><td colspan="2">Issuer information</td></tr><tr><td>Share price (EUR)</td><td>152.32</td></tr><tr><td>Target price (EUR)</td><td>205.00</td></tr><tr><td>RIC (Equity)</td><td>ENR1n.BE</td></tr><tr><td>Bloomberg (Equity)</td><td>ENR GR</td></tr><tr><td>Market cap (USDm)</td><td>149,677</td></tr></table>

<table><tr><td>Free float</td><td>72%</td></tr><tr><td>Sector</td><td>Energy Equipment</td></tr><tr><td>Country/Region</td><td>Germany</td></tr><tr><td>Analyst</td><td>Sean McLoughlin</td></tr><tr><td>Contact</td><td>+44 20 7991 3464</td></tr></table>

Price relative  
![](images/eada777b4d3b6965dd39daa44dab57bbf8fafe79ebfeedfb975c09f6605cbbfe.jpg)  
Source: HSBC  
Note: Priced at close of 22 Jul 2026

ENR total gas power commitments (GW)  
![](images/235b28a80f583ce0502cb74973c6476b9fd33c54297bbfff661eb0188c256278.jpg)  
Note: Sep FYE. Source: company data, HSBC estimates

GEV total gas power commitments (GW)  
![](images/8cf9ed8ae751e234ee822336d1d8f20544ecbb4088c153486844338092bd425b.jpg)  
Note: Dec FYE. Source: company data, HSBC estimates

Mitsubishi Heavy gas turbine backlog (GW)  
![](images/6fdf369a4ad176fac0bd98919916a10ff94fe1827e00abea6d0253b63bf76d02.jpg)  
Note: March FYE. Source: company data

We expect an H2 order fade (EURm) in ENR Gas Services as guided...  
![](images/51a9b0be707af88f13abf3a28a9686f2d9139c209a1262b8e449fba824ebca93.jpg)  
Source: company data, HSBC estimates

We expect ENR Grid Technologies orders (EURm) to hold up better in H2e  
![](images/7cdb8be92e2a8644fda8d50e03bc5f23768fbc60b4d8bdea71294abcf864c6c9.jpg)  
Source: company data, HSBC estimates

Siemens Gamesa is finally reaching positive profit (EURm) in H2e  
![](images/89d78a8637960e810a527ce4610bb926db39c732c7679d02be13c89a5a5c44e7.jpg)  
Source: company data, HSBC estimates

Siemens Energy Q3 FY26 results preview table

<table><tr><td>Figures in EURm, Sept end</td><td>Q2 FY25</td><td>Q3 FY25</td><td>Q4 FY25</td><td>Q1 FY26</td><td>Q2 FY26</td><td>Q3 FY26e</td><td>y-o-y</td><td>Cons</td><td>Vs. cons.</td></tr><tr><td colspan="10">Orders:</td></tr><tr><td>--Gas Services</td><td>7,038</td><td>6,180</td><td>4,769</td><td>8,751</td><td>8,869</td><td>7,994</td><td>29.4%</td><td>8,167</td><td>-2.1%</td></tr><tr><td>--Grid Technologies</td><td>5,209</td><td>4,218</td><td>6,880</td><td>5,964</td><td>6,996</td><td>5,666</td><td>34.3%</td><td>5,579</td><td>1.6%</td></tr><tr><td>--Transformation of Industry</td><td>1,564</td><td>1,356</td><td>1,629</td><td>1,579</td><td>1,254</td><td>1,432</td><td>5.6%</td><td>1,422</td><td>0.7%</td></tr><tr><td>Aggregate</td><td>13,811</td><td>11,754</td><td>13,278</td><td>16,294</td><td>17,119</td><td>15,091</td><td>28.4%</td><td>15,168</td><td>-0.5%</td></tr><tr><td>--Siemens Gamesa</td><td>875</td><td>4,890</td><td>1,123</td><td>1,556</td><td>846</td><td>935</td><td>-80.9%</td><td>1,560</td><td>-40.1%</td></tr><tr><td>Total Segments</td><td>14,686</td><td>16,644</td><td>14,401</td><td>17,850</td><td>17,965</td><td>16,026</td><td>-3.7%</td><td>16,728</td><td>-4.2%</td></tr><tr><td>--Reconciliation</td><td>-253</td><td>-31</td><td>-187</td><td>-242</td><td>-216</td><td>-128</td><td>-313.6%</td><td>-99</td><td>-29.9%</td></tr><tr><td>Siemens Energy</td><td>14,433</td><td>16,613</td><td>14,214</td><td>17,608</td><td>17,749</td><td>15,898</td><td>-4.3%</td><td>16,629</td><td>-4.4%</td></tr><tr><td colspan="10">Revenue:</td></tr><tr><td>--Gas Services</td><td>3,163</td><td>3,118</td><td>3,094</td><td>3,097</td><td>3,478</td><td>3,704</td><td>18.8%</td><td>3,678</td><td>0.7%</td></tr><tr><td>--Grid Technologies</td><td>2,861</td><td>2,819</td><td>3,145</td><td>3,054</td><td>3,067</td><td>3,712</td><td>31.7%</td><td>3,617</td><td>2.6%</td></tr><tr><td>--Transformation of Industry</td><td>1,411</td><td>1,361</td><td>1,614</td><td>1,303</td><td>1,422</td><td>1,469</td><td>7.9%</td><td>1,451</td><td>1.2%</td></tr><tr><td>Aggregate</td><td>7,435</td><td>7,298</td><td>7,853</td><td>7,454</td><td>7,967</td><td>8,885</td><td>21.7%</td><td>8,746</td><td>1.6%</td></tr><tr><td>--Siemens Gamesa</td><td>2,706</td><td>2,506</td><td>2,744</td><td>2,355</td><td>2,526</td><td>2,594</td><td>3.5%</td><td>2,581</td><td>0.5%</td></tr><tr><td>Total Segments</td><td>10,141</td><td>9,804</td><td>10,597</td><td>9,809</td><td>10,493</td><td>11,478</td><td>17.1%</td><td>11,327</td><td>1.3%</td></tr><tr><td>--Reconciliation</td><td>-180</td><td>-59</td><td>-169</td><td>-134</td><td>-197</td><td>-138</td><td>-133.5%</td><td>-127</td><td>-8.5%</td></tr><tr><td>Siemens Energy</td><td>9,961</td><td>9,745</td><td>10,428</td><td>9,675</td><td>10,296</td><td>11,341</td><td>16.4%</td><td>11,200</td><td>1.3%</td></tr><tr><td colspan="10">Profit before special items:</td></tr><tr><td>--Gas Services</td><td>511</td><td>406</td><td>251</td><td>515</td><td>552</td><td>556</td><td>36.9%</td><td>567</td><td>-2.0%</td></tr><tr><td>--Grid Technologies</td><td>571</td><td>448</td><td>463</td><td>538</td><td>524</td><td>705</td><td>57.4%</td><td>710</td><td>-0.7%</td></tr><tr><td>--Transformation of Industry</td><td>155</td><td>157</td><td>177<

[中间内容因长度限制已省略]

 any purpose. Both HBAP SLS and HBAP SEL are regulated by the Financial Services Commission and the Financial Supervisory Service of Korea. In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All U.S. persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Bank plc, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Bank plc.
"""
