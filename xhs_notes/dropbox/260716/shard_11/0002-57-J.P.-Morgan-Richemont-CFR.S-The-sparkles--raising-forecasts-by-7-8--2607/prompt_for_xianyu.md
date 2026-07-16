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
# JPM

## Richemont

The sparkles: raising forecasts by 7-8%

Richemont kicked off the H1/Q2 26 reporting season yesterday morning with, once again, a stellar performance. Momentum was solid not just in the Jewellery Maisons division (which was up an incredible +24%! but also in the Specialist Watchmakers and Other divisions, which also came in ahead of expectations. As we have been arguing, structural tailwinds in jewellery are clearly benefiting the Group (see more in our deep-dive note Richemont: 18 Karats of strength); still, the broad-based nature, magnitude, and consistency of growth also reflect, in our view the superior quality of execution. This should be increasingly rewarded by investors, notably in the context of a luxury backdrop that remains highly polarised and volatile. Banking in the solid beat on Q1 27 numbers, faster momentum and better operating leverage, we have raised our forecasts by 7-8%, taking our price target to CHF220 (CHF200). Despite and already solid outperformance YTD (+14% vs sector around -10%), we think the story has further legs thanks to sustained momentum and earnings growth acceleration from here. Hence, Richemont remains our top pick in luxury.

\- Superior business quality, delivering best results. The key highlight of the trading update was clearly the outstanding performance in Jewellery Maisons, +24% ex-FX in Q1, accelerating from an already exceptional +16% in Q4. Positively, all regions and all brands contributed to this, with balanced momentum among domestic consumers and tourists. This balanced growth in our view is very important. In fact, looking at such high level of growth, the fear could be on the sustainability of these numbers and whether penetration is being pushed too far. Such a balanced delivery, by nationality, brand, family line, different SKUs in our view dilutes the risk of over penetration and over reliance on a key best seller, leaving the growth journey more sustainable for longer (as we have explored for instance for Van Cleef Alhambra here). To support this, we think that the level of newness and innovation across all jewellery maisons have been carrying on (if anything seemingly accelerating in recent months) has been instrumental in feeding the momentum and supporting growth in such a robust way. While growth should not sustain at such high levels as we move on tougher comps, we still expect very sustained trends throughout the years, standing at a whole other level vs the rest of the sector (we model at +17% ex-FX in both Q2 and for the FY). Importantly, we think this proactive brand and product management is increasingly spreading to the broader portfolio, with sharper collections also at some of the brands in the other divisions (e.g. Piaget recent drops for both jewellery and watches), leading to healthier results there too.

\- Where does this leave us for the rest of reporting? We think this outperformance is, to a large extent, driven by category- and company-specific dynamics. Having said this, the extent of the acceleration, also at brands where momentum is more mixed (notably in the Other division) in our view sends a generally positive read to the rest of the sector. As we discussed in our preview book last week, we think the luxury backdrop is not as unfavorable as some of the broader narrative would suggest; Richemont trading update clearly confirmed this. With luxury share prices reacting positively to this print, the

Sources for: Style Exposure – JPM Global Markets Strategy; all other tables are company data and JPM estimates.

See page 8 for analyst certification and important disclosures, including non-US analyst disclosures.

## Overweight

CFR.S, CFR SW
Price (15 Jul 26): CHF194.95

▲ Price Target (Dec-27): CHF220.00

Prior (Dec-27): CHF200.00

## European Luxury & Sporting Goods

Chiara Battistini AC
(39-02) 8895-2700
chiara.x.battistini@JPM.com
JPM Securities plc/ JPM Securities (Asia Pacific) Limited

Wendy Liu
(44-20) 3493-9733
wendy.liu@JPM.com
JPM Securities plc

Apurva Vishwaraj
apurva.vishwaraj@jpmchase.com
JPM Securities plc
Victoria Saden
(44-20) 3493-0435
victoria.saden@JPM.com
JPM Securities plc

Specialist Sales contact details:

## Olivia Petronilho - Specialist Sales - European Consumer

(44-20) 3493-3709
olivia.b.petronilho@JPM.com

## Key Changes (FYE Mar)

<table><tr><td></td><td>Prev</td><td>Cur</td><td> $\Delta$ </td></tr><tr><td>Revenue - 27E (€ mn)</td><td>24,549</td><td>25,697</td><td>4.7%</td></tr><tr><td>Revenue - 28E (€ mn)</td><td>26,502</td><td>27,951</td><td>5.5%</td></tr><tr><td>Adj. EPS - 27E (€)</td><td>6.96</td><td>7.49</td><td>7.7%</td></tr><tr><td>Adj. EPS - 28E (€)</td><td>7.95</td><td>8.55</td><td>7.5%</td></tr><tr><td>Adj. EBIT - 27E (€ mn)</td><td>5,168</td><td>5,654</td><td>9.4%</td></tr><tr><td>Adj. EBIT - 28E (€ mn)</td><td>5,906</td><td>6,451</td><td>9.2%</td></tr></table>

Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>85</td><td>84</td><td>82</td><td>71</td><td>64</td></tr><tr><td>Growth</td><td>54</td><td>39</td><td>5</td><td></td><td></td></tr><tr><td>Momentum</td><td>25</td><td>21</td><td>59</td><td>23</td><td>55</td></tr><tr><td>Quality</td><td>25</td><td>38</td><td>41</td><td>58</td><td>55</td></tr><tr><td>Low Vol</td><td>45</td><td>45</td><td>47</td><td>45</td><td>36</td></tr><tr><td>ESGQ</td><td>24</td><td>16</td><td>34</td><td>29</td><td>79</td></tr></table>

Price Performance  
![](images/a738f7f69af802e7f17c8c98035428ce55c41fe1a1e7b31e9cee936b9ebca061.jpg)

— CFR.S Price (CHF) — MSCI-Eu (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>13.3%</td><td>7.9%</td><td>27.1%</td><td>31.6%</td></tr><tr><td>Rel</td><td>4.6%</td><td>6.6%</td><td>22.8%</td><td>13.6%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>588</td></tr><tr><td>52-week range (CHF)</td><td>196.95-127.20</td></tr><tr><td>Market cap ($ mn)</td><td>141,773.10</td></tr><tr><td>Exchange rate</td><td>0.81</td></tr><tr><td>Free float (%)</td><td>96.6%</td></tr><tr><td>3M ADV (mn)</td><td>0.92</td></tr><tr><td>3M ADV ($ mn)</td><td>192.6</td></tr><tr><td>Volatility (90 Day)</td><td>34</td></tr><tr><td>Index</td><td>MSCI Europe</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>20|11|1</td></tr></table>

Key Metrics (FYE Mar)

<table><tr><td>€ in millions</td><td>FY26A</td><td>FY27E</td><td>FY28E</td><td>FY29E</td></tr><tr><td colspan="5">Financial Estimates</td></tr><tr><td>Revenue</td><td>22,420</td><td>25,697</td><td>27,951</td><td>29,810</td></tr><tr><td>Adj. EBITDA</td><td>6,101</td><td>7,424</td><td>8,267</td><td>9,043</td></tr><tr><td>Adj. EBIT</td><td>4,492</td><td>5,654</td><td>6,451</td><td>7,181</td></tr><tr><td>Adj. net income</td><td>3,464</td><td>4,419</td><td>5,041</td><td>5,630</td></tr><tr><td>Adj. EPS</td><td>5.88</td><td>7.49</td><td>8.55</td><td>9.55</td></tr><tr><td>BBG EPS</td><td>6.15</td><td>6.95</td><td>7.94</td><td>-</td></tr><tr><td>Cashflow from operations</td><td>4,880</td><td>4,468</td><td>6,286</td><td>7,065</td></tr><tr><td>FCFF</td><td>3,932</td><td>3,557</td><td>5,317</td><td>6,032</td></tr><tr><td colspan="5">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>4.8%</td><td>14.6%</td><td>8.8%</td><td>6.7%</td></tr><tr><td>Gross margin</td><td>64.4%</td><td>63.4%</td><td>63.7%</td><td>63.9%</td></tr><tr><td>EBITDA margin</td><td>27.2%</td><td>28.9%</td><td>29.6%</td><td>30.3%</td></tr><tr><td>EBIT margin</td><td>20.0%</td><td>22.0%</td><td>23.1%</td><td>24.1%</td></tr><tr><td>Adj. EPS growth</td><td>(8.1%)</td><td>27.6%</td><td>14.1%</td><td>11.7%</td></tr><tr><td colspan="5">Ratios</td></tr><tr><td>Adj. tax rate</td><td>20.0%</td><td>19.1%</td><td>19.1%</td><td>19.1%</td></tr><tr><td>Interest cover</td><td>89.2</td><td>137.8</td><td>159.3</td><td>182.2</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROCE</td><td>10.1%</td><td>12.2%</td><td>13.0%</td><td>13.2%</td></tr><tr><td>ROE</td><td>15.0%</td><td>17.7%</td><td>18.3%</td><td>18.1%</td></tr><tr><td colspan="5">Valuation</td></tr><tr><td>FCFF yield</td><td>3.2%</td><td>2.9%</td><td>4.3%</td><td>4.8%</td></tr><tr><td>Dividend yield</td><td>2.0%</td><td>1.7%</td><td>1.9%</td><td>2.1%</td></tr><tr><td>EV/Revenue</td><td>4.9</td><td>4.3</td><td>3.8</td><td>3.5</td></tr><tr><td>EV/EBITDA</td><td>18.1</td><td>14.8</td><td>12.9</td><td>11.5</td></tr><tr><td>Adj. P/E</td><td>35.9</td><td>28.2</td><td>24.7</td><td>22.1</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

Richemont is the global leader in branded jewellery and one of the leaders in high-end watches. It is strongly positioned with Cartier and VC&A to tap into the jewellery segment's long-term strong fundamentals. The Group has evolved meaningfully over the past 15 years, increasing exposure to the jewellery category and a higher retail mix, and has been working on its cost base to make it increasingly variable. Further, we think the jewellery space in general has also changed structurally in the last few years, with more attractive value for money propositions vs leather goods, more wearable designs and stronger marketing campaigns increasingly driving traction with self-purchasing women. These features and changing dynamics should benefit Richemont the most globally and help it navigate through a slowdown better than in the past, smoothing out historical operational and financial volatility, possibly better than what is perceived by investors currently and what is priced in at current valuation levels. We rate the stock Overweight.

## Valuation

Our Dec-27 DCF-based target price of CHF220 is based on the following factors: March 2027-31 explicit forecast, medium-term growth of 5.5%, terminal growth of 3.5% and WACC of 9% reflecting the current cost of equity.

![](images/80c55b95f2d616f194014cb942964643eeeca457e4c31d2f5847246bf5edaa17.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Europe ex UK</td><td>0.78</td><td>0.71</td></tr><tr><td>Sect: Cons Discretionary</td><td>0.76</td><td>0.64</td></tr><tr><td>Ind: Cons Dur &amp; Apparel</td><td>0.85</td><td>0.80</td></tr><tr><td>Macro:</td><td></td><td></td></tr><tr><td>Citi Eco Surprise Eurozone</td><td>0.41</td><td>0.21</td></tr><tr><td>Eurozone CPI</td><td>-0.12</td><td>-0.08</td></tr><tr><td>Eurozone Exports</td><td>0.20</td><td>0.07</td></tr><tr><td>Quant Styles:</td><td></td><td></td></tr><tr><td>Growth</td><td>-0.22</td><td>-0.18</td></tr><tr><td>Momentum</td><td>-0.25</td><td>-0.09</td></tr><tr><td>Size</td><td>-0.18</td><td>0.08</td></tr></table>

'bar' should have clearly gone up now. Still within the mix, we think polarisation of performance and specific category dyanamics (notably the leather goods fatigue) will continue to drive a visible divide between winners and laggards. Within the winners, we expect Zegna and Brunello to report particularly strong results. While the former is up almost 30% YTD, Brunello stock has lagged and hence we see the current share price level as particularly attractive and we would be positive into the next update (on the 30 $^{th}$ of July, recall we have placed the stock on Positive Catalyst Watch into this).

## Q1 27 sales in focus

Table 1: Richemont – Sales by segment (€m)

<table><tr><td></td><td>Q1 26</td><td>Q1 27A</td><td>Q1 27E</td></tr><tr><td>Jewellery maisons</td><td>3,914</td><td>4,732</td><td>4,364</td></tr><tr><td>% Change</td><td>7%</td><td>21%</td><td>12%</td></tr><tr><td>% constant currency</td><td>11%</td><td>24%</td><td>14%</td></tr><tr><td>Specialist watchmakers</td><td>824</td><td>873</td><td>840</td></tr><tr><td>% Change</td><td>-10%</td><td>6%</td><td>2%</td></tr><tr><td>% constant currency</td><td>-7%</td><td>8%</td><td>4%</td></tr><tr><td>Other</td><td>674</td><td>724</td><td>691</td></tr><tr><td>% Change</td><td>-4%</td><td>7%</td><td>2%</td></tr><tr><td>% constant currency</td><td>-1%</td><td>9%</td><td>5%</td></tr><tr><td>Total Sales</td><td>5,412</td><td>6,329</td><td>5,895</td></tr><tr><td>% Change</td><td>3%</td><td>17%</td><td>9%</td></tr><tr><td>% constant currency</td><td>6%</td><td>20%</td><td>11%</td></tr></table>

Source: JPM estimates, Company data.

Table 2: Richemont – Sales by region (€m)

<table><tr><td></td><td>Q1 26</td><td>Q1 27A</td><td>Q1 27E</td></tr><tr><td>Europe</td><td>1,295</td><td>1,429</td><td>1,391</td></tr><tr><td>% Change</td><td>11%</td><td>10%</td><td>7%</td></tr><tr><td>% Forex</td><td>0%</td><td>-1%</td><td>0%</td></tr><tr><td>% constant currency</td><td>11%</td><td>11%</td><td>7%</td></tr><tr><td>Japan</td><td>527</td><td>632</td><td>585</td></tr><tr><td>% Change</td><td>-13%</td><td>20%</td><td>11%</td></tr><tr><td>% Forex</td><td>2%</td><td>-16%</td><td>-11%</td></tr><tr><td>% constant currency</td><td>-15%</td><td>36%</td><td>22%</td></tr><tr><td>Asia Excl Japan</td><td>1,731</td><td>2,068</td><td>1,872</td></tr><tr><td>% Change</td><td>-4%</td><td>19%</td><td>8%</td></tr><tr><td>% Forex</td><td>-4%</td><td>-2%</td><td>0%</td></tr><tr><td>% constant currency</td><td>0%</td><td>21%</td><td>8%</td></tr><tr><td>Americas</td><td>1,335</td><td>1,670</td><td>1,546</td></tr><tr><td>% Change</td><td>10%</td><td>25%</td><td>16%</td></tr><tr><td>% Forex</td><td>-7%</td><td>-2%</td><td>-3%</td></tr><tr><td>% constant currency</td><td>17%</td><td>27%</td><td>18%</td></tr><tr><td>Middle East/Africa</td><td>524</td><td>530</td><td>500</td></tr><tr><td>% Change</td><td>11%</td><td>1%</td><td>-5%</td></tr><tr><td>% Forex</td><td>-6%</td><td>-2%</td><td>-3%</td></tr><tr><td>% constant currency</td><td>17%</td><td>3%</td><td>-2%</td></tr><tr><td>Total</td><td>5,412</td><td>6,329</td><td>5,895</td></tr><tr><td>% Change</td><td>3%</td><td>17%</td><td>9%</td></tr><tr><td>% Forex</td><td>-3%</td><td>-3%</td><td>-2%</td></tr><tr><td>% constant currency</td><td>6%</td><td>20%</td><td>11%</td></tr></table>

Source: JPM estimates, Company data.

Table 3: Richemont – Sales by channel (€m)

<table><tr><td></td><td>Q1 26</td><td>Q1 27A</td><td>Q1 27E</td></tr><tr><td>Retail</td><td>3,734</td><td>4,504</td><td>4,145</td></tr><tr><td>% Change</td><td>3%</td><td>21%</td><td>11%</td></tr><tr><td>% Forex</td><td>-3%</td><td>-3%</td><td>-2%</td></tr><tr><td>% constant currency</td><td>6%</td><td>24%</td><td>13%</td></tr><tr><td>Wholesale</td><td>1,355</td><td>1,452</td><td>1,423</td></tr><tr><td>% Change</td><td>2%</td><td>7%</td><td>5%</td></tr><tr><td>% Forex</td><td>-4%</td><td>-2%</td><td>-2%</td></tr><tr><td>% constant currency</td><td>6%</td><td>9%</td><td>7%</td></tr><tr><td>Online</td><td>323</td><td>373</td><td>328</td></tr><tr><td>% Change</td><td>3%</td><td>15%</td><td>2%</td></tr><tr><td>% Forex</td><td>-3%</td><td>-3%</td><td>-2%</td></tr><tr><td>% constant currency</td><td>6%</td><td>18%</td><td>4%</td></tr><tr><td>Total</td><td>5,412</td><td>6,329</td><td>5,895</td></tr><tr><td>% Change</td><td>3%</td><td>17%</td><td>9%</td></tr><tr><td>% Forex</td><td>-3%</td><td>-3%</td><td>-2%</td></tr><tr><td>% constant currency</td><td>6%</td><td>20%</td><td>11%</td></tr></table>

Source: JPM estimates, Company data.

## Changes to JPM forecasts and price target

Table 4: Richemont - Summary of changes to JPM forecasts (€m)

<table><tr><td></td><td>FY26A</td><td>FY27E Old</td><td>FY27E New</td><td>% Change</td><td>FY28E Old</td><td>FY28E New</td><td>% Change</td><td>FY29E Old</td><td>FY29E New</td><td>% Change</td></tr><tr><td>Sales</td><td>22,420</td><td>24,549</td><td>25,697</td><td>5%</td><td>26,502</td><td>27,951</td><td>5

[中间内容因长度限制已省略]

 market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results.

Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
