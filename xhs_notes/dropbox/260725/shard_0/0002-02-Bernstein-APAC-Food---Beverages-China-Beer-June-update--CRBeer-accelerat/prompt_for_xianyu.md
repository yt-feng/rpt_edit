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

# China Beer June update: CRBeer accelerates while Bud continues to languish

![](images/d49b87f2d6ab73d9004b8014513337faed62c2764988b5f50c1781f3a29621c4.jpg)  
Euan McLeish  
+81 3 5962 9611

euan.mcleish@bernsteinsg.com

![](images/6c30aac69820a2d77f06a1e833f4a016a33beb4a3576b84ba10dc42ed28eb9a2.jpg)

Hao Wang, CFA

+852 2123 2627

hao.wang@bernsteinsg.com

![](images/8bb5d20179ddfa3c85a31765d81e8266330bb66c01da4ada5091c87d207d60bb.jpg)

Mufei Gao

+81 3 6777 6995

mufei.gao@bernsteinsg.com

Makoto Morozumi

+81 3 6777 6972

makoto.morozumi@bernsteinsg.com

China beer total sell-out value growth moderated to +1% in June 2026 from +2% in May, as restaurant channel growth slowed to +1% from +3%, while off-trade strengthened to +2% from +1%. Yanjing (not covered) remained the clear outperformer with value growth +15% YoY, CRBeer improved to +6% (from +3% in May), ahead of Chongqing (not covered) at +1%. Tsingtao's decline narrowed to -1%, but Bud China's declines continued at -4%. Our regressions now indicate that Bud China's decline will narrow to c. -3%, and Tsingtao's will widen to c. -3% based on Q2 sell-out performance to date, but the CRBeer r $^{2}$ remains too low to drive meaningful estimates.

Province-level performance was mixed. Guangdong remained the strongest province with +9% overall value growth and +11% in restaurants, while Shandong remained the biggest underperformer at -11% and this continued to weigh on Tsingtao. Zhejiang and Jiangsu remained positive in both channels, while Fujian deteriorated further to -4% from 0% in May. By segment, Premium remained the key growth driver at +3%, while Super Premium stayed under pressure at -14% and Mainstream+ accelerated slightly. Off-trade momentum was stronger than restaurant in June, helped by a return to positive growth across most segments.

CRBeer's June value growth accelerated to +6%, up from +3% in May and ahead of Q1's +4% average. Growth was driven by a sharp rebound in the off-trade channel (+8% vs +1% in May), while restaurant growth remained healthy at +4%. Premium continued to be the key growth driver and Guangdong again stood out, with restaurant growth accelerating to +46%. Our regressions indicate CRBeer's topline growth should improve to c. 2% in 1H26, but we note the relatively low $r^2$ .

Bud China's value declined by $4\%$ in June, worsening from $-3\%$ in May and remaining one of the weakest performers in the industry. Off-trade improved slightly to $-9\%$ from $-10\%$ , but restaurant growth slipped back to $-1\%$ after $+2\%$ in May. Zhejiang remained one of the few bright spots and Premium trends remained less negative, but Bud continued to lag in Guangdong despite another month of strong provincial growth. The June data suggest Bud's turnaround remains elusive.

Tsingtao's June value was -1% YoY, improving from -2% in May and better than Q1's -2% average. Off-trade growth remained positive at +3%, partially offsetting a -3% decline in restaurants. Shandong continued to be the largest drag, with restaurant sales still down -15%, although stronger trends in Guangdong, Fujian and Shaanxi helped narrow the overall decline.

Chongqing (not covered) overall value growth slowed to +1% YoY in June, down from +9% in May and in Q1. Restaurant channel growth decelerated sharply to +1% from +19%, while off-trade improved modestly to +1%. Xinjiang remained strong, but softer trends in Guangdong and Chongqing province weighed on overall performance.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="2">23 Jul 2026</td><td rowspan="2">Price Target</td><td rowspan="2">TTM Rel. Perf.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>1876.HK (Bud APAC)</td><td>M</td><td>HKD</td><td>6.59</td><td>7.30</td><td>(53.1)%</td><td>USD</td><td>0.04</td><td>0.05</td><td>0.05</td><td>22.7</td><td>18.6</td><td>16.2</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>7.40</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>291.HK (CRB)</td><td>O</td><td>HKD</td><td>23.88</td><td>47.50</td><td>(41.3)%</td><td>CNY</td><td>1.80</td><td>2.00</td><td>2.17</td><td>11.5</td><td>10.3</td><td>9.5</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>46.00</td><td></td><td></td><td></td><td>1.98</td><td></td><td></td><td></td><td></td></tr><tr><td>168.HK (Tsingtao)</td><td>O</td><td>HKD</td><td>45.80</td><td>69.00</td><td>(42.3)%</td><td>CNY</td><td>3.36</td><td>3.43</td><td>3.51</td><td>11.8</td><td>11.5</td><td>11.3</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>71.00</td><td></td><td></td><td></td><td>3.53</td><td>3.60</td><td></td><td></td><td></td></tr><tr><td>600600.CH (Tsingtao)</td><td>M</td><td>CNY</td><td>53.85</td><td>60.00</td><td>(50.6)%</td><td>CNY</td><td>3.36</td><td>3.43</td><td>3.51</td><td>16.0</td><td>15.7</td><td>15.3</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>62.00</td><td></td><td></td><td></td><td>3.53</td><td>3.60</td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,907.19</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate CRBeer Outperform with a Price Target of HK\$47.5 (from HK\$46.0 before), as we have raised our FY26E EPS by 1% to reflect H1 strength, while maintaining our multiple target at 18.5x NTM P/E. Model: 291.HK

We rate Tsingtao H-Share Outperform with a Price Target of HK\$69 and Tsingtao's A-share Market-Perform with a Price Target of RMB60 (from HK\$71 and RMB62 before), as we have cut our EPS estimates by \~3% to reflect this weak Q2, while maintaining our multiple target at 17.0x NTM P/E. Model: 168.HK

We rate Bud APAC Market-Perform with a Price Target of HK\$7.30 (from HK\$7.40 before). We have cut our EPS estimates by \~1% to reflect this weak Q2. We maintain our multiple target at 17.5x NTM P/E Model: 1876.HK

## DETAILS

EXHIBIT 1: Our regressions now indicate that CRBeer's topline growth will accelerate to c. 2% in H1, Bud China's decline will narrow to c. -3% in Q2, and Tsingtao's to widen to c. -3% based on our regression formulae and the Q2/H1 to date monthly sales

China Beer Q1 Actual & Q2 Regression-based Revenue YoY % Est.

![](images/972a34d43678be98de0ae84e88b3d5244d57fb9febb1fa261f7a7a8eb81f5240.jpg)  
Regression is based on H1 for CRBeer and Q2 for the rest; CRBeer's two bars are 2H25 actual and 1H26 est. based on regression Source: BigOne Lab, company reports, Bernstein analysis and estimates  
EXHIBIT 2: We see a 73-96% correlation between BigOne Lab quarterly brewer value growth and reported revenue growth  
Regression R-square of BigOne National Sell-out Value YoY % vs Reported Beer Revenue YoY % (22Q3-26Q1)

![](images/6b127ed3d88eae9ae86e1027a42d8a18770ae8740b3ff54e5ca78cc1cbf426f2.jpg)  
CRBeer reports semi-annually  
Source: BigOne Lab, company reports, Bernstein analysis

## MONTHLY OVERVIEW

Our BigOne Lab China beer data set leverages the POS sell-out data to track 180k supermarket stores and menu QR code data for 230k restaurant outlets nationally, allowing us to track brewer sell-out value performance by province and price segment on a monthly basis. The data set does not cover the nightlife channel, however.

In June 2026 we saw 3-month rolling overall national beer value growth remain at +2% in the period ending June 30 (Exhibit 3). On a standalone basis, June value growth moderated to +1% YoY from +2% in May, as restaurant channel growth slowed while off-trade continued to improve. By brewer, Yanjing (not covered) remained the strongest performer with value growth accelerating to +15% YoY, followed by CRBeer at +6%, while Chongqing slowed to +1%. Tsingtao's decline narrowed to -1%, whereas Bud China deteriorated further to -4%, remaining the weakest performer among major brewers.

Looking ahead, July comparisons become tougher for CRBeer and Bud China but notably easier for Tsingtao, while Chongqing also faces a softer comparison base (Exhibit 14).

EXHIBIT 3: National beer value growth moderated slightly to +1% in June 2026

China Total Beer Value Growth (Rolling 3-month / Monthly YoY %)  
![](images/0f19f8457b6c00331f52a9b3e3dd9d43fac25c7021837f28229d8e50433adbfa.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 4: Restaurant channel growth slowed to +1% YoY in June despite soft comps  
China Restaurant Beer Value Growth Monthly YoY %  
![](images/a7668cc01aff35f64c95f0b2f335c6ff143f42293ff81dcfb14d963cf6da15cd.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 5: Off-trade value growth improved further to +2% YoY in June  
China Off-Trade Beer Value Growth Monthly YoY %  
![](images/b34e7c6d60466c8054f22d6ac722ef188872ffd06b5124168048de91f1d77f62.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 6: Yanjing strengthened in Q2 while Bud China remained in decline but narrowing  
China Total Beer Value Growth YoY% by Brewer  
![](images/68daae0470fde4e146318abef3f07da06ade6bef6636ea866fbf79904a0a87b9.jpg)  
Bernstein does not cover Yanjing or Chongqing Source: BigOne Lab, Bernstein analysis  
EXHIBIT 7: Value growth accelerated for CRBeer and Yanjing while Bud weakened further in June

China Total Beer Value Growth YoY% by Brewer  
![](images/bc09c5aacda0990d0d13cfb6796f7e1b8462077e9b140ff97409b1041abb15e9.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 8: Yanjing continued to outperform across most segments while Bud underperformed in most segments apart from Premium and MS+

Beer Value YoY % in May 2026 by Segment by Brewer (Both Channel)

![](images/a33e0a81a88a549143392efd879d16c921284c9f5e4e72733bf75bb93f26fc87.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 9: Yanjing & CRBeer were top in share gains while Bud China's share loss narrowed in Q2  
China Total Beer Value Share Gain/Loss (YoY in bps)

![](images/408e29e4be5057ae778100618aaf45177a7ea6d8cb39f26d359f915dd9bfdbc7.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 10: CRBeer and Yanjing gained further share in June while Bud continued to lose share  
China Total Beer Value Share Gain/Loss (YoY in bps)

![](images/88e793be3147a6719e23fa9dab6b1897d444bf5245211cdc174942bde710d3e4.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 11: At the national level CRBeer gained share across most segments while Bud China lost share broadly in June  
June '26 National Segment Share Gain/Loss in bps YoY  
![](images/304c39fdd2d22aefa0da85e5f528f85e27c8c0306fa0e998f7dc4a9b2504b0af.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 12: In the off-trade channel CRBeer gained the most share while Bud China was maintaining its share in MS+  
June '26 National Off-Trade Segment Share Gain/Loss in bps YoY

![](images/1ee5114c4af3db87efb1311091d3660e6ec47e7b49888f09a55e6793c16ebec4.jpg)  
Source: BigOne Lab, Bernstein analysis  
EXHIBIT 13: Restaurant channel share gains were concentrated in CRBeer and Yanjing in June  
June '26 National Restaurant Segment Share Gain/Loss in bps YoY

![](images/4c98654796e95eef216400819fd8b3744422f38fa403ef4f43071c035edbc4cc.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 14: July comps become tougher for Tsingtao and CRBeer but extremely soft for Bud China
Forthcoming Comps - China Total Beer Value Growth YoY% by Brewer  
![](images/b7bda48d6db7b41329caf4c2017253d580c6fe84c75e93bcf64c4bae2f45ffbd.jpg)  
Source: BigOne Lab, Bernstein analysis

EXHIBIT 15: Guangdong remained strongest in June while Shandong continued to lag and Premium growth moderated

<table><tr><td rowspan="3" colspan="2"></td><td rowspan="3">Wtg in FY25 National Value</td><td colspan="4">Combined CHANNELS</td></tr><tr><td colspan="4">Brewer&#x27;s Value Growth YoY %</td></tr><tr><td>Apr-2026</td><td>May-2026</td><td>Jun-2026</td><td>Last 3m Avg</td></tr><tr><td rowspan="7">By Province</td><td>Guangdong</td><td>17%</td><td>16%</td><td>17%</td><td>9%</td><td>14%</td></tr><tr><td>Fujian</td><td>5%</td><td>1%</td><td>0%</td><td>-4%</td><td>-1%</td></tr><tr><td>Zhejiang</td><td>7%</td><td>-2%</td><td>11%</td><td>5%</td><td>5%</td></tr><tr><td>Jiangsu</td><td>6%</td><td>-6%</td><td>5%</td><td>5%</td><td>2%</td></tr><tr><td>Shandong</td><td>12%</td><td>-11%</td><td>-14%</td><td>-11%</td><td>-12%</td></tr><tr><td>Others</td><td>53%</td><td>1%</td><td>0%</td><td>2%</td><td>1%</td></tr><tr><td>Total</td><td></td><td>1%</td><td>2%</td><td>1%</td><td>2%</td></tr><tr><td rowspan="5">By Segment</td><td>Super Premium</td><td>5%</td><td>-18%</td><td>-10%</td><td>-14%</td><td>-13%</td></tr><tr><td>Premium</td><td>42%</td><td>4%</td><td>5%</td><td>3%</td><td>5%</td></tr><tr><td>Mainstream+</td><td>28%</td><td>3%</td><td>0%</td><td>2%</td><td>2%</td></tr><tr><td>M/S &amp; Eco</td><td>26%</td><td>-2%</td><td>2%</td><td>1%</td><td>-1%</td></tr><tr><td>Total</td><td></td><td>1%</td><td>2%</td><td>1%</td><td>2%</td></tr></table>

Source: BigOne Lab, Bernstein analysis

EXHIBIT 16: National monthly growth diagnostic by Province and Segment and Channel

<table><tr><td rowspan="3" colspan="2"></td><td colspan="5">RESTAURANT CHANNEL</td><td colspan="5">OFF-TRADE CHANNEL</td></tr><tr><td rowspan="2">Wtg in FY25 National Value</td><td colspan="4">Brewer&#x27;s Value Growth YoY %</td><td rowspan="2">Wtg in FY25 National Value</td><td colspan="4">Brewer&#x27;s Value Growth YoY %</td></tr><tr><td>Apr-2026</td><td>May-2026</td><td>Jun-2026</td><td>Last 3m Avg</td><td>Apr-2026</td><td>May-2026</td><td>Jun-2026</td><td>Last 3m Avg</td></tr><tr><td rowspan="7">By Province</td><td>Guangdong</td><td>15%</td><td>22%</td><td>20%</td><td>11%</td><td>17%</td><td>19%</td><td>10%</td><td>14%</td><td>7%</td><td>11%</td></tr><tr><td>Fujian</td><td>5%</td><td>3%</td><td>1%</td><td>-2%</td><td>0%</td><td>4%</td><td>-3%</td><td>0%</td><td>-5%</td><td>-3%</td></tr><tr><td>Zhejiang</td><td>7%</td><td>3%</td><td>12%</td><td>4%</td><td>6%</td><td>8%</td><td>-7%</td><td>11%</td><td>5%</td><td>4%</td></tr><tr><td>Jiangsu</td><td>5%</td><td>1%</td><td>4%</td><td>8%</td><td>5%</td><td>7%</td><td>-11%</td><td>5%</td><td>2%</td><td>-1%</td></tr><tr><td>Shandong</td><td>16%</td><td>-16%</td><td>-20%</td><td>-16%</td><td>-18%</td><td>8%</td><td>0%</td><td>1%</td><td>-1%</td><td>0%</td></tr><tr><td>Others</td><td>52%</td><td>4%</td><td>5%</td><td>4%</td><td>4%</td><td>54%</td><td>-3%</td><td>-5%</td><td>0%</td><td>-3%</td></tr><tr><td>Total</td><td></td><td>3%</td><td>3%</td><td>1%</td><td>2%</td><td></td><td>-1%</td><td>1%</td><td>2%</td><td>1%</td></tr><tr><td rowspan="5">By Segment</td><td>Super Premium</td><td>6%</td><td>-23%</td><td>-16%</td><td>-18%</td><td>-19%</td><td>3%</td><td>-6%</td><td>5%</td><td>8%</td><td>3%</td></tr><tr><td>Premium</td><td>50%</td><td>9%</td><td>8%</td><td>5%</td><td>7%</td><td>33%</td><td>-3%</td><td>1%</td><td>2%</td><td>0%</td></tr><tr><td>Mainstream+</td><td>32%</td><td>4%</td><td>2%</td><td>2%</td><td>3%</td><td>23%</td><td>3%</td><td>-2%</td><td>3%</td><td>1%</td></tr><tr><td>M/S &amp; Eco</td><td>12%</td><td>-8%</td><td>-4%</td><td>-4%</td><td>-5%</td><td>41%</td><td>-2%</td><td>3%</td><td>0%</td><td>1%</td></tr><tr><td>Total</td><td></td><td>3%</td><td>3%</td><td>1%</td><td>2%</td><td></td><td>-1%</td><td>1%</td><td>2%</td><td>1%</td></tr></table>

Source: BigOne Lab, Bernstein analysis

## OFF-TRADE / RESTAURANT CHANNEL MOMENTUM BY BREWER

## BUD CHINA

Guangdong and Zhejiang remained the largest contributors to Bud China's res

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
