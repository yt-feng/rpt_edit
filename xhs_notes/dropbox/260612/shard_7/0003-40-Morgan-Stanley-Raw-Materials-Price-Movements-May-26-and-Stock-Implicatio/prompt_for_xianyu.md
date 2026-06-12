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
# China Consumer: Raw Materials Price Chartbook | Asia Pacific

# Raw Materials Price Movements (May-26) and Stock Implications

In last month's summary of key raw material price trends and implications for relevant Hong Kong/China consumer stocks, we highlight the uptick in tin and copper prices, while PET and gold prices declined.

## Implications for stocks

Yili (600887.SS, OW), Mengniu (2319.HK, OW): We expect raw milk prices to gradually stabilize in 2026, and we see more balanced supply-demand dynamics in 2026. Both Mengniu and Yili target liquid milk to resume growth in 2026, and expect market share gains from smaller players amid potential recovery of raw milk prices. On the other hand, provisions for inventory will likely be largely reduced in 2026, which should benefit net margin.

WH Group (288.HK, OW): Unit returns for packaged meat could remain elevated amid lower hog prices in China, which reduce raw material costs for downstream operations – the company's core business in the market. In the US, upstream operations benefit from sustained high hog prices, while downstream businesses continue to improve product mix and operating efficiency.

More on the next page...

MS ASIA LIMITED+

## Lillian Lou

Equity Analyst

Lillian.Lou@morganstanley.com +852 2848-6502

## Dustin Wei

Equity Analyst

Dustin.Wei@morganstanley.com +852 2239-7823

MS TAIWAN LIMITED+

## Terence Cheng

Equity Analyst

Terence.Cheng@morganstanley.com +886 2 2730-2873

MS ASIA LIMITED+

## Hildy Ling

Equity Analyst

Hildy.Ling@morganstanley.com +852 2239-7834

## Jenny Yu

Research Associate

Jenny.Yu1@morganstanley.com +852 3963-1925

MS TAIWAN LIMITED+

## Jenny Ting

Research Associate

Jenny.Ting@morganstanley.com +886 2 2730-2995

MS ASIA LIMITED+

## Carlos Liu, CFA

Research Associate

Carlos.Liu@morganstanley.com +852 2848-5206

## Asia Summer School 2026

![](images/e5e7eb790fb6b02b6d46eaaf87554509ed3631963c7d001290951172b6357c1e.jpg)

## CHINA/HONG KONG CONSUMER

Asia Pacific

Industry View In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Further implications for stocks

![](images/3d2f119ed4b47b325747eb4331b27f65ccb2a6302653f3ccbb1c681c3633974b.jpg)

= Muyuan (002714.SZ/2714.HK, OW): Despite near-term earnings pressure, a continued decline in hog prices should accelerate industry capacity rationalization and bring forward a price inflection, which we expect around mid-2026. As the industry leader, we believe Muyuan is well positioned to benefit and capture greater upside once hog prices recover.

= Eastroc (605499.SS/9980.HK, OW): Eastroc benefits from lock-in of PET costs for full-year 2026 and sugar cost for \~six months at prices below last year's level. Energy drink and Water Boost growth momentum as well as other key SKUs performance are the keys to watch amid intense market competition.

=/- Tingyi (0322.HK, EW) and Uni-President China (0220.HK, EW): Beverages – PET prices stay elevated alongside rising oil prices. We expect pressure to emerge from late 2Q-3Q onward on Tingyi and UPC's beverage segment margins. Noodles – Higher palm oil and wheat prices could weigh on margins but should be largely manageable, in our view. Competitive dynamics going into summer peak in the beverage segment remain a key determinant of performance in 2026.

= Beer companies (1876.HK, 0291.HK, 0168.HK, 600600.SS, 600132.SS, 000729.SZ): Overall cost pressure remains manageable, in our view, as other raw material costs have stayed relatively steady despite higher aluminum prices. We expect improved ASP trends – driven by a more favorable channel mix, reduced consumer promotions, and a shift toward mid-range products – to offset the impact.

=Laopu (6181.HK, OW): Gold price decline might drag consumer demand for fixed price gold jewelry products, which Laopu is 100% exposed to. This could be partially offset by improving margin given lower raw material costs. Stock sentiment might remain under pressure in near-term as capital market turn skeptical on demand vs. long-term growth potential via brand building.

## China Consumer: Order of Preference

Exhibit 1: China Consumer: Order of Preference

<table><tr><td></td><td>Yili 600887.SS</td><td>Mengniu 2319.HK</td><td>WH 0288.HK</td><td>Laopu 6181.HK</td><td>Muyuan 002714.SZ</td><td>Eastroc 605499.SS</td><td>CRB 0291.HK</td><td>Bud APAC 1876.HK</td><td>Tsingtao 600600.SS</td><td>UPC 0220.HK</td><td>Tingyi 0322.HK</td><td>Yanjing 000729.SZ</td><td>Chongqing 600132.SS</td></tr><tr><td>Rating</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Overweight</td><td>Equal-Weight</td><td>Equal-Weight</td><td>Equal-Weight</td><td>Underweight</td><td>Underweight</td></tr><tr><td>Reporting Currency</td><td>CNY</td><td>CNY</td><td>USD</td><td>CNY</td><td>CNY</td><td>CNY</td><td>CNY</td><td>USD</td><td>CNY</td><td>CNY</td><td>CNY</td><td>CNY</td><td>CNY</td></tr><tr><td>Trading Currency</td><td>CNY</td><td>HKD</td><td>HKD</td><td>HKD</td><td>CNY</td><td>CNY</td><td>HKD</td><td>HKD</td><td>CNY</td><td>HKD</td><td>HKD</td><td>CNY</td><td>CNY</td></tr><tr><td>Price Target</td><td>33.00</td><td>20.00 HKD</td><td>12.70 HKD</td><td>1,010.00 HKD</td><td>57.00</td><td>223.00</td><td>35.00 HKD</td><td>9.00 HKD</td><td>66.00</td><td>9.20 HKD</td><td>13.50 HKD</td><td>10.90</td><td>42.00</td></tr><tr><td>Current Price</td><td>25.12</td><td>16.12</td><td>8.79</td><td>456.40</td><td>34.23</td><td>133.20</td><td>23.32</td><td>6.87</td><td>59.59</td><td>7.45</td><td>11.75</td><td>11.14</td><td>48.70</td></tr><tr><td>Upside /(Downside) %</td><td>31%</td><td>24%</td><td>44%</td><td>121%</td><td>67%</td><td>67%</td><td>50%</td><td>31%</td><td>11%</td><td>23%</td><td>15%</td><td>-2%</td><td>-14%</td></tr><tr><td>Market Cap (US$ mn)</td><td>22,696 USD</td><td>7,982 USD</td><td>14,397</td><td>9,063 USD</td><td>52,598 USD</td><td>26,490 USD</td><td>9,658 USD</td><td>11,595</td><td>10,356 USD</td><td>4,108 USD</td><td>8,455 USD</td><td>4,629 USD</td><td>3,475 USD</td></tr><tr><td>Average Daily Traded Vol (US$mn)</td><td>198.3</td><td>48.8</td><td>43.9</td><td>95.6</td><td>308.3</td><td>125.4</td><td>34.1</td><td>14.1</td><td>51.5</td><td>11.6</td><td>27.2</td><td>67.9</td><td>35.5</td></tr><tr><td>Bull Case Value</td><td>39.00</td><td>26.00 HKD</td><td>14.00 HKD</td><td>1,675.00 HKD</td><td>74.00</td><td>271.00</td><td>41.00 HKD</td><td>10.90 HKD</td><td>104.00</td><td>13.90 HKD</td><td>17.60 HKD</td><td>18.70</td><td>71.00</td></tr><tr><td>Upside %</td><td>55%</td><td>61%</td><td>59%</td><td>267%</td><td>116%</td><td>103%</td><td>76%</td><td>59%</td><td>75%</td><td>87%</td><td>50%</td><td>68%</td><td>46%</td></tr><tr><td>Bear Case Value</td><td>18.00</td><td>10.40 HKD</td><td>8.00 HKD</td><td>550.00 HKD</td><td>23.00</td><td>119.00</td><td>20.00 HKD</td><td>5.20 HKD</td><td>46.00</td><td>6.30 HKD</td><td>7.30 HKD</td><td>8.70</td><td>35.00</td></tr><tr><td>Downside %</td><td>-28%</td><td>-35%</td><td>-9%</td><td>21%</td><td>-33%</td><td>-11%</td><td>-14%</td><td>-24%</td><td>-23%</td><td>-15%</td><td>-38%</td><td>-22%</td><td>-28%</td></tr><tr><td>Risk/Reward Skew</td><td>1.95</td><td>1.73</td><td>6.59</td><td>-13.02</td><td>3.54</td><td>9.70</td><td>5.33</td><td>2.41</td><td>3.27</td><td>5.61</td><td>1.31</td><td>3.10</td><td>1.63</td></tr><tr><td colspan="14">MS Estimates</td></tr><tr><td colspan="14">FY26e</td></tr><tr><td>Sales</td><td>120,192 e</td><td>86,795 e</td><td>29,140 e</td><td>42,263 e</td><td>130,538 e</td><td>26,050 e</td><td>39,778 e</td><td>5,909 e</td><td>33,156 e</td><td>33,244 e</td><td>81,362 e</td><td>14,787 e</td><td>13,896 e</td></tr><tr><td>Net Profit</td><td>12,321 e</td><td>4,784 e</td><td>1,668 e</td><td>8,080 e</td><td>15,153 e</td><td>5,807 e</td><td>6,056 e</td><td>640 e</td><td>4,917 e</td><td>2,185 e</td><td>4,446 e</td><td>1,810 e</td><td>1,260 e</td></tr><tr><td>EPS</td><td>1.95 e</td><td>1.23 e</td><td>0.12 e</td><td>45.81 e</td><td>2.63 e</td><td>7.91 e</td><td>1.87 e</td><td>0.05 e</td><td>3.60 e</td><td>0.51 e</td><td>0.79 e</td><td>0.64 e</td><td>2.60 e</td></tr><tr><td colspan="14">FY27e</td></tr><tr><td>Sales</td><td>126,514 e</td><td>90,398 e</td><td>30,096 e</td><td>49,626 e</td><td>143,737 e</td><td>31,937 e</td><td>41,604 e</td><td>6,117 e</td><td>34,894 e</td><td>34,645 e</td><td>83,613 e</td><td>15,380 e</td><td>14,070 e</td></tr><tr><td>Net Profit</td><td>13,366 e</td><td>5,376 e</td><td>1,727 e</td><td>9,463 e</td><td>27,334 e</td><td>6,865 e</td><td>6,631 e</td><td>707 e</td><td>5,411 e</td><td>2,431 e</td><td>4,759 e</td><td>1,916 e</td><td>1,327 e</td></tr><tr><td>EPS</td><td>2.11 e</td><td>1.38 e</td><td>0.13 e</td><td>53.66 e</td><td>4.74 e</td><td>9.35 e</td><td>2.04 e</td><td>0.05 e</td><td>3.97 e</td><td>0.56 e</td><td>0.84 e</td><td>0.68 e</td><td>2.74 e</td></tr><tr><td colspan="14">FY26e MSe vs. Consensus Mean</td></tr><tr><td>Sales</td><td>(1.0%)</td><td>0.4%</td><td>0.2%</td><td>(0.3%)</td><td>3.3%</td><td>1.3%</td><td>1.1%</td><td>(0.8%)</td><td>0.3%</td><td>(0.3%)</td><td>0.3%</td><td>(7.7%)</td><td>(6.7%)</td></tr><tr><td>Net Profit</td><td>(0.1%)</td><td>(3.6%)</td><td>0.4%</td><td>(3.7%)</td><td>115.8%</td><td>5.5%</td><td>3.7%</td><td>2.6%</td><td>2.1%</td><td>(0.9%)</td><td>(1.0%)</td><td>(9.3%)</td><td>(0.1%)</td></tr><tr><td>EPS</td><td>(0.1%)</td><td>(3.6%)</td><td>0.4%</td><td>(3.7%)</td><td>115.8%</td><td>5.5%</td><td>3.7%</td><td>2.6%</td><td>2.1%</td><td>(0.9%)</td><td>(1.0%)</td><td>(9.3%)</td><td>(0.1%)</td></tr><tr><td colspan="14">FY27e MSe vs. Consensus Mean</td></tr><tr><td>Sales</td><td>(0.6%)</td><td>0.4%</td><td>0.6%</td><td>(0.3%)</td><td>(5.1%)</td><td>4.7%</td><td>2.7%</td><td>(0.5%)</td><td>3.0%</td><td>(0.9%)</td><td>0.5%</td><td>(7.9%)</td><td>(7.5%)</td></tr><tr><td>Net Profit</td><td>0.2%</td><td>(2.4%)</td><td>0.1%</td><td>(3.4%)</td><td>(5.1%)</td><td>5.6%</td><td>6.3%</td><td>3.0%</td><td>6.6%</td><td>3.5%</td><td>(0.4%)</td><td>(16.0%)</td><td>0.8%</td></tr><tr><td>EPS</td><td>0.2%</td><td>(2.4%)</td><td>0.1%</td><td>(3.4%)</td><td>(5.1%)</td><td>5.6%</td><td>6.3%</td><td>3.0%</td><td>6.6%</td><td>3.5%</td><td>(0.4%)</td><td>(16.0%)</td><td>0.8%</td></tr></table>

Source: FactSet, MS estimates. Note: Current prices as of the market close on Jun 9, 2026.

## Key Charts of the Month

Exhibit 2: PET Prices (Weekly)  
![](images/7f02df9d321ecb89f1f157aeea3d89e88fabd4872dcba575fbb3a2511d77b66f.jpg)

<details>
<summary>line chart</summary>

| Date     | USD/MT | Volume (USD/barrel) |
|----------|--------|---------------------|
| May-19   | ~1,000 | ~135                |
| Nov-19   | ~900   | ~135                |
| May-20   | ~1,000 | ~135                |
| Nov-20   | ~1,200 | ~135                |
| May-21   | ~1,400 | ~135                |
| Nov-21   | ~1,300 | ~135                |
| May-22   | ~1,200 | ~135                |
| Nov-22   | ~1,100 | ~135                |
| May-23   | ~1,000 | ~135                |
| Nov-23   | ~950   | ~135                |
| May-24   | ~900   | ~135                |
| Nov-24   | ~850   | ~135                |
| May-25   | ~800   | ~135                |
| Nov-25   | ~750   | ~135                |
| May-26   | ~95    | ~135                |
</details>

Source: Bloomberg, MS.

Exhibit 3: Hog/Piglet/Pork Price (Weekly)  
![](images/4b57f51922558bf67d7bc33edd582ab308e24a6d0ffbdc4461a28884344d935f.jpg)

<details>
<summary>line chart</summary>

| Date    | Piglet Price | Pork Price (Retail) | Pork Price (Wholesale) | Hog Price |
|---------|--------------|---------------------|-------------------------|-----------|
| May-16  | ~40          | ~30                 | ~25                     | ~20       |
| Nov-16  | ~50          | ~35                 | ~30                     | ~25       |
| May-17  | ~45          | ~35                 | ~25                     | ~20       |
| Nov-17  | ~40          | ~30                 | ~25                     | ~15       |
| May-18  | ~35          | ~25                 | ~20                     | ~15       |
| Nov-18  | ~30          | ~20                 | ~15                     | ~10       |
| May-19  | ~40          | ~30                 | ~25                     | ~20       |
| Nov-19  | ~80          | ~60                 | ~50                     | ~40       |
| May-20  | ~110         | ~70                 | ~60                     | ~50       |
| Nov-20  | ~100         | ~65                 | ~55                     | ~45       |
| May-21  | ~85          | ~60                 | ~50                     | ~40       |
| Nov-21  | ~30          | ~25                 | ~20                     | ~15       |
| May-22  | ~40          | ~35                 | ~30                     | ~25       |
| Nov-22  | ~45          | ~40                 | ~35                     | ~30       |
| May-23  | ~40          | ~35                 | ~30                     | ~25       |
| Nov-23  | ~35          | ~30                 | ~25                     | ~20       |
| May-24  | ~40          | ~35                 | ~30                     | ~25       |
| Nov-24  | ~35          | ~30                 | ~25                     | ~20       |
| May-25  | ~30          | ~25                 | ~20                     | ~15       |
| Nov-25  | ~25          | ~20                 | ~15                     | ~10       |
| May-26  | ~20          | ~15                 | ~10                     | ~5        |
</details>

Source: Efeedlink, NDRC, MoC, MS.

Exhibit 4: Palm Oil Spot Price (Daily)  
![](images/f436d51525811c5ac67bc4501285b7740dae2b3b5010908fe1326311c1339b8b.jpg)

<details>
<summary>line chart</summary>

| Date    | FOB Malaysia | Tiajin Spot Price |
|---------|--------------|-------------------|
| May-16  | ~650         | ~700              |
| Nov-16  | ~700         | ~750              |
| May-17  | ~680         | ~730              |
| Nov-17  | ~670         | ~720              |
| May-18  | ~660         | ~710              |
| Nov-18  | ~650         | ~700              |
| May-19  | ~640         | ~690              |
| Nov-19  | ~630         | ~680              |
| May-20  | ~620         | ~670              |
| Nov-20  | ~610         | ~660              |
| May-21  | ~600         | ~650              |
| Nov-21  | ~590         | ~640              |
| May-22  | ~1,500       | ~2,100            |
| Nov-22  | ~800         | ~1,400            |
| May-23  | ~750         | ~1,300            |
| Nov-23  | ~730         | ~1,250            |
| May-24  | ~740         | ~1,300            |
| Nov-24  | ~760         | ~1,350            |
| May-25  | ~780         | ~1,400            |
| Nov-25  | ~800         | ~1,450            |
| May-26  | ~820         | ~1,500            |
</details>

Source: CEIC, Bloomberg, MS.

## China Consumer: Raw Material Price Trends

## Raw Material Price Trends:

![](images/910074319624db2cbc34f257ca448a7e5380e2cb78aaa455c691cee3e1341a2e.jpg)

China – hogs/pork: China's hog prices were Rmb10.1/kg as of May; prices were up 0.8%

MoM. China's pork retail prices were down 2% MoM in May (vs. down 9% MoM in April), while wholesale pork prices were down 0.2% MoM in May (vs. 

[中间内容因长度限制已省略]

SZ)</td><td>U (03/04/2025)</td><td>Rmb12.09</td></tr><tr><td>Ecovacs Robotics Co Ltd (603486.SS)</td><td>E (10/30/2023)</td><td>Rmb58.47</td></tr><tr><td>Foshan Haitian Flavouring and Food (603288.SS)</td><td>E (07/28/2025)</td><td>Rmb35.10</td></tr><tr><td>Foshan Haitian Flavouring and Food (3288.HK)</td><td>E (05/21/2026)</td><td>HK$31.62</td></tr><tr><td>Haidilao International Holding Ltd (6862.HK)</td><td>O (05/26/2021)</td><td>HK$12.68</td></tr><tr><td>Hangzhou Robam Appliances Co Ltd (002508.SZ)</td><td>U (02/21/2024)</td><td>Rmb16.48</td></tr><tr><td>Laopu Gold (6181.HK)</td><td>O (10/20/2025)</td><td>HK$450.80</td></tr><tr><td>Super Hi (HDL.O)</td><td>E (01/14/2025)</td><td>US$13.09</td></tr><tr><td>Zhejiang Supor Co. Ltd. (002032.SZ)</td><td>E (01/17/2022)</td><td>Rmb42.95</td></tr></table>

Lillian Lou

<table><tr><td>Anhui Gujing Distillery Company Limited (000596.SZ)</td><td>U (02/13/2026)</td><td>Rmb87.21</td></tr><tr><td>Budweiser Brewing Company APAC Ltd (1876.HK)</td><td>O (11/04/2019)</td><td>HK$6.95</td></tr><tr><td>Chagee Holdings Ltd (CHA.O)</td><td>O (06/02/2025)</td><td>US$10.90</td></tr><tr><td>China Mengniu Dairy (2319.HK)</td><td>O (09/14/2017)</td><td>HK$16.54</td></tr><tr><td>China Resources Beer Holdings Co Ltd (0291.HK)</td><td>O (12/11/2018)</td><td>HK$23.38</td></tr><tr><td>Chongqing Brewery Co. Ltd. (600132.SS)</td><td>U (07/30/2021)</td><td>Rmb50.79</td></tr><tr><td>Eastroc Beverages (605499.SS)</td><td>O (03/12/2026)</td><td>Rmb131.88</td></tr><tr><td>Eastroc Beverages (9980.HK)</td><td>O (03/12/2026)</td><td>HK$128.60</td></tr><tr><td>Gree Electric Appliances Inc of Zhuhai (000651.SZ)</td><td>O (04/14/2020)</td><td>Rmb38.20</td></tr><tr><td>Haier Smart Home Co Ltd (600690.SS)</td><td>E (01/17/2022)</td><td>Rmb20.42</td></tr><tr><td>Haier Smart Home Co Ltd (6690.HK)</td><td>E (01/17/2022)</td><td>HK$21.26</td></tr><tr><td>Kweichow Moutai Company Ltd. (600519.SS)</td><td>O (10/17/2014)</td><td>Rmb1,275.88</td></tr><tr><td>Luzhou Lao Jiao Co. Ltd (000568.SZ)</td><td>E (01/23/2019)</td><td>Rmb85.41</td></tr><tr><td>Midea Group Co Ltd. (0300.HK)</td><td>O (11/01/2024)</td><td>HK$90.65</td></tr><tr><td>Midea Group Co Ltd. (000333.SZ)</td><td>O (01/17/2022)</td><td>Rmb83.90</td></tr><tr><td>Muyuan Foodstuff Co. Ltd (2714.HK)</td><td>O (03/17/2026)</td><td>HK$32.22</td></tr><tr><td>Muyuan Foodstuff Co. Ltd (002714.SZ)</td><td>O (03/17/2026)</td><td>Rmb34.43</td></tr><tr><td>Nongfu Spring Co Ltd (9633.HK)</td><td>E (07/30/2021)</td><td>HK$42.62</td></tr><tr><td>Shanxi Xinghuacun Fen Wine Factory Co. (600809.SS)</td><td>O (10/28/2020)</td><td>Rmb118.79</td></tr><tr><td>Shuanghui Development (000895.SZ)</td><td>U (03/16/2021)</td><td>Rmb24.32</td></tr><tr><td>Tingyi (Cayman Islands) (0322.HK)</td><td>E (07/25/2025)</td><td>HK$10.62</td></tr><tr><td>Tsingtao Brewery Co Ltd (0168.HK)</td><td>E (11/01/2024)</td><td>HK$49.50</td></tr><tr><td>Tsingtao Brewery Co Ltd (600600.SS)</td><td>E (02/28/2024)</td><td>Rmb61.03</td></tr><tr><td>Uni-President China (0220.HK)</td><td>E (07/25/2025)</td><td>HK$7.41</td></tr><tr><td>Want Want China Holdings Ltd (0151.HK)</td><td>E (11/29/2023)</td><td>HK$4.10</td></tr><tr><td>WH Group (0288.HK)</td><td>O (02/24/2025)</td><td>HK$8.75</td></tr><tr><td>Wuliangye Yibin Company Ltd. (000858.SZ)</td><td>E (08/15/2024)</td><td>Rmb79.14</td></tr><tr><td>Yanghe Brewery (002304.SZ)</td><td>U (01/05/2021)</td><td>Rmb43.24</td></tr><tr><td>Yanjing Brewery (000729.SZ)</td><td>U (09/02/2015)</td><td>Rmb11.85</td></tr><tr><td>Yili Industrial (600887.SS)</td><td>O (01/29/2014)</td><td>Rmb25.58</td></tr><tr><td>Yum China Holdings Inc. (YUMC.N)</td><td>O (03/20/2018)</td><td>US$42.72</td></tr><tr><td>ZJLD Group (6979.HK)</td><td>E (02/13/2026)</td><td>HK$7.85</td></tr><tr><td colspan="3">Terence Cheng</td></tr><tr><td>Chervon Holdings Ltd. (2285.HK)</td><td>E (04/12/2024)</td><td>HK$15.36</td></tr><tr><td>Crystal International Group Ltd. (2232.HK)</td><td>E (06/23/2025)</td><td>HK$6.07</td></tr><tr><td>Gongniu Group Co Ltd (603195.SS)</td><td>O (05/08/2023)</td><td>Rmb40.75</td></tr><tr><td>Hangzhou Greatstar Industrial Co Ltd (002444.SZ)</td><td>E (10/26/2022)</td><td>Rmb30.80</td></tr><tr><td>Huali Industrial Group Co (300979.SZ)</td><td>U (02/10/2026)</td><td>Rmb33.21</td></tr><tr><td>Shenzhou International Group Holdings (2313.HK)</td><td>O (07/13/2017)</td><td>HK$43.60</td></tr><tr><td>Stella International Holdings Ltd (1836.HK)</td><td>E (06/23/2025)</td><td>HK$13.40</td></tr><tr><td>Techtronic Industries Co Ltd (0669.HK)</td><td>O (12/05/2019)</td><td>HK$113.90</td></tr><tr><td>Yue Yuen Industrial Hldg (0551.HK)</td><td>E (09/14/2021)</td><td>HK$14.06</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
