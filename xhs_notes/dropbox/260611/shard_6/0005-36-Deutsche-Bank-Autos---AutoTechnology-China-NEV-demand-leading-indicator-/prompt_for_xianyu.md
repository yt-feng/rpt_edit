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
Asia

China

Consumer

Autos & Auto Technology

Industry

## Autos & Auto Technology

Date

9 June 2026

Industry Update

# China NEV demand leading indicator (weekly new orders) - June 1st week

This chartbook tracks China passenger vehicle new orders on a weekly basis, detailing new order flow trends for key Chinese new energy vehicle (NEV) automakers.

Figure 1: Weekly new order summary for key OEMs

<table><tr><td colspan="2">(unit)</td><td>Jun-26</td><td>May-26</td><td>Jun-25</td><td>WoW</td><td>YoY</td></tr><tr><td colspan="2">Week #</td><td>W23</td><td>W22</td><td>W23</td><td></td><td></td></tr><tr><td colspan="2">Calendar days</td><td>1-7D</td><td>25-31D</td><td>2-8D</td><td></td><td></td></tr><tr><td colspan="7">Weekly New Orders of key OEMs</td></tr><tr><td>1211 HK</td><td>BYD</td><td>47.7 k</td><td>48.7 k</td><td>75 k</td><td>-2%</td><td>-36%</td></tr><tr><td>0175 HK</td><td>Geely (Zeekr and Galaxy)</td><td>24.8 k</td><td>22.1 k</td><td></td><td>12%</td><td></td></tr><tr><td>9927 HK</td><td>HIMA (mainly AITO)</td><td>24.2 k</td><td>40.7 k</td><td>11.4 k</td><td>-41%</td><td>112%</td></tr><tr><td>9863 HK</td><td>Leap Motor</td><td>14.6 k</td><td>15.1 k</td><td></td><td>-3%</td><td></td></tr><tr><td>TSLA US</td><td>Tesla</td><td>14.2 k</td><td>14 k</td><td>12 k</td><td>1%</td><td>18%</td></tr><tr><td>9866 HK</td><td>NIO</td><td>28 k</td><td>38.8 k</td><td>5.4 k</td><td>-28%</td><td>419%</td></tr><tr><td>2015 HK</td><td>Li Auto</td><td>6.7 k</td><td>8.7 k</td><td>8.9 k</td><td>-24%</td><td>-25%</td></tr><tr><td>1810 HK</td><td>Xiaomi</td><td>7.4 k</td><td>8.6 k</td><td>5 k</td><td>-14%</td><td>48%</td></tr><tr><td>9868 HK</td><td>XPeng</td><td>9.5 k</td><td>11.1 k</td><td>11.3 k</td><td>-14%</td><td>-16%</td></tr></table>

Source : Thinkercar

Bin Wang

Research Analyst

+852-220-35496

Wei Huang

Research Associate

+852-2203-7057

Figure 2: Weekly new orders trend of key automakers (Li, NIO, XPeng, Leap, Xiaomi, Tesla)  
![](images/d0e1ffe6855d9cca27c9d4cc8b60d1fe102676ec3ff646f2d89efbedbbc10413.jpg)  
Source : Thinkercar

Figure 3: Weekly BYD, Geely, HIMA (mainly AITO) new orders trend  
![](images/864d5a0fa2524bea915bbee6a1ad4b07d77b5a6533b5471d15f9cb0e1348cf41.jpg)

<details>
<summary>line chart</summary>

| Month    | BYD  | HIMA (mainly AITO) | Geely (Galaxy+Zeekr) |
|----------|------|--------------------|----------------------|
| Jan-26 W1 | 5    | 3                  | 3                    |
| Jan-26 W2 | 20   | 5                  | 5                    |
| Jan-26 W3 | 30   | 6                  | 6                    |
| Jan-26 W4 | 38   | 7                  | 7                    |
| Jan-26 W5 | 35   | 8                  | 8                    |
| Feb-26 W1 | 30   | 7                  | 7                    |
| Feb-26 W2 | 25   | 6                  | 6                    |
| Feb-26 W3 | 12   | 5                  | 5                    |
| Feb-26 W4 | 18   | 6                  | 6                    |
| Mar-26 W1 | 45   | 10                 | 15                   |
| Mar-26 W2 | 48   | 9                  | 18                   |
| Mar-26 W3 | 55   | 10                 | 20                   |
| Mar-26 W4 | 85   | 11                 | 22                   |
| Apr-26 W1 | 65   | 12                 | 20                   |
| Apr-26 W2 | 55   | 11                 | 22                   |
| Apr-26 W3 | 48   | 10                 | 35                   |
| Apr-26 W4 | 45   | 65                 | 35                   |
| May-26 W1 | 50   | 50                 | 30                   |
| May-26 W2 | 45   | 30                 | 25                   |
| May-26 W3 | 40   | 35                 | 20                   |
| May-26 W4 | 45   | 40                 | 35                   |
| May-26 W5 | 48   | 40                 | 25                   |
| Jun-26 W1 | 48   | 30                 | 25                   |
</details>

Source : Thinkercar

Figure 4: Weekly HIMA (mainly AITO) new orders trend  
![](images/c879681054c2ef674e8b59d37c2defa727be66f000f2fd3216e0a015f2f05d7a.jpg)

<details>
<summary>line chart</summary>

| Date       | Value (000 units) |
| ---------- | ----------------- |
| Jan-26 W1  | 2                 |
| Jan-26 W2  | 5                 |
| Jan-26 W3  | 6                 |
| Jan-26 W4  | 7                 |
| Jan-26 W5  | 7                 |
| Feb-26 W1  | 7                 |
| Feb-26 W2  | 5                 |
| Feb-26 W3  | 3                 |
| Feb-26 W4  | 5                 |
| Mar-26 W1  | 12                |
| Mar-26 W2  | 9                 |
| Mar-26 W3  | 9                 |
| Mar-26 W4  | 11                |
| Apr-26 W1  | 11                |
| Apr-26 W2  | 11                |
| Apr-26 W3  | 10                |
| Apr-26 W4  | 65                |
| May-26 W1  | 50                |
| May-26 W2  | 30                |
| May-26 W3  | 32                |
| May-26 W4  | 21                |
| May-26 W5  | 41                |
| Jun-26 W1  | 24                |
</details>

Source : Thinkercar

Figure 5: Weekly Li Auto new orders trend  
![](images/6f485c05bf5df0c03b8087c06f3eb4f79c0893dfcb20d2488123f30f9487a73c.jpg)

<details>
<summary>line chart</summary>

| Date       | Value (000 units) |
| ---------- | ----------------- |
| Jan-26 W1  | 2                 |
| Jan-26 W2  | 4                 |
| Jan-26 W3  | 4                 |
| Jan-26 W4  | 4                 |
| Jan-26 W5  | 4.5               |
| Feb-26 W1  | 4                 |
| Feb-26 W2  | 3                 |
| Feb-26 W3  | 2.5               |
| Feb-26 W4  | 4                 |
| Mar-26 W1  | 5.5               |
| Mar-26 W2  | 5                 |
| Mar-26 W3  | 6                 |
| Mar-26 W4  | 7                 |
| Apr-26 W1  | 8.5               |
| Apr-26 W2  | 9.5               |
| Apr-26 W3  | 9                 |
| Apr-26 W4  | 8                 |
| May-26 W1  | 7                 |
| May-26 W2  | 6                 |
| May-26 W3  | 13.5              |
| May-26 W4  | 12                |
| May-26 W5  | 9                 |
| May-26 W6  | 7                 |
| Jun-26 W1  | 6                 |
</details>

Source : Thinkercar

Figure 6: Weekly NIO group new orders trend  
![](images/512b3273449375d2255779dcc38ac6a87e4c9d7532096cf75edeed71d6778131.jpg)

<details>
<summary>line chart</summary>

| Date       | Value (000 units) |
| ---------- | ----------------- |
| Jan-26 W1 | 1                 |
| Jan-26 W2 | 3                 |
| Jan-26 W3 | 4                 |
| Jan-26 W4 | 5                 |
| Jan-26 W5 | 4                 |
| Feb-26 W1 | 3                 |
| Feb-26 W2 | 2                 |
| Feb-26 W3 | 2                 |
| Feb-26 W4 | 8                 |
| Mar-26 W1 | 9                 |
| Mar-26 W2 | 8                 |
| Mar-26 W3 | 9                 |
| Mar-26 W4 | 10                |
| Apr-26 W1 | 10                |
| Apr-26 W2 | 9                 |
| Apr-26 W3 | 10                |
| Apr-26 W4 | 11                |
| May-26 W1 | 10                |
| May-26 W2 | 10                |
| May-26 W3 | 21                |
| May-26 W4 | 12                |
| May-26 W5 | 39                |
| Jun-26 W1 | 28                |
</details>

Source : Thinkercar

Figure 7: Weekly Tesla new orders trend  
![](images/fc2625f6289329464e56fd514017026638fbbbcf3a65bbc8b00d5d35fb0c58e1.jpg)

<details>
<summary>line chart</summary>

| Date     | Value (000 units) |
| -------- | ----------------- |
| Jan-26 W1 | 2                 |
| Jan-26 W2 | 7                 |
| Jan-26 W3 | 8                 |
| Jan-26 W4 | 7                 |
| Jan-26 W5 | 8                 |
| Feb-26 W1 | 9                 |
| Feb-26 W2 | 8                 |
| Feb-26 W3 | 6                 |
| Feb-26 W4 | 10                |
| Mar-26 W1 | 11                |
| Mar-26 W2 | 14                |
| Mar-26 W3 | 15                |
| Mar-26 W4 | 15                |
| Apr-26 W1 | 15                |
| Apr-26 W2 | 16                |
| Apr-26 W3 | 13                |
| Apr-26 W4 | 13                |
| May-26 W1 | 15                |
| May-26 W2 | 14                |
| May-26 W3 | 11                |
| May-26 W4 | 12                |
| May-26 W5 | 14                |
| Jun-26 W1 | 14                |
</details>

Source : Thinkercar

Figure 8: Weekly Xiaomi new orders trend  
![](images/f0f5d4d2b28de4fe1f4e0c2fc9076463af786959ace2bba574b3885a8393e70f.jpg)

<details>
<summary>line chart</summary>

| Date     | Value (000 units) |
| -------- | ----------------- |
| Jan-26 W1 | 0                 |
| Jan-26 W2 | 1                 |
| Jan-26 W3 | 1                 |
| Jan-26 W4 | 2                 |
| Jan-26 W5 | 2                 |
| Feb-26 W1 | 2                 |
| Feb-26 W2 | 1                 |
| Feb-26 W3 | 2                 |
| Feb-26 W4 | 4                 |
| Mar-26 W1 | 3                 |
| Mar-26 W2 | 3                 |
| Mar-26 W3 | 36                |
| Mar-26 W4 | 14                |
| Apr-26 W1 | 10                |
| Apr-26 W2 | 8                 |
| Apr-26 W3 | 7                 |
| Apr-26 W4 | 5                 |
| May-26 W1 | 8                 |
| May-26 W2 | 7                 |
| May-26 W3 | 5                 |
| May-26 W4 | 10                |
| May-26 W5 | 9                 |
| Jun-26 W1 | 7                 |
</details>

Source : Thinkercar

Figure 9: Weekly XPeng new orders trend  
![](images/60d0449690d49aa661f9ffaa22f2a56dee7c70dda75f7173ad856821f65d5790.jpg)

<details>
<summary>line chart</summary>

| Date       | Value (000 units) |
| ---------- | ----------------- |
| Jan-26 W1  | 0                 |
| Jan-26 W2  | 3                 |
| Jan-26 W3  | 4                 |
| Jan-26 W4  | 5                 |
| Jan-26 W5  | 5                 |
| Feb-26 W1  | 5                 |
| Feb-26 W2  | 3                 |
| Feb-26 W3  | 2                 |
| Feb-26 W4  | 4                 |
| Mar-26 W1  | 16                |
| Mar-26 W2  | 8                 |
| Mar-26 W3  | 5                 |
| Mar-26 W4  | 6                 |
| Apr-26 W1  | 16                |
| Apr-26 W2  | 9                 |
| Apr-26 W3  | 8                 |
| Apr-26 W4  | 7                 |
| May-26 W1  | 7                 |
| May-26 W2  | 7                 |
| May-26 W3  | 5                 |
| May-26 W4  | 29                |
| May-26 W5  | 11                |
| Jun-26 W1  | 9                 |
</details>

Source : Thinkercar

## Appendix 1

Important Disclosures

\*Other information available upon request

\*Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst about the subject issuers and the securities of those issuers. In addition, the undersigned lead analyst has not and will not receive any compensation for providing a specific recommendation or view in this report. Bin Wang.

Equity rating dispersion and banking relationships  
![](images/ee167a3d37146ad7d30ccd97c3d9e0e680a4a072b49c59d98b764941b35ab3fc.jpg)

<details>
<summary>bar chart</summary>

Asia Universe
| Category | companies covered (%) | Cos. w/ Banking Relationship (%) | MIFID Investment & Ancillary Services (%) |
| :--- | :--- | :--- | :--- |
| BUY | 81 | 30 | 67 |
| HOLD | 15 | 16 | 56 |
| SELL | 4 | 0 | 50 |
</details>

## Equity Rating and Dispersion Key

The Equity Rating Dispersion Chart depicts the following:

The proportion of recommendations that are rated "buy", "sell" and "hold" over the previous 12 months. This is shown for securities issued in the stated region e.g. "Europe Universe". See rating definitions below. This is represented by the "Companies Covered" bars in the chart. The percentage value displayed above the bar is the proportion as a percentage. E.g. 50% above the "buy" / "Companies Covered" bar means that 50% of DB's equity research covered companies over the past 12 months have a "buy" rating.

Next to each of the three respective bars showing the proportion of "buy", "sell" and "hold" recommendations we provide two additional bars to show:

\- The proportion of "buy", "sell" or "hold recommendations where DB and or/Affiliates provided MIFID Investment or Ancillary Services in the past 12 months. This is represented in the "MIFID Investment and Ancillary Services" bar. The percentage value displayed above the bar shows the proportion of Companies Covered with the given rating where DB has also provided MIFID Investment and Ancillary Services in the past 12 months. E.g. 50% above the "Cos. w/ MIFID Investment and Ancillary Services" bar means 50% of the Companies Covered with the rating stated have also received MIFID Investment and Ancillary Services from DB.

\- The proportion of "buy" (or "sell" or "hold") recommendations where DB and or/Affiliates has provided Investment Banking services in the past 12 months for which it has received compensation. The percentage value displayed above the bar shows the proportion of Companies Covered with the stated rating where DB has also provided Investment Banking services in the past 12 months. E.g. 50% above the "Cos. w/ Investment Banking relationship" bar means 50% of the Companies Covered with the rating stated also have an Investment Banking Relationship with DB.

Buy: Based on a current 12-month view of TSR, we recommend that investors buy the stock.

Sell: Based on a current 12-month view of TSR, we recommend that investors sell the stock.

Hold: We take a neutral view on the stock 12-months out and, based on this time horizon, do not recommend either a Buy or Sell.

TSR = Total Shareholder Return. Percentage change in share price from current price to projected target price plus projected dividend yield

Newly issued research recommendations and target prices supersede previously published research.

## Additional Information

The information and opinions in this report were prepared by DB AG or one of its affiliates (collectively 'DB'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, DB makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. DB neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of DB in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a DB analyst, DB may act as principal for its own account or as agent for another person.

DB may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within DB, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. DB issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communica

[中间内容因长度限制已省略]

 performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

## David Folkerts-Landau

Group Chief Economist and Global Head of Research

Pam Finelli
COO and Head of Fixed
Income Research

Steve Pollard
Global Head of Company
Research and Sales

Jim Reid
Global Head of Macro and
Thematic Research

Tim Rokossa
Head of European
Company Research

Matthew Barnard
Head of Americas
Company Research

Debbie Jones
Global Head of
Sustainability and Data
Innovation, Research

Robin Winkler
Head of German Macro
Research

Sameer Goel
Global Head of EM &
APAC Research

Francis Yared
Global Head of Rates
Research

George Saravelos
Global Head of FX
Research

Peter Hooper
Vice-Chair of Research

Nilendra de-Mel
Head of APAC & Middle
East Product
Development

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr><tr><td>DB AG</td><td>DB Securities Inc.</td><td>DB AG</td><td></td></tr><tr><td>21 Moorfields</td><td>The DB Center</td><td>Filiale Singapur</td><td></td></tr><tr><td>London EC2Y 9DB</td><td>1 Columbus Circle</td><td>One Raffles Quay, South</td><td></td></tr><tr><td>United Kingdom</td><td>New York, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>
"""
