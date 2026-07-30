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
<table><tr><td>Close Date</td><td></td><td></td><td colspan="2">27 Jul 2026</td></tr><tr><td>AI.FP Close Price (EUR)</td><td></td><td></td><td colspan="2">177.18</td></tr><tr><td>Price Target (EUR)</td><td></td><td></td><td colspan="2">202.00</td></tr><tr><td>Upside/(Downside)</td><td></td><td></td><td colspan="2">14%</td></tr><tr><td>52-Week Range</td><td></td><td></td><td colspan="2">182.26/140.78</td></tr><tr><td>EDME</td><td></td><td></td><td colspan="2">--</td></tr><tr><td>FYE</td><td></td><td></td><td colspan="2">Dec</td></tr><tr><td>Div Yield</td><td></td><td></td><td colspan="2">1.9%</td></tr><tr><td>Market Cap (EUR) (M)</td><td></td><td></td><td colspan="2">110,198</td></tr><tr><td>EV (EUR) (M)</td><td></td><td></td><td colspan="2">126,141</td></tr><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>18.5</td><td>(0.1)</td><td>21.1</td><td>10.2</td></tr><tr><td>EDME (%)</td><td></td><td></td><td></td><td></td></tr><tr><td>Relative (%)</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="5">Source: Bloomberg, Bernstein estimates and analysis.</td></tr></table>

European Chemicals
Air Liquide SA

Rating
Outperform

Price Target

AI.FP

202.00 EUR (189.00 OLD)

![](images/9129dc7d264c86db584fb3182b66478f2934a5df0eaf91eded224388d12e9bd4.jpg)

James Hooper
+44 20 7676 6995
james.hooper@bernsteinsg.com

![](images/668158590124553050d8b02cb5b4768cc6c271de196432c37dac295d22a2434f.jpg)

Sebastien Afoy
+44 207 762 1032
sebastien.afoy@bernsteinsg.com

Specialist Sales

![](images/5b61c9690199f2c92eb6620757458edcf0b123fc98a4a1c3f301831234cacc49.jpg)

James Brady
+44 20 7762 5272
james.brady@bernsteinsg.com

## Air Liquide 1H26 - Speed bump, but remain Outperform

We identified the potential for Air Liquide's 1H26 results to be a speed bump, and the market has taken issue with a tricky print but limited impact on longer-term fundamentals, in our view (Quick Take: Air Liquide 1H26 - Complicated, but not thesis-changing). After perhaps a slight expectations reset, we believe the road gets easier from here. The backlog remains at record levels, we remain optimistic on further growth acceleration, and the 5 October CMD remains a catalyst. We remain Outperform, and see 1H26 weakness as an entry point.

We actually raise our comparable growth forecasts for 2H26 by 40 bps, upgrading expectations in Electronics and Industrial Merchant. Although we maintain our Large Industries conservatism, we follow management guidance of sustainable 8-9% growth in Electronics and forecast a sequential 50bps improvement in Industrial Merchant based on easing helium supply constraints and stable qoq pricing. Overall, we forecast FY26 comparable growth of +3.2% in line with various consensus sources (FY26 estimates of +3.0% for Vara, and +3.4% for VA). This implies 2H growth is sequentially 90bps above 1H, but only +20bps vs. 2Q, and we believe this is consistent with the ever conservative Air Liquide definition of “slightly higher than the first half”, particularly in the context of their previous 1Q=2Q guide. We continue to forecast higher sequential margin improvement in 2H26, at +120bps yoy, also based on the easing helium headwind.

There may be a helium overhang for a few more quarters, however. Our understanding is that pre-Iran Air Liquide was overweight Qatari helium, implying they sourced over 1/3 of their product from Qatar (link), and this is higher than peers. Although production has restarted, which can then be trucked to other ports by road, helium volumes are not likely to reach prior levels until Qatar can freely export LNG through the Strait of Hormuz. We see Air Liquide's helium headwind as temporary, but normalcy may be some quarters away and until then helium is likely to dampen the margin improvement story. And we see Air Liquide's helium impact as being greater than their US peers, hence our current preference for Linde and Air Products.

## Investment Implications

We rate Air Liquide Outperform with a raised Price Target of €202. We raise our 26 & 27 EPS estimates by c.+3% and c.+5%, respectively. We roll our valuation framework from a FY26 P/E to a NTM P/E incorporating the average of our FY26 and FY27 EPS. On a multiple of 28x NTM P/E (unchanged), our price target is raised to €202 from €189.

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>AI.FP (EUR)</td><td>6.70</td><td>6.96</td><td>7.44</td><td>EBIT (M)</td><td>5,582</td><td>6,154</td><td>6,797</td><td>--</td></tr><tr><td>OLD</td><td>--</td><td>6.76</td><td>7.06</td><td>Dividend/Share</td><td>3.70</td><td>3.96</td><td>4.24</td><td>--</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.  
Price Performance, 1YR

![](images/f632799a0f665dfaca6ea994feba73a777cc2c570107e4a8dfa20983dfa212b2.jpg)

<table><tr><td>Valuation Metrics</td><td>25A</td><td>26E</td><td>27E</td></tr><tr><td>Reported P/E (x)</td><td>29.0</td><td>29.3</td><td>25.0</td></tr></table>

## DETAILS

EXHIBIT 1: The backlog reached a record €6.0bn in 2Q26, with €500m more projects sequentially  
Est. Air Liquide Backlog breakdown (€m)  
![](images/6ce1fa5835f5bfc2a1d22ff4cd7848b8c0dc7e192c91c7e87833cfe6903abbc2.jpg)  
Source: Company information, Bernstein estimates and analysis

EXHIBIT 2: Air Liquide IM cumulative price by region vs 2020 (%)

Air Liquide: Industrial Merchant Cumulative Quarterly Pricing Growth by Region vs 1Q20 (%)  
![](images/08b676bda78221d533865e80fd1911f40bef4cfafaf82990093f7a4787b2bd22.jpg)  
Europe Includes Africa & the Middle East as of 4Q24  
Source: Bernstein analysis and estimates, company data

EXHIBIT 3: We believe Air Liquide base volumes are yet to inflect, not helped by helium  
Gas majors - base volume growth yoy 2019-2Q26 (%)  
![](images/1b778f9bbc859db3cb89c584d655fa06cdf2413f22b5fa9ba5dd8ea70c47a405.jpg)  
Calendar quarters  
APD and Linde have not published their 2QFY26 figures yet Source: Company information, Bernstein estimates and analysis

EXHIBIT 4: Efficiency benefits by Air Liquide have been stepping up, although yoy growth rates slowed in 2Q26  
Air Liquide: Quarterly "Efficiencies" Cost Reduction (1Q21-2Q26, €m)  
![](images/10eaed40454dbc3a5e135310f22f275a3ed4c3818ba8af81fde4bb58c5ca1812.jpg)  
Source: Company information, Bernstein analysis

Gas majors annual underlying EBIT margin improvement, bps

EXHIBIT 5: Air Liquide's margins continue to make progress, even if Asia was down in 1H26  
Air Liquide - Underlying EBIT margin advance by region 2021-2026 (bps)  
![](images/0be2ac772f98e2db0f49a0acee777a041cd35341cf6301320de185b1b25fdd66.jpg)  
Europe and MEA have been amalgamated from 1H25; Europe's margin has been restated for internal transfers to Industrial Merchants Source: Bernstein analysis, company data  
EXHIBIT 6: Air Liquide continues to make progress improving their margins

![](images/9ba40bd9d4e86696a7d7db5089cc443b492b4e08fd76ead2801558145e378cf0.jpg)  
Source: Company data, Bernstein analysis and estimates

EXHIBIT 7: They have made significant improvements vs. 2020  
![](images/a657fba77c25bb93dce1a0f0d8499de3481658ec5cc0b3de0e3e4da50400dd9b.jpg)  
Source: Company data, Bernstein analysis and estimates

EXHIBIT 8: Air Liquide's valuation has returned to close to historical averages  
![](images/ffb42e1573851a9052dba07de0e2fef5a6b37b06a4a598e844c0d65ed1e86a0d.jpg)  
Source: Bloomberg, Bernstein analysis

EXHIBIT 9: Air Liquide's premium to the Eurostoxx 600 is also close to averages  
![](images/cbf006a173557866387149822c9302f74c04bc0b5397549b6e16023aefd7c3ca.jpg)  
Source: Bloomberg, Bernstein analysis

## KEY INDUSTRIAL GASES RESEARCH

## INDUSTRIAL GASES

• 22 Jul 2026 - The Future of European Chemicals: The carbon tax conundrum - updated for last week's ETS changes

• 15 Jul 2026 - Chemicals: Specialty or Commodity, with potentially tough times in between

• 26 May 2026 - The Long View: Chemicals - Analysing the lasting impact on upstream chemicals of the Iran war

• 07 May 2026 - The Bernstein Industrial Gases Primer: How the industry structure can support long-term outperformance

• 21 Apr 2026 - Chemicals 1Q26 Preview: Poker Faces

• 20 Apr 2026 - Chemicals: Positioning for an Iran-related cycle and upgrading Arkema to Market-Perform

• 16 Mar 2026 - The Future of European Chemicals: The carbon tax conundrum

• 13 Mar 2026 - Global Industrial Gases & Semis: Assessing the helium impact

• 23 Feb 2026 - The Long View: The Industrial Gas space opportunity - rocket fuel for growth

• 12 Feb 2026 - Chemicals: There is still share price upside if we see a cyclical recovery - a scenario analysis

\- 08 Jan 2026 - Chemicals Outlook 2026: A slow start, but there could be considerable upside potential. Downgrading Solvay to Market-Perform.

• 01 Dec 2025 - The Long View: How Industrial Gases revenues can compound at the magic 5% through 2030

• 13 Aug 2025 - European Chemicals: War and Peace II - Refreshing our Ukraine war scenarios

• 10 Jul 2025 - Reflections on the European Chemicals Action Plan: First aid, but no cure

• 27 May 2025 - Chemicals: Amongst the tariff turmoil

\- 9 April 2025 - Industrial Gas Majors - It's a big world, after all but gases don't travel so "Hold Tough" and Buy

## AIR LIQUIDE

• 29 Apr 2026 - Air Liquide 1Q26: Who is the guidance for?

• 23 Feb 2026 - Air Liquide 2H25: More growth and more margin improvement

• 28 Jan 2026 - Air Liquide: Best European Idea First Quarter 2026 – Improving growth that isn't priced in. Outperform

• 03 Dec 2025 - Quick Take: A day with Air Liquide at the SDC Premium Review

• 29 Oct 2025 - Air Liquide 3Q25: Typically solid, and potentially the growth trough

• 25 Sep 2025 - Air Liquide at the Bernstein European Industrials Forum: Reassuringly Consistent

• 22 Aug 2025 - Quick Take: Air Liquide acquires DIG Airgas - a high price, but a worthy purchase

• 30 Jul 2025 - Air Liquide 1H25: "This is just the beginning"

• 28 Jul 2025 - Air Liquide: Marginal Gains

• 29 May 2025 - Quick Take: Air Liquide Americas CEO at the SDC

• 24 April 2025 - Air Liquide - Steady as she goes

• 21 February 2025 - Air Liquide - Pushing the margin again...

• 14 February 2025 - Air Liquide- We see the FY24 EBIT margin +110bp and scope for c.500bp more from there

## AIR PRODUCTS

• 17 Jul 2026 - Air Products: Sustainable above-consensus EPS growth, even including NEOM

• 30 Jun 2026 - Quick Take: Air Products cancels Darrow & 3QFY26 update

• 27 May 2026 - Bernstein SDC: Air Products Takeaways

• 01 May 2026 - Air Products 2QFY26: This may not be the last guidance raise of the year

• 02 Feb 2026 - Air Products 1QFY26: Turnaround in Motion

• 08 Dec 2025 - Air Products gives a mega-project update: the industrial gas energy transition story is not over yet

• 26 Nov 2025 - Air Products 4QFY25: Making progress as focus moves to Darrow

• 31 Jul 2025 - Quick Take: APD 3Q25 - A first beat for new management

• 1 May 2025 - Quick Take: Air Products 2Q25 — a sobering update on the job in hand

• 25 February 2025 - Air Products - rapid megaproject rationalisation shows a renewed focus on shareholder value

• 6 February 2025 - Air Products - No surprises from the 1Q25 release

• 4 February 2025 - New leadership at Air Products to support density, discipline, de-risking and ... dependability

• 31 January 2025 - Air Products - Upgrading to outperform Density, discipline, de-risking...dependability?

## LINDE

• 05 May 2026 - Linde 1Q26: Earnings Aristocrat, and potentially improving core growth

• 19 Feb 2026 - Linde 4Q25: Earnings Aristocrat, and well positioned for all macro scenarios

• 3 Nov 2025 - Linde 3Q25: Earnings Aristocrat, but also an underappreciated growth story

• 31 Oct 2025 - Quick Take: Linde 3Q25 - 27 Adj. EPS beats in a row, but a guidance narrow rather than raise

• 4 Aug 2025 - Linde 2Q25: Earnings Aristocrat

• 1 Aug 2025 - Quick Take: Linde 2Q25 - 26 EPS beats in a row, and what's 3 cents between friends?

• 22 July 2025 - Linde: Earnings aristocrat 2Q25 - we see the 26th quarter of consecutive EPS beats

\- 4 Jun 2025 - Linde: A day with the CEO at the SDC - "The value is visible" ... in the field, networks, density, benchmarking, ownership, 45Q ...

\- 29 Apr 2025 - Linde: Earnings Aristocrat? 1Q25 - we see the 25th quarter of consecutive EPS beat and underlying sequential growth

• 6 February 2025 - Linde - As expected the $24^{th}$ beat, 1Q and FY25 guidance light and a share reaction like with 3Q24...

• 4 February 2025 - Linde - We see the 24 $^{th}$ consecutive EPS beat, and qoq growth but the macro drag on guidance, but...

## APPENDIX - FINANCIAL FORECASTS

EXHIBIT 10: Air Liquide financial summary

<table><tr><td>Air Liquide (EURmn)</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td colspan="17">P&amp;L</td></tr><tr><td>Net sales</td><td>21,920</td><td>20,485</td><td>23,335</td><td>29,934</td><td>27,608</td><td>27,057</td><td>26,940</td><td>6,786</td><td>7,042</td><td>7,239</td><td>7,325</td><td>28,392</td><td>29,883</td><td>31,344</td><td>32,892</td><td>34,497</td></tr><tr><td>Gas &amp; Services</td><td>21,040</td><td>19,656</td><td>22,267</td><td>28,573</td><td>26,360</td><td>25,809</td><td>26,085</td><td>6,596</td><td>6,812</td><td>7,019</td><td>7,088</td><td>27,515</td><td>28,984</td><td>30,427</td><td>31,956</td><td>33,542</td></tr><tr><td>E&amp;C / E&amp;T (from 2025)</td><td>328</td><td>250</td><td>387</td><td>474</td><td>390</td><td>412</td><td>855</td><td>190</td><td>230</td><td>220</td><td>237</td><td>877</td><td>899</td><td>917</td><td>935</td><td>954</td></tr><tr><td>Global Markets &amp; Technology</td><td>552</td><td>579</td><td>681</td><td>887</td><td>858</td><td>836</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total growth</td><td>4.3%</td><td>-6.5%</td><td>13.9%</td><td>28.3%</td><td>-7.8%</td><td>-2.0%</td><td>-0.4%</td><td>-3.4%</td><td>5.2%</td><td>9.7%</td><td>10.7%</td><td>5.4%</td><td>5.2%</td><td>4.9%</td><td>4.9%</td><td>4.9%</td></tr><tr><td>COGS</td><td>-8,154</td><td>-7,198</td><td>-9,389</td><td>-13,813</td><td>-11,147</td><td>-10,008</td><td>-9,651</td><td></td><td>-4,953</td><td></td><td>-4,980</td><td>-9,933</td><td>-9,812</td><td>-9,947</td><td>-10,111</td><td>-10,282</td></tr><tr><td>Gross profit</td><td>13,766</td><td>13,288</td><td>13,946</td><td>16,121</td><td>16,461</td><td>17,050</td><td>17,289</td><td></td><td>8,875</td><td></td><td>9,585</td><td>18,514</td><td>20,071</td><td>21,397</td><td>22,781</td><td>24,214</td></tr><tr><td>margin</td><td>62.8%</td><td>64.9%</td><td>59.8%</td><td>53.9%</td><td>59.6%</td><td>63.0%</td><td>64.2%</td><td></td><td>64.2%</td><td></td><td>65.8%</td><td>65.2%</td><td>67.2%</td><td>68.3%</td><td>69.3%</td><td>70.2%</td></tr><tr><td>Operating expenses</td><td>-8,022</td><td>-7,500</td><td>-7,764</td><td>-9,364</td><td>-9,407</td><td>-9,599</td><td>-9,447</td><td></td><td>-4,780</td><td></td><td>-5,092</td><td>-9,872</td><td>-10,463</td><td>-10,959</td><td>-11,484</td><td>-12,029</td></tr><tr><td>Operating income recurring before D&amp;A</td><td>5,932</td><td>5,928</td><td>6,333</td><td>7,328</td><td>7,550</td><td>7,897</td><td>8,145</td><td></td><td>4,219</td><td></td><td>4,642</td><td>8,915</td><td>9,881</td><td>10,711</td><td>11,570</td><td>12,458</td></tr><tr><td>EBITDA</td><td>5,744</td><td>5,788</td><td>6,182</td><td>6,757</td><td>7,054</td><td>7,451<

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
