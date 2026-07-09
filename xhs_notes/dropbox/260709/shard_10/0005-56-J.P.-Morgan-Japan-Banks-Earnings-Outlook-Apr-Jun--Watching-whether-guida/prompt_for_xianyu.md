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
# Japan Banks: Earnings Outlook (Apr-Jun)

## Watching whether guidance is revised at 1Q results to reflect BOJ rate hike in June

We expect many major regional banks that did not announce a share buyback in May to announce buybacks during the Japan bank sector's 1Q FY2026 results reporting season (Figure 4). An even more important watchpoint is whether banks will incorporate the June BOJ rate hike into their guidance. As shown in Figure 3, many banks have not factored in the rate hike. If their guidance takes into account interest rate sensitivity to only a single rate hike, some banks may decide that they do not need to revise guidance, but if any banks move quickly to revise guidance with 1Q results, we would view this positively as a sign of confidence in business progress. Among the megabanks, we believe Mitsubishi UFJ Financial Group (MUFG) is the least likely to report eventful 1Q results. We do not expect MUFG to revise guidance with 1Q results, as its guidance already assumes a mid-2026 rate hike. Among other banks, we expect Sumitomo Mitsui Trust Group (SMTG) and Japan Post Bank (JPB) to post higher YoY rates of profit growth. We expect SMTG to record large gains on the sale of stocks and one-off profits in 1Q. We expect JPB to see a rebound in profit, as net interest income (NII) in the international division was weak in 1Q FY2025 due to a time lag.

YoY growth rates and progress for net profit in 1Q depends on company-specific factors: For Resona Holdings, major regional banks, and other banks, we expect a wide range of YoY growth rates for net profit in 1Q. Some banks recorded gains on asset sales or transient tax benefits in 1Q FY2025, and in these cases we expect relatively large profit declines (for example, at SBI Shinsei Bank, Aozora Bank, and Fukuoka Financial Group). At Seven Bank, we expect a subsidiary to record an extraordinary loss in 1Q FY2026. In addition, we expect YoY profit growth at regional banks to vary depending on whether credit costs or losses on the sale of securities were recorded in 1Q FY2025.

We expect regional banks to announce buybacks: Unless net profit guidance is revised, we do not expect any changes to dividend guidance, so buybacks are likely to be the shareholder return action at 1Q results. The megabanks, SMTG, and Resona Holdings already announced buybacks in May, while the major regional banks in our coverage opted not to announce buybacks in May. Against this backdrop, we expect Shizuoka Financial Group and Yokohama Financial Group to announce share buybacks of ¥40 billion (equivalent to one year's worth or close to it) with 1Q results, while we expect Mebuki Financial Group and Chiba Bank to announce buybacks equal to half their annual forecast amount or less.

Japan Equity Research
Banks

Takahiro Yano, CFA AC
(81-3) 6736-8616
takahiro.yano@JPM.com

Kohichi Takano

(81-3) 6736 8621

kohichi.takano@JPM.com

JPM Securities Japan Co., Ltd.

## Accelerating growth in domestic loan balances

According to BOJ statistics, the average balance of domestic loans grew 5.7% YoY in May 2026. The YoY growth rate slowed to the mid-2% level in 1H 2025 but has started rising again (Figure 8). Growth has accelerated markedly in 2026 (Figures 8-9). At city banks, the growth rate for loans to large corporations reached +10% YoY in March 2026 and accelerated further to +14% in May (Figure 10). At regional banks, loans to large corporations continue to grow at a high-single-digit YoY rate (Figure 11). The three-month TIBOR yield, which often serves as a benchmark for market rate-linked loan yields, has risen further following the rate hikes in December 2025 and June 2026 (Figures 15-16). We see no notable changes in the number of bankruptcies in Japan (Figure 17).

## Valuation gains/losses on available-for-sale (AFS) securities worsened compared with end-March

From end-March to end-June 2026, JGB yields rose slightly in the short-term zone and increased more significantly in the 7-10 year zone. US Treasury yields rose relatively sharply in the 2-3 year zone, while the increase in the 10-year zone was more moderate. Meanwhile, TOPIX rose sharply, up 14% QoQ. At many banks, the increase in equity valuation gains more than offset the deterioration in yen bond and foreign bond valuation gains/losses, so it seems overall valuation gains/losses improved QoQ (Figures 22-24).

## Deposits continued to grow at online banks

Rakuten Bank is an online bank we cover, and its monthly disclosures show that the deposit balance growth rate slowed in 2025. However, the YoY growth rate bottomed at +7.2% in June 2025 and rebounded to around +10% in 2H 2025. Since the start of 2026, YoY growth has remained at +13–15%, partly due to a low year-ago hurdle (Figure 38).

## SBI Holdings

SBI Securities made online trading of domestic stocks commission-free from end-September 2023, so we expect financial income (such as margin trading-related income) and trading gains/losses (such as from forex transactions) to drive its income growth. Looking at the market as a whole, margin trading balances have increased to record-high levels compared to the past (Figure 39). We expect further growth in margin trading-related fees. Meanwhile, over-the-counter FX margin trading slowed QoQ in April-May 2026 (Figure 40). We expect SBI Holdings to post a YoY decline in net profit in 1Q, mainly due to quarterly volatility in tax rates and minority interests. For pretax profit in the core financial services businesses, we forecast a 34% YoY increase in 1Q, supported by gains on the sale of a subsidiary.

Figure 1: TOPIX Bank Index and JGB 10-year yield  
![](images/162f6ff90bdd6d47677934810488eda4967e945c60a8b4b1961c8f89124a2c48.jpg)  
Source: Compiled by JPM based on data from Bloomberg Finance L.P.

Figure 2: Share price performance (1M)

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Company</td><td rowspan="2">Rating</td><td rowspan="2">Target price (¥)</td><td>Mkt Cap (Y bn)</td><td colspan="3">Share price (¥)</td><td colspan="2">Share price (¥)</td></tr><tr><td>7/3/2026</td><td>7/3/2026</td><td>6/5/2026</td><td>12/30/2025</td><td>2026/6/5-7/3</td><td>2025/12/30-</td></tr><tr><td>7186</td><td>Yokohama FG</td><td>OW</td><td>1,980</td><td>2,115</td><td>1,848</td><td>1,647</td><td>1,294</td><td>+12.2%</td><td>+42.9%</td></tr><tr><td>8331</td><td>Chiba bank</td><td>OW</td><td>2,890</td><td>2,067</td><td>2,665</td><td>2,381</td><td>1,748</td><td>+12.0%</td><td>+52.5%</td></tr><tr><td>5831</td><td>Shizuoka FG</td><td>OW</td><td>3,500</td><td>1,875</td><td>3,232</td><td>2,897</td><td>2,432</td><td>+11.6%</td><td>+32.9%</td></tr><tr><td>7167</td><td>Mebuki FG</td><td>OW</td><td>1,580</td><td>1,429</td><td>1,509</td><td>1,358</td><td>1,038</td><td>+11.2%</td><td>+45.4%</td></tr><tr><td>7164</td><td>Zenkoku Hosho</td><td>N</td><td>3,000</td><td>425</td><td>3,082</td><td>2,808</td><td>3,121</td><td>+9.8%</td><td>(-1.2%)</td></tr><tr><td>5838</td><td>Rakuten Bank</td><td>N</td><td>5,390</td><td>941</td><td>5,395</td><td>4,950</td><td>6,912</td><td>+9.0%</td><td>(-21.9%)</td></tr><tr><td>8309</td><td>SMTG</td><td>N</td><td>6,470</td><td>4,421</td><td>6,326</td><td>5,828</td><td>4,777</td><td>+8.5%</td><td>+32.4%</td></tr><tr><td>8304</td><td>Aozora</td><td>N</td><td>2,850</td><td>396</td><td>2,830</td><td>2,623</td><td>2,509</td><td>+7.9%</td><td>+12.8%</td></tr><tr><td>8316</td><td>SMFG</td><td>OW</td><td>7,700</td><td>25,537</td><td>6,672</td><td>6,230</td><td>5,041</td><td>+7.1%</td><td>+32.4%</td></tr><tr><td>8354</td><td>Fukuoka FG</td><td>N</td><td>7,470</td><td>1,380</td><td>7,221</td><td>6,797</td><td>5,067</td><td>+6.2%</td><td>+42.5%</td></tr><tr><td>8308</td><td>Resona HD</td><td>N</td><td>2,400</td><td>5,181</td><td>2,246</td><td>2,118</td><td>1,493</td><td>+6.0%</td><td>+50.4%</td></tr><tr><td>8411</td><td>Mizuho FG</td><td>OW</td><td>9,530</td><td>19,733</td><td>8,078</td><td>7,716</td><td>5,700</td><td>+4.7%</td><td>+41.7%</td></tr><tr><td>8410</td><td>Seven Bank</td><td>UW</td><td>235</td><td>341</td><td>289</td><td>276</td><td>305</td><td>+4.6%</td><td>(-5.3%)</td></tr><tr><td>8303</td><td>SBI Shinsei Bank</td><td>UW</td><td>1,520</td><td>1,296</td><td>1,448</td><td>1,396</td><td>1,740</td><td>+3.7%</td><td>(-16.8%)</td></tr><tr><td>8306</td><td>MUFG</td><td>OW</td><td>3,870</td><td>39,472</td><td>3,326</td><td>3,219</td><td>2,493</td><td>+3.3%</td><td>+33.4%</td></tr><tr><td>7182</td><td>JP Bank</td><td>OW</td><td>3,900</td><td>11,550</td><td>3,230</td><td>3,161</td><td>2,209</td><td>+2.2%</td><td>+46.2%</td></tr><tr><td>8473</td><td>SBI HD</td><td>OW</td><td>4,180</td><td>1,782</td><td>2,696</td><td>2,887</td><td>3,375</td><td>(-6.6%)</td><td>(-20.1%)</td></tr><tr><td>TPNBNK Index</td><td>TOPIX Bank</td><td>-</td><td>-</td><td>135,816</td><td>708</td><td>670</td><td>517</td><td>+5.7%</td><td>+37.0%</td></tr><tr><td>TPX Index</td><td>TOPIX</td><td>-</td><td>-</td><td>1,350,794</td><td>4,065</td><td>3,949</td><td>3,409</td><td>+2.9%</td><td>+19.2%</td></tr></table>

Source: Compiled by JPM based on data from Bloomberg Finance L.P.

Figure 3: Comparison of quarterly net profit results and forecasts

<table><tr><td colspan="2"></td><td colspan="11">Profits attributable to owners of parent (JPY mn)</td></tr><tr><td colspan="2">(¥ million)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26e</td><td>FY2026 CE</td><td>YoY</td><td>FY2026 JPMe (X)</td><td>1Q25 vs FY2025A</td><td>1Q26e vs FY2026CE</td><td>1Q26e YoY</td></tr><tr><td>8306 JT</td><td>MUFG</td><td>546,000</td><td>746,900</td><td>520,600</td><td>613,700</td><td>568,788</td><td>2,700,000</td><td>+11%</td><td>2,712,500</td><td>22%</td><td>21%</td><td>+4%</td></tr><tr><td>8316 JT</td><td>SMFG</td><td>376,900</td><td>556,600</td><td>461,300</td><td>188,200</td><td>388,488</td><td>1,700,000</td><td>+7%</td><td>1,917,900</td><td>24%</td><td>23%</td><td>+3%</td></tr><tr><td>8411 JT</td><td>Mizuho FG</td><td>290,500</td><td>399,447</td><td>329,853</td><td>228,832</td><td>302,133</td><td>1,300,000</td><td>+4%</td><td>1,425,100</td><td>23%</td><td>23%</td><td>+4%</td></tr><tr><td>8309 JT</td><td>SMTG</td><td>90,800</td><td>80,500</td><td>95,300</td><td>50,900</td><td>116,968</td><td>380,000</td><td>+20%</td><td>402,200</td><td>29%</td><td>31%</td><td>+29%</td></tr><tr><td>7182 JT</td><td>JP Bank</td><td>104,862</td><td>135,534</td><td>137,277</td><td>147,910</td><td>138,156</td><td>660,000</td><td>+26%</td><td>660,900</td><td>20%</td><td>21%</td><td>+32%</td></tr><tr><td>8308 JT</td><td>Resona</td><td>70,530</td><td>72,336</td><td>79,265</td><td>36,586</td><td>65,424</td><td>310,000</td><td>+20%</td><td>320,500</td><td>27%</td><td>21%</td><td>(-7%)</td></tr><tr><td>5831 JT</td><td>Shizuoka FG</td><td>22,582</td><td>23,928</td><td>23,184</td><td>20,775</td><td>27,013</td><td>105,000</td><td>+16%</td><td>116,000</td><td>25%</td><td>26%</td><td>+20%</td></tr><tr><td>7167 JT</td><td>Mebuki FG</td><td>22,223</td><td>21,552</td><td>20,881</td><td>19,507</td><td>22,063</td><td>95,000</td><td>+13%</td><td>92,400</td><td>26%</td><td>23%</td><td>(-1%)</td></tr><tr><td>7186 JT</td><td>Yokohama FG</td><td>27,036</td><td>27,991</td><td>29,981</td><td>21,515</td><td>26,462</td><td>129,000</td><td>+21%</td><td>133,900</td><td>25%</td><td>21%</td><td>(-2%)</td></tr><tr><td>8331 JT</td><td>Chiba</td><td>21,783</td><td>22,439</td><td>24,583</td><td>25,258</td><td>24,595</td><td>107,000</td><td>+14%</td><td>113,700</td><td>23%</td><td>23%</td><td>+13%</td></tr><tr><td>8354 JT</td><td>Fukuoka FG</td><td>22,836</td><td>20,738</td><td>26,773</td><td>15,081</td><td>20,872</td><td>100,000</td><td>+17%</td><td>105,100</td><td>27%</td><td>21%</td><td>(-9%)</td></tr><tr><td colspan="13"></td></tr><tr><td>5838 JT</td><td>Rakuten Bank</td><td>16,835</td><td>17,172</td><td>19,112</td><td>19,953</td><td>19,532</td><td>81,325</td><td>+11%</td><td>88,550</td><td>23%</td><td>24%</td><td>+16%</td></tr><tr><td>8303 JT</td><td>SBI Shinsei</td><td>44,200</td><td>25,100</td><td>21,600</td><td>22,500</td><td>19,742</td><td>92,400</td><td>(-19%)</td><td>93,000</td><td>39%</td><td>21%</td><td>(-55%)</td></tr><tr><td>8304 JT</td><td>Aozora</td><td>6,326</td><td>7,287</td><td>8,212</td><td>3,880</td><td>5,288</td><td>27,000</td><td>+5%</td><td>27,100</td><td>25%</td><td>20%</td><td>(-16%)</td></tr><tr><td>8410 JT</td><td>Seven</td><td>4,188</td><td>5,778</td><td>(1,191)</td><td>4,701</td><td>3,311</td><td>17,000</td><td>+26%</td><td>17,800</td><td>31%</td><td>19%</td><td>(-21%)</td></tr><tr><td>7164 JT</td><td>Zenkoku Hosho</td><td>5,999</td><td>5,675</td><td>6,339</td><td>14,513</td><td>5,595</td><td>32,700</td><td>+1%</td><td>33,300</td><td>18%</td><td>17%</td><td>(-7%)</td></tr><tr><td>8473 JT</td><td>SBI Holdings</td><td>84,605</td><td>81,196</td><td>183,335</td><td>78,441</td><td>59,142</td><td>N.A.</td><td></td><td>167,430</td><td>20%</td><td>N.A.</td><td>(-30%)</td></tr></table>

Source: Company data and JPM estimates.  
Note: CE is company guidance.

<table><tr><td>Assumptions</td></tr><tr><td>One hike in mid-2026, ignore Middle East risk</td></tr><tr><td>No hikes in FY2026, reflect Middle East risk</td></tr><tr><td>No hikes in FY2026, ignore Middle East risk</td></tr><tr><td>No hikes in FY2026</td></tr><tr><td>One hike in mid-2026 and another hike in early 2027</td></tr><tr><td>One hike in Jan 2027</td></tr><tr><td>No hikes in FY2026</td></tr><tr><td>No hikes in FY2026</td></tr><tr><td>No hikes in FY2026</td></tr><tr><td>No hikes in FY2026</td></tr><tr><td>No hikes in FY2026</td></tr><tr><td>Two hikes in FY2026</td></tr><tr><td>Two hikes in FY2026</td></tr><tr><td>No benefit from price hike in FY2026</td></tr><tr><td>Ignore any inorganic investment</td></tr></table>

Figure 4: FY2026 DPS and share buyback estimates

<table><tr><td rowspan="2" colspan="2"></td><td colspan="5">DPS (JPY)</td></tr><tr><td>FY2023A</td><td>FY2024A</td><td>FY2025A</td><td>FY2026CE</td><td>FY2026JPMe</td></tr><tr><td>8306 JT</td><td>MUFG</td><td>41.0</td><td>64.0</td><td>86.0</td><td>96.0</td><td>96.0</td></tr><tr><td>8316 JT</td><td>SMFG</td><td>90.0</td><td>122.0</td><td>157.0</td><td>180.0</td><td>200.0</td></tr><tr><td>8411 JT</td><td>Mizuho FG</td><td>105.0</td><td>140.0</td><td>145.0</td><td>150.0</td><td>150.0</td></tr><tr><td>8309 JT</td><td>SMTG</td><td>110.0</td><td>155.0</td><td>185.0</td><td>190.0</td><td>195.0</td></tr><tr><td>7182 JT</td><td>JP Bank</td><td>51.0</td><td>58.0</td><td>74.0</td><td>93.0</td><td>93.0</td></tr><tr><td>8308 JT</td><td>Resona</td><td>22.0</td><td>25.0</td><td>29.0</td><td>37.0</td><td>38.0</td></tr><tr><td>5831 JT</td><td>Shizuoka FG</td><td>39.0</td><td>60.0</td><td>80.0</td><td>98.0</td><td>110.0</td></tr><tr><td>7167 JT</td><td>Mebuki FG</td><td>12.0</td><td>16.0</td><td>28.0</td><td>40.0</td><td>40.0</td></tr><tr><td>7186 JT</td><td>Yokohama FG</td><td>23.0</td><td>29.0</td><td>38.0</td><td>47.0</td><td>49.0</td></tr><tr><td>8331 JT</td><td>Chiba</td><td>32.0</td><td>40.0</td><td>52.0</td><td>64.0</td><td>66.0</td></tr><tr><td>8354 JT</td><td>Fukuoka FG</td><td>115.0</td><td>135.0</td><td>180.0</td><td>210.0</td><td>220.0</td></tr><tr><td>5838 JT</td><td>Rakuten Bank</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>8303 JT</td><td>SBI Shinsei</td><td>N.A.</td><td>N.A.</td><td>42.0</td><td>42.0</td><td>42.0</td></tr><tr><td>8304 JT</td><td>Aozora</td><td>76.0</td><td>79.0</td><td>91.0</td><td>100.0</td><td>100.0</td></tr><tr><td>8410 JT</td><td>Seven</td><td>11.0</td><td>11.0</td><td>11.0</td><td>11.0</td><td>11.0</td></tr><tr><td>7164 JT</td><td>Zenkoku Hosho</td><td>85.0</td><td>106.0</td><td>120.0</td><td>123.0</td><td>127.0</td></tr><tr><td>8473 JT</td><td>SBI Holdings</td><td>80.0</td><td>85.0</td><td>95.0</td><td>N.A.</td><td>124.0</td></tr></table>

Source: Compan

[中间内容因长度限制已省略]

er JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer
"""
