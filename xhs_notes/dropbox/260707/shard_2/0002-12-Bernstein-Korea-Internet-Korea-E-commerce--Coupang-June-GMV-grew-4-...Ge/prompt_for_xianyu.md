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
Korea Internet

# Korea E-commerce: Coupang June GMV grew 4%...Getting richer doesn't mean buying groceries twice

![](images/09a81ff5b6bdd7f7a2a30c8e82dac82f2f54bbae3ec589cbb1cf0504b5800d55.jpg)  
Min-Joo Kang  
+852 2123 2644

minjoo.kang@bernsteinsg.com

![](images/635216eb8e611b2eadcaf5fa289bb828133215c7123281dce723cd1d1d0a894e.jpg)

Robin Zhu

+852 2123 2659

robin.zhu@bernsteinsg.com

![](images/c38936611b328f1ddb383c057320d53df0d26b7026ffdab06cd3e1390c763a4c.jpg)

Charles Gou

+852 2123 2618

![](images/f79a10e823fc29ca488e68ad927d9a9d2dc3b61fe1257281d059c2423891fdd0.jpg)

charles.gou@bernsteinsg.com

Hyrum Caesar

+81 3 6777 6979

hyrum.caesar@bernsteinsg.com

We share our June GMV update across major e-commerce and food delivery platforms, together with the latest May market data. Recently, investor discussions have centered on one question: Will Coupang benefit as Koreans become wealthier? We believe this is the wrong lens through which to view the opportunity. Instead, the key issue is how spending patterns are evolving within Korea's increasingly polarized consumer landscape. In this note, we outline our views on the Korean retail market and assess the respective growth runways for Coupang and Naver.

Korea is getting richer, but not equally. Korea's affluent population continues to expand. The number of high-net-worth individuals (HNWIs) reached 576k in 2025 (+3.3% YoY), while their share of the population increased to 0.9% from 0.7% in 2020. At the same time, wealth concentration is accelerating: the top decile now accounts for 46.1% of national net wealth in 2025, up 1.6ppt YoY, while the highest income quintile captured 45.2% of household income in Q1 2026, up 0.8ppt YoY. These trends point to an increasingly pronounced K-shaped economy.

Premium spending is flowing to department stores, not groceries. Affluent consumers do not simply buy more everyday necessities. Instead, incremental spending is increasingly concentrated in premium and luxury brands such as Chanel, Van Cleef & Arpels, and Cartier. Semi-durable goods such as fashion continue to outgrow most retail categories, while department stores (+19% YoY in May) are consistently outperforming hypermarkets (-7% YoY in May) despite serving a narrower customer base. In other words, rising wealth benefits premium retail channels more than mass-market grocery platforms.

June data suggests Coupang may be losing share. Coupang's GMV grew 4% YoY in June, according to Wiseapp data released on July 3. In comparison, Naver's GMV increased 14% YoY over the same period. Meanwhile, KOSIS online retail sales data, published on July 1, showed 9% YoY market growth (excl. food delivery and auto) in May. Given that Coupang delivered 10% YoY growth in May, the June result suggests that its growth has decelerated to only low single-digit levels above, or potentially below, overall market growth.

Naver's share gain story remains intact. Naver's stronger growth performance is being driven by its expanding Brand Store ecosystem, which is well positioned to capture demand in item categories such as semi-durable goods. As a result, Naver appears to be gaining share in higher-value merchandise categories where brand engagement and product discovery are key differentiators. Naver appears to be pulling ahead while remaining in full combat mode through aggressive pricing and 1P fulfillment investments (Link).

Baemin holds the line as Coupang Eats growth normalizes. In food delivery, Baemin (Delivery Hero, covered by Annick Maas) and Coupang Eats posted 10% and 12% YoY GTV growth, respectively, in June, while market shares remained broadly unchanged at 63% and 37%. With growth rates converging, Coupang Eats' share gain story appears to be maturing. The next key strategic question is whether Coupang Eats adopts a 3P marketplace model to expand beyond major metropolitan areas (Link).

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">2 Jul 2026</td><td colspan="2">TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">Rel. Perf.</td><td rowspan="2">Cur</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td></td></tr><tr><td>CPNG (Coupang)</td><td>U</td><td>USD</td><td>18.56</td><td>12.00</td><td>(57.9)%</td><td>USD</td><td>0.11</td><td>(0.38)</td><td>0.21</td><td>164.7</td><td>(49.0)</td><td>88.1</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>(0.37)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>035420.KS (Naver)</td><td>O</td><td>KRW</td><td>196,500</td><td>330,000</td><td>(59.3)%</td><td>KRW</td><td>13,065</td><td>14,068</td><td>15,783</td><td>15.0</td><td>14.0</td><td>12.5</td><td></td></tr><tr><td>OLD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>14,089</td><td>15,745</td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,483.24</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,977.84</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

## We rate Coupang Underperform and Naver Outperform.

We reiterate our view that in e-commerce, competition ultimately dictates margins. Naver remains firmly in combat mode in Commerce, with recent promotional activity appearing increasingly aggressive. In terms of incremental GMV growth, we believe Naver Brand Store ecosystem is better positioned to capture demand, potentially gaining share.

We trimmed our Coupang Q2 estimates to reflect: (1) c.4% YoY revenue growth, impacted by foreign exchange headwinds, and (2) the USD 410 million fine, which we expect to be recognized in Q2 OG&A, reducing operating profit and EPS. We modelled Q2 adjusted EBITDA margin at 2%, in line with management's guidance from the previous earnings call for a consolidated adjusted EBITDA margin contraction of approximately 300-400 bps YoY.

We revised our Naver 2026-2027 EPS estimates slightly due to changes in non-operating costs.

## VALUATION COMPS TABLE

EXHIBIT 1: Asia Internet: valuation summary

<table><tr><td></td><td>Rating</td><td>Price target</td><td>Last price</td><td>Crncy</td><td>Market cap (US$mn)</td><td>2026E</td><td>PE 2027E</td><td>2028E</td><td>2026E</td><td>EV/sales 2027E</td><td>2028E</td></tr><tr><td colspan="12">China Internet coverage</td></tr><tr><td>Tencent</td><td>O</td><td>780</td><td>447.60</td><td>HKD</td><td>518,934</td><td>13.0x</td><td>11.2x</td><td>9.7x</td><td>4.3x</td><td>3.7x</td><td>3.2x</td></tr><tr><td>PDD</td><td>M</td><td>110</td><td>82.39</td><td>USD</td><td>117,274</td><td>7.6x</td><td>6.8x</td><td>6.1x</td><td>0.6x</td><td>0.4x</td><td>0.1x</td></tr><tr><td>Meituan</td><td>M</td><td>85</td><td>74.00</td><td>HKD</td><td>58,264</td><td>165.7x</td><td>15.3x</td><td>8.9x</td><td>0.8x</td><td>0.6x</td><td>0.5x</td></tr><tr><td>NetEase</td><td>O</td><td>150</td><td>127.24</td><td>USD</td><td>81,195</td><td>14.0x</td><td>13.0x</td><td>12.4x</td><td>3.3x</td><td>3.1x</td><td>2.9x</td></tr><tr><td>Boss Zhipin</td><td>O</td><td>18</td><td>13.00</td><td>USD</td><td>6,154</td><td>10.5x</td><td>8.7x</td><td>7.8x</td><td>2.3x</td><td>1.6x</td><td>1.1x</td></tr><tr><td>JD</td><td>O</td><td>40</td><td>26.62</td><td>USD</td><td>36,358</td><td>8.6x</td><td>6.3x</td><td>4.8x</td><td>0.2x</td><td>0.2x</td><td>0.2x</td></tr><tr><td>Alibaba</td><td>O</td><td>180</td><td>96.14</td><td>USD</td><td>230,812</td><td>24.1x</td><td>14.1x</td><td>12.0x</td><td>1.6x</td><td>1.5x</td><td>1.4x</td></tr><tr><td colspan="12">China Internet other</td></tr><tr><td>Kuaishou</td><td></td><td></td><td>45.58</td><td>HKD</td><td>25,148</td><td>10.5x</td><td>9.3x</td><td>8.1x</td><td>1.0x</td><td>0.9x</td><td>0.9x</td></tr><tr><td>Bilibili</td><td></td><td></td><td>17.14</td><td>USD</td><td>7,285</td><td>16.8x</td><td>13.3x</td><td>10.2x</td><td>1.1x</td><td>1.0x</td><td>0.9x</td></tr><tr><td>TME</td><td></td><td></td><td>8.63</td><td>USD</td><td>14,339</td><td>9.1x</td><td>8.1x</td><td>7.4x</td><td>1.8x</td><td>1.7x</td><td>1.5x</td></tr><tr><td>Baidu</td><td></td><td></td><td>113.30</td><td>USD</td><td>38,551</td><td>14.2x</td><td>12.7x</td><td>10.3x</td><td>1.1x</td><td>1.0x</td><td>0.9x</td></tr><tr><td>VIPshop</td><td></td><td></td><td>13.26</td><td>USD</td><td>6,368</td><td>5.1x</td><td>5.0x</td><td>4.8x</td><td>0.2x</td><td>0.2x</td><td>0.2x</td></tr><tr><td>Tencent Music</td><td></td><td></td><td>8.63</td><td>USD</td><td>14,339</td><td>9.1x</td><td>8.1x</td><td>7.4x</td><td>1.8x</td><td>1.7x</td><td>1.5x</td></tr><tr><td>Trip.com</td><td></td><td></td><td>41.00</td><td>USD</td><td>25,818</td><td>11.6x</td><td>10.0x</td><td>9.0x</td><td>1.9x</td><td>1.7x</td><td>1.5x</td></tr><tr><td>KE Holdings</td><td></td><td></td><td>15.09</td><td>USD</td><td>17,464</td><td>16.1x</td><td>13.7x</td><td>13.5x</td><td>1.0x</td><td>0.9x</td><td>0.9x</td></tr><tr><td colspan="12">Asian Internet</td></tr><tr><td>Naver</td><td>O</td><td>330,000</td><td>195,700</td><td>KRW</td><td>20,023</td><td>13.9x</td><td>12.4x</td><td>10.8x</td><td>1.5x</td><td>1.1x</td><td>0.8x</td></tr><tr><td>Kakao</td><td>O</td><td>80,000</td><td>35,550</td><td>KRW</td><td>10,269</td><td>20.0x</td><td>17.7x</td><td>14.5x</td><td>1.0x</td><td>0.8x</td><td>0.5x</td></tr><tr><td>Hybe</td><td>O</td><td>400,000</td><td>215,000</td><td>KRW</td><td>6,043</td><td>21.4x</td><td>21.1x</td><td>17.3x</td><td>1.4x</td><td>1.5x</td><td>1.3x</td></tr><tr><td>Coupang</td><td>U</td><td>12</td><td>18.56</td><td>USD</td><td>33,316</td><td>-49.0x</td><td>88.1x</td><td>42.8x</td><td>0.8x</td><td>0.7x</td><td>0.7x</td></tr><tr><td>Sea Ltd.</td><td></td><td></td><td>103.30</td><td>USD</td><td>63,270</td><td>27.8x</td><td>20.3x</td><td>16.0x</td><td>1.9x</td><td>1.5x</td><td>1.3x</td></tr><tr><td>Grab</td><td></td><td></td><td>3.90</td><td>USD</td><td>15,992</td><td>39.4x</td><td>26.2x</td><td>19.5x</td><td>2.8x</td><td>2.4x</td><td>2.0x</td></tr><tr><td colspan="12">US Internet</td></tr><tr><td>Amazon</td><td></td><td></td><td>242.67</td><td>USD</td><td>2,610,428</td><td>23.7x</td><td>21.1x</td><td>17.1x</td><td>3.3x</td><td>2.9x</td><td>2.6x</td></tr><tr><td>Alphabet</td><td></td><td></td><td>359.91</td><td>USD</td><td>4,359,726</td><td>25.2x</td><td>23.5x</td><td>19.6x</td><td>10.1x</td><td>8.5x</td><td>7.1x</td></tr><tr><td>Meta</td><td></td><td></td><td>582.90</td><td>USD</td><td>1,479,647</td><td>14.7x</td><td>15.2x</td><td>12.5x</td><td>5.9x</td><td>4.9x</td><td>4.2x</td></tr><tr><td>Netflix</td><td></td><td></td><td>77.65</td><td>USD</td><td>326,969</td><td>22.1x</td><td>20.2x</td><td>16.9x</td><td>6.4x</td><td>5.8x</td><td>5.2x</td></tr><tr><td>Uber</td><td></td><td></td><td>74.43</td><td>USD</td><td>151,510</td><td>22.7x</td><td>16.7x</td><td>13.6x</td><td>2.7x</td><td>2.4x</td><td>2.1x</td></tr><tr><td>Spotify</td><td></td><td></td><td>485.97</td><td>USD</td><td>100,028</td><td>33.1x</td><td>26.8x</td><td>22.0x</td><td>4.1x</td><td>3.6x</td><td>3.2x</td></tr><tr><td>DoorDash</td><td></td><td></td><td>192.01</td><td>USD</td><td>83,662</td><td>41.6x</td><td>28.1x</td><td>21.6x</td><td>4.6x</td><td>3.8x</td><td>3.2x</td></tr></table>

Pricing date July 6, 2026. The valuation multiples of our China and Asian Internet coverage are based on Bernstein estimates; the other companies shown reflect Bloomberg consensus estimates.  
Source: Corporate reports, Bloomberg, Bernstein estimates and analysis.

## DETAILS

## KEY CHARTS

EXHIBIT 2: Coupang's GMV grew 3.9% in June, meanwhile Naver outpaced it with 14% growth.  
2022-2026: Korea E-Commerce Monthly GMV growth trend  
![](images/87c02c82d092c2f2bc9cbe0f492813e96b21d09aa550e3acf99f4d1395e24a0e.jpg)  
Source: Wiseapp, Bernstein analysis.  
EXHIBIT 3: Baemin and Coupang Eats posted YoY GTV growth of 10% and 11.8%, respectively, in June 2026. With growth rates converging, Coupang Eats' outsized top-line growth story in food delivery appears largely played out.

2022-2026: Korea Food Delivery Monthly GTV growth trend  
![](images/a207db0b940612d6573e71ee1bd1deca50c1f95fe9949b2cb8a53c825ab1d9ba.jpg)  
Source: Wiseapp, Bernstein analysis.

## COUPANG JUNE GMV GREW 4%...GETTING RICHER DOESN'T MEAN BUYING GROCERIES TWICE

EXHIBIT 4: The number of high-net-worth individuals (HNWIs) in Korea increased 3.3% YoY to 576,000 in 2025, while the share of HNWIs in the total population rose to 0.9%, up from 0.7% in 2020.

The number of high-net-worth individuals (HNWIs) in Korea ('000)

![](images/d668df1229dc92aed7d878db59049bac809605834420db218e63c443a54d71b5.jpg)  
Source: KB Bank, Bernstein analysis.  
EXHIBIT 5: The top decile accounted for 46.1% of total net wealth in 2025, up 1.6%p YoY, suggesting that wealth polarization in Korea continues to deepen.

2017-2025: Net Wealth Share of the 10th Decile  
![](images/32778187bdd81501043244a23ebd75b952681523c05d3deda35269941381417e.jpg)  
Source: KOSTAT, Bernstein analysis.

EXHIBIT 6: For household income in Korea, the income share of the fifth quintile rose to 45.2%, up 0.8%p YoY, while the income share of the bottom quintile remained flat in Q1 2026.  
2021-2026: Income Share by Quintile  
![](images/2a9ab8159e1614ad69a86212bc916e94e8c16e797a622bc89db7dc6ae4855887.jpg)  
5th Quintile 4th Quintile 3rd Quintile 2nd Quintile 1st Quintile  
Source: KOSTAT, Bernstein analysis.

EXHIBIT 7: Within the overall retail market, semi-durable goods (i.e., fashion) are outgrowing other product categories.  
2023-2026: Quarterly household consumption expenditure by product category  
![](images/878a7e565989b0f23f0743ea1f8af0e333f6195364fba14e42f48a961db4f31d.jpg)  
Source: KOSTAT, Bernstein analysis.

EXHIBIT 8: Among retail channels, department stores are outperforming hypermarkets in growth, despite the latter being the preferred shopping destination for middle-income consumers.  
2023-2026: Monthly YoY GMV growth in Korea's retail market  
![](images/d170cda7baf50d54a086698c2e149f65bd77d931adf6bf7b172f69edd674897e.jpg)  
Source: KOSIS, Bernstein analysis.

EXHIBIT 9: The Korean e-commerce market grew 9% in May 2026.  
2017-2026: Korea e-Commerce market  
![](images/11a476f05f5367d4ed5c269931f7c185259960a6b01c14b087340d247519958d.jpg)  
Note: Korea e-commerce market sizing approach: We estimate the market using KOSIS data, excluding the auto and food-delivery sectors. Source: KOSIS, Bernstein analysis.

EXHIBIT 10: Item goods (i.e., fashion) category penetration remains below the overall online penetration rate of the Korean e-commerce market.  
2022-2026: Online penetration rate by category  
![](images/7c28bfa246500bb0d1be4baccf3f181e633639d86ca8a039c487d77d883e8dbe.jpg)  
Item (Fashion & Beauty, Living & Healthcare) Grocery (Fresh foods, Packaged foods) Commodity (Daily necessities, Electronics) Total retail (ex.auto and gas)  
Source: KOSIS, Bernstein analysis.  
EXHIBIT 11: KOSIS online GMV trends indicate that, entering 2026, incremental GMV growth is coming from item goods and grocery categories.  
5M 2026: Korea e-commerce and food delivery GMV growth by category

![](images/aac9ee3c8aaaa7ed1ae405850554f1d9805fb72c77290386a456f1b3abf2c896.jpg)  
Source: KOSIS, Bernstein analysis.

EXHIBIT 12: Naver's GMV outperformance is primarily driven by its strong Brand Stor

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
