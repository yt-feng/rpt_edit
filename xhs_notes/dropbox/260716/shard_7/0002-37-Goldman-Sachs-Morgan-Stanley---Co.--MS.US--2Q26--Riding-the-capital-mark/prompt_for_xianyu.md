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
12m Price Target: \$241.00

Price: \$227.67

Upside: $5.9\%$

MS reported 2Q26 EPS of \$3.46 vs GSe/Visible Alpha Consensus Data at \$3.44/\$2.94, while core EPS of \$3.52 was better than GSe/consensus like estimates of \$3.47/\$2.95 $^{1}$ . The company once again delivered results well in excess of its targets: 1) a 30.5% core wealth management (GWM) pre-tax margin (vs. a 30% target); 2) a 65.1% core efficiency ratio (vs. a 70% target); and 3) a 27.1% core ROTCE (vs. a 20% target). While management has not revised their targets and have stated that the bar for them to do so is high, given the robust pipelines in capital markets, the heightened levels of client engagement across both retail and institutional businesses, as well as the increasingly fixed cost nature of the business we would expect MS to run above these targets at least in the near term.

Results and management commentary supported a constructive outlook: 1) A robust capital markets backdrop, with the company highlighting a strong investment banking backdrop, with a healthy, globally broadening pipeline. In trading, the company highlighted a solid operating backdrop, noting that there is broadening client activity, and that MS has made investments across the franchise that have driven share gains, such as in equity derivatives. 2) A strong ability to continue to bring in robust flows through the workplace (stock plan) channel, with slightly more than $50\%$ of 2Q26 net new assets in the quarter from workplace, and management highlighting that $70\%$ of the largest 100 unicorns are in their workplace channel. 3) We see structural upside to WM margins, given a portion of the net new assets the company is bringing in from the workplace channel will convert to fee-based assets, which have higher margins than regular fee-based assets, given a lower advisor payout, and thus we model 130bps of 2025-28E core GWM pre-tax margin expansion. 4) While the company sees a variety of organic

## NEUTRAL

Richard Ramsden
+1(212)357-9981 | richard.ramsden@gs.com
GS & Co. LLC

James Yaro
+1(212)902-1913 | james.e.yaro@gs.com
GS & Co. LLC

Divyam Harlalka
+1(332)245-7818 | divyam.harlalka@gs.com
GS India SPL

Key Data

Market cap: \$357.9bn  
3m ADTV: \$1.2bn  
United States  
Americas Banks and Advisors  
M&A Rank: 3

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue ($ mn) New</td><td>70,645.0</td><td>81,966.3</td><td>86,222.0</td><td>91,758.3</td></tr><tr><td>Revenue ($ mn) Old</td><td>70,645.0</td><td>81,028.9</td><td>85,810.9</td><td>91,110.1</td></tr><tr><td>EPS ($) New</td><td>10.21</td><td>13.35</td><td>14.19</td><td>15.69</td></tr><tr><td>EPS ($) Old</td><td>10.21</td><td>13.01</td><td>14.11</td><td>15.66</td></tr><tr><td>P/E (X)</td><td>13.9</td><td>17.1</td><td>16.0</td><td>14.5</td></tr><tr><td>P/B (X)</td><td>2.8</td><td>3.3</td><td>3.1</td><td>3.0</td></tr><tr><td>ROE (%)</td><td>16.7</td><td>20.2</td><td>20.2</td><td>21.5</td></tr><tr><td>TCE ratio (%)</td><td>6.4</td><td>6.0</td><td>6.0</td><td>5.9</td></tr><tr><td>Dividend yield (%)</td><td>2.7</td><td>1.9</td><td>2.2</td><td>2.5</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS ($)</td><td>3.46</td><td>3.36</td><td>3.09</td><td>3.84</td></tr></table>

GS Factor Profile

![](images/5c34453e2d039c8973eb29e2b871711f179e961102ecb1cdc4e9008c0e207cb1.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## MS & Co. (MS)

Rating since Sep 10, 2024

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>13.9</td><td>17.1</td><td>16.0</td><td>14.5</td></tr><tr><td>P/B (X)</td><td>2.8</td><td>3.3</td><td>3.1</td><td>3.0</td></tr><tr><td>P/Tangible book (X)</td><td>3.6</td><td>4.2</td><td>4.0</td><td>3.8</td></tr><tr><td>ROA (%)</td><td>1.2</td><td>1.4</td><td>1.3</td><td>1.4</td></tr><tr><td>ROE (%)</td><td>16.7</td><td>20.2</td><td>20.2</td><td>21.5</td></tr><tr><td>ROTE (%)</td><td>21.8</td><td>25.9</td><td>25.8</td><td>27.3</td></tr><tr><td>Tier 1 capital ratio (%)</td><td>18.3</td><td>17.6</td><td>-</td><td>-</td></tr><tr><td>Efficiency ratio (%)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Provisions/avg. tot. loans (%)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net charge-off rate (%)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Reserves/tot. nonperf loans (%)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Reserves/tot. EOP loans (%)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Avg loans/avg earn. assets (%)</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr></table>

Income Statement (\$ mn)

<table><tr><td colspan="5">Income Statement (SMM)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net interest income</td><td>10,046.0</td><td>11,537.8</td><td>11,744.7</td><td>11,719.1</td></tr><tr><td>Non-interest income</td><td>60,250.0</td><td>70,004.5</td><td>73,999.0</td><td>79,523.1</td></tr><tr><td>Gain on sale of securities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other operating income</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total revenue</td><td>70,645.0</td><td>81,966.3</td><td>86,222.0</td><td>91,758.3</td></tr><tr><td>Compensation &amp; benefits exp.</td><td>(29,216.0)</td><td>(32,807.4)</td><td>(34,490.4)</td><td>(36,773.1)</td></tr><tr><td>Total operating expenses</td><td>(48,342.0)</td><td>(53,762.0)</td><td>(56,375.3)</td><td>(59,681.8)</td></tr><tr><td>Other costs</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total provision expense</td><td>(349.0)</td><td>(424.0)</td><td>(478.3)</td><td>(516.1)</td></tr><tr><td>Net operating profit</td><td>21,954.0</td><td>27,780.3</td><td>29,368.4</td><td>31,560.4</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Exceptional income/(expense)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Pre-tax profit</td><td>21,954.0</td><td>27,780.3</td><td>29,368.4</td><td>31,560.4</td></tr><tr><td>Provision for taxes</td><td>(4,929.0)</td><td>(6,087.8)</td><td>(6,983.5)</td><td>(7,653.4)</td></tr><tr><td>After tax profit</td><td>17,025.0</td><td>21,692.5</td><td>22,384.9</td><td>23,907.0</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Post-tax other</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Minorities</td><td>(164.0)</td><td>(223.0)</td><td>(160.0)</td><td>(160.0)</td></tr><tr><td>Preferred dividends</td><td>(612.0)</td><td>(618.0)</td><td>(677.0)</td><td>(736.0)</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>16,249.0</td><td>20,851.5</td><td>21,547.9</td><td>23,011.0</td></tr></table>

Growth & Margins (%)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net int. inc. growth</td><td>16.7</td><td>14.8</td><td>1.8</td><td>(0.2)</td></tr><tr><td>Non-int. inc. growth</td><td>13.9</td><td>16.2</td><td>5.7</td><td>7.5</td></tr><tr><td>Expense growth</td><td>10.1</td><td>11.2</td><td>4.9</td><td>5.9</td></tr><tr><td>Net inc. growth</td><td>26.9</td><td>28.3</td><td>3.3</td><td>6.8</td></tr><tr><td>Net interest margin</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax margin</td><td>31.1</td><td>33.9</td><td>34.1</td><td>34.4</td></tr><tr><td>Loan growth</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Deposit growth</td><td>10.5</td><td>9.5</td><td>5.8</td><td>3.9</td></tr></table>

Price Performance  
![](images/a18a3148f0d95156056927ab9a9fe5ce9bf22ed904beb398edf976430387839c.jpg)  
Source: FactSet. Price as of 14 Jul 2026 close.

<table><tr><td>EPS (basic, pre-except) ($)</td><td>10.32</td><td>13.50</td><td>14.43</td><td>16.08</td></tr><tr><td>EPS (diluted, post-except) ($)</td><td>10.21</td><td>13.35</td><td>14.19</td><td>15.69</td></tr><tr><td>DPS ($)</td><td>3.85</td><td>4.30</td><td>4.94</td><td>5.64</td></tr><tr><td>Dividend payout ratio (%)</td><td>37.3</td><td>31.9</td><td>34.2</td><td>35.1</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>1,574.0</td><td>1,544.7</td><td>1,493.2</td><td>1,430.6</td></tr><tr><td>Wtd avg shares out. (diluted) (mn)</td><td>1,592.3</td><td>1,561.6</td><td>1,518.3</td><td>1,466.2</td></tr></table>

Balance Sheet (\$ mn)

<table><tr><td colspan="5">Balance Sheet ($ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>4,462.0</td><td>6,012.0</td><td>6,012.0</td><td>6,012.0</td></tr><tr><td>Total personal lending</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Domestic commercial lending</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Gross loans to customers</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Net customer loans &amp; advances</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Debt securities</td><td>2,343,315.0</td><td>2,652,404.5</td><td>2,789,376.6</td><td>2,937,021.0</td></tr><tr><td>Other interest earning assets</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Interest earning assets</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Other assets</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total assets</td><td>1,420,270.0</td><td>1,610,250.5</td><td>1,643,029.7</td><td>1,677,887.7</td></tr><tr><td>Non-interest bearing deposits</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Customer deposits</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>ST borrow. &amp; oth int. liabs</td><td>1,837,282.1</td><td>1,472,645.1</td><td>984,617.1</td><td>496,589.1</td></tr><tr><td>Subordinated liabs. (LT debt)</td><td>341,681.0</td><td>361,432.2</td><td>365,413.5</td><td>380,837.9</td></tr><tr><td>Interest bearing liabilities</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>Total liabilities</td><td>1,307,618.0</td><td>1,491,379.0</td><td>1,521,714.7</td><td>1,555,903.3</td></tr><tr><td>Total common equity</td><td>100,862.0</td><td>105,925.5</td><td>107,369.0</td><td>107,038.5</td></tr><tr><td>Minority interests</td><td>1,020.0</td><td>1,098.0</td><td>1,098.0</td><td>1,098.0</td></tr><tr><td>Total shareholders&#x27; equity</td><td>111,632.0</td><td>117,773.5</td><td>120,217.0</td><td>120,886.5</td></tr><tr><td>Total liabilities &amp; equity</td><td>1,420,270.0</td><td>1,610,250.5</td><td>1,643,029.7</td><td>1,677,887.7</td></tr></table>

Source: Company data, GS estimates.

investment opportunities across both trading businesses and wealth, the company continues to evaluate inorganic growth opportunities, although the bar for acquisitions is high. 5) MS continues to have considerable levels of excess capital (we estimate 250bps of CET1 or \$15bn) $^{2}$ which places them in strong position to benefit from elevated levels of client demand for financing, across a range of businesses, in which risk adjusted returns are currently very attractive.

Factoring quarterly results and management commentary, we increase our 2026E/27E EPS estimates by 3%/1%. We increase our target P/E multiple by 0.5x to 17.0x, resulting in our price target increasing to \$241 (from \$233 previously).

■ Strong wealth management trends: MS delivered 8.1%/5.6% annualized net new assets/fee based flows, vs. GSe of 7.8%/6.5%, with net new assets/fee-based flows above the high end/at the lower end of MS' long term guidance of 5-7%. Wealth NII came in 3% above consensus, as wealth deposit balances were 3% above the Street, while avg. wealth deposit costs of 2.54% were 1bp higher QoQ, and 1bps above GSe. The company noted that slightly more than 50% of their 2Q26 NNA was from the workplace channel. It also guided to modest sequential 3Q26 NII growth QoQ. Finally, the company reiterated its 30% pre-tax margin, and did not commit to increasing this, noting that it continues to invest in the business. Altogether, our 2028E GWM revenue increases 1%, and our 2026E/27E/28E GWM PT margins changes by \~+5bps/-5bps/-5bps.

■ Capital markets: Trading revenue was 19% above the Street on 36% better Equities, partially offset by 3% lower FICC (both vs. Street). Investment banking came in 11% above the Street, driven by beats across ECM/DCM/Advisory (+22%/8%/3%). MS noted IBanking pipelines remain robust, with healthy, broad-based client dialogues, with large strategies prosecuting their strategic objectives, and the need for solutions and capital. Further, pipelines are broadening globally, and the company remains constructive on both IPOs and sponsor activity building. Overall, stronger capital market results and management commentary lead us to increase our 2026/27E/28E capital markets revenue forecasts by 3%/2%/2%.

\- Expenses and margins: Core efficiency of 65.1% was \~295bps better than Street expectations. Specific to wealth, the core PT margin (ex. DCP) of 30.5% was \~35bps above GSe/consensus. Overall, we reduce our 2026E/27E/28E efficiency ratio by \~60bps/20bps/15bps.

Capital position: MS' binding Standardized CET1 ratio decreased 30bps QoQ to 14.8%, on \$3.1bn higher CET1 (despite \$1.5bn of buybacks, vs. \$1.8bn for consensus), more than offset by \$30.3bn higher RWA, with 6% higher trading VaR QoQ. This suggests 250bps of excess capital vs. MS's estimated target of 12.3%. $^{3}$ The company highlighted that it continues to prioritize organic investment first, with capital demands in fixed income, equities, as well as in wealth. That being said, the company continues to evaluate inorganic opportunities, and they could bolt on something.

New vs old: Reflecting earnings results and management commentary, we increase our 2026E/27E EPS estimates by 3%/1%, and increase our 2027E P/E target multiple by 0.5x to 17.0x. This results in our 12-month price target increasing by 3% to \$241 (vs. \$233 previously).

Key risks: Downside risks include higher capital requirements, market share losses or more material normalization in trading and investment banking, the impact of lower market levels in WM and IM, and the potential for a slowdown in the robust inflows into wealth management that could impact investor perceptions of the growth potential. Upside risks include higher wealth management margin, stronger equity markets, better capital markets performance.

## Disclosure Appendix

## Reg AC

I, Richard Ramsden, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Richard Ramsden GS & Co. LLC, James Yaro GS & Co. LLC, Divyam Harlalka GS India SPL, Matthew Weng GS & Co. LLC, Lokesh Kumar Sangewar GS India SPL.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by 

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
