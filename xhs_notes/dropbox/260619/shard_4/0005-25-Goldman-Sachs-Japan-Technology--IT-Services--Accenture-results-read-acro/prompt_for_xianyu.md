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
# Japan Technology: IT Services: Accenture results read-across: Orders soften amid geopolitical headwinds; AI business expands

IT services major Accenture (Buy, covered by US Telecom/IT Services analyst James Schneider) announced 3Q8/26 (March-May) results at 20:00 JST (07:00 US local time) on June 18, followed by a conference call at 21:00 JST. 3Q sales were mostly in line with consensus, but 3Q orders turned down amid effects from the Middle East situation, and the company noted the potential for the negative impact from the Middle East could worsen in 4Q compared with 3Q. Based on its progress to date and other factors, management made slight revisions to its full-year sales guidance, lowering the upper end and midpoint of its forecast range. Although the situation is driven by impacts stemming from geopolitics rather than AI disruption, it could prolong weak investor sentiment toward system integrators. At the same time, corporate appetite for AI investment is robust, and AI-related business is expanding, centered on support for AI implementation, consulting on AI-led business transformation, data infrastructure, and security. In terms of read-across for the Japanese IT Services sector, based on our industry research, while the Middle East situation has had a limited impact on IT services demand in Japan, we see this as a slight headwind for NTT (Buy), given its subsidiary NTT Data's high overseas revenue exposure (60% overseas sales ratio in FY3/26). Meanwhile, Japan is starting to see a similar trend in terms of expansion in AI-related business, and we see NOM Institute (Buy) and Trend Micro (Neutral) as well-placed to benefit. Below, we outline our key takeaways from the call (growth rates are all on a local-currency, or LC, basis).

3Q8/26 earnings: 3Q8/26 sales of US\$18.72 bn (+3% yoy; 2Q growth was +4% yoy) landed at the midpoint of the guidance range (+1% to +5% yoy) and in line with the Bloomberg consensus (US\$18.76 bn). By region, sales growth was +1% yoy in the Americas (2Q: +3% yoy), +4% in EMEA (+2%), and +8% in Asia (+10%; Exhibit 1). The Americas was challenged from an ongoing impact of restrained investment by the US government (-2 pp), while growth improved in EMEA, mainly driven by the UK and Italy, and growth in Asia was led by Japan, Australia, and Singapore. By client industry, communications, media, and technology (+9% yoy) was strong, while demand was sluggish in healthcare & public services (flat yoy), mainly centered on US government business. Operating profits came in at US\$3.17 bn (+6% yoy), the operating margin rose +0.1 pp yoy (Exhibit 2), headcount increased +1.6% qoq, and the attrition rate was 14% (-2 pp yoy/+1 pp qoq; Exhibit 3).

■ Orders environment: Turning to orders, 3Q new bookings swung to negative

Chikai Tanaka, CFA

+81(3)4587-9840

chikai.tanaka@gs.com

GS Japan Co., Ltd.

Yuki Sato

+81(3)4587-8536 | yuki.z.sato@gs.com

GS Japan Co., Ltd.

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

growth for the first time in four quarters at -3% yoy (LC basis; 2Q: +1% yoy; Exhibit 4). By service type, consulting orders, a leading indicator for system integration and development demand, accelerated to +13% yoy (vs. +8% in 2Q; USD basis, no disclosure on LC basis), but managed services turned negative at -15% yoy (vs. +3% in 2Q). The number of clients with bookings of over US\$100 mn was flat at 30 (versus 30 in 2Q). Amid impacts from the Middle East situation, decision-making by some clients was delayed, resulting in negative impacts of c.US\$100 mn in sales and c.US\$400 mn in orders, primarily in consulting. The impact was particularly severe in the manufacturing and automotive industries, and Accenture noted the potential for this impact to rise further in 4Q. Client-specific factors also led to large managed service projects being pushed back to FY8/27 (delayed rather than lost). Meanwhile, corporate appetite for AI investment remains robust, as the focus shifts from proof of concept (PoC) to commercial deployment, fueling demand for AI implementation support and AI-driven business transformation consulting.

Guidance: FY8/26 sales guidance (LC) was lowered to +3% to +4% yoy (from +3% to +5% yoy), or to +4% to +5% yoy (from +4% to +6% yoy) excluding US government business (which is expected to have a -1 pp impact on growth). This downward revision to both the upper end and midpoint of the range leaves the new midpoint below the Bloomberg consensus. By quarter, 4Q sales guidance (LC) calls for +1% to +5% yoy growth (+2% to +6% yoy excluding US government business). Management noted that negative effects from the Middle East situation could be greater than in 3Q.

Exhibit 1: North America slows, Europe accelerates, and Asia remains solid  
Accenture sales growth by region (local-currency basis)  
![](images/9a31766ecc3f79ec72252f21458eabb2706ba1c1ee25f4064b824330d17fa8f7.jpg)  
Regional definitions changed in 1Q8/24, reclassifying Latin America sales from Growth to North America, and with this North America was changed to Americas, while Growth was changed to Asia Pacific; EMEA unchanged.

Exhibit 2: Both sales and profit growth rates slow slightly
Accenture sales growth (LC basis) and operating profits/adjusted operating profits  
![](images/d207898ea17f1beb71656d879382364fd573fbb061eb482b0ba51af4c08fbc5d.jpg)

<details>
<summary>line chart</summary>

| Period | Revenue (y-y) (%) | Operating Income (y-y) (%) | Adjusted Operating Income (y-y) (%) |
|---|---|---|---|
| 9-11 19/8 | 9.5 | 8.5 | 9.0 |
| 12-2 3-5 | 8.0 | 6.0 | 7.5 |
| 6-8 | 8.5 | 7.0 | 8.0 |
| 9-11 12-2 | 8.0 | 8.5 | 8.0 |
| 12-2 3-5 | 0.0 | -1.0 | -0.5 |
| 6-8 | -1.0 | -2.0 | -1.5 |
| 9-11 12-2 | 4.0 | 10.0 | 3.0 |
| 12-2 3-5 | 15.0 | 25.0 | 20.0 |
| 21/8 | 17.0 | 28.0 | 25.0 |
| 6-8 | 28.0 | 30.0 | 30.0 |
| 9-11 12-2 | 27.0 | 25.0 | 23.0 |
| 12-2 3-5 | 22.0 | 23.0 | 21.0 |
| 6-8 | 15.0 | 15.0 | 13.0 |
| 9-11 23/8 | 5.0 | -5.0 | -4.0 |
| 12-2 3-5 | -5.0 | -15.0 | -13.0 |
| 6-8 | -3.0 | -5.0 | -4.0 |
| 9-11 12-2 | -1.0 | -10.0 | -8.0 |
| 12-2 3-5 | -2.0 | -5.0 | -4.0 |
| 6-8 | -1.0 | -3.0 | -2.0 |
| 9-11 24/8 | -1.0 | -1.0 | -1.0 |
| 12-2 3-5 | -3.0 | -5.0 | -4.0 |
| 6-8 | -1.0 | -3.0 | -2.0 |
| 9-11 25/8 | -3.0 | -15.0 | -13.0 |
| 12-2 3-5 | -5.0 | -10.0 | -8.0 |
| 6-8 | -7.0 | -5.0 | -4.0 |
| 9-11 26/8 | -3.0 | -3.0 | -2.0 |
| 12-2 3-5 | -4.0 | -5.0 | -4.0 |
| 6-8 | -6.0 | -7.0 | -6.0 |
The chart displays the percentage values for Revenue (y-y), Operating Income (y-y), and Adjusted Operating Income (y-y) over time, with each data point labeled by its respective date and value in parentheses. The x-axis represents the fiscal years from September to March of each year.
</details>

Adjusted operating profits = operating profits + business optimization costs.  
Source: Company data, Data compiled by GS Global Investment Research  
Source: Company data, Data compiled by GS Global Investment Research

Exhibit 3: Headcount rises slightly qoq Accenture headcount and attrition rate  
![](images/c92b5d1c85dbec7a79f3b5a4070c5c6f28ba529ff46a7ae56f09836fdef65ff3.jpg)

<details>
<summary>line chart</summary>

| Date | Employees | Attrition rate (hrs) |
| --- | --- | --- |
| 9-11 | 200 | 600 |
| 12-2 | 200 | 700 |
| 3-5 | 200 | 750 |
| 6-8 | 200 | 700 |
| 9-11 | 200 | 550 |
| 12-2 | 200 | 450 |
| 3-5 | 200 | 500 |
| 6-8 | 200 | 350 |
| 9-11 | 200 | 400 |
| 12-2 | 200 | 500 |
| 3-5 | 200 | 650 |
| 6-8 | 200 | 750 |
| 9-11 | 200 | 700 |
| 12-2 | 200 | 650 |
| 3-5 | 200 | 750 |
| 6-8 | 200 | 750 |
| 9-11 | 200 | 550 |
| 12-2 | 200 | 550 |
| 3-5 | 200 | 550 |
| 6-8 | 200 | 550 |
| 9-11 | 200 | 550 |
| 12-2 | 200 | 550 |
| 3-5 | 200 | 550 |
| 6-8 | 200 | 550 |
| 9-11 | 200 | 55 |
| 12-2 | 200 | -10 |
| 3-5 | 200 | -15 |
| 6-8 | 200 | -15 |
| 9-11 | 200 | -15 |
| 12-2 | 200 | -15 |
| 3-5 | 200 | -15 |
| 6-8 | 200 | -15 |
| 9-11 | 200 | -15 |
| 12-2 | 200 | -15 |
| 3-5 | 200 | -15 |
| 6-8* | 200 | -15 |
| 9-11 | 200 | -15 |
| 12-2 | 200 | -15 |
| 3-5 | 200 | -15 |
| 6-8* | 200 | -15 |
| 9-11 | 200+ | -15% |
| 12-2 | 20 | -15% |
| 3-5 | 2 | -15% |
| 6-8* | -1 | -15% |
| 9-11 | -1 | -15% |
| 12-2 | -1 | -15% |
| 3-5 | -1 | -15% |
| 6-8* | -1 | -15% |
| 9-11 | -1 | -15% |
| 12-2 | -1 | -15% |
| 3-5 | -1 | -15% |
| 6-8* | -1 | -15% |
| 9+ | -1 | -15% |
| 12+ | -1 | -15% |
| 3+ | -1 | -15% |
| + | -1 | -15% |
| + | -1 | -15% |
| + | -1 | -15% |
| + | -1 | -15% |
| + | -1 | -15% |
| + | -1 | -15% |
| + | -1 | -15% |
</details>

Source: Company data, Data compiled by GS Global Investment Research

Exhibit 4: 3Q order growth turns negative at $-3\%$ yoy Accenture orders (USD basis)  
![](images/80135865ce2e55937ed3ab5f8c6d61bdf8c8fce72c8e5db60ac3392d6f0fe0c3.jpg)

<details>
<summary>bar-line hybrid</summary>

| Date | New Booking (Consulting) (bn $) | Outsourcing (bn $) | New Bookings (y-y)(rhs) (%) |
|---|---|---|---|
| 9-11 | 5.0 | 4.0 | 8.0 |
| 12-2 | 6.0 | 5.0 | 13.0 |
| 3-5 | 7.0 | 6.0 | -10.0 |
| 6-8 | 6.0 | 5.0 | 14.0 |
| 9-11 | 6.0 | 6.0 | 8.0 |
| 12-2 | 7.0 | 7.0 | 14.0 |
| 3-5 | 6.0 | 6.0 | 9.0 |
| 6-8 | 6.0 | 8.0 | 10.0 |
| 9-11 | 7.0 | 9.0 | 16.0 |
| 12-2 | 8.0 | 10.0 | 12.0 |
| 3-5 | 8.0 | 12.0 | 42.0 |
| 6-8 | 9.0 | 13.0 | 10.0 |
| 9-11 | 10.0 | 14.0 | 18.0 |
| 12-2 | 11.0 | 15.0 | 22.0 |
| 3-5 | 12.0 | 16.0 | 24.0 |
| 6-8 | 13.0 | 17.0 | 26.0 |
| 9-11 | 14.0 | 18.0 | 28.0 |
| 12-2 | 15.0 | 20.0 | 32.0 |
| 3-5 | 16.0 | 22.0 | 34.0 |
| 6-8 | 17.0 | 24.0 | 36.0 |
| 9-11 | 18.0 | 26.0 | 38.0 |
| 12-2 | 19.0 | 28.0 | 40.0 |
| 3-5 | 20.0 | 30.0 | 42.0 |
| 6-8 | 21.0 | 32.0 | 44.0 |
| 9-11 | 22.0 | 34.0 | 46.0 |
| 12-2 | 23.0 | 36.0 | 48.0 |
| 3-5 | 24.0 | 38.0 | 50.0 |
| 6-8 | 25.0 | 40.0 | 52.0 |
| 9-11 | 26.0 | 42.0 | 54.0 |
| 12-2 | 27.0 | 44.0 | 56.0 |
| 3-5 | 28.0 | 46.0 | 58.0 |
| 6-8 | 29.0 | 48.0 | 60.0 |
| 9-11 | 30.0 | 50.0 | 62.0 |
| 12-2 | 31.0 | 52.0 | 64.0 |
| 3-5 | 32.0 | 54.0 | 66.0 |
| 6-8 | 33.0 | 56.0 | 68.0 |
| 9-11 | 34.0 | 58.0 | 70.0 |
| 12-2 | 35.0 | 60.0 | 72.0 |
| 3-5 | 36.0 | 62.0 | 74.0 |
| 6-8 | 37.0 | 64.0 | 76.0 |
| 9-11 | 38.0 | 66.0 | 78.0 |
| 12-2 | 39.0 | 68.0 | 80.0 |
| 3-5 | 40.0 | 70.0 | 82.0 |
| 6-8 | 41.0 | 72.0 | 84.0 |
| 9-11 | 42.0 | 74.0 | 86.0 |
| 12-2 | 43.0 | 76.0 | 88.0 |
| 3-5 | 44.0 | 78.0 | 90.0 |
| 6-8 | 45.0 | 80.0 | 92.0 |
| 9-11 | 46.0 | 82.0 | 94.0 |
| 12-2 | 47.0 | 84.0 | 96.0 |
| 3-5 | 48.0 | 86.0 | 98.0 |
| ... (repeated values) are possible to be extracted from the provided image as they are not explicitly labeled in the chart.
</details>

Source: Company data, Data compiled by GS Global Investment Research

Exhibit 5: 3Q8/26 sales mostly in line with consensus, but negative order growth of $-3\%$ yoy missed consensus  
Accenture: Earnings statement

<table><tr><td>Accenture (ACN)(mn $)</td><td>24/89-11</td><td>12-2</td><td>3-5</td><td>6-8</td><td>25/89-11</td><td>12-2</td><td>3-5</td><td>6-8</td><td>26/89-11</td><td>12-2</td><td>3-5</td></tr><tr><td>New Bookings(y-y)(y-y: LC)(BB ratio)Consulting(y-y)(BB ratio)Managed Services(y-y)(BB ratio)</td><td>18,45013.7%1.148,6206.3%1.029,83021.2%1.27</td><td>21,580-2.3%-2.0%1.311,060-3.2%1.42</td><td>21,06022.1%26.0%1.289,2803.9%1.1011,78041.6%1.47</td><td>20,15021.1%24.0%1.238,5901.4%1.0411,55041.4%1.42</td><td>18,7001.4%1.0%1.069,2207.0%1.029,480-3.6%1.10</td><td>20,910-3.1%0.0%1.2610,470-0.5%1.2610,440-5.6%1.25</td><td>19,700-6.5%-7.0%1.119,080-2.2%1.0110,620-9.8%1.22</td><td>21,3105.8%3.0%1.218,8703.3%1.011,2407.7%1.41</td><td>20,94012.0%10.0%1.109,8807.2%1.0511,06016.7%1.19</td><td>22,1105.7%1.0%1.2011,3308.2%1.2810,7803.3%1.17</td><td>19,320-1.9%-3.0%1.0010,26013.0%1.109,060-14.7%0.96</td></tr><tr><td colspan="12">P/L</td></tr><tr><td>Revenues(y-y)(y-y: LC)</td><td>16,2243.0%1.0%</td><td>15,800-0.1%0.0%</td><td>16,467-0.6%1.4%</td><td>16,4062.6%5.0%</td><td>17,6909.0%8.0%</td><td>16,6595.4%8.5%</td><td>17,7287.7%7.0%</td><td>17,5967.3%4.5%</td><td>18,7426.0%5.0%</td><td>18,0448.3%4.0%</td><td>18,7185.6%3.0%</td></tr><tr><td>Operating Income(y-y)(OPM)</td><td>2,565-1.1%15.8%</td><td>2,0465.2%13.0%</td><td>2,63111.5%16.0%</td><td>2,35423.0%14.3%</td><td>2,94815.0%16.7%</td><td>2,2459.7%13.5%</td><td>2,98313.4%16.8%</td><td>2,050-12.9%11.6%</td><td>2,874-2.5%15.3%</td><td>2,49411.1%13.8%</td><td>3,1756.5%17.0%</td></tr><tr><td>Business Optimization Cost (SGA)AmericasEMEAAsia PacificAdjusted Operating Income(y-y)(OPM)</td><td>1405071192,7054.3%16.7%</td><td>11512862,162-1.2%13.7%</td><td>77-47562,7080.1%16.4%</td><td>1062517642,4603.1%15.0%</td><td>615420132632,9489.0%16.7%</td><td>3086710.1%13.5%</td><td>420132632,98310.1%16.8%</td><td>615420132632,98310.1%15.1%</td><td>3086710.1%13.8%</td><td>420132632,98310.1%17.0%</td><td>3,1756.5%17.0%</td></tr><tr><td colspan="12">Revenues &amp; Operating Income by Geographic Markets</td></tr><tr><td>Americas(y-y)(y-y: LC)(% of sales)EMEA(y-y)(y-y: LC)(% of sales)Asia Pacific(y-y)(y-y: LC)(% of sales)</td><td>8,027---49.5%5,8049.2%2,394---14.8%</td><td>7,816---49.5%5,5990.8%2,385---15.1%</td><td>8,28750.3%5,777-1.6%35.1%2,404---14.6%</td><td>8,423---51.3%5,6391.5%34.4%2,344---4.3%</td><td>8,7338.8%11.0%49.4%6,41210.5%36.2%2,5446.3%4.0%14.4%</td><td>8,5539.4%11.0%51.3%5,8043.7%34.8%2,302-3.5%1.0%13.8%</td><td>8,9668.2%9.0%50.6%6,2327.9%6.0%35.2%5.2%4.0%14.3%</td><td>8,8044.5%5.0%50.0%6,1969.9%3.0%35.2%2,59610.7%6.0%14.8%</td><td>9,0804.0%4.0%4.0%48.4%6,9358.2%4.0%37.0%2,7277.2%9.0%14.6%</td><td>8,8964.0%3.0%49.3%6,5692.0%36.4%2,57812.0%10.0%14.3%</td><td>9,1381.9%1.0%48.8%6,87310.3%4.0%36.7%2,7077.0%8.0%14.5%</td></tr><tr><td>Americas(y-y)(OPM)EMEA(y-y)(OPM)Asia Pacific(y-y)(OPM)</td><td>1,293---16.1%82413.3%14.2448---18.7%</td><td>1,083---13.9%529-14.0%9.4%434---18.2%</td><td>1,408---17.0%75011.9%13.0%473---19.7%</td><td>1,296---15.4%70148.9%12.4%357---21.2%</td><td>1,3776.5%15.8%1,03625.8%16.2%53519.4%21.0%</td><td>1,24014.5%14.5%63920.8%11.0%365-15.9%15.9%</td><td>1,72022.2%19.2%7530.4%12.1%5107.8%20.2%</td><td>987-23.8%11.2%663-5.5%10.7%40012.1%15.4%</td><td>1,52710.9%16.8%900-13.1%13.0%446-16.7%16.4%</td><td>1,39312.3%15.7%6775.9%10.3%42416.1%16.4%</td><td>1,708-0.7%18.7%99432.0%14.5%473-7.2%17.5%</td></tr><tr><td colspan="12">Revenues by Industry Groups</td></tr><tr><td>Comm. Media &amp; Tech(y-y)(y-y: LC)(% of sales)Financial Services(y-y)(y-y: LC)(% of sales)Health &amp; Public Service(y-y)(y-y: LC)(% of sales)Products(y-y)(y-y: LC)(% of sales)Resources(y-y)(y-y: LC)(% of sales)</td><td>2,669-10.4%-11.0%16.5%3,0342.4%0.0%18.7%3,37712.6%12.0%20.8%4,8608.5%1.0%30.0%2,2846.8%0.0%8.5%1.0%52.1%7,7686.4%5.0%47.9%</td><td>2,654-8.0%-7.0%16.8%2,809-6.5%-6.0%17.8%3,33410.3%10.0%4,7620.9%0.0%30.1%2,2412.6%4.0%49.8%0.3%30.3%2,310-0.1%3.0%48.6%0.3%2.0%30.3%2,220-0.4%3.0%48.6%</td><td>2,763-4.1%-1.0%16.8%2,895-7.8%-5.0%17.6%3,5157.6%9.0%21.3%4,9830.3%2,310-0.1%3.0%48.6%</td><td>2,7511.6%5.0%16.8%2,873-5.1%-2.0%17.5%3,61410.5%22.0%4,9494.2%6.0%30.2%2,220-0.4%3.0%13.5%</td><td>2,8587.1%7.0%16.2%3,1694.5%4.0%17.9%3,81312.9%21.6%5,42511.6%10.0%30.7%6.2%6.0%13.7%</td><td>2,7302.8%5.4%6.0%16.4%3,0107.2%11.0%18.1%3,6097.5%30.3%2,2584.5%4.0%13.6%</td><td>2,9125.4%5.0%16.4%3,27913.3%13.0%18.5%3,778-1.4%7.0%21.3%5,3447.2%7.0%30.6%2,3874.5%5.0%4.0%13.6%</td><td>2,9547.4%5.0%16.8%3,31615.4%12.0%18.8%3,564-1.4%-3.0%20.3%5,3768.6%5.0%30.6%2,3877.5%-3.0%20.3%5,7415.8%4.0%30.6%2,3877.5%-3.0%20.3%</td><td>3,1028.5%10.0%16.6%3,60213.7

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
