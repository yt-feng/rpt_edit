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

## Honeywell

## Updating Model to Reflect Aero Spin; Establishing PT of \$250

We are updating our model to reflect the Aerospace spin and updated Honeywell Technologies guidance. We see upside to the midpoint of 2026 EPS guidance helped by improving organic growth trends, with double digit EPS growth (excluding the impact of stranded cost, trademark license fee) in 2027, with upside assuming volume acceleration, with cycle timing favorable particularly at IA and PA&T, and continued \~DD order trends at BA. If HON delivers to the MT algorithm laid out, which we see a credible pathway to (see link to investor day takeaway note), we think there is no reason HON can't re-rate to a sector multiple. We establish our price target of \$250 assuming a 22x multiple (\~on par with the sector) on our FY27 estimate and accounting for the Quantinuum stake, and reiterate our OW rating.

\- Establishing estimates. We update our model to reflect the Aerospace spin and updated Honeywell Technologies guidance. Our '26/'27 adj EPS estimates go to \$8.30/\$10.00 ('26 EPS guide of \$3.95-4.15 before 1-for-2 reverse stock split). For '26, we assume sales increase +2.7% organically (+2-3% guide), with pricing +3.9% and volumes -1.2%, while acq/div is a \~1.6% headwind. We model segment margins at 20.1% (19.8-20.3% guide). By segment, we assume IA +1% organic (\~flat guide) on 17.6% margins, BA +6.5% organic (MSD+ guide) on 27.1% margins, and PA&T flat organic (\~flat guide) on 23.2% margins. For '27, we assume organic sales up 4.5% (4-6% three year target) with pricing +3.5% and volumes +1.0%, while acq/div is a \~5.7% headwind. We model segment margins at 23.6%. By segment, we assume IA +2% organic on 23.0% margins, BA +4% organic on 27.6% margins, and PA&T +7% organic on 23.5% margins. On FCF, we model \$2.0 B/\$2.9 B for 2026/2027 or 77%/93% conversion, with 2H26 FCF of \~\$1.5B or \~97% conversion. In terms of capital allocation, we model capex at \~3% of sales in 2026/2027 and R&D at 4.8%/4.5% of sales in 2026/2027. We expect HON to prioritize debt paydown in the near term with gross leverage expected to be below 3x by 2026 end and below 2.5x in \~two years. We assume annual dividend payout ratio of 35% of net income and 1% from share repo, both in line with medium term guidance.

## Overweight

HON, HON US
Price (02 Jul 26):\$229.86

▼ Price Target (Dec-26):\$250.00
Prior (Dec-26):\$260.00

## Electrical Equipment & Multi-Industry

Chigusa Katoku AC (1-212) 622-0855 chigusa.katoku@jpmchase.com

Piyush Khaitan  
(1-212) 622-0605  
piyush.khaitan@jpmchase.com  
JPM Securities LLC

<table><tr><td colspan="4">Key Changes (FYE Dec)</td></tr><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. EPS - 26E ($)</td><td>10.30</td><td>8.30</td><td>-19.5%</td></tr><tr><td>Adj. EPS - 27E ($)</td><td>11.80</td><td>10.00</td><td>-15.3%</td></tr></table>

<table><tr><td colspan="4">Adj. EPS ($)</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>1.18</td><td>1.80A</td><td></td></tr><tr><td>Q2</td><td>1.75</td><td>1.80</td><td></td></tr><tr><td>Q3</td><td>1.68</td><td>2.33</td><td></td></tr><tr><td>Q4</td><td>1.85</td><td>2.36</td><td></td></tr><tr><td>FY</td><td>6.46</td><td>8.30</td><td>10.00</td></tr></table>

Price Performance  
![](images/004ae46f7ab3a6773bfec260c1ec0dd9416da0c5b0b5c5d1e18f2e1c0814f491.jpg)

— HON Price (\$) — S&P500 (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>17.8%</td><td>-2.3%</td><td>0.2%</td><td>-3.9%</td></tr><tr><td>Rel</td><td>8.5%</td><td>-0.6%</td><td>-13.5%</td><td>-24.1%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>319</td></tr><tr><td>52-week range ($)</td><td>260.15-195.77</td></tr><tr><td>Market cap ($ mn)</td><td>73,371.31</td></tr><tr><td>Exchange rate</td><td>1.00</td></tr><tr><td>Free float (%)</td><td>99.9%</td></tr><tr><td>3M ADV (mn)</td><td>2.60</td></tr><tr><td>3M ADV ($ mn)</td><td>1,074.3</td></tr><tr><td>Volatility (90 Day)</td><td>32</td></tr><tr><td>Index</td><td>S&amp;P 500</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>18|7|1</td></tr></table>

Key Metrics (FYE Dec)

<table><tr><td>$ in millions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td></tr><tr><td colspan="4">Financial Estimates</td></tr><tr><td>Revenue</td><td>19,945</td><td>20,141</td><td>19,900</td></tr><tr><td>Adj. EBITDA</td><td>3,349</td><td>4,663</td><td>5,309</td></tr><tr><td>Adj. EBIT</td><td>3,349</td><td>3,756</td><td>4,402</td></tr><tr><td>Adj. net income</td><td>2,074</td><td>2,649</td><td>3,173</td></tr><tr><td>Adj. EPS</td><td>6.46</td><td>8.30</td><td>10.00</td></tr><tr><td>BBG EPS</td><td>19.99</td><td>18.21</td><td>17.05</td></tr><tr><td>Cashflow from operations</td><td>0</td><td>2,651</td><td>3,545</td></tr><tr><td>FCFF</td><td>0</td><td>2,046</td><td>2,948</td></tr><tr><td colspan="4">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>3.4%</td><td>1.0%</td><td>(1.2%)</td></tr><tr><td>EBITDA margin</td><td>16.8%</td><td>23.1%</td><td>26.7%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>3.3%</td><td>39.2%</td><td>13.9%</td></tr><tr><td>EBIT margin</td><td>16.8%</td><td>18.6%</td><td>22.1%</td></tr><tr><td>Net margin</td><td>10.4%</td><td>13.2%</td><td>15.9%</td></tr><tr><td>Adj. EPS growth</td><td>6.8%</td><td>28.5%</td><td>20.5%</td></tr><tr><td colspan="4">Ratios</td></tr><tr><td>Adj. tax rate</td><td>19.0%</td><td>19.0%</td><td>19.0%</td></tr><tr><td>Interest cover</td><td>4.3</td><td>9.6</td><td>10.9</td></tr><tr><td>Net debt/Equity</td><td>-</td><td>0.4</td><td>0.4</td></tr><tr><td>Net debt/EBITDA</td><td>0.0</td><td>1.8</td><td>1.5</td></tr><tr><td>ROCE</td><td>-</td><td>19.1%</td><td>11.0%</td></tr><tr><td>ROE</td><td>-</td><td>28.8%</td><td>16.7%</td></tr><tr><td colspan="4">Valuation</td></tr><tr><td>FCFF yield</td><td>0.0%</td><td>2.8%</td><td>4.0%</td></tr><tr><td>Dividend yield</td><td>0.0%</td><td>1.3%</td><td>1.5%</td></tr><tr><td>EV/Revenue</td><td>3.7</td><td>4.1</td><td>4.1</td></tr><tr><td>EV/EBITDA</td><td>21.9</td><td>17.8</td><td>15.5</td></tr><tr><td>Adj. P/E</td><td>35.6</td><td>27.7</td><td>23.0</td></tr></table>

## Summary Investment Thesis and Valuation Investment Thesis

We view that HON's margin expansion in core ops is 1) front loaded helped by operational self help at IA and cycle timing and 2) the $24\%$ targeted by 2029 does not rely on volumes, driven by price cost, cost productivity supported by a shift to a shared services model and a mix shift toward services and software targeted to exceed $45\%$ of revenue; if there are volumes there is upside. Pricing guided in the $3 - 4\%$ range is impressive in our view, underscoring the differentiation of offerings, driven by Forge's connected strategy, NPI, and proximity to customers, with opportunity for improvement at IA. Bottom line, HON provided 2029 targets ahead of expectations, backed by a credible pathway driving $10\%+$ EPS growth algorithm on par with the multi-industry sector, with further opportunity for upside. We establish our PT of \$250 and reiterate OW rating.

## Valuation

Our Dec 2026 price target of \$250, down from \$260, assumes a \~5% discount to our group target P/E multiple of \~23x, reflecting HON's growth and cash flow characteristics, while accounting for the Quantinuum stake. Our group target multiple is \~23x, at a premium (above the historical 5-10% sector average) to the S&P 500 FY2 multiple reflecting cycle timing.

Figure 1: HON Estimates

<table><tr><td></td><td>2026</td><td>2027</td></tr><tr><td></td><td>Current</td><td>Current</td></tr><tr><td colspan="3">SALES</td></tr><tr><td>Industrial Automation</td><td>5,286</td><td>3,843</td></tr><tr><td>Building Automation</td><td>7,846</td><td>8,160</td></tr><tr><td>Process Automation &amp; Technology</td><td>7,010</td><td>7,898</td></tr><tr><td>SALES</td><td>$20,141</td><td>$19,900</td></tr><tr><td colspan="3">PROFITS</td></tr><tr><td>Industrial Automation</td><td>928</td><td>884</td></tr><tr><td>Building Automation</td><td>2,122</td><td>2,252</td></tr><tr><td>Process Automation &amp; Technology</td><td>1,623</td><td>1,856</td></tr><tr><td>Corporate</td><td>(617)</td><td>(290)</td></tr><tr><td>PROFITS</td><td>$4,056</td><td>$4,702</td></tr><tr><td>Segment Margin</td><td>20.1%</td><td>23.6%</td></tr><tr><td>Net Interest</td><td>(485)</td><td>(485)</td></tr><tr><td>Other Below-the-liners</td><td>(300)</td><td>(300)</td></tr><tr><td>Tax rate</td><td>19.0%</td><td>19.0%</td></tr><tr><td>Share count</td><td>319</td><td>317</td></tr><tr><td>EPS</td><td>$8.30</td><td>$10.00</td></tr><tr><td>FCF ($ billions)</td><td>$2.0</td><td>$2.9</td></tr><tr><td colspan="3">Segment margins</td></tr><tr><td>Industrial Automation</td><td>17.6%</td><td>23.0%</td></tr><tr><td>Building Automation</td><td>27.1%</td><td>27.6%</td></tr><tr><td>Process Automation &amp; Technology</td><td>23.2%</td><td>23.5%</td></tr></table>

Source: JPM estimates.

In terms of the EPS Bridge, in 2026 we dial in low 30% core volume incrementals, \~90c price cost benefit, \~50c stranded cost tailwind, \~20c tailwind from trademark license fee, \~15c acq/div tailwind and \~45c BTL tailwind driven by interest expense, and \~5c tailwind from share count. In 2027, we dial in low 30% core volume incrementals, \~75c price cost benefit, \~65c stranded cost tailwind, \~20c tailwind from trademark license fee, offset by 10c acq/div headwind, and \~5c tailwind from share count.

Figure 2: HON EPS Bridge

<table><tr><td></td><td>26 JPM</td><td>27 JPM</td></tr><tr><td>Beginning</td><td>6.46</td><td>8.30</td></tr><tr><td>Price/Cost</td><td>0.89</td><td>0.74</td></tr><tr><td>Currency</td><td>0.00</td><td>0.00</td></tr><tr><td>Corporate</td><td>(0.01)</td><td>0.00</td></tr><tr><td>Stranded Cost</td><td>0.50</td><td>0.65</td></tr><tr><td>Trademark License Fee</td><td>0.19</td><td>0.19</td></tr><tr><td>Acquisitions/Divestitures</td><td>0.14</td><td>(0.10)</td></tr><tr><td>Other</td><td>(0.11)</td><td>0.00</td></tr><tr><td>Aggregate Below The Line</td><td>0.46</td><td>0.06</td></tr><tr><td>Gains/Other income</td><td>(1.15)</td><td>0.00</td></tr><tr><td>Interest</td><td>0.76</td><td>0.00</td></tr><tr><td>Stock Comp</td><td>(0.02)</td><td>0.00</td></tr><tr><td>Repositioning/Other Charges</td><td>0.81</td><td>0.00</td></tr><tr><td>Share Count</td><td>0.05</td><td>0.06</td></tr><tr><td>Tax rate</td><td>0.00</td><td>0.00</td></tr><tr><td>Base</td><td>8.51</td><td>9.84</td></tr><tr><td>Volume/Mix</td><td>(0.22)</td><td>0.16</td></tr><tr><td>Ending</td><td>8.30</td><td>10.00</td></tr><tr><td>Prior Year Sales</td><td>19,945</td><td>20,141</td></tr><tr><td>Current Year Sales</td><td>20,141</td><td>19,900</td></tr><tr><td>Current Year Price</td><td>773</td><td>705</td></tr><tr><td>Current Year Currency</td><td>0</td><td>0</td></tr><tr><td>Current Year Acquisitions</td><td>(314)</td><td>(1,151)</td></tr><tr><td>Current Year Organic Volume Sales</td><td>(263)</td><td>205</td></tr><tr><td>Organic Volume Growth</td><td>-1%</td><td>1%</td></tr><tr><td>Implied $ Profit Incr/(Decr)</td><td>(85)</td><td>63</td></tr><tr><td>Implied Incr/Decr Margin</td><td>32%</td><td>31%</td></tr></table>

Source: JPM estimates.

# Investment Thesis, Valuation and Risks

Honeywell (Overweight; Price Target: \$250.00)

## Investment Thesis

We view that HON's margin expansion in core ops is 1) front loaded helped by operational self help at IA and cycle timing and 2) the $24\%$ targeted by 2029 does not rely on volumes, driven by price cost, cost productivity supported by a shift to a shared services model and a mix shift toward services and software targeted to exceed $45\%$ of revenue; if there are volumes there is upside. Pricing guided in the $3 - 4\%$ range is impressive in our view, underscoring the differentiation of offerings, driven by Forge's connected strategy, NPI, and proximity to customers, with opportunity for improvement at IA. Bottom line, HON provided 2029 targets ahead of expectations, backed by a credible pathway driving $10\%+$ EPS growth algorithm on par with the multi-industry sector, with further opportunity for upside. We establish our PT of \$250 and reiterate OW rating.

## Valuation

Our Dec 2026 price target of \$250 assumes a \~5% discount to our group target P/E multiple of \~23x, reflecting HON's growth and cash flow characteristics, while accounting for the Quantinuum stake. Our group target multiple is \~23x, at a premium (above the historical 5-10% sector average) to the S&P 500 FY2 multiple reflecting cycle timing.

## Risks to Rating and Price Target

Downside risks to our rating and price target include (1) a moderation in the degree of pricing power/margin improvement, (2) declines in global commodity prices hurting related businesses at HPS and UOP, (3) a slowdown in key short cycle industrial end markets, and (3) execution risk around future potential acquisitions that could weaken management's track record on capital allocation.

Honeywell: Summary of Financials

<table><tr><td>Income Statement - Annual</td><td>FY24A</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Revenue</td><td>19,281</td><td>19,945</td><td>20,141</td><td>19,900</td><td>-</td></tr><tr><td>COGS</td><td>(11,507)</td><td>(12,065)</td><td>(12,085)</td><td>(11,741)</td><td>-</td></tr><tr><td>Gross profit</td><td>7,774</td><td>7,880</td><td>8,056</td><td>8,159</td><td>-</td></tr><tr><td>SG&amp;A</td><td>(4,513)</td><td>(4,663)</td><td>(4,431)</td><td>(3,881)</td><td>-</td></tr><tr><td>Adj. EBITDA</td><td>3,242</td><td>3,349</td><td>4,663</td><td>5,309</td><td>-</td></tr><tr><td>D&amp;A</td><td>0</td><td>0</td><td>(907)</td><td>(907)</td><td>-</td></tr><tr><td>Adj. EBIT</td><td>3,242</td><td>3,349</td><td>3,756</td><td>4,402</td><td>-</td></tr><tr><td>Net Interest</td><td>(797)</td><td>(788)</td><td>(485)</td><td>(485)</td><td>-</td></tr><tr><td>Adj. PBT</td><td>2,445</td><td>2,561</td><td>3,271</td><td>3,917</td><td>-</td></tr><tr><td>Tax</td><td>(465)</td><td>(487)</td><td>(621)</td><td>(744)</td><td>-</td></tr><tr><td>Minority Interest</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td></tr><tr><td>Adj. Net Income</td><td>1,980</td><td>2,074</td><td>2,649</td><td>3,173</td><td>-</td></tr><tr><td>Reported EPS</td><td>6.05</td><td>6.46</td><td>8.30</td><td>10.00</td><td>-</td></tr><tr><td>Adj. EPS</td><td>6.05</td><td>6.46</td><td>8.30</td><td>10.00</td><td>-</td></tr><tr><td>DPS</td><td>0.00</td><td>0.00</td><td>2.90</td><td>3.50</td><td>-</td></tr><tr><td>Payout ratio</td><td>0.0%</td><td>0.0%</td><td>35.0%</td><td>35.0%</td><td>-</td></tr><tr><td>Shares outstanding</td><td>327</td><td>321</td><td>319</td><td>317</td><td>-</td></tr><tr><td>Balance Sheet &amp; Cash Flow Statement</td><td>FY24A</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Cash and cash equivalents</td><td>0</td><td>0</td><td>4,764</td><td>5,602</td><td>-</td></tr><tr><td>Accounts receivable</td><td>0</td><td>0</td><td>4,784</td><td>5,058</td><td>-</td></tr><tr><td>Inventories</td><td>0</td><td>0</td><td>1,804</td><td>1,806</td><td>-</td></tr><tr><td>Other current assets</td><td>0</td><td>0</td><td>10,443</td><td>10,720</td><td>-</td></tr><tr><td>Current assets</td><td>0</td><td>0</td><td>15,208</td><td>16,322</td><td>-</td></tr><tr><td>PP&amp;E</td><td>0</td><td>0</td><td>2,471</td><td>2,433</td><td>-</td></tr><tr><td>LT investments</td><td>0</td><td>0</td><td>1,298</td><td>1,298</td><td>-</td></tr><tr><td>Other non current assets</td><td>0</td><td>0</td><td>6,013</td><td>6,013</td><td>-</td></tr><tr><td>Total assets</td><td>0</td><td>0</td><td>46,556</td><td>47,360</td><td>-</td></tr><tr><td>Short term borrowings</td><td>0</td><td>0</td><td>7,724</td><td>7,724</td><td>-</td></tr><tr><td>Payables</t

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 06 Jul 2026 09:07 AM EDT

Disseminated 06 Jul 2026 09:07 AM EDT
"""
