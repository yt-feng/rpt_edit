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

# China Beer May update: Heineken rapidly accelerating while Bud still languishes

![](images/a155a8007989766b4016ecc8d8f9cf6a20786cbdc53a98d07a8d7cfb03f50d9e.jpg)  
Euan McLeish  
+81 3 5962 9611  
euan.mcleish@bernsteinsg.com

![](images/837643d63510e7942c73ecce021563ed278bfa2173a97ca789bc92812e052f1b.jpg)

Hao Wang, CFA

+852 2123 2627

hao.wang@bernsteinsg.com

![](images/57f4c1274d6a8d09ee19c742e0cd19360dcf2b3012f908e9add47fb2e756a13d.jpg)

Mufei Gao

+81 3 6777 6995

mufei.gao@bernsteinsg.com

China beer total sell-out value was +2% in May 2026, reflecting a small step up from April's 1% growth. Restaurant channel value growth continued in line with April at +3%, while off-trade value growth improved to +1% from -1% in April. Yanjing (not covered) was again the strongest performer in May with value +17% YoY (slowing down somewhat from April's +19%), followed by Chongqing (not covered) at +9% and CRBeer +3%, while Tsingtao value was -2%, and Bud China again underperforming the industry with a -3% decline.

Our regressions now indicate that CRBeer's topline growth will accelerate to c. 2% in Q2, Bud China's decline will narrow to c. -2%, and Tsingtao's will widen to c. -3% based on the Q2 to date monthly sales. We have observed a 96% correlation between Bud's reported growth over the last 15 months, compared to 84% for Yanjing, 81% for Tsingtao and Chongqing at 73%. CRBeer's correlation is low given they only report semi-annually.

Total off-trade beer sales improved MoM in all five key provinces, led by Zhejiang and Jiangsu which improved to +11%/+5%, from -7%/-11%, and Guangdong's off-trade growth continued to accelerate to +14% YoY vs +10% in April. All segments, other than MS+, bounced back to growth in the off-trade. In the restaurant channel, Guangdong again outperformed at +20% but we still haven't seen this filter through to Bud China. Shandong led the decline at -20%, dragging Tsingtao down. Premium segment value was up 8%, while Super Premium and M/S&Econ both declined in May.

CRBeer's April value growth came in at +3% in May, ahead of April's +2% but below Q1's +4% average yoy. CRBeer outperformed the Premium segment (+11% vs overall segment +5%) in May, driven by Heineken at +37%, with 11% value growth in both channels and both accelerating vs April. Overall, CRB grew value in both channels in May and the most pronounced growth was recorded in Guangdong and Fujian provinces where both channels registered double-digit growths in both channels (Exhibit 21).

Bud China's value was $-3\%$ again in May, similar to April and up from $-8\%$ in Q1 and $-11\%$ in Q4. Both channels showed modest trajectory improvement, but the lack of material uptick in the off-trade (- $10\%$ in May vs $-12\%$ in March & April) suggests that Bud's route to market expansion strategy is yet to deliver the goods. Bud improved in both channels in Zhejiang and also in Premium (Exhibit 19), but performance in the Guangdong restaurant channel slowed down and was materially behind overall channel performance.

Tsingtao's May value was -2% YoY, in line with Q1's -2% but marginally below March's 0% and April's -1%. Its home province Shandong (36% of Tsingtao's national sell-out value) was the biggest drag in the month with provincial value in restaurant channel performing much worse than March and April (Exhibit 25).

Chongqing (not covered) overall value was +9% YoY in May, in line with +9% in the

$1^{st}$ Quarter but slowing down from April's +12%, as the restaurant channel delivered significant sequential improvement in key provinces apart from Guangdong, but off-trade channel deteriorated in the month.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="3">22 Jun 2026</td><td colspan="2">TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td></td><td colspan="2">Closing</td><td>Price</td><td>Rel.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Price</td><td>Target</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>1876.HK (Bud APAC)</td><td>M</td><td>HKD</td><td>6.46</td><td>7.60</td><td>(66.4)%</td><td>USD</td><td>0.04</td><td>0.05</td><td>0.05</td><td>22.2</td><td>17.6</td><td>15.4</td></tr><tr><td>291.HK (CRB)</td><td>O</td><td>HKD</td><td>21.42</td><td>46.00</td><td>(57.8)%</td><td>CNY</td><td>1.80</td><td>1.98</td><td>2.17</td><td>10.3</td><td>9.3</td><td>8.5</td></tr><tr><td>168.HK (Tsingtao)</td><td>O</td><td>HKD</td><td>44.88</td><td>71.00</td><td>(58.4)%</td><td>CNY</td><td>3.36</td><td>3.53</td><td>3.60</td><td>11.5</td><td>11.0</td><td>10.8</td></tr><tr><td>600600.CH (Tsingtao)</td><td>M</td><td>CNY</td><td>53.92</td><td>62.00</td><td>(71.2)%</td><td>CNY</td><td>3.36</td><td>3.53</td><td>3.60</td><td>16.0</td><td>15.3</td><td>15.0</td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,048.07</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate CRBeer Outperform with a Price Target of HK\$46. Model: 291.HK

We rate Tsingtao H-Share Outperform with a Price Target of HK\$71 and Tsingtao's A-share Market-Perform with a Price Target of RMB62. Model: 168.HK

We rate Bud APAC Market-Perform with a Price Target of HK\$7.60. Model: 1876.HK

## DETAILS

EXHIBIT 1: Our regressions now indicate that CRBeer's topline growth will accelerate to c. 2% in Q2, Bud China's decline will narrow to c. -2%, and Tsingtao's to widen to c. -3% based on our regression formulae and the Q2 to date monthly sales.

China Beer Q1 Actual & Q2 Regression-based Revenue YoY % Est.

![](images/03f326730aa3c9ef7636cd45dcc10f826e852e8e28f0940d98f3c52c9489907b.jpg)  
Regression is based on Jan-May for CRBeer and Apr-May for the rest; CRBeer's two bars are 2H25 actual and 1H26 est. based on regression Source: BigOne Lab, company reports, Bernstein analysis and estimates  
Regression R-square of BigOne National Sell-out Value YoY % vs Reported Beer Revenue YoY % (22Q3-26Q1)

EXHIBIT 2: We see a 73-96% correlation between BigOne Lab quarterly brewer value growth and reported revenue growth

![](images/7b58d4a0ce695ed9810a6750409b9dfe1e129c7c6a631e9835145c75ea93a3a6.jpg)  
CRBeer reports semi-annually  
Source: BigOne Lab, company reports, Bernstein analysis

## MONTHLY OVERVIEW

Our BigOne Lab China beer data set leverages the POS sell-out data to track 180k supermarket stores and menu QR code data for 230k restaurant outlets nationally, allowing us to track brewer sell-out value performance by province and price segment on a monthly basis. The data set does not cover the nightlife channel, however.

In May 2026 we saw 3-month rolling overall national beer value growth (i.e Off-Trade + Restaurant channel) +2% in the period ending May 31 (Exhibit 3). Comparing May vs April and March, May standalone value was +1% YoY, slightly better than March's -1% and April's +1%. Monthly value growth performance improved for CRBeer, Bud was at similar rate vs April, and all others saw deterioration in the month. By brewer, Yanjing (not covered) was again the strongest performer in May with value +17% YoY (slowing down somewhat from April's +19%), followed by Chongqing at +9% and CRBeer +3%, while Tsingtao value was -2%, and Bud China again underperforming the industry with a -3% decline in the month.

Going into June, comps are similar versus May (Exhibit 14), before they become much tougher in July for most brewers apart from Bud China and Yanjing.

EXHIBIT 3: In May 2026 we saw a marginal growth in national beer value growth

China Total Beer Value Growth (Rolling 3-month / Monthly YoY %)  
![](images/3ff2dc0a29168f2a2ba4b42d1109006e52b05bacbfe05527bb64f15345f6df60.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 4: In May, Restaurant channel value was again in growth  
China Restaurant Beer Value Growth Monthly YoY %  
![](images/208ced775340ba07d63e28c499e26c801602871e2c82e851c279b3e239702a4b.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 5: Off-trade value was in marginal growth at +1% YoY in the month  
China Off-Trade Beer Value Growth Monthly YoY %  
![](images/352a2af896b3be785c638238499108569cea89a94b13868d9cfb02377055e86d.jpg)  
Source: BigOne Lab, Bernstein analysis  
China Total Beer Value Growth YoY% by Brewer

EXHIBIT 6: In Q1 Bud China / Chongqing / Yanjing performed sequentially better than Q4

![](images/29e83de757cd3b126100d92be5e9bec5d595faf7caab030267c042c34dd3fd7b.jpg)  
EXHIBIT 7: Monthly value growth improved for CRBeer but worsened for Chongqing / Yanjing / Tsingtao in May vs April  
Bernstein does not cover Yanjing or Chongqing Source: BigOne Lab, Bernstein analysis

China Total Beer Value Growth YoY% by Brewer  
![](images/013629f10f780bf23d5da287002c8ece0feca132aca4064878c434cfa8ba98f8.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 8: Yanjing materially outperformed in most segments in the month  
Beer Value YoY % in May 2026 by Segment by Brewer (Both Channel)  
![](images/83c7fef70611ede46b2f961fe13e638ee524a3019421d9986050e482c875b1db.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 9: Yanjing & Chongqing were top in share gains while Bud China's share loss narrowed  
China Total Beer Value Share Gain/Loss (YoY in bps)

![](images/2d7fb9f91539b092dcfe22aa8bfda481d2aa229a7fa53411bb2c248ef96bbf9f.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 10: And similarly in May vs April  
China Total Beer Value Share Gain/Loss (YoY in bps)

![](images/9a7f20bca067a3ec89658eaea884187165beb894b389a05ac460f6d17345ffbd.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 11: At the national level Bud China's share loss was across the board in May while CRB gained the most in Super Premium and M/S&Econ  
May '26 National Segment Share Gain/Loss in bps YoY  
![](images/2801914be3f6d74ea7745c2080c15b5aca868f1244e343e2e6c6597bf66e8a2f.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 12: In the Off-Trade, Bud China was maintaining its share in MS+  
May '26 National Off-Trade Segment Share Gain/Loss in bps YoY

![](images/58c6a588bf7c7495cbaa56999d5029bab09475db454005ad6a767532cf68346a.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 13: And they even gained share in Premium segment of Restaurant channel  
May '26 National Restaurant Segment Share Gain/Loss in bps YoY

![](images/11131cb6e2f74cb5bd92100f842974d7142e0daf19847e983a215c25272ae30b.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 14: In June comps are softer for CRBeer and Bud China but tougher for Chongqing and Yanjing

Forthcoming Comps - China Total Beer Value Growth YoY% by Brewer

![](images/f31b614c63500b2a6c0b09de64e57fe2078e9f8647966ec8464bc9cc6b98c4ea.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 15: By province Jiangsu and Zhejiang were improving MoM in May while Fujian and Shandong decelerated

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">Wtg in FY25 National Value</td><td colspan="4">COMBINED CHANNELS</td></tr><tr><td>Mar-2026</td><td>Apr-2026</td><td>May-2026</td><td>Last 3m Avg</td></tr><tr><td rowspan="7">By Province</td><td>Guangdong</td><td>17%</td><td>7%</td><td>16%</td><td>17%</td><td>14%</td></tr><tr><td>Fujian</td><td>5%</td><td>-1%</td><td>1%</td><td>0%</td><td>0%</td></tr><tr><td>Zhejiang</td><td>7%</td><td>-6%</td><td>-2%</td><td>11%</td><td>2%</td></tr><tr><td>Jiangsu</td><td>6%</td><td>-7%</td><td>-6%</td><td>5%</td><td>-2%</td></tr><tr><td>Shandong</td><td>12%</td><td>-6%</td><td>-11%</td><td>-14%</td><td>-11%</td></tr><tr><td>Others</td><td>53%</td><td>-2%</td><td>1%</td><td>0%</td><td>0%</td></tr><tr><td>Total</td><td></td><td>-1%</td><td>1%</td><td>2%</td><td>1%</td></tr><tr><td rowspan="5">By Segment</td><td>Super Premium</td><td>5%</td><td>-19%</td><td>-18%</td><td>-10%</td><td>-15%</td></tr><tr><td>Premium</td><td>42%</td><td>1%</td><td>4%</td><td>5%</td><td>4%</td></tr><tr><td>Mainstream+</td><td>28%</td><td>2%</td><td>3%</td><td>0%</td><td>2%</td></tr><tr><td>M/S &amp; Eco</td><td>26%</td><td>-5%</td><td>-2%</td><td>2%</td><td>-2%</td></tr><tr><td>Total</td><td></td><td>-1%</td><td>1%</td><td>2%</td><td>1%</td></tr></table>

Source: BigOne Lab, Bernstein analysis

EXHIBIT 16: National monthly growth diagnostic by Province and Segment and Channel

<table><tr><td rowspan="3" colspan="2"></td><td colspan="5">RESTAURANT CHANNEL</td><td colspan="5">OFF-TRADE CHANNEL</td></tr><tr><td rowspan="2">Wtg in FY25 National Value</td><td colspan="4">Brewer&#x27;s Value Growth YoY %</td><td rowspan="2">Wtg in FY25 National Value</td><td colspan="4">Brewer&#x27;s Value Growth YoY %</td></tr><tr><td>Mar-2026</td><td>Apr-2026</td><td>May-2026</td><td>Last 3m Avg</td><td>Mar-2026</td><td>Apr-2026</td><td>May-2026</td><td>Last 3m Avg</td></tr><tr><td rowspan="7">By Province</td><td>Guangdong</td><td>15%</td><td>8%</td><td>22%</td><td>20%</td><td>17%</td><td>19%</td><td>6%</td><td>10%</td><td>14%</td><td>10%</td></tr><tr><td>Fujian</td><td>5%</td><td>8%</td><td>3%</td><td>1%</td><td>4%</td><td>4%</td><td>-8%</td><td>-3%</td><td>0%</td><td>-3%</td></tr><tr><td>Zhejiang</td><td>7%</td><td>-2%</td><td>3%</td><td>12%</td><td>5%</td><td>8%</td><td>-10%</td><td>-7%</td><td>11%</td><td>0%</td></tr><tr><td>Jiangsu</td><td>5%</td><td>-1%</td><td>1%</td><td>4%</td><td>2%</td><td>7%</td><td>-12%</td><td>-11%</td><td>5%</td><td>-5%</td></tr><tr><td>Shandong</td><td>16%</td><td>-10%</td><td>-16%</td><td>-20%</td><td>-16%</td><td>8%</td><td>7%</td><td>0%</td><td>1%</td><td>2%</td></tr><tr><td>Others</td><td>52%</td><td>1%</td><td>4%</td><td>5%</td><td>4%</td><td>54%</td><td>-5%</td><td>-3%</td><td>-5%</td><td>-4%</td></tr><tr><td>Total</td><td></td><td>0%</td><td>3%</td><td>3%</td><td>2%</td><td></td><td>-3%</td><td>-1%</td><td>1%</td><td>-1%</td></tr><tr><td rowspan="5">By Segment</td><td>Super Premium</td><td>6%</td><td>-26%</td><td>-23%</td><td>-16%</td><td>-21%</td><td>3%</td><td>-5%</td><td>-6%</td><td>5%</td><td>-1%</td></tr><tr><td>Premium</td><td>50%</td><td>5%</td><td>9%</td><td>8%</td><td>8%</td><td>33%</td><td>-5%</td><td>-3%</td><td>1%</td><td>-2%</td></tr><tr><td>Mainstream+</td><td>32%</td><td>1%</td><td>4%</td><td>2%</td><td>3%</td><td>23%</td><td>3%</td><td>3%</td><td>-2%</td><td>1%</td></tr><tr><td>M/S &amp; Eco</td><td>12%</td><td>-13%</td><td>-8%</td><td>-4%</td><td>-8%</td><td>41%</td><td>-4%</td><td>-2%</td><td>3%</td><td>0%</td></tr><tr><td>Total</td><td></td><td>0%</td><td>3%</td><td>3%</td><td>2%</td><td></td><td>-3%</td><td>-1%</td><td>1%</td><td>-1%</td></tr></table>

Source: BigOne Lab, Bernstein analysis

## OFF-TRADE / RESTAURANT CHANNEL MOMENTUM BY BREWER

## BUD CHINA

Guangdong and Zhejiang were the largest contributors to Bud China's growth in the Restaurant channel (Exhibit 17). And similarly is Premium segment in the same channel (Exhibit 18), while in the off-trade Mainstream+ delivered marginal decline in the month.

Comparing May vs April, Bud's performance in the off-trade channel improved slightly on a national basis, and particularly in ZJ&JS, and also in the M/S&Econ segment. In the restaurant channel, we saw relatively better performance in ZJ&HeN and the Premium segment (Exhibit 19).

EXHIBIT 17: Bud China Value bridge by PROVINCE

Bud China Value Bridge by PROVINCE (Indexed to May '25 = 100)

![](images/14f6137f2e5a6e16ce470b8cdc7b6e8314a26cfcd5742e3903cabdb524330cac.jpg)  
Source: BigOne Lab, Bernstein analysis  
Restaurant Channel

![](images/3627a0b45866d41bd934f26f98767e482e97a08c288d80571475359239bc12cc.jpg)

EXHIBIT 18: Bud China Value bridge

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
