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
RIC: MMM.N BBG: MMM US

# 3M Company

# Why Consensus is 10% too low; Raising target to \$218

We reiterate our Buy rating and raise our price target for MMM to \$218, implying more than 25% further upside from current levels.

We view 2Q results as an important inflection point for the company, with clear evidence that management's long-cycle efforts to reinvigorate growth is starting to yield results.

As a result of better growth, we are raising our prior Street-high 2027 EPS estimate even higher (to \$10.46 vs. \$10.02 prior and now 10% above Consensus). We assume 5% organic growth (vs. +4% prior), 35% core incremental margin and \$600 million of net productivity, partially offset by about \$300 million in higher investments and stranded costs. The net result is \$800 million in higher year-on-year operating profit in 2027, which is about double this year's profit improvement. We have high conviction in this outlook and expect Consensus expectations to melt higher over time.

Our new price target is based on 24x our NTM EPS forecast (vs. 23x before), which reflects the better growth outlook, and we deduct \$30 per share for potential new PFAS cash calls (we think it'll likely be much lower than this, but we prefer to be conservative).

2Q details: 3M's management has invested heavily in its new product innovation engine, which takes time to show up in numbers, but can drive sustainable growth. This is now starting to show up, with the company on track to launch over 1,000 new products by 2027 (>350 just in this year). This should support accelerating growth in 2027 and beyond (2–3-year new product maturity cycle). This implies mid-single digit through-cycle growth, which could allow meaningful re-rating from current levels (less than 20x this year's earnings after today's move higher).

\- 3M reported a 2Q operational beat on sales and margin. Organic sales of +5.4% was 150 basis points ahead of Consensus. EPS of \$2.40 was 7% ahead.

\- 2026 guidance raised to org growth >3.5% (prior 3%) and EPS of \$8.80-8.95 (prior \$8.50-8.70, vs. Cons \$8.74).

\- The company noted continued order momentum with strength in general industrial, safety, and data center in addition to strong backlog.

## Equities

Organic growth accelerated to +5.4%, the strongest quarterly performance in nearly five years and about 150 basis points above expectations. More importantly, we believe 3M remains in the early stages of a multi-year growth acceleration, with the benefits of its expanding new product pipeline only beginning to materialize.

<table><tr><td>United States</td></tr><tr><td>Industrial, Diversified</td></tr></table>

12-month rating Buy

12m price target US\$218.00
Prior : US\$190.00

Price (21 Jul 2026) US\$172.16

<table><tr><td colspan="2">Trading data and key metrics</td></tr><tr><td>52-wk range</td><td>US$174.61-141.20</td></tr><tr><td>Market cap.</td><td>US$91.1b</td></tr><tr><td>Shares o/s</td><td>529m (COM)</td></tr><tr><td>Free float</td><td>100%</td></tr><tr><td>Avg. daily volume (&#x27;000)</td><td>1,185</td></tr><tr><td>Avg. daily value (m)</td><td>US$182.4</td></tr><tr><td>Common s/h equity (12/26E)</td><td>US$3.39b</td></tr><tr><td>P/BV (12/26E)</td><td>24.4x</td></tr><tr><td>Net debt to EBITDA (12/26E)</td><td>1.3x</td></tr></table>

EPS (UBS, diluted) (USD)

<table><tr><td rowspan="2"></td><td colspan="4">12/26E</td></tr><tr><td>From</td><td>To</td><td>% ch</td><td>Cons.</td></tr><tr><td>Q1</td><td>2.14</td><td>2.14</td><td>0</td><td>2.14</td></tr><tr><td>Q2</td><td>2.25</td><td>2.40</td><td>7</td><td>2.25</td></tr><tr><td>Q3E</td><td>2.45</td><td>2.45</td><td>-0</td><td>2.37</td></tr><tr><td>Q4E</td><td>2.01</td><td>2.05</td><td>2</td><td>1.99</td></tr><tr><td>12/26E</td><td>8.85</td><td>9.04</td><td>2</td><td>8.74</td></tr><tr><td>12/27E</td><td>10.02</td><td>10.46</td><td>4</td><td>9.49</td></tr><tr><td>12/28E</td><td>10.65</td><td>11.17</td><td>5</td><td>10.18</td></tr></table>

Amit Mehrotra
Analyst
amit.mehrotra@ubs.com
+1-201-352 1410

Neal Burk
Analyst
neal.burk@ubs.com
+1-212-713 4066

Pratap Singh
Analyst
pratap-za.singh@ubs.com
+1-212-821 3112

<table><tr><td>Highlights (US$m)</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>Revenues</td><td>31,392</td><td>23,630</td><td>24,279</td><td>25,455</td><td>26,893</td><td>28,007</td><td>29,173</td><td>30,395</td></tr><tr><td>EBIT (UBS)</td><td>6,388</td><td>5,067</td><td>5,693</td><td>6,160</td><td>6,964</td><td>7,336</td><td>7,800</td><td>8,293</td></tr><tr><td>Net earnings (UBS)</td><td>5,120</td><td>4,032</td><td>4,362</td><td>4,720</td><td>5,344</td><td>5,641</td><td>6,013</td><td>6,407</td></tr><tr><td>EPS (UBS, diluted) (US$)</td><td>9.24</td><td>7.30</td><td>8.06</td><td>9.04</td><td>10.46</td><td>11.17</td><td>12.13</td><td>13.19</td></tr><tr><td>DPS (net) (US$)</td><td>6.00</td><td>3.61</td><td>2.92</td><td>3.12</td><td>3.31</td><td>3.57</td><td>3.69</td><td>3.85</td></tr><tr><td>Net (debt) / cash</td><td>(10,102)</td><td>(7,444)</td><td>(7,367)</td><td>(10,177)</td><td>(10,467)</td><td>(9,131)</td><td>(7,738)</td><td>(4,856)</td></tr></table>

<table><tr><td>Profitability/valuation</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>EBIT (UBS) margin %</td><td>20.3</td><td>21.4</td><td>23.4</td><td>24.2</td><td>25.9</td><td>26.2</td><td>26.7</td><td>27.3</td></tr><tr><td>ROIC (EBIT) %</td><td>30.4</td><td>38.5</td><td>48.6</td><td>48.0</td><td>45.6</td><td>41.7</td><td>41.7</td><td>43.4</td></tr><tr><td>EV/EBITDA (UBS core) x</td><td>8.4</td><td>11.4</td><td>13.4</td><td>12.5</td><td>11.2</td><td>10.7</td><td>10.1</td><td>9.5</td></tr><tr><td>P/E (UBS, diluted) x</td><td>11.2</td><td>15.5</td><td>18.9</td><td>17.6</td><td>15.2</td><td>14.2</td><td>13.1</td><td>12.1</td></tr><tr><td>Equity FCF (UBS) yield %</td><td>30.1</td><td>0.8</td><td>3.0</td><td>3.7</td><td>2.4</td><td>5.1</td><td>5.7</td><td>7.4</td></tr><tr><td>Dividend yield (net) %</td><td>5.8</td><td>3.2</td><td>1.9</td><td>1.8</td><td>1.9</td><td>2.1</td><td>2.1</td><td>2.2</td></tr></table>

Source: Company accounts, LSEG Eikon, UBS estimates. Metrics marked as (UBS) have had analyst adjustments applied. Valuations: based on an average share price that year, (E): based on a share price of US\$ 172.16 on 21-Jul-2026 13:35:37 EDT

This report has been prepared by UBS LLC. ANALYST CERTIFICATION AND REQUIRED DISCLOSURES, INCLUDING INFORMATION ON THE QUANTITATIVE RESEARCH REVIEW PUBLISHED BY UBS, BEGIN ON PAGE 7.

\- After \$4.54 of EPS in 1H, the 2026 guide implies 2H EPS of \$4.33, which suggests some conservatism and potential upside to the full-year guide.

## Valuation:

Our new \$218 price target is based on 24x applied to our 2H27-1H28 EPS forecast. We raise our multiple from 23x to reflect 3M's improved organic sales growth performance, which we believe justifies a smaller discount to the XLI at 25x.

<table><tr><td>Income Statement (US$m)</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>%ch</td><td>12/27E</td><td>%ch</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>Revenues</td><td>31,392</td><td>23,630</td><td>24,279</td><td>25,455</td><td>4.8</td><td>26,893</td><td>5.6</td><td>28,007</td><td>29,173</td><td>30,395</td></tr><tr><td>Gross profit</td><td>13,556</td><td>9,957</td><td>9,685</td><td>10,039</td><td>3.7</td><td>10,845</td><td>8.0</td><td>11,545</td><td>12,288</td><td>13,076</td></tr><tr><td>EBITDA (UBS)</td><td>8,375</td><td>6,430</td><td>7,001</td><td>7,586</td><td>8.3</td><td>8,470</td><td>11.7</td><td>8,903</td><td>9,432</td><td>9,991</td></tr><tr><td>Depreciation &amp; amortisation</td><td>(1,987)</td><td>(1,363)</td><td>(1,308)</td><td>(1,426)</td><td>-9.0</td><td>(1,506)</td><td>-5.6</td><td>(1,567)</td><td>(1,631)</td><td>(1,698)</td></tr><tr><td>EBIT (UBS)</td><td>6,388</td><td>5,067</td><td>5,693</td><td>6,160</td><td>8.2</td><td>6,964</td><td>13.1</td><td>7,336</td><td>7,800</td><td>8,293</td></tr><tr><td>Associates &amp; investment income</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>0</td><td>-</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other non-operating income</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>0</td><td>-</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Net interest</td><td>(184)</td><td>(40)</td><td>(298)</td><td>(211)</td><td>29.4</td><td>(237)</td><td>-12.6</td><td>(237)</td><td>(237)</td><td>(237)</td></tr><tr><td>Exceptionals (incl goodwill)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>0</td><td>-</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Pre-tax profit</td><td>6,204</td><td>5,027</td><td>5,395</td><td>5,949</td><td>10.3</td><td>6,727</td><td>13.1</td><td>7,099</td><td>7,563</td><td>8,056</td></tr><tr><td>Tax</td><td>(1,084)</td><td>(986)</td><td>(1,073)</td><td>(1,191)</td><td>-11.0</td><td>(1,345)</td><td>-13.0</td><td>(1,420)</td><td>(1,513)</td><td>(1,611)</td></tr><tr><td>Profit after tax</td><td>5,119</td><td>4,041</td><td>4,322</td><td>4,758</td><td>10.1</td><td>5,382</td><td>13.1</td><td>5,679</td><td>6,051</td><td>6,445</td></tr><tr><td>Preference dividends</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>0</td><td>-</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Minorities</td><td>1</td><td>(9)</td><td>40</td><td>(38)</td><td>-</td><td>(38)</td><td>0.0</td><td>(38)</td><td>(38)</td><td>(38)</td></tr><tr><td>Extraordinary items</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>0</td><td>-</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Net earnings (local GAAP)</td><td>5,120</td><td>4,032</td><td>4,362</td><td>4,720</td><td>8.2</td><td>5,344</td><td>13.2</td><td>5,641</td><td>6,013</td><td>6,407</td></tr><tr><td>Net earnings (UBS)</td><td>5,120</td><td>4,032</td><td>4,362</td><td>4,720</td><td>8.2</td><td>5,344</td><td>13.2</td><td>5,641</td><td>6,013</td><td>6,407</td></tr><tr><td>Tax rate (%)</td><td>17.5</td><td>19.6</td><td>19.9</td><td>20.0</td><td>0.7</td><td>20.0</td><td>-0.1</td><td>20.0</td><td>20.0</td><td>20.0</td></tr><tr><td>Per Share (US$)</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>%ch</td><td>12/27E</td><td>%ch</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>EPS (UBS, diluted)</td><td>9.24</td><td>7.30</td><td>8.06</td><td>9.04</td><td>12.2</td><td>10.46</td><td>15.7</td><td>11.17</td><td>12.13</td><td>13.19</td></tr><tr><td>EPS (local GAAP, diluted)</td><td>9.24</td><td>7.30</td><td>8.06</td><td>9.04</td><td>12.2</td><td>10.46</td><td>15.7</td><td>11.17</td><td>12.13</td><td>13.19</td></tr><tr><td>EPS (UBS, basic)</td><td>9.24</td><td>7.32</td><td>8.12</td><td>9.09</td><td>12.0</td><td>10.52</td><td>15.7</td><td>11.24</td><td>12.21</td><td>13.27</td></tr><tr><td>DPS (net) (US$)</td><td>6.00</td><td>3.61</td><td>2.92</td><td>3.12</td><td>6.8</td><td>3.31</td><td>6.1</td><td>3.57</td><td>3.69</td><td>3.85</td></tr><tr><td>Cash EPS (UBS, diluted) 1</td><td>12.82</td><td>9.77</td><td>10.47</td><td>11.77</td><td>12.4</td><td>13.41</td><td>13.9</td><td>14.27</td><td>15.43</td><td>16.69</td></tr><tr><td>Book value per share</td><td>8.78</td><td>7.07</td><td>8.73</td><td>6.53</td><td>-25.2</td><td>12.81</td><td>96.1</td><td>18.04</td><td>23.25</td><td>29.42</td></tr><tr><td>Average shares (diluted)</td><td>554</td><td>552</td><td>541</td><td>522</td><td>-3.5</td><td>511</td><td>-2.2</td><td>505</td><td>496</td><td>486</td></tr><tr><td>Balance Sheet (US$m)</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>%ch</td><td>12/27E</td><td>%ch</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>Cash and equivalents</td><td>5,933</td><td>5,600</td><td>5,235</td><td>2,374</td><td>-54.6</td><td>2,084</td><td>-12.2</td><td>3,420</td><td>4,813</td><td>7,695</td></tr><tr><td>Other current assets</td><td>10,446</td><td>10,284</td><td>11,152</td><td>10,075</td><td>-9.7</td><td>11,388</td><td>13.0</td><td>11,465</td><td>12,498</td><td>12,687</td></tr><tr><td>Total current assets</td><td>16,379</td><td>15,884</td><td>16,387</td><td>12,449</td><td>-24.0</td><td>13,473</td><td>8.2</td><td>14,885</td><td>17,312</td><td>20,382</td></tr><tr><td>Net tangible fixed assets</td><td>9,159</td><td>7,388</td><td>7,101</td><td>6,764</td><td>-4.7</td><td>6,335</td><td>-6.4</td><td>5,888</td><td>5,424</td><td>4,941</td></tr><tr><td>Net intangible fixed assets</td><td>17,153</td><td>7,491</td><td>7,522</td><td>7,427</td><td>-1.3</td><td>7,427</td><td>0.0</td><td>7,427</td><td>7,427</td><td>7,427</td></tr><tr><td>Investments / other assets</td><td>7,889</td><td>9,105</td><td>6,723</td><td>6,508</td><td>-3.2</td><td>6,508</td><td>0.0</td><td>6,508</td><td>6,508</td><td>6,508</td></tr><tr><td>Total assets</td><td>50,580</td><td>39,868</td><td>37,733</td><td>33,148</td><td>-12.2</td><td>33,742</td><td>1.8</td><td>34,708</td><td>36,671</td><td>39,258</td></tr><tr><td>Trade payables &amp; other ST liabilities</td><td>12,350</td><td>9,337</td><td>7,925</td><td>9,469</td><td>19.5</td><td>9,725</td><td>2.7</td><td>9,713</td><td>9,980</td><td>9,980</td></tr><tr><td>Short term debt</td><td>2,947</td><td>1,919</td><td>1,670</td><td>1,647</td><td>-1.4</td><td>1,647</td><td>0.0</td><td>1,647</td><td>1,647</td><td>1,647</td></tr><tr><td>Total current liabilities</td><td>15,297</td><td>11,256</td><td>9,595</td><td>11,116</td><td>15.8</td><td>11,372</td><td>2.3</td><td>11,360</td><td>11,627</td><td>11,627</td></tr><tr><td>Long term debt</td><td>13,088</td><td>11,125</td><td>10,932</td><td>10,904</td><td>-0.3</td><td>10,904</td><td>0.0</td><td>10,904</td><td>10,904</td><td>10,904</td></tr><tr><td>Other long term liabilities</td><td>17,327</td><td>13,593</td><td>12,459</td><td>7,738</td><td>-37.9</td><td>4,962</td><td>-35.9</td><td>3,389</td><td>2,687</td><td>2,525</td></tr><tr><td>Preferred shares</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>0</td><td>-</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Total liabilities (incl pref shares)</td><td>45,712</td><td>35,974</td><td>32,986</td><td>29,758</td><td>-9.8</td><td>27,237</td><td>-8.5</td><td>25,652</td><td>25,218</td><td>25,056</td></tr><tr><td>Common s/h equity</td><td>4,868</td><td>3,894</td><td>4,747</td><td>3,391</td><td>-28.6</td><td>6,505</td><td>91.8</td><td>9,055</td><td>11,452</td><td>14,202</td></tr><tr><td>Minority interests</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-</td><td>0</td><td>-</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Total liabilities &amp; equity</td><td>50,580</td><td>39,868</td><td>37,733</td><td>33,148</td><td>-12.2</td><td>33,742</td><td>1.8</td><td>34,708</td><td>36,671</td><td>39,258</td></tr><tr><td>Cash Flow (US$m)</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>%ch</td><td>12/27E</td><td>%ch</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>Net income (before pref divs)</td><td>5,120</td><td>4,032</td><td>4,362</td><td>4,720</td><td>8.2</td><td>5,344</td><td>13.2</td><td>5,641</td><td>6,013</td><td>6,407</td></tr><tr><td>Depreciation &amp; amortisation</td><td>1,987</td><td>1,363</td><td>1,308</td><td>1,426</td><td>9.0</td><td>1,506</td><td>5.6</td><td>1,567</td><td>1,631</td><td>1,698</td></tr><tr><td>Net change in working capital</td><td>535</td><td>201</td><td>(51)</td><td>694</td><td>-</td><td>(1,057)</td><td>-</td><td>(89)</td><td>(765)</td><td>(188)</td></tr><tr><td>Other operating</td><td>11,136</td><td>(3,935)</td><td>(2,217)</td><td>(2,351)</td><td>-6.0</td><td>(2,575)</td><td>-9.5</td><td>(1,371)</td><td>(500)</td><td>2</td></tr><tr><td>Operating cash flow</td><td>18,778</td><td>1,661</td><td>3,402</td><td>4,489</td><td>31.9</td><td>3,217</td><td>-28.3</td><td>5,748</td><td>6,379</td><td>7,918</td></tr><tr><td>Tangible capital expendit

[中间内容因长度限制已省略]

 not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

![](images/eb8455a8b6453d81d412eade1a2d8acfe87d0f6fe6ed497a80afab5be25fd277.jpg)

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
