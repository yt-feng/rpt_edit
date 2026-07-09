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
# Taiwan Electronic Components & Equipment

Riding the AIDC BBU Growth Cycle; Initiate Dynapack at Buy

## CITI'S TAKE

We believe AI infrastructure is entering a new power architecture cycle, where rising power density is driving a structural shift from centralized UPS toward rack-level backup power. We expect this transition to significantly increase both BBU content value per rack and industry penetration over the next several years, creating a multi-year growth opportunity that remains underappreciated by the market. We initiate Dynapack at Buy with TP NT\$800 (32x 2027E P/E) as we believe it is one of the most direct beneficiaries of this structural transition. Boosted by accelerating BBU demand, improving product mix and expanding profitability, we forecast 34% sales CAGR and 60% earnings CAGR over 2025-2028E.

AI power architecture is shifting toward distributed backup power, making BBU increasingly essential — Battery Backup Unit (BBU) is emerging as a key enabling technology in next gen AIDC as rack power density continues to rise. Compared with centralized UPS, localized backup power provides faster ride-through capability, lower power conversion losses and better scalability. We believe this represents a structural evolution in AI power architecture, making BBU an increasingly standard component in high-density AI racks.

We see both BBU content value and penetration expanding meaningfully as AI power architecture evolves — Based on our bottom-up module approach, we estimate BBU content value per AI rack rises from c.US\$15-16K today for GB300 NVL72 to US\$17-18K for Rubin and could exceed US\$33K under Rubin Ultra as higher-power BBU modules become necessary. We also estimate BBU penetration increases from 40-45% in 2025 to 60-65% in 2026 and above 85% in 2027, supported by the adoption of rack-scale architectures and HVDC power distribution. We believe the combination of rising content value and penetration creates a compelling structural growth opportunity for the BBU ecosystem.

Initiate Dynapack at Buy with TP NT\$800 as we view it as the most direct beneficiary of the strong BBU growth cycle — We believe the company is well positioned to benefit from the structural migration toward rack-level backup power, capturing accelerating BBU demand as AI rack power increases, driving 34% group sales CAGR in 2025-2028E, supported by 74% CAGR in non-IT sales. With product mix shifting toward high-margin BBU products, we forecast GPM to reach 28.4% in 2028E from 16.6% in 2025, driving 60% earnings CAGR over 2025-2028E. We assign a 32x target P/E on our 2027E EPS of NT\$25 to derive our TP NT\$800.

Prefer Dynapack over AES — While AES remains the dominant BBU supplier given its scale, customer relationships, and technology leadership, we believe Dynapack offers a more attractive risk-reward profile at the current stage of the AI infrastructure investment cycle, as its earnings remain in the early phase of a multi-year growth and margin expansion story. We estimate 60% earnings CAGR over 2025-2028E for Dynapack vs. AES's 27% driven by product mix improvement and stronger op leverage.

Angela Hsu AC

+886-2-8726-9083

angela.hc.hsu@citi.com

## Data Summary

<table><tr><td rowspan="2" colspan="14"></td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td><td></td></tr><tr><td colspan="2">EPS</td><td colspan="2">EPS</td><td></td></tr><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Ccy</td><td rowspan="2">Price</td><td rowspan="2">Mkt Cap (M)</td><td rowspan="2">Date &amp; Time</td><td colspan="2">Rating</td><td rowspan="2">Short-Term View</td><td colspan="2">Target Price</td><td rowspan="2">ESPR (%)</td><td rowspan="2">Div Yld (%)</td><td rowspan="2">ETR (%)</td><td rowspan="2">Last Rpt Yr</td><td rowspan="2">Old</td><td rowspan="2">New</td><td rowspan="2">Old</td><td rowspan="2">New</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td></tr><tr><td>Advanced Energy Solution</td><td>6781.TW</td><td>NT$</td><td>1,250.00</td><td>106,773</td><td>06 Jul 13:30</td><td>1</td><td>nc</td><td>-</td><td>1,660.00</td><td>1,680.00</td><td>34.4</td><td>1.8</td><td>36.2</td><td>Dec-25</td><td>51.89</td><td>46.35</td><td>65.91</td><td>61.35</td></tr><tr><td>Dynapack International</td><td>3211.TWO</td><td>NT$</td><td>422.50</td><td>65,194</td><td>06 Jul 15:00</td><td></td><td>1</td><td>-</td><td>-</td><td>800.00</td><td>89.3</td><td>2.8</td><td>92.2</td><td>Dec-25</td><td>-</td><td>15.00</td><td>-</td><td>25.00</td></tr><tr><td colspan="6">1 = Buy, 2 = Neutral, 3 = Sell, H = High Risk</td><td colspan="13">ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change</td></tr><tr><td colspan="6">Source: Citi</td><td colspan="13">^Catalyst Watch</td></tr></table>

Earnings Estimates

<table><tr><td colspan="4"></td><td colspan="5">Last Reported Year</td><td colspan="5">Current Fiscal Year</td><td colspan="5">Next Fiscal Year</td></tr><tr><td>Company Name</td><td>Ticker</td><td>Last Rpt Year</td><td>Currency</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY0</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY1</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY2</td></tr><tr><td>Advanced Energy Solution</td><td>6781.TW</td><td>Dec-25</td><td>NT$</td><td>9.70</td><td>9.66</td><td>9.35</td><td>9.49</td><td>38.20</td><td>10.64</td><td>11.41</td><td>12.12</td><td>12.19</td><td>46.35</td><td>12.79</td><td>14.64</td><td>16.73</td><td>17.19</td><td>61.35</td></tr><tr><td>Old</td><td></td><td>Dec-24</td><td>NT$</td><td>5.41</td><td>5.22</td><td>6.27</td><td>8.49</td><td>25.39</td><td>9.70</td><td>9.66</td><td>10.71</td><td>9.99</td><td>40.06</td><td>8.89</td><td>11.76</td><td>15.75</td><td>15.49</td><td>51.89</td></tr><tr><td>Dynapack International</td><td>3211.TWO</td><td>Dec-25</td><td>NT$</td><td>1.07</td><td>3.89</td><td>1.56</td><td>2.53</td><td>9.05</td><td>2.05</td><td>2.37</td><td>4.19</td><td>6.39</td><td>15.00</td><td>3.85</td><td>3.82</td><td>6.78</td><td>10.55</td><td>25.00</td></tr><tr><td colspan="19">Source: Citi</td></tr></table>

## Contents

Executive Summary 6
BBU: Powering Next Gen AI Racks 12
A Closer Look at BBU Supply Chain 17
BBU: Rising Content Value and Penetration As Power
Density Further Accelerates 20
Dynapack (3211.TWO): Our Investment Thesis 26
Investment positive #1 – riding on the strong demand of BBU from AIDC buildout, driving structural growth 26
Investment positive #2 – Intact margin expansion from rising non-IT sales 30
Investment positive #3 – Strong Partnership with PSU operators provides access to a broader CSP base 32
Dynapack (3211.TWO): Financial Analysis 35
Dynapack (3211.TWO): Valuation Methodology and Risks 40
Dynapack (3211.TWO): Company Overview 42
Bull/Bear: Advanced Energy Solution (6781.TW) 49
Bull/Bear: Dynapack International (3211.TWO) 50
Advanced Energy Solution 51
Company description 51
Investment strategy 51
Valuation 51
Risks 51
Dynapack International 51
Company description 51
Investment strategy 52
Valuation 52
Risks 52
Appendix A-1 53

Figure 1. Valuation Comp of BBU Supply Chain

<table><tr><td rowspan="2">Company</td><td rowspan="2">RIC</td><td rowspan="2">Rating*</td><td rowspan="2">Curr</td><td rowspan="2">Target Price</td><td rowspan="2">Price 6-Jul</td><td rowspan="2">Mkt-Cap US$M</td><td rowspan="2">3M ADT US$M</td><td colspan="3">P/E (x)</td><td colspan="3">EV/EBITDA (x)</td><td colspan="3">P/B (x)</td><td colspan="3">Dividend yield (%)</td><td colspan="2">25-27E 2yr EPS</td><td colspan="2">ROE</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>CAGR (%)</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="24">Taiwan</td></tr><tr><td>Dynapack</td><td>3211.TWO</td><td>1</td><td>TWD</td><td>800.0</td><td>422.5</td><td>2,041.1</td><td>116.9</td><td>28.2</td><td>16.9</td><td>11.3</td><td>19.2</td><td>11.7</td><td>7.9</td><td>7.3</td><td>6.7</td><td>6.0</td><td>2.8</td><td>4.7</td><td>7.1</td><td>66.3</td><td>24%</td><td>41%</td><td>56%</td></tr><tr><td>AES-KY</td><td>6781.TW</td><td>1</td><td>TWD</td><td>1,680.0</td><td>1,250.0</td><td>3,342.8</td><td>61.1</td><td>27.0</td><td>20.4</td><td>16.0</td><td>18.4</td><td>13.6</td><td>10.6</td><td>5.2</td><td>4.5</td><td>3.8</td><td>1.8</td><td>2.4</td><td>3.1</td><td>26.7</td><td>21%</td><td>24%</td><td>26%</td></tr><tr><td>STL</td><td>4931.TWO</td><td>NR</td><td>TWD</td><td>NA</td><td>261.0</td><td>535.8</td><td>72.2</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td></tr><tr><td>Sysgration</td><td>5309.TWO</td><td>NR</td><td>TWD</td><td>NA</td><td>68.9</td><td>496.9</td><td>18.4</td><td>53.0</td><td>20.4</td><td>na</td><td>na</td><td>na</td><td>na</td><td>7.4</td><td>5.7</td><td>na</td><td>0.9</td><td>1.7</td><td>na</td><td>72.8</td><td>9%</td><td>26%</td><td>na</td></tr><tr><td>Simplo</td><td>6121.TWO</td><td>1</td><td>TWD</td><td>480.0</td><td>467.5</td><td>2,707.3</td><td>12.0</td><td>14.6</td><td>12.3</td><td>na</td><td>4.5</td><td>3.6</td><td>na</td><td>2.4</td><td>2.2</td><td>na</td><td>4.9</td><td>5.8</td><td>na</td><td>16.2</td><td>17%</td><td>19%</td><td>na</td></tr><tr><td>Celxpert</td><td>3323.TWO</td><td>NR</td><td>TWD</td><td>NA</td><td>37.6</td><td>117.0</td><td>2.1</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td></tr><tr><td>Delta</td><td>2308.TW</td><td>1</td><td>TWD</td><td>2,480.0</td><td>1,995.0</td><td>162,239.7</td><td>849.2</td><td>50.9</td><td>32.3</td><td>19.6</td><td>26.7</td><td>17.8</td><td>10.9</td><td>13.3</td><td>9.7</td><td>6.7</td><td>1.0</td><td>1.6</td><td>2.6</td><td>63.3</td><td>28%</td><td>35%</td><td>40%</td></tr><tr><td>Lite-On</td><td>2301.TW</td><td>NR</td><td>TWD</td><td>NA</td><td>224.0</td><td>16,242.7</td><td>229.6</td><td>25.9</td><td>18.7</td><td>14.9</td><td>16.2</td><td>11.5</td><td>9.8</td><td>5.2</td><td>4.7</td><td>4.6</td><td>2.9</td><td>3.8</td><td>4.8</td><td>34.6</td><td>21%</td><td>27%</td><td>31%</td></tr><tr><td>AcBel</td><td>6282.TW</td><td>NR</td><td>TWD</td><td>NA</td><td>59.8</td><td>1,602.7</td><td>74.7</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td></tr><tr><td>Voltronic</td><td>6409.TW</td><td>NR</td><td>TWD</td><td>NA</td><td>1,290.0</td><td>3,564.3</td><td>34.5</td><td>38.8</td><td>30.9</td><td>25.6</td><td>26.0</td><td>22.1</td><td>18.7</td><td>12.0</td><td>10.7</td><td>9.9</td><td>2.4</td><td>2.5</td><td>2.8</td><td>2.6</td><td>31%</td><td>36%</td><td>41%</td></tr><tr><td>Chicony</td><td>6412.TW</td><td>NR</td><td>TWD</td><td>NA</td><td>92.0</td><td>1,154.3</td><td>9.7</td><td>16.3</td><td>13.9</td><td>na</td><td>7.9</td><td>6.2</td><td>na</td><td>2.2</td><td>2.4</td><td>na</td><td>4.5</td><td>5.5</td><td>na</td><td>13.0</td><td>14%</td><td>19%</td><td>na</td></tr><tr><td>Sub-Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>31.8</td><td>20.7</td><td>17.5</td><td>17.0</td><td>12.3</td><td>11.6</td><td>6.9</td><td>5.8</td><td>6.2</td><td>2.7</td><td>3.5</td><td>4.1</td><td>36.9</td><td>21%</td><td>28%</td><td>39%</td></tr><tr><td colspan="24">Korea &amp; Japan</td></tr><tr><td>Panasonic</td><td>6752.T</td><td>1</td><td>JPY</td><td>5,100.0</td><td>4,557.0</td><td>65,932.3</td><td>272.7</td><td>65.5</td><td>23.3</td><td>18.5</td><td>17.9</td><td>11.1</td><td>9.3</td><td>2.0</td><td>1.9</td><td>1.8</td><td>0.9</td><td>1.2</td><td>1.5</td><td>11.7</td><td>3%</td><td>9%</td><td>10%</td></tr><tr><td>Murata</td><td>6981.T</td><td>1</td><td>JPY</td><td>15,000.0</td><td>10,250.0</td><td>115,618.9</td><td>1,175.3</td><td>80.7</td><td>53.8</td><td>37.8</td><td>38.6</td><td>28.9</td><td>21.1</td><td>6.9</td><td>6.4</td><td>5.7</td><td>0.6</td><td>0.7</td><td>0.8</td><td>21.8</td><td>9%</td><td>12%</td><td>16%</td></tr><tr><td>Samsung SDI</td><td>006400.KS</td><td>1</td><td>KRW</td><td>900,000.0</td><td>451,500.0</td><td>23,791.5</td><td>294.5</td><td>161.9</td><td>21.5</td><td>16.4</td><td>29.5</td><td>9.3</td><td>8.2</td><td>1.4</td><td>1.4</td><td>1.3</td><td>0.2</td><td>0.2</td><td>0.2</td><td>na</td><td>1%</td><td>6%</td><td>8%</td></tr><tr><td>LG Energy</td><td>373220.KS</td><td>1</td><td>KRW</td><td>565,000.0</td><td>354,500.0</td><td>54,242.5</td><td>142.6</td><td>335.8</td><td>38.1</td><td>16.6</td><td>18.9</td><td>11.6</td><td>7.5</td><td>3.8</td><td>3.4</td><td>2.9</td><td>na</td><td>na</td><td>na</td><td>na</td><td>1%</td><td>9%</td><td>19%</td></tr><tr><td>Sub-Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>160.9</td><td>34.2</td><td>22.3</td><td>26.2</td><td>15.2</td><td>11.5</td><td>3.5</td><td>3.3</td><td>2.9</td><td>0.6</td><td>0.7</td><td>0.8</td><td>16.8</td><td>4%</td><td>9%</td><td>13%</td></tr><tr><td colspan="24">China</td></tr><tr><td>Kehua</td><td>002335.SZ</td><td>NR</td><td>CNY</td><td>NA</td><td>37.9</td><td>4,188.7</td><td>263.5</td><td>38.0</td><td>27.9</td><td>22.4</td><td>20.2</td><td>16.4</td><td>14.5</td><td>3.7</td><td>3.4</td><td>3.1</td><td>1.3</td><td>1.8</td><td>3.0</td><td>56.0</td><td>11%</td><td>15%</td><td>17%</td></tr><tr><td>KSTAR</td><td>002518.SZ</td><td>NR</td><td>CNY</td><td>NA</td><td>47.5</td><td>4,081.2</td><td>120.9</td><td>30.4</td><td>21.6</td><td>16.7</td><td>22.1</td><td>16.2</td><td>12.4</td><td>5.0</td><td>4.3</td><td>3.5</td><td>1.3</td><td>1.9</td><td>2.7</td><td>44.2</td><td>17%</td><td>20%</td><td>22%</td></tr><tr><td>INVT</td><td>002334.SZ</td><td>NR</td><td>CNY</td><td>NA</td><td>7.1</td><td>858.1</td><td>53.1</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td></tr><tr><td>CATL</td><td>300750.SZ</td><td>1</td><td>CNY</td><td>603.0</td><td>374.5</td><td>262,482.4</td><td>2,231.0</td><td>16.6</td><td>13.5</td><td>11.5</td><td>11.0</td><td>8.5</td><td>6.8</td><td>4.2</td><td>3.6</td><td>3.0</td><td>3.0</td><td>3.7</td><td>4.4</td><td>32.3</td><td>28%</td><td>29%</td><td>29%</td></tr><tr><td>BYD</td><td>002594.SZ</td><td>1</td><td>CNY</td><td>131.0</td><td>87.5</td><td>97,413.2</td><td>643.4</td><td>19.8</td><td>16.8</td><td>12.7</td><td>4.5</td><td>3.6</td><td>2.7</td><td>2.9</td><td>2.6</td><td>2.3</td><td>na</td><td>na</td><td>na</td><td>21.0</td><td>15%</td><td>16%</td><td>19%</td></tr><tr><td>EVE Energy</td><td>300014.SZ</td><td>1</td><td>CNY</td><td>87.9</td><td>59.4</td><td>19,060.9</td><td>747.5</td><td>14.8</td><td>12.0</td><td>9.0</td><td>10.6</td><td>8.7</td><td>6.1</td><td>2.5</td><td>2.2</td><td>1.8</td><td>1.7</td><td>2.1</td><td>2.7</td><td>57.8</td><td>18%</td><td>20%</td><td>22%</td></tr><tr><td>Sunwoda</td><td>300207.SZ</td><td>NR</td><td>CNY</td><td>NA</td><td>18.2</td><td>4,964.4</td><td>253.2</td><td>13.9</td><td>9.5</td><td>7.4</td><td>6.9</td><td>4.9</td><td>3.5</td><td>1.3</td><td>1.1</td><td>1.0</td><td>1.6</td><td>2.4</td><td>3.0</td><td>83.3</td><td>9%</td><td>12%</td><td>14%</td></tr><tr><td>Sub-Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>22.2</td><td>16.9</td><td>13.3</td><td>12.6</td><td>9.7</td><td>7.7</td><td>3.3</td><td>2.9</td><td>2.5</td><td>1.8</td><td>2.4</td><td>3.1</td><td>49.1</td><td>16%</td><td>19%</td><td>20%</td></tr><tr><td colspan="24">Global</td></tr><tr><td>Vertiv</td><td>VRT.N</td><td>1</td><td>USD</td><td>414.0</td><td>318.5</td><td>122,327.1</td><td>

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
