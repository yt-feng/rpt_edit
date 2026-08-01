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
APAC Food & Beverages

# Eastroc Beverage Group Co Ltd

Rating

Market-Perform

Price Target

605499.CH

9980.HK

133.00 RMB (142.00 OLD)

131.00 HKD (138.00 OLD)

![](images/5a6a891f064b5ef24501eed82a3a67bd1656ecf98c622ca90b41745effd507f9.jpg)

Price Target Downgrade

![](images/de4e80a648669630f8edf2240e257a7cb7ed7f2c4f8dfc1fc9fd281e68d83b22.jpg)

Euan McLeish
+81 3 5962 9611
euan.mcleish@bernsteinsg.com

![](images/a1903557dc40048fc162ebb58546767c512b08f85c52a0e28da5e9ff9e8cd05f.jpg)

Hao Wang, CFA
+852 2123 2627
hao.wang@bernsteinsg.com

Mufei Gao
+81 3 6777 6995
mufei.gao@bernsteinsg.com

Makoto Morozumi
+81 3 6777 6972
makoto.morozumi@bernsteinsg.com

## Eastroc Q2: Out of Energy

Eastroc reported a weak Q2 last night with 11% revenue growth clocking the slowest rate since IPO and missing expectations by HSD. The miss narrowed slightly at OP (+14% YoY) with better than expected COGS enhancing margin by \~400bps, and NP came in +15%, c. 5% below us and consensus. Energy drink top line growth was the biggest issue, dropping from a pretty consistent DD run rate to only 1% in Q2 and, concerningly, management flagged increasing competition as a major issue. To mitigate the weak result, Eastroc announced a 10% H-share buy back (despite just listing in HK a few months ago and a very thin free float), raised their interim dividend to 76% from 55%, and set a minimum 80% payout through 2028.

Beyond the Energy segment (69% of Q2 revenues), Electrolyte growth also moderated slightly from 13% in Q1 to 11% in Q2, but the Other segment was still growing rapidly at 97% (from 120% in Q1) driven by RTD Tea offerings which grew 2x in H1, albeit off a low base. In Q3, we expect their trajectory of Energy Drink revenues to bounce back, but for the margin upside to be partially offset by World Cup related marketing spend.

We expect management's strategy of becoming a “soft drinks platform company”, reiterated on today's call, to exert a material medium term drag on margins given that non-energy Gross Margins are 16-35% points lower outside the Energy segment in FY25 and these business lines remain sub-scale. On the plus side, we were glad to hear management's focus on innovating behind low/no sugar health and wellness trends.

## Investment Implications

We maintain Market-Perform and cut Price Target to RMB133/HK\$131 per share reflecting Q2 results and 4/6/6% reduction in our FY26-28 EPS estimates, while maintaining our multiple target at 15.7x NTM P/E for A-share and 13.3x for H-share (model).

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>605499.CH (RMB)</td><td>8.49</td><td>7.06</td><td>7.85</td></tr><tr><td>OLD</td><td>--</td><td>7.37</td><td>8.34</td></tr><tr><td>9980.HK (RMB)</td><td>8.49</td><td>7.06</td><td>7.85</td></tr><tr><td>OLD</td><td>--</td><td>7.37</td><td>8.34</td></tr></table>

<table><tr><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>Net Earnings (M)</td><td>4,415</td><td>5,128</td><td>5,672</td><td>13.3%</td></tr><tr><td>Net Debt/EBITDA (x)</td><td>(1.27)</td><td>(2.45)</td><td>(2.56)</td><td>42.3%</td></tr></table>

<table><tr><td>Close Date</td><td>30 Jul 2026</td></tr><tr><td>605499.CH Close Price (RMB)</td><td>138.20</td></tr><tr><td>Price Target (RMB)</td><td>133.00</td></tr><tr><td>Upside/(Downside)</td><td>(4)%</td></tr><tr><td>52-Week Range</td><td>243.83/108.80</td></tr><tr><td>ASIAX</td><td>1,808.17</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>2.8%</td></tr><tr><td>Market Cap (RMB) (M)</td><td>99,636</td></tr><tr><td>EV (RMB) (M)</td><td>84,988</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>(32.8)</td><td>12.0</td><td>(28.2)</td><td>(36.1)</td></tr><tr><td>ASIAX (%)</td><td>10.6</td><td>(9.0)</td><td>3.5</td><td>24.1</td></tr><tr><td>Relative (%)</td><td>(43.4)</td><td>21.0</td><td>(31.7)</td><td>(60.2)</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

Price Performance, 1YR  
![](images/118a291115a089b344fc5bbb670dab35ac1bf68c193b17a14899275e1f3953d6.jpg)

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Adjusted P/E (x)</td><td>16.3</td><td>19.6</td><td>17.6</td></tr><tr><td>Div Yield (%)</td><td>3.8</td><td>4.1</td><td>4.5</td></tr><tr><td>EV/EBIT (x)</td><td>16.6</td><td>14.3</td><td>12.8</td></tr><tr><td>EV/EBITDA (x)</td><td>15.2</td><td>13.1</td><td>11.6</td></tr><tr><td>PEG Adjusted (x)</td><td>0.5</td><td>(1.2)</td><td>1.6</td></tr><tr><td>PEG Reported (x)</td><td>0.5</td><td>(1.2)</td><td>1.6</td></tr><tr><td>Reported P/E (x)</td><td>16.3</td><td>19.6</td><td>17.6</td></tr></table>

## DETAILS

EXHIBIT 1: Eastroc 2Q26 Results Summary

<table><tr><td>(in RMB million unless otherwise stated)</td><td>FY25Q2</td><td>FY26Q2</td><td>YoY % / bps</td><td>Bernstein</td><td>Delta</td></tr><tr><td>Gross Revenue</td><td>5,889</td><td>6,555</td><td>11.3%</td><td>7,339</td><td>-10.7%</td></tr><tr><td>COGS</td><td>(3,197)</td><td>(3,298)</td><td>3.1%</td><td>(3,962)</td><td>-16.8%</td></tr><tr><td>Gross Profit</td><td>2,691</td><td>3,257</td><td>21.0%</td><td>3,377</td><td>-3.6%</td></tr><tr><td>% margin</td><td>45.7%</td><td>49.7%</td><td>399</td><td>46.0%</td><td>367</td></tr><tr><td>Selling Expenses</td><td>(873)</td><td>(1,126)</td><td>29.0%</td><td>(1,124)</td><td></td></tr><tr><td>as % of Revenue</td><td>-14.8%</td><td>-17.2%</td><td>(236)</td><td>-15.3%</td><td></td></tr><tr><td>Tax &amp; Others</td><td>(63)</td><td>(73)</td><td>16.6%</td><td>(78)</td><td></td></tr><tr><td>Admin &amp; R&amp;D Expenses</td><td>(154)</td><td>(226)</td><td>46.1%</td><td>(185)</td><td>21.8%</td></tr><tr><td>Operating Profit</td><td>1,602</td><td>1,832</td><td>14.4%</td><td>1,989</td><td>-7.9%</td></tr><tr><td>% margin</td><td>27.2%</td><td>28.0%</td><td>75</td><td>27.1%</td><td>84</td></tr><tr><td>Other Income</td><td>46</td><td>(83)</td><td>-280.8%</td><td>46</td><td>-280.8%</td></tr><tr><td>Net Finance Income</td><td>36</td><td>21</td><td></td><td>36</td><td></td></tr><tr><td>Others</td><td>85</td><td>285</td><td>236.4%</td><td>85</td><td>236.4%</td></tr><tr><td>Profit before Tax</td><td>1,768</td><td>2,055</td><td>16.2%</td><td>2,156</td><td>-4.7%</td></tr><tr><td>Income Tax Expense</td><td>(374)</td><td>(444)</td><td>18.9%</td><td>(456)</td><td>-2.5%</td></tr><tr><td>% effective tax rate</td><td>21.1%</td><td>21.6%</td><td>49</td><td>21.1%</td><td>49</td></tr><tr><td>Profit after Tax</td><td>1,395</td><td>1,610</td><td>15.5%</td><td>1,700</td><td>-5.3%</td></tr><tr><td>Net Profit</td><td>1,395</td><td>1,609</td><td>15.4%</td><td>1,701</td><td>-5.4%</td></tr><tr><td>% margin</td><td>23.7%</td><td>24.6%</td><td>87</td><td>23.2%</td><td>138</td></tr><tr><td>Earnings per Share (RMB)</td><td>2.68</td><td>2.19</td><td>-18.3%</td><td>2.32</td><td>-5.7%</td></tr></table>

Source: S&P Capital IQ, company reports, Bernstein analysis and estimates  
EXHIBIT 2: We have cut our estimates by 5% in FY26 and 7% in FY27-28

Eastroc Revenue & OP Forecasts (RMBbn)  
![](images/ca3564cf2d89fe88eafaa4b59513dfc51a4292b2707bb25daf9dc1e07d98a559.jpg)  
Source: Bernstein analysis and estimates  
EXHIBIT 3: The revenue estimate cuts are across both energy and electrolyte drinks  
Eastroc Revenue by Segment (RMBbn)

![](images/1f0d908c6e0cd632a9ab88faddcab97c7a7de709d4a0fd057de8af5a1f09e78e.jpg)  
Source: Bernstein analysis and estimates

EXHIBIT 4: Eastroc 2Q26 Segmental Summary

<table><tr><td>(in RMB million unless otherwise stated)</td><td>FY25Q2</td><td>FY26Q2</td><td>YoY % / bps</td><td>Bernstein</td><td>Delta</td></tr><tr><td>Total Revenue by Segments</td><td>5,889</td><td>6,555</td><td>11.3%</td><td>7,339</td><td>-10.7%</td></tr><tr><td>Energy Drinks</td><td>4,460</td><td>4,525</td><td>1.4%</td><td>5,129</td><td>-11.8%</td></tr><tr><td>Electrolyte Drinks</td><td>923</td><td>1,026</td><td>11.2%</td><td>1,200</td><td>-14.4%</td></tr><tr><td>Other Drinks</td><td>503</td><td>991</td><td>97.3%</td><td>1,005</td><td>-1.3%</td></tr><tr><td>Other Revenue</td><td>3</td><td>12</td><td>285.2%</td><td>5</td><td>140.7%</td></tr><tr><td>Drinks Revenue by Channels</td><td>5,885</td><td>6,543</td><td>11.2%</td><td></td><td></td></tr><tr><td>Distribution</td><td>5,067</td><td>5,405</td><td>6.7%</td><td></td><td></td></tr><tr><td>KA</td><td>632</td><td>793</td><td>25.5%</td><td></td><td></td></tr><tr><td>Online</td><td>186</td><td>344</td><td>84.3%</td><td></td><td></td></tr><tr><td>Other Channels</td><td>0</td><td>1</td><td>193.6%</td><td></td><td></td></tr><tr><td>Drinks Revenue by Regions</td><td>5,885</td><td>6,543</td><td>11.2%</td><td></td><td></td></tr><tr><td>South</td><td>1,720</td><td>1,769</td><td>2.8%</td><td></td><td></td></tr><tr><td>Central</td><td>1,201</td><td>1,478</td><td>23.0%</td><td></td><td></td></tr><tr><td>East</td><td>1,053</td><td>1,054</td><td>0.1%</td><td></td><td></td></tr><tr><td>West</td><td>940</td><td>1,126</td><td>19.8%</td><td></td><td></td></tr><tr><td>North</td><td>753</td><td>821</td><td>9.0%</td><td></td><td></td></tr><tr><td>Others</td><td>217</td><td>294</td><td>35.8%</td><td></td><td></td></tr></table>

Source: S&P Capital IQ, company reports, Bernstein analysis and estimates

EXHIBIT 5: Eastroc topline growth dropped to 11% in Q2
Eastroc Total Revenue Growth YoY%  
![](images/c5804e1823871b7f02495ec160b7c6e452e01e9527cd24af55e869ea71c4771b.jpg)  
Source: company reports, Bernstein analysis

EXHIBIT 6: Energy Drinks revenue share narrowed significantly this quarter and Electrolyte Drinks & Other Drinks (Tea) continued to widen  
Eastroc Revenue Split by Segments  
![](images/673b7247a174b5e4c1feaaeb62f452b54aa074e2386245a6c43e9c3503ff1a0f.jpg)  
Source: company reports, Bernstein analysis

EXHIBIT 7: Energy Drinks revenue growth dropped significantly to 1% this quarter

Eastroc Energy Drinks Revenue Growth YoY%

![](images/22a787c198e6459773181193aca2910e41978f3e6f52251b05c035466792aabf.jpg)  
Source: company reports, Bernstein analysis  
EXHIBIT 8: Electrolyte Drinks revenue growth also slowed down sequentially

Eastroc Electrolyte Drinks Revenue Growth YoY%  
![](images/b4ef72ac8e0978500c188e1fa88fc566d7a35667fb12d5b206c8c10d5d4f886a.jpg)  
Source: company reports, Bernstein analysis  
EXHIBIT 9: Growth slowed materially in most regions with the exception of Central which saw sequential acceleration  
Eastroc Revenue Growth YoY by Region

![](images/f1498bb860d3d77d825a95bae64f836adc25eb3be13559265e44e39d4c9b5a8b.jpg)  
Source: company reports, Bernstein analysis  
EXHIBIT 10: The growth of Eastroc's distributor team continued to moderate in Q2  
Eastroc Distributors by Region

![](images/942b260c8240466a65616cec67927e100b3e7d971d97c42548758228c54cca1b.jpg)  
Source: company reports, Bernstein analysis

EXHIBIT 11: Our Eastroc revenue estimates are 2% below consensus for the next three years

Eastroc Beverage Revenue (RMBbn)  
![](images/bde305de4970f4c18c1389f95c1d7de75a1f4e9e75aed69e6d641e54ef108504.jpg)  
Source: S&P Capital IQ's Visible Alpha, Bernstein analysis and estimates  
EXHIBIT 12: And 4-6% below in EPS estimates

Eastroc Beverage EPS (RMB)  
![](images/e6f68f193a1ffc483e53d80e21951c8924f42ab22342cd43363c556f0d048019.jpg)  
Source: S&P Capital IQ's Visible Alpha, Bernstein analysis and estimates

EXHIBIT 13: Eastroc-A is trading at 1.6x stdev below historical average multiple  
Eastroc-A Consensus NTM P/E  
![](images/010e11480a59e3b39392bba30e1cdad114776723cc28f685f08227330b54fb8e.jpg)  
Source: Bloomberg, Bernstein analysis

EXHIBIT 14: Its premium vs benchmark index is now 1.7x stdev below historical level  
![](images/c1160e7ba8d45b9acad507b4e4768401c65b8559c5dfb6edc0a190c9e50c2655.jpg)  
Source: Bloomberg, Bernstein analysis

EXHIBIT 15: Eastroc-A EPS consensus has been coming down since May  
![](images/ec7255e3f458986a7cb95ce3a994747f6d86e76113cd60d53129e10a787b5274.jpg)  
Source: Bloomberg, Bernstein analysis

EXHIBIT 16: RMB:HKD  
![](images/fbb5624c1815262855b48df3fb8fe6437256581a09bc5c7b8f4ec4c2659dd7a9.jpg)  
Source: Bloomberg, Bernstein analysis

EXHIBIT 17: Eastroc H-Share price is now at 23% discount vs. its A-Share price  
Eastroc H-Share Price Discounts vs. A-Share since IPO  
![](images/6261e8303fa2778255158346219a0db8aa96c47d2dc3c941f30afc1e8b9731e4.jpg)  
Source: Bloomberg, Bernstein analysis

## APPENDIX - FINANCIAL FORECASTS

EXHIBIT 18: Eastroc Beverage Income Statement

<table><tr><td colspan="9">Eastroc Beverage Income Statement(in RMB million unless otherwise stated)</td></tr><tr><td></td><td>2023</td><td>2024</td><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2029e</td><td>2030e</td></tr><tr><td>Gross Revenue</td><td>11,263</td><td>15,839</td><td>20,875</td><td>24,364</td><td>28,236</td><td>32,199</td><td>35,241</td><td>37,347</td></tr><tr><td>COGS</td><td>(6,412)</td><td>(8,742)</td><td>(11,501)</td><td>(12,878)</td><td>(15,135)</td><td>(16,853)</td><td>(18,458)</td><td>(19,666)</td></tr><tr><td>Gross Profit</td><td>4,851</td><td>7,097</td><td>9,374</td><td>11,486</td><td>13,102</td><td>15,345</td><td>16,783</td><td>17,681</td></tr><tr><td>Tax &amp; Others</td><td>(121)</td><td>(160)</td><td>(219)</td><td>(257)</td><td>(282)</td><td>(322)</td><td>(352)</td><td>(373)</td></tr><tr><td>SG&amp;A</td><td>(2,379)</td><td>(3,169)</td><td>(4,048)</td><td>(5,274)</td><td>(6,175)</td><td>(7,132)</td><td>(7,812)</td><td>(8,280)</td></tr><tr><td>EBIT</td><td>2,351</td><td>3,768</td><td>5,107</td><td>5,954</td><td>6,644</td><td>7,891</td><td>8,618</td><td>9,028</td></tr><tr><td>D&amp;A</td><td>270</td><td>359</td><td>496</td><td>551</td><td>676</td><td>786</td><td>614</td><td>776</td></tr><tr><td>EBITDA</td><td>2,621</td><td>4,127</td><td>5,603</td><td>6,505</td><td>7,320</td><td>8,677</td><td>9,233</td><td>9,804</td></tr><tr><td>Others</td><td>228</td><td>339</td><td>478</td><td>538</td><td>538</td><td>538</td><td>538</td><td>538</td></tr><tr><td>Profit Before Tax</td><td>2,579</td><td>4,107</td><td>5,584</td><td>6,492</td><td>7,182</td><td>8,429</td><td>9,156</td><td>9,566</td></tr><tr><td>Income Taxes</td><td>(539)</td><td>(781)</td><td>(1,170)</td><td>(1,365)</td><td>(1,510)</td><td>(1,857)</td><td>(2,109)</td><td>(2,299)</td></tr><tr><td>Profit after tax</td><td>2,040</td><td>3,326</td><td>4,414</td><td>5,127</td><td>5,671</td><td>6,572</td><td>7,048</td><td>7,267</td></tr><tr><td>Attributable to:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Non-controlling interests</td><td>-</td><td>(0)</td><td>(1)</td><td>(1)</td><td>(1)</td><td>(1)</td><td>(1)</td><td>(1)</td></tr><tr><td>Shareholders of the company</td><td>2,040</td><td>3,327</td><td>4,415</td><td>5,128</td><td>5,672</td><td>6,573</td><td>7,049</td><td>7,268</td></tr><tr><td>Basic EPS (RMB)</td><td>5.10</td><td>6.40</td><td>8.49</td><td>7.06</td><td>7.85</td><td>9.10</td><td>9.76</td><td>10.06</td></tr><tr><td>Total shares outstanding (mm)</td><td>400</td><td>520</td><td>520</td><td>726</td><td>723</td><td>723</td><td>723</td><td>723</td></tr><tr><td>Key Ratios</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue growth %</td><td>32.4%</td><td>40.6%</td><td>31.8%</td><td>16.7%</td><td>15.9%</td><td>14.0%</td><td>9.5%</td><td>6.0%</td></tr><tr><td>EBIT growth %</td><td>33.7%</td><td>60.2%</td><td>35.5%</td><td>16.6%</td><td>11.6%</td><td>18.8%</td><td>9.2%</td><td>4.8%</td></tr><tr><td>Net profit growth %</td><td>41.6%</td><td>63.1%</td><td>32.7%</td><td>16.1%</td><td>10.6%</td><td>15.9%</td><td>7.2%</td><td>3.1%</td></tr><tr><td>Gross profit as % of Revenue</td><td>43.1%</td><td>44.8%</td><td>44.9%</td><td>47.1%</td><td>46.4%</td><td>47.7%</td><td>47.6%</td><td>47.3%</td></tr><tr><td>EBIT as % of Rev

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
