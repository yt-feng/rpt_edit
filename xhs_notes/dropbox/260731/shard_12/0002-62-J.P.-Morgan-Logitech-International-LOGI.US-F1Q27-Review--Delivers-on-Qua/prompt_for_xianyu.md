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
Quarterly Forecasts (FYE Mar)
Adj. EPS (\$)

# JPM

## Logitech International

F1Q27 Review: Delivers on Quarterly Beat but Supply Disruption Tests Near-Term Outlook

Logitech reported a solid F1Q27 (Jun-end) beat, driven by better-than expected margins and consistent execution across the portfolio, with the upside supported by a \$61 mn tariff refund. However, the more notable development was an incident at one of Logitech's semiconductor component supplier in late June that forced the temporary closure of the supplier's fab, impacting both the Gaming and Personal Workspace portfolios and likely constraining the company's ability to fully meet demand near-term. On the demand side, trends remain constructive, with Gaming benefiting from broad strength on premium products and the North America market returning to mid-single-digit growth, while Video Collaboration sustained momentum as enterprise customers continue investing in meeting room infrastructure. Share gains were broad across geographies, enforcing the view that constraints are centered on supply rather than demand. Looking ahead, management sized the estimated supplier impact at \$20 mn in F2Q and \$200 mn in F3Q before being largely resolved by F4Q, noting that outside of the disruption, top-line momentum would track near F1Q rates through the balance of FY27. Full-year operating margin is still expected to track near the high-end of the 15% to 18% long-term target range, driven by healthy underlying performance and the add-on benefit of the one-time tariff refund, even as the company drives higher investment into R&D and S&M. We expect investors to focus on the supply impact relative to 2Q and 3Q and visibility into when the disruption is resolved, with the overhang adding to an already cautious backdrop filled with macro uncertainty, questions around consumer spending resilience, and the sustainability of enterprise peripheral attach rates with concerns surrounding PC trends. That said, given management's confidence in a F4Q resolution and intact underlying demand trends, we do not see a material impact to our out-year trajectory, while moderating our near-term estimates on the disruption at the semiconductor component supplier.

\- F1Q27 (Jun-end) Results: Solid earnings beat led by better revenue and margin trends with the latter helped by tariff refund. Revenue rose +7% y/y (+5% y/y CC) to \$1,227 mn, (vs. JPMe of \$1,202 mn and consensus of \$1,200 mn) led by stronger-than-expected demand for Pointing Devices (+16% y/y), Gaming (+12% y/y) and Video Collaboration (+11% y/y). By geography, Asia Pacific rose +9% y/y to \$368 mn, EMEA fell -1% to \$344 mn, and Americas rose +12% y/y to \$516 mn. Meanwhile, gross margins tracked to 44.8%, excluding the \$61 mn tariff refund (vs. JPMe of 43.5% and consensus of 43.3%), as a weaker Euro (\~240-250 bps), higher ASPs (\~100 bps), and product cost reduction (\~100 bps) were partly offset by higher spend on promotions. Better gross margins more than offset opex tracking slightly above expectations at \$320 mn (vs. JPMe of \$318 mn and consensus of \$315 mn), driving operating margins of 18.7% (vs. JPMe and consensus of 17.0%), excluding tariff benefits, and leading EPS to track to \$1.85 (includes tariff benefits vs. JPMe of \$1.28 and consensus of \$1.33).

\- F2Q27 (Sep-end) Guide: Revenue and operating margin outlook track below consensus given headwind from semiconductor supplier incident. Revenue was guided in a range of \$1,185-\$1,220 mn (vs. JPMe of \$1,250 mn and consensus of \$1,230 mn), including a \$20 mn headwind related to a supplier incident. Meanwhile, operating income was guided in a range of \$185-

Sources for: Style Exposure – JPM Global Markets Strategy; all other tables are company data and JPM estimates. See page 6 for analyst certification and important disclosures.

## Neutral

LOGI, LOGI US
Price (29 Jul 26):\$102.99

▼Price Target (Dec-27):\$120.00
Prior (Dec-27):\$123.00

IT Hardware/ Telecom & Networking Equipment

Joseph Cardoso AC
(1-212) 622-9036
joseph.cardoso@jpmchase.com

Akanksh Chauhan
(1-212) 622-0045
akanksh.chauhan@JPM.com

Manmohanpreet Singh
(1-212) 622-4527
manmohanpreet.singh@jpmchase.com

Marc Vitenzon
(1-212) 622-3342
marc.vitenzon@jpmchase.com
JPM Securities LLC

<table><tr><td colspan="4">Key Changes (FYE Mar)</td></tr><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. EPS - 28E ($)</td><td>6.40</td><td>6.10</td><td>-4.7%</td></tr></table>

<table><tr><td></td><td>2026A</td><td>2027E</td><td>2028E</td></tr><tr><td>Q1</td><td>1.26</td><td>1.85A</td><td>1.37</td></tr><tr><td>Q2</td><td>1.45</td><td>1.26</td><td>1.44</td></tr><tr><td>Q3</td><td>1.93</td><td>1.67</td><td>2.14</td></tr><tr><td>Q4</td><td>1.13</td><td>1.00</td><td>1.16</td></tr><tr><td>FY</td><td>5.78</td><td>5.80</td><td>6.10</td></tr></table>

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>50</td><td>42</td><td>51</td><td>35</td><td>54</td></tr><tr><td>Growth</td><td>46</td><td>68</td><td>16</td><td>25</td><td>15</td></tr><tr><td>Momentum</td><td>49</td><td>42</td><td>37</td><td>41</td><td>65</td></tr><tr><td>Quality</td><td>11</td><td>5</td><td>4</td><td>8</td><td>4</td></tr><tr><td>Low Vol</td><td>11</td><td>16</td><td>15</td><td>31</td><td>19</td></tr></table>

Price Performance  
![](images/97dbe3073a792a7f296d6365974a0738ad108dfc71cfe57200434267a9a57574.jpg)

— LOGI Price (\$) — RTY (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>2.8%</td><td>4.4%</td><td>5.4%</td><td>9.8%</td></tr><tr><td>Rel</td><td>-14.3%</td><td>7.9%</td><td>-0.7%</td><td>-19.7%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>145</td></tr><tr><td>52-week range ($)</td><td>129.66-83.32</td></tr><tr><td>Market cap ($ mn)</td><td>14,937.46</td></tr><tr><td>Exchange rate</td><td>1.00</td></tr><tr><td>Free float (%)</td><td>83.0%</td></tr><tr><td>3M ADV (mn)</td><td>1.23</td></tr><tr><td>3M ADV ($ mn)</td><td>130.5</td></tr><tr><td>Volatility (90 Day)</td><td>42</td></tr><tr><td>Index</td><td>RUSSELL 2000</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>10|4|1</td></tr></table>

Key Metrics (FYE Mar)

<table><tr><td>$ in millions</td><td>FY26A</td><td>FY27E</td><td>FY28E</td><td>FY29E</td></tr><tr><td colspan="5">Financial Estimates</td></tr><tr><td>Revenue</td><td>4,841</td><td>4,992</td><td>5,283</td><td>5,489</td></tr><tr><td>Adj. EBIT</td><td>911</td><td>893</td><td>912</td><td>965</td></tr><tr><td>Adj. EBITDA</td><td>988</td><td>968</td><td>991</td><td>1,048</td></tr><tr><td>Adj. net income</td><td>857</td><td>819</td><td>814</td><td>860</td></tr><tr><td>Adj. EPS</td><td>5.78</td><td>5.80</td><td>6.10</td><td>6.80</td></tr><tr><td>BBG EPS</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cashflow from operations</td><td>1,037</td><td>911</td><td>930</td><td>983</td></tr><tr><td>FCFF</td><td>976</td><td>836</td><td>851</td><td>900</td></tr><tr><td colspan="5">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>6.3%</td><td>3.1%</td><td>5.8%</td><td>3.9%</td></tr><tr><td>EBIT margin</td><td>18.8%</td><td>17.9%</td><td>17.3%</td><td>17.6%</td></tr><tr><td>EBIT Growth Y/Y (%)</td><td>17.6%</td><td>(2.0%)</td><td>2.2%</td><td>5.8%</td></tr><tr><td>EBITDA margin</td><td>20.4%</td><td>19.4%</td><td>18.8%</td><td>19.1%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>15.7%</td><td>(2.0%)</td><td>2.4%</td><td>5.7%</td></tr><tr><td>Net margin</td><td>17.7%</td><td>16.4%</td><td>15.4%</td><td>15.7%</td></tr><tr><td>Adj. EPS growth</td><td>19.3%</td><td>0.3%</td><td>5.2%</td><td>11.4%</td></tr><tr><td colspan="5">Ratios</td></tr><tr><td>Adj. tax rate</td><td>11.0%</td><td>14.2%</td><td>14.5%</td><td>14.5%</td></tr><tr><td>Interest cover</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROE</td><td>39.5%</td><td>37.7%</td><td>39.4%</td><td>44.1%</td></tr><tr><td colspan="5">Valuation</td></tr><tr><td>FCFF yield</td><td>6.4%</td><td>5.7%</td><td>6.2%</td><td>6.9%</td></tr><tr><td>Dividend yield</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EV/Revenue</td><td>2.8</td><td>2.6</td><td>2.3</td><td>2.1</td></tr><tr><td>EV/EBITDA</td><td>13.7</td><td>13.3</td><td>12.3</td><td>11.0</td></tr><tr><td>Adj. P/E</td><td>17.8</td><td>17.8</td><td>16.9</td><td>15.2</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

We maintain LOGI shares at Neutral as we believe the rebound of the product portfolio to healthy growth in the medium term will remain constrained by a challenging macro, and efforts to drive growth will likely need to return to robust promotional levels. However, we continue to believe that Logitech is the industry leader in peripherals and devices, with a consistent history of execution, and will benefit whenever end demand recovers.

## Valuation

We are lowering our December 2027 price target to \$120 (from \$123 prior) based on our updated CY28E EPS valued at \~18x P/E multiple, which is below both the current and long-term historical average multiples of \~19x, which we believe is justified given Logitech's leading position in the market, constrained by a challenging macro backdrop.

Performance Drivers  
![](images/73ec1903b1faf127e6dfc4c59b7f66929c38e8c835910bd39ad4daaa3ed32966.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI US</td><td>0.51</td><td>0.74</td></tr><tr><td>Sect: Technology</td><td>0.22</td><td>0.04</td></tr><tr><td>Ind: Tech Hard Equip</td><td>0.38</td><td>0.38</td></tr><tr><td>Macro:</td><td></td><td></td></tr><tr><td>Non-Energy Commodity</td><td>0.02</td><td>0.23</td></tr><tr><td>Economic Surprise</td><td>-0.01</td><td>0.19</td></tr><tr><td>US 10yr Breakeven</td><td>-0.15</td><td>0.15</td></tr><tr><td>Quant Styles:</td><td></td><td></td></tr><tr><td>Growth</td><td>-0.25</td><td>-0.35</td></tr><tr><td>Size</td><td>-0.21</td><td>-0.29</td></tr><tr><td>Value</td><td>0.20</td><td>0.28</td></tr></table>

\$210 mn, implying an operating margin of \~16.4% (vs. JPMe of 17.8% and consensus of 17.5%).

# Investment Thesis, Valuation and Risks

Logitech International (Neutral; Price Target: \$120.00)

## Investment Thesis

We maintain LOGI shares at Neutral as we believe the rebound of the product portfolio to healthy growth in the medium term will remain constrained by a challenging macro, and efforts to drive growth will likely need to return to robust promotional levels. However, we continue to believe that Logitech is the industry leader in peripherals and devices, with a consistent history of execution, and will benefit whenever end demand recovers.

## Valuation

We are lowering our December 2027 price target to \$120 (from \$123 prior) based on our updated CY28E EPS valued at \~18x P/E multiple, which is below both the current and long-term historical average multiples of \~19x, which we believe is justified given Logitech's leading position in the market, constrained by a challenging macro backdrop.

## Logitech P/E-Based Price Target

\$ in Millions, except per share amounts

<table><tr><td rowspan="2"></td><td>NTM</td><td rowspan="2">CY28E</td></tr><tr><td>Qtrs 1-4</td></tr><tr><td>JPM Net Income</td><td>$736</td><td>$842</td></tr><tr><td>JPM EPS</td><td>$5.29</td><td>$6.59</td></tr><tr><td>P/E Multiple</td><td>19x</td><td></td></tr><tr><td>JPM P/E Multiple</td><td></td><td>18x</td></tr><tr><td>Implied Equity Value</td><td>$14,618</td><td>$15,318</td></tr><tr><td>Average Diluted Share Count</td><td>145</td><td>128</td></tr><tr><td>Implied Share Price</td><td>$101</td><td>$120</td></tr><tr><td>Current Value per Share</td><td>$101</td><td>$101</td></tr><tr><td>Upside vs. Current</td><td></td><td>19%</td></tr><tr><td>Memo:</td><td></td><td></td></tr><tr><td>(-) Net Cash/(Debt)</td><td>$1,750</td><td>$1,461</td></tr><tr><td>Enterprise Value</td><td>$12,869</td><td>$13,857</td></tr><tr><td>JPM EBITDA</td><td>$885</td><td>$1,026</td></tr><tr><td>Implied EV/EBITDA</td><td>14.5x</td><td>13.5x</td></tr></table>

Source: Company reports and JPM estimates.

Risks to Rating and Price Target

Our rating and price target could be at risk to the downside for any of the following reasons:

\- Consumer spending headwinds increase relative to already depressed levels;

\- Specific product category demand decelerates quicker than expected;

\- Operating margin targets step down on FX impacts, component costs, lower sell-through;

\- Trade wars impact overall component costs and pressure both revenues and margins;

Our rating and price target could be at risk to the upside for any of the following reasons:

\- Consumer spending recovery buoys the top line sooner than expected;

\- Ramp into B2B endeavors drives revenue recovery faster than expected;

\- Leveraging inorganic opportunities may drive better revenue growth outlook;

Logitech International: Summary of Financials

<table><tr><td>Income Statement - Annual</td><td>FY25A</td><td>FY26A</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Revenue</td><td>4,555</td><td>4,841</td><td>4,992</td><td>5,283</td></tr><tr><td>COGS</td><td>(2,573)</td><td>(2,732)</td><td>(2,760)</td><td>(3,012)</td></tr><tr><td>Gross profit</td><td></td><td>-</td><td>-</td><td>-</td></tr><tr><td>SG&amp;A</td><td>(1,208)</td><td>(1,198)</td><td>(1,339)</td><td>(1,359)</td></tr><tr><td>Adj. EBITDA</td><td>854</td><td>988</td><td>968</td><td>991</td></tr><tr><td>D&amp;A</td><td>(80)</td><td>(77)</td><td>(75)</td><td>(79)</td></tr><tr><td>Adj. EBIT</td><td>775</td><td>911</td><td>893</td><td>912</td></tr><tr><td>Net Interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Adj. PBT</td><td>829</td><td>963</td><td>954</td><td>952</td></tr><tr><td>Tax</td><td>(89)</td><td>(106)</td><td>(135)</td><td>(138)</td></tr><tr><td>Minority Interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Adj. Net Income</td><td>740</td><td>857</td><td>819</td><td>814</td></tr><tr><td>Reported EPS</td><td>4.84</td><td>5.78</td><td>5.80</td><td>6.10</td></tr><tr><td>Adj. EPS</td><td>4.84</td><td>5.78</td><td>5.80</td><td>6.10</td></tr><tr><td>DPS</td><td></td><td>-</td><td>-</td><td>-</td></tr><tr><td>Payout ratio</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Shares outstanding</td><td>153</td><td>148</td><td>141</td><td>133</td></tr></table>

<table><tr><td>Balance Sheet &amp; Cash Flow Statement</td><td>FY25A</td><td>FY26A</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Cash and cash equivalents</td><td>1,503</td><td>1,742</td><td>1,670</td><td>1,564</td></tr><tr><td>Accounts receivable</td><td>455</td><td>506</td><td>496</td><td>476</td></tr><tr><td>Inventories</td><td>504</td><td>490</td><td>523</td><td>525</td></tr><tr><td>Other current assets</td><td>1,090</td><td>1,174</td><td>1,230</td><td>1,213</td></tr><tr><td>Current assets</td><td>2,593</td><td>2,915</td><td>2,900</td><td>2,777</td></tr><tr><td>PP&amp;E</td><td>114</td><td>116</td><td>114</td><td>115</td></tr><tr><td>LT investments</td><td></td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other non current assets</td><td>344</td><td>339</td><td>324</td><td>324</td></tr><tr><td>Total assets</td><td>3,539</td><td>3,849</td><td>3,815</td><td>3,691</td></tr><tr><td>Short term borrowings</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Payables</td><td>415</td><td>531</td><td>582</td><td>601</td></tr><tr><td>Other short term liabilities</td><td>687</td><td>782</td><td>765</td><td>765</td></tr><tr><td>Current liabilities</td><td>1,101</td><td>1,313</

[中间内容因长度限制已省略]

 market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and

should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
