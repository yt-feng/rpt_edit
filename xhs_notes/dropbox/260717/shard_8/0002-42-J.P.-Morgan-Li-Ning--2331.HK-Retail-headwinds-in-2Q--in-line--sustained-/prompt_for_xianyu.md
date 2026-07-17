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

## Li Ning (2331)

## Retail headwinds in 2Q, in-line; sustained investments for long-term growth; maintain OW

Li Ning reported 2Q operational updates with retail sell-through facing headwinds (down LSD if excl. kids and flat incl. kids), in-line with our expectations (see report). This was mainly due to weaker-than-expected traffic amid a lukewarm retail environment and unfavorable weather. Inventory level remained robust at c.4 months (vs. c.5 months as of 1Q) with a healthy inventory age profile, despite deepened discounts (offline/online by MSD/LSD; overall at mid-30s off). Despite headwinds lingering in early July, management maintained its full year guidance (sales +HSD, HSD NPM), given multiple catalysts to boost the retail trend in 2H (such as the launch of the new cushioned running shoe collection, the debut of the Loong store and the Asian Games-related campaigns) and initiatives to uphold margins (such as supply-chain optimization, closing underperforming stores, efficiency enhancement, etc.). Meanwhile, management reaffirmed its commitment to long-term strategic investments, including R&D (such as the newly launched BOOM Arc technology) and brand equity (such as the partnership with Curry and sponsorship of elite athletes and top-tier sports events). This strengthened our confidence in Li Ning's long-term recovery. We maintain our 2026-28 earnings estimates. Our DCF-based Dec-26 PT of HK\$23 implies a 12-month forward P/E of 17x. Maintain OW.

\- Progress of the Curry partnership. Regarding products, a dedicated team has been set up for the Curry brand and it has kicked off product planning. The products will focus on basketball in 2H and a broader range of products (such as lifestyle and golf) will be rolled-out in 2027. The commemorative T-shirt launched in July was welcomed by consumers. Regarding expenses, related expenses include signing fees, co-branding fees and operational and marketing expenses. As a long term partnership, the related expenses will be amortized during the partnership. The financial impact on 2026 shall be limited, per management.

\- Swing factors on margin in 2H. Despite challenges on margin, management has rolled out multiple initiatives to maintain a solid margin profile. The challenges include: 1) pressures on discount levels amid the lukewarm retail environment which would weigh on GPM; and 2) increase in A&P expenses, given the Curry partnership, Asian Games-related campaigns, and sponsorship of sports events (such as the Chengdu Marathon). The initiatives include: 1) supply chain optimization, such as pre-locked raw material prices and product design optimization to offset deeper discounts; 2) strict control on non-essential expenses, such as closure of

## Overweight

2331.HK, 2331 HK
Price (15 Jul 26): HK\$15.12

Price Target (Dec-26): HK\$23.00

## China

Consumer

Qian Yao AC
(86-21) 6106 6277
qian.q.yao@JPM.com
SAC Registration Number: S1730521050001

Carson Fan
(86-21) 6106-6294
rong.fan@JPM.com
SAC Registration Number: S1730522070002
JPM Securities (China) Company Limited

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>55</td><td>47</td><td>45</td><td>74</td><td>86</td></tr><tr><td>Growth</td><td>78</td><td>87</td><td>75</td><td>32</td><td>26</td></tr><tr><td>Momentum</td><td>19</td><td>56</td><td>67</td><td>71</td><td>13</td></tr><tr><td>Quality</td><td>43</td><td>46</td><td>35</td><td>22</td><td>16</td></tr><tr><td>Low Vol</td><td>48</td><td>63</td><td>81</td><td>85</td><td>78</td></tr><tr><td>ESGQ</td><td>95</td><td>27</td><td>13</td><td>9</td><td>3</td></tr></table>

10 Jul 2026 Li Ning: Industry softness weighed pressures in 2Q; long-term recovery trend intact; maintain OW

10 Jul 2026 China Sportswear: Takeaways from expert call

22 Jun 2026 China Sportswear: How can brands be successful in China – lessons from Adidas "Urban Errand" viral marketing campaign

2 Jun 2026 Li Ning: Landmark partnership with Curry

27 Apr 2026 China Sportswear: What's moving in the landscape

22 Apr 2026 Li Ning: 1Q26 in line; validated recovery signals; maintain OW

23 Mar 2026 Li Ning: Earlier than expected recovery; upgrade to OW

28 Feb 2026 China Sportswear: Takeaways from expert call

underperforming stores; and 3) efficiency enhancement.

\- 2Q26 in-line. Li Ning's (excl. kids) 2Q26 retail sell-through declined by LSD yoy, while it was flat if incl. kids (kids +low-teens). By channel, e-commerce grew by MSD, and offline declined by LSD (retail down LSD despite outlets delivering positive growth; wholesale down MSD). By category, core categories all faced headwinds (running and lifestyle turned negative; basketball saw widening declines), despite fitness remaining resilient (driven by functional apparels) and outdoor and Glory collections maintaining momentum (representing MSD and LSD of overall retail sell-through, respectively; in-line with the management's expectations). As of 2Q26, Li Ning Adults POS in China amounted to 6,063, net -28 vs. 2025, with retail/wholesale -66/+38. Li Ning Young POS totaled 1,516, net +2 vs. 2025.

Price Performance  
![](images/0562bd5635f70923807f8e15399bd3d74dffa51fcfa4885d34765d78709a7cf3.jpg)

— 2331.HK Price (HK\$) HSCEI (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>-19.0%</td><td>-12.4%</td><td>-28.1%</td><td>-4.8%</td></tr><tr><td>Rel</td><td>-10.8%</td><td>-10.1%</td><td>-21.9%</td><td>3.0%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>2,585</td></tr><tr><td>52-week range (HK$)</td><td>23.42-14.21</td></tr><tr><td>Market cap ($ mn)</td><td>4,986</td></tr><tr><td>Exchange rate</td><td>7.84</td></tr><tr><td>Free float (%)</td><td>85.3%</td></tr><tr><td>3M ADV (mn)</td><td>20.65</td></tr><tr><td>3M ADV ($ mn)</td><td>46.9</td></tr><tr><td>Volatility (90 Day)</td><td>36</td></tr><tr><td>Index</td><td>HSCEI</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>42|6|1</td></tr></table>

Key Metrics (FYE Dec)

<table><tr><td>Rmb in millions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="5">Financial Estimates</td></tr><tr><td>Revenue</td><td>29,598</td><td>31,351</td><td>32,617</td><td>33,933</td></tr><tr><td>Adj. EBITDA</td><td>4,444</td><td>4,310</td><td>4,944</td><td>5,461</td></tr><tr><td>Adj. EBIT</td><td>3,669</td><td>3,537</td><td>3,990</td><td>4,384</td></tr><tr><td>Adj. net income</td><td>2,936</td><td>2,820</td><td>3,129</td><td>3,384</td></tr><tr><td>Adj. EPS</td><td>1.14</td><td>1.09</td><td>1.21</td><td>1.31</td></tr><tr><td>BBG EPS</td><td>1.03</td><td>1.18</td><td>1.32</td><td>1.48</td></tr><tr><td>Cashflow from operations</td><td>4,852</td><td>3,000</td><td>4,130</td><td>4,555</td></tr><tr><td>FCFF</td><td>4,794</td><td>979</td><td>2,049</td><td>2,426</td></tr><tr><td colspan="5">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>3.2%</td><td>5.9%</td><td>4.0%</td><td>4.0%</td></tr><tr><td>Gross margin</td><td>49.0%</td><td>49.1%</td><td>49.3%</td><td>49.6%</td></tr><tr><td>EBITDA margin</td><td>15.0%</td><td>13.7%</td><td>15.2%</td><td>16.1%</td></tr><tr><td>EBIT margin</td><td>12.4%</td><td>11.3%</td><td>12.2%</td><td>12.9%</td></tr><tr><td>Adj. EPS growth</td><td>(2.1%)</td><td>(3.9%)</td><td>11.0%</td><td>8.1%</td></tr><tr><td colspan="5">Ratios</td></tr><tr><td>Adj. tax rate</td><td>29.9%</td><td>29.9%</td><td>29.9%</td><td>29.9%</td></tr><tr><td>Interest cover</td><td>NM</td><td>NM</td><td>NM</td><td>261.1</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROCE</td><td>9.6%</td><td>8.7%</td><td>9.4%</td><td>9.8%</td></tr><tr><td>ROE</td><td>10.9%</td><td>10.0%</td><td>10.5%</td><td>10.8%</td></tr><tr><td colspan="5">Valuation</td></tr><tr><td>FCFF yield</td><td>14.2%</td><td>2.9%</td><td>6.1%</td><td>7.2%</td></tr><tr><td>Dividend yield</td><td>4.3%</td><td>4.2%</td><td>4.6%</td><td>5.0%</td></tr><tr><td>EV/Revenue</td><td>0.4</td><td>0.4</td><td>0.4</td><td>0.4</td></tr><tr><td>EV/EBITDA</td><td>2.9</td><td>3.1</td><td>2.6</td><td>2.2</td></tr><tr><td>Adj. P/E</td><td>11.5</td><td>12.0</td><td>10.8</td><td>10.0</td></tr></table>

## Summary Investment Thesis and Valuation

Li Ning is the second-largest domestic sportswear player in China, with a 9.4% market share in 2025 (source: Euromonitor). We have been looking for two signs of a recovery at Li Ning: 1) a regaining of market share after a loss since 2022 (a 1.3ppt loss, per Euromonitor); and 2) relatively effective cost control. Li Ning has now shown us both signs, and its 1Q results validate our confidence in its recovery. Maintain OW.

Our DCF-based Dec-26 PT of HK\$23 implies a 17x 2027E P/E. We derive our 10.1% WACC by assuming a 4.5% risk-free rate, a 7.0% risk premium, a 12.2% cost of equity and a terminal growth rate of 2.0%.

Performance Drivers  
![](images/d58183d0359f878409fcf94ce6efc9f3c60d4a5fc76d622512e3ac90bd78ac12.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Asia Pac ex JP</td><td>0.11</td><td>0.16</td></tr><tr><td>Region: China</td><td>-0.31</td><td>0.11</td></tr><tr><td colspan="3">Macro:</td></tr><tr><td>JPM GBI-EM Global Div</td><td>0.22</td><td>0.25</td></tr><tr><td>JPM EM Currency(EMCI) Fixing</td><td>0.10</td><td>0.18</td></tr><tr><td>JPM China A-shares Sentiment</td><td>0.08</td><td>0.17</td></tr><tr><td colspan="3">Quant Styles:</td></tr><tr><td>Quality</td><td>-0.23</td><td>-0.16</td></tr><tr><td>Size</td><td>-0.45</td><td>-0.16</td></tr><tr><td>Growth</td><td>-0.25</td><td>-0.12</td></tr></table>

## Investment Thesis, Valuation and Risks

Li Ning Co Ltd (Overweight; Price Target: HK\$23.00)

## Investment Thesis

Li Ning is the second-largest domestic sportswear player in China, with a 9.4% market share in 2025 (source: Euromonitor). We have been looking for two signs of a recovery at Li Ning: 1) a regaining of market share after a loss since 2022 (a 1.3ppt loss, per Euromonitor); and 2) relatively effective cost control. Li Ning has now shown us both signs, and its 1Q results validate our confidence in its recovery. Maintain OW.

## Valuation

Our DCF-based Dec-26 PT of HK\$23 implies a 17x 2027E P/E. We derive our 10.1% WACC by assuming a 4.5% risk-free rate, a 7.0% risk premium, a 12.2% cost of equity and a terminal growth rate of 2.0%.

DCF valuation

<table><tr><td>Rmb in millions</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td><td>2032E</td><td>2033E</td><td>2034E</td></tr><tr><td>Sales</td><td>31,351</td><td>32,617</td><td>33,933</td><td>34,961</td><td>35,662</td><td>36,265</td><td>36,874</td><td>37,489</td><td>38,109</td></tr><tr><td>EBIT</td><td>3,537</td><td>3,990</td><td>4,384</td><td>4,517</td><td>4,608</td><td>4,685</td><td>4,764</td><td>4,844</td><td>4,924</td></tr><tr><td>Investment income from associate</td><td>273</td><td>284</td><td>296</td><td>305</td><td>311</td><td>316</td><td>321</td><td>327</td><td>332</td></tr><tr><td>Tax rate %</td><td>30%</td><td>30%</td><td>30%</td><td>30%</td><td>30%</td><td>30%</td><td>30%</td><td>30%</td><td>30%</td></tr><tr><td>NOPAT</td><td>2,670</td><td>2,995</td><td>3,279</td><td>3,379</td><td>3,447</td><td>3,505</td><td>3,564</td><td>3,623</td><td>3,683</td></tr><tr><td>D&amp;A</td><td>773</td><td>954</td><td>1,121</td><td>1,276</td><td>1,417</td><td>1,544</td><td>1,658</td><td>1,761</td><td>1,854</td></tr><tr><td>W.C. change</td><td>-593</td><td>46</td><td>51</td><td>36</td><td>24</td><td>21</td><td>21</td><td>224</td><td>243</td></tr><tr><td>Capex</td><td>-1,948</td><td>-2,028</td><td>-2,112</td><td>-2,177</td><td>-2,221</td><td>-2,260</td><td>-2,298</td><td>-2,337</td><td>-2,376</td></tr><tr><td>as % of sales</td><td>-6.2%</td><td>-6.2%</td><td>-6.2%</td><td>-6.2%</td><td>-6.2%</td><td>-6.2%</td><td>-6.2%</td><td>-6.2%</td><td>-6.2%</td></tr><tr><td>FCFF</td><td>902</td><td>1,967</td><td>2,339</td><td>2,513</td><td>2,667</td><td>2,811</td><td>2,945</td><td>3,271</td><td>3,404</td></tr><tr><td>NPV of FCFF</td><td>14,958</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PV of terminal value</td><td>19,899</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net debt</td><td>-17,419</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Minority</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Equity value</td><td>52,275</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td># of shares O/S (in millions)</td><td>2,586</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Value per share (Rmb)</td><td>20.2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Value per share (HK$)</td><td>23.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: JPM estimates.

## Risks to Rating and Price Target

Downside risks to our rating and price target include: 1) intensified competition from both international brands and domestic peers; 2) failure to execute strategies such as branding initiatives, new store formats, product innovation, etc.; 3) weaker-than-expected consumer sentiment; and 4) slower-than-expected margin expansion.

Upside catalysts include: (1) a greater-than-expected improvement in fundamentals, including enhancement in product offerings, channel optimization, elevation in brand equity, etc.; (2) better-than-expected consumer sentiment; and (3) earlier-than-expected margin expansion.

Li Ning (2331): Summary of Financials

<table><tr><td>Income Statement</td><td>FY24A</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Revenue</td><td>28,676</td><td>29,598</td><td>31,351</td><td>32,617</td><td>33,933</td></tr><tr><td>COGS</td><td>(14,520)</td><td>(15,110)</td><td>(15,948)</td><td>(16,544)</td><td>(17,113)</td></tr><tr><td>Gross profit</td><td>14,156</td><td>14,489</td><td>15,402</td><td>16,074</td><td>16,820</td></tr><tr><td>SG&amp;A</td><td>(10,627)</td><td>(10,820)</td><td>(11,866)</td><td>(12,084)</td><td>(12,436)</td></tr><tr><td>Adj. EBITDA</td><td>4,687</td><td>4,444</td><td>4,310</td><td>4,944</td><td>5,461</td></tr><tr><td>D&amp;A</td><td>(1,158)</td><td>(775)</td><td>(773)</td><td>(954)</td><td>(1,077)</td></tr><tr><td>Adj. EBIT</td><td>3,529</td><td>3,669</td><td>3,537</td><td>3,990</td><td>4,384</td></tr><tr><td>Net Interest</td><td>175</td><td>33</td><td>57</td><td>28</td><td>(21)</td></tr><tr><td>Adj. PBT</td><td>4,110</td><td>4,189</td><td>4,024</td><td>4,465</td><td>4,828</td></tr><tr><td>Tax</td><td>(1,097)</td><td>(1,253)</td><td>(1,204)</td><td>(1,336)</td><td>(1,445)</td></tr><tr><td>Minority Interest</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Adj. Net Income</td><td>3,013</td><td>2,936</td><td>2,820</td><td>3,129</td><td>3,384</td></tr><tr><td>Reported EPS (Basic)</td><td>1.16</td><td>1.14</td><td>1.09</td><td>1.21</td><td>1.31</td></tr><tr><td>Adj. EPS</td><td>1.16</td><td>1.14</td><td>1.09</td><td>1.21</td><td>1.31</td></tr><tr><td>DPS</td><td>0.58</td><td>0.57</td><td>0.55</td><td>0.61</td><td>0.65</td></tr><tr><td>Payout ratio</td><td>50.0%</td><td>50.0%</td><td>50.0%</td><td>50.0%</td><td>50.0%</td></tr><tr><td>Shares outstanding</td><td>2,598</td><td>2,586</td><td>2,586</td><td>2,586</td><td>2,586</td></tr><tr><td>Balance Sheet</td><td>FY24A</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Cash a

[中间内容因长度限制已省略]

ies discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
