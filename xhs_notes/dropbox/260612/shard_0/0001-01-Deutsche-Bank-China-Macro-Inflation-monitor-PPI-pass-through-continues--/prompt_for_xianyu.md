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
Economics

China Macro

# Inflation monitor: PPI pass-through continues; CPI points to softer demand

China's PPI reflation continued as expected in May, while the underlying drivers are shifting. Headline PPI inflation rose to $3.9\%$ YoY, accelerating by 1.1ppt from April. On a MoM basis, PPI inflation moderated by 1.2ppt from the previous month but remained positive at $0.5\%$ MoM. With international oil prices broadly stable during the month, oil-related sectors saw a small MoM drop in prices. Meanwhile, the pass-through of earlier energy price increases to mid- and downstream sectors continued, with chemicals, ferrous metals and textiles all registering faster sequential price gains. In addition, AI-related demand continued to push up prices in non-ferrous metals such as tin and copper, electrical machinery, optical fibers, wires and cables, as well as computers.

Looking ahead, we maintain our forecast that PPI inflation will rise to around $5\%$ by year-end, averaging $3.3\%$ in 2026. While energy prices were the key driver in March and April, the focus ahead will be on the breadth of pass-through to mid- and downstream sectors, as well as the strength of AI-related demand.

Headline CPI inflation was unchanged at 1.2% YoY, but the breakdown points to softening domestic demand. Sequential inflation turned negative, falling 0.1% MoM after a 0.3% increase in April. Services, food, household goods and autos all saw MoM declines and slower YoY inflation, pointing to softer consumer demand. Energy prices declined 0.1% MoM, compared with a 5.7% rise in the previous month. Meanwhile, AI-related demand lifted prices of mobile phones and computers, which rose 1.6% and 1.1% MoM, respectively, while the arrival of summer also supported stronger clothing prices.

As the boost to goods consumption from the trade-in subsidies will likely diminish marginally, consumer demand is likely to remain soft. We therefore lower our full-year CPI inflation forecast to 1.5% from 1.6%, and now expect it to rise to 1.8% by year-end, compared with our previous forecast of 2.0%.

Date

10 June 2026

Deyun Ou

Economist

+852-2203-6166

Yi Xiong, Ph.D.

Chief Economist

+852-2203-6139

Figure 1: PPI reflation was in line with our forecast  
![](images/f1f920deed54ecbbf0f654cf3b9099779d53bcb4ad480032bd874385ea481c16.jpg)

<details>
<summary>line chart</summary>

| Date       | 2002 Dec | 2009 Dec | 2016 Sep | 2021 Jan | Consensus Fcst. |
|------------|----------|----------|----------|----------|-----------------|
| PPI % YoY  | -12      | -12      | -12      | -12      | -12             |
| 12 month   | -9       | -9       | -9       | -9       | -9              |
| 24 month   | -3       | -3       | -3       | -3       | -3              |
| 3 month     | 0        | 0        | 0        | 0        | 0               |
| 6 month     | 3        | 3        | 3        | 3        | 3               |
| 9 month     | 6        | 6        | 6        | 6        | 6               |
| 12 month    | 9        | 9        | 9        | 9        | 9               |
| 15 month    | 7        | 7        | 7        | 7        | 7               |
| 18 month    | 5        | 5        | 5        | 5        | 5               |
| 21 month    | 3        | 3        | 3        | 3        | 3               |
| 24 month    | 1        | 1        | 1        | 1        | 1               |
</details>

Source: DB, Wind

Figure 2: Pass-through of energy price increases continued  
![](images/387754dc9801c14206aa1256b549dadd9702aa9ef38154287b3b4c77abe678f5.jpg)

<details>
<summary>bar chart</summary>

| Category                  | April | May |
| ------------------------- | ----- | --- |
| Petroleum Extraction      | 18.0  | -   |
| Production & Supply of Gas | -     | -   |
| Ferrous Metal Mining      | -     | -   |
| Non-ferrous Metals Processing | -     | -   |
| Ferrous Metals Processing  | -     | -   |
| Rubber & Plastic Products  | -     | -   |
| Chemical Fibres           | -     | -   |
| Chemical Materials & Products | 8.0   | -   |
| Coal Mining               | -     | 3.0 |
| Production & Supply of Gas  | -     | -   |
</details>

Source: DB, Wind

Figure 3: CPI was unchanged at 1.2% YoY, while core CPI slowed to 1.1% YoY  
![](images/1143cd4ab75313c02e7e7cecfe2fe7c20666eb4170748013014648df07e34241.jpg)

<details>
<summary>line chart</summary>

| Year | Headline | Core |
|------|----------|------|
| '15  | 1.0      | 1.5  |
| '16  | 1.8      | 1.7  |
| '17  | 2.5      | 2.0  |
| '18  | 2.0      | 1.8  |
| '19  | 2.8      | 1.5  |
| '20  | 5.5      | 1.0  |
| '21  | -0.5     | 0.5  |
| '22  | 1.5      | 1.0  |
| '23  | 2.8      | 0.8  |
| '24  | -0.8     | 0.5  |
| '25  | 0.5      | 1.0  |
</details>

Source: DB, Wind

Figure 4: Energy price increases continued to support CPI inflation  
![](images/255c2f3806a0e03188d062fdf67bde8413fcb10ed63df478669decc7c9d455d6.jpg)

<details>
<summary>stacked bar chart</summary>

| Month | Pork (%) | Energy and fuels (%) | Transport & communication (%) | Education & health care (%) | Other food (%) | Rent, HH goods & services (%) | Travel (%) | CPI (%) |
|---|---|---|---|---|---|---|---|---|
| Jan-24 | -0.8 | 0.1 | -0.1 | 0.5 | -0.9 | 0.1 | 0.1 | -0.7 |
| Apr-24 | 0.1 | 0.1 | -0.3 | 0.7 | 0.3 | 0.1 | 0.1 | 0.3 |
| Jul-24 | 0.3 | 0.4 | -0.4 | 0.8 | 0.2 | 0.1 | 0.1 | 0.2 |
| Oct-24 | 0.2 | 0.3 | -0.3 | 0.6 | 0.3 | 0.1 | 0.1 | 0.2 |
| Jan-25 | 0.1 | 0.1 | -0.5 | 0.4 | 0.2 | 0.1 | 0.1 | 0.1 |
| Apr-25 | 0.1 | 0.1 | -0.3 | 0.3 | 0.2 | 0.1 | 0.1 | 0.1 |
| Jul-25 | -0.1 | -0.2 | -0.4 | 0.4 | -0.1 | 0.1 | 0.1 | -0.3 |
| Oct-25 | -0.2 | -0.3 | -0.5 | 0.5 | -0.2 | 0.1 | 0.1 | -0.2 |
| Jan-26 | -0.3 | -0.4 | -0.6 | 0.6 | -0.3 | 0.1 | 0.1 | 0.7 |
| Apr-26 | -0.3 | -0.4 | -0.6 | 0.6 | -0.3 | 0.1 | 0.1 | 1.2 |
The chart displays a stacked bar chart with categories including 'Pork', 'Energy and fuels', 'Transport & communication', 'Education & health care', 'Other food', 'Rent, HH goods & services', 'Travel', and 'CPI'. The values for each category are labeled on top of each bar.
</details>

Source: DB, Wind

Figure 5: Core inflation declined on a MoM basis  
![](images/7a8a80f0ad5d0b5acc75b44a7799d94cd14b25dd4053699cfda6fdef07b2ba65.jpg)

<details>
<summary>area chart</summary>

| Month | 2022-25 interval (%) | 2026 (%) |
|---|---|---|
| Feb | 0.38 | 0.51 |
| Mar | -0.64 | -0.71 |
| Apr | 0.19 | 0.21 |
| May | -0.18 | -0.11 |
| Jun | 0.08 | -0.05 |
| Jul | 0.48 | 0.10 |
| Aug | -0.21 | -0.03 |
| Sep | 0.05 | 0.01 |
| Oct | 0.20 | 0.01 |
| Nov | -0.31 | -0.06 |
| Dec | 0.19 | 0.03 |
</details>

Source: DB, Wind

Figure 6: Food inflation rebounded slightly but was still in negative territory  
![](images/8f00567f88ba04376cc7abf4f5cbcbc04b06fe6160f9b52491a0f80b916c1b34.jpg)

<details>
<summary>area chart</summary>

| Month | 2022-25 interval (%) | 2026 (%) |
|---|---|---|
| Feb | 1.8 | 1.0 |
| Mar | -1.3 | -2.8 |
| Apr | 0.9 | -1.4 |
| May | -0.2 | -0.5 |
| Jun | -1.7 | -0.3 |
| Jul | 3.0 | -0.1 |
| Aug | 3.4 | 0.5 |
| Sep | 1.8 | 0.3 |
| Oct | 0.3 | -0.2 |
| Nov | 0.5 | -2.8 |
| Dec | 0.9 | -0.6 |
</details>

Source: DB, Wind

Figure 7: We revise down the full-year CPI forecast to 1.5% from 1.6%  
![](images/7ec3a420b7229f7a9ae4a3b42ae3f53ed3e812de5232ac5b9057e26600ac0c90.jpg)

<details>
<summary>line chart</summary>

| Year | % YoY |
|------|-------|
| 2018 | ~2.5  |
| 2019 | ~2.0  |
| 2020 | ~5.5  |
| 2021 | ~-0.5 |
| 2022 | ~2.5  |
| 2023 | ~2.0  |
| 2024 | ~-0.5 |
| 2025 | ~0.5  |
| 2026 | ~1.5  |
| 2027 | ~3.0  |
</details>

Source: DB, Wind

Figure 8: PPI reflation emerged in mid- and downstream sectors  
![](images/bf64813992817fe75be2970e1ddd73178ac517105c113aa4c94058d98bcd2103.jpg)

<details>
<summary>line chart</summary>

| Year | Downstream | Upstream | Midstream |
|------|------------|----------|-----------|
| '20  | -          | 4.5      | -         |
| '21  | -          | 20.0     | 6.0       |
| '22  | 2.5        | 18.0     | 10.5      |
| '23  | -          | 1.0      | -         |
| '24  | -          | -        | -         |
| '25  | -          | 4.0      | -         |
| '26  | -          | 12.0     | 1.5       |
</details>

Source: DB, Wind

Figure 9: May inflation momentum

<table><tr><td>%, YoY</td><td>21avg</td><td>22avg</td><td>23avg</td><td>24avg</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Headline CPI</td><td>0.9</td><td>2.0</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.7</td><td>0.8</td><td>0.2</td><td>1.3</td><td>1.0</td><td>1.2</td><td>1.2</td></tr><tr><td>Core CPI</td><td>0.8</td><td>0.9</td><td>0.7</td><td>0.5</td><td>1.2</td><td>1.2</td><td>1.2</td><td>0.8</td><td>1.8</td><td>1.1</td><td>1.2</td><td>1.1</td></tr><tr><td>Food, Tobacco and Liquor</td><td>-0.3</td><td>2.5</td><td>0.3</td><td>-0.1</td><td>-1.6</td><td>0.3</td><td>0.8</td><td>-0.2</td><td>1.4</td><td>0.4</td><td>-1.6</td><td>-1.7</td></tr><tr><td>Clothing</td><td>0.3</td><td>0.5</td><td>1.0</td><td>1.4</td><td>1.7</td><td>1.9</td><td>1.7</td><td>1.9</td><td>1.9</td><td>1.6</td><td>1.5</td><td>1.4</td></tr><tr><td>Housing</td><td>0.8</td><td>0.7</td><td>0.0</td><td>0.1</td><td>0.1</td><td>0.0</td><td>-0.2</td><td>-0.1</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>-0.2</td></tr><tr><td>Household Articles &amp; Services</td><td>0.4</td><td>1.2</td><td>0.1</td><td>0.5</td><td>1.9</td><td>2.1</td><td>2.2</td><td>2.6</td><td>2.8</td><td>1.5</td><td>1.4</td><td>1.8</td></tr><tr><td>Transportation and Communication</td><td>4.2</td><td>5.2</td><td>-2.3</td><td>-1.9</td><td>-1.5</td><td>-2.3</td><td>-2.6</td><td>-3.4</td><td>-0.7</td><td>0.9</td><td>4.6</td><td>5.4</td></tr><tr><td>Recreation, Education and Cultural Srvcs</td><td>1.9</td><td>1.8</td><td>2.0</td><td>1.5</td><td>0.9</td><td>0.8</td><td>0.9</td><td>0.0</td><td>2.0</td><td>1.1</td><td>1.3</td><td>1.3</td></tr><tr><td>Medicine, Medical Care, Personal Articles</td><td>0.4</td><td>0.6</td><td>1.1</td><td>1.3</td><td>1.4</td><td>1.6</td><td>1.8</td><td>1.7</td><td>1.9</td><td>1.9</td><td>2.2</td><td>2.1</td></tr><tr><td colspan="13"></td></tr><tr><td>PPI</td><td>8.1</td><td>4.2</td><td>-3.0</td><td>-2.2</td><td>-2.1</td><td>-2.2</td><td>-1.9</td><td>-1.4</td><td>-0.9</td><td>0.5</td><td>2.8</td><td>3.9</td></tr><tr><td>Mining &amp; Quarrying</td><td>34.8</td><td>18.7</td><td>-7.6</td><td>-2.8</td><td>-7.8</td><td>-6.1</td><td>-4.7</td><td>-8.1</td><td>-5.3</td><td>2.0</td><td>10.6</td><td>15.8</td></tr><tr><td>Raw Materials</td><td>15.9</td><td>10.7</td><td>-4.3</td><td>-1.6</td><td>-2.5</td><td>-2.9</td><td>-2.6</td><td>-2.0</td><td>-1.9</td><td>1.1</td><td>7.1</td><td>9.2</td></tr><tr><td>Manufacturing</td><td>6.7</td><td>1.6</td><td>-3.3</td><td>-2.9</td><td>-1.9</td><td>-1.9</td><td>-1.6</td><td>-0.4</td><td>0.3</td><td>0.9</td><td>1.5</td><td>2.3</td></tr></table>

Source: DB, Wind

## Appendix 1

## Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst(s). In addition, the undersigned lead analyst(s) has not and will not receive any compensation for providing a specific recommendation or view in this report. Deyun Ou, Yi Xiong, Ph.D..

## Important Disclosures

Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For further information regarding disclosures relevant to DB, please visit our global disclosure look-up page on our website at

https://research.db.com/Research/Disclosures/FICCDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Additional Information

The information and opinions in this report were prepared by DB AG or one of its affiliates (collectively 'DB'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, DB makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. DB neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of DB in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a DB analyst, DB may act as principal for its own account or as agent for another person.

DB may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within DB, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. DB issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communication may differ from recommendations contained in others, whether as a result of differing time horizons, methodologies, perspectives or otherwise. DB and/or its affiliates may also be holding debt or equity securities of the issuers it writes on. Analysts are paid in part based on the profitability of DB AG and its affiliates, which includes investment banking, trading and principal trading revenues.

Opinions, estimates and projections constitute the current judgment of the author as of the date of this report. They do not necessarily reflect the opinions of DB and are subject to change without notice. DB provides liquidity for buyers and sellers of securities issued by the companies it covers. DB analysts sometimes have shorter-term trade ideas that may be inconsistent with DB's existing longer-term ratings. Some trade ideas for equities are listed as Catalyst Calls on the Research Website (https://research.db.com/Research/), and can be found on the general coverage list and also on the covered company's page. A Catalyst Call represents a high-conviction belief by an analyst that a stock will outperform or underperform the market and/or a specified sector over a time frame of no less than two weeks and no more than three months. In addition to Catalyst Calls, analysts may occasionally discuss with our clients, and with DB salespersons and traders, trading strategies or ideas that reference catalysts or events that may have a near-term or medium-term impact on the market price of the securities discussed in this report, which impact may be directionally counter to the analysts' current 12-month view of total return or investment return as described herein. DB has no obligation to update, modify or amend this report or to otherwise notify a recipient thereof if an opinion, forecast or estimate changes or becomes inaccurate. Coverage and the frequency of changes in market conditions and in both general and company-specific economic prospects make it difficult to update research at defined intervals. Updates are at the sole discretion of the coverage analyst or of the Research Department Management, and the majority of reports are published at irregular intervals. This report is provided for informational purposes only and does not take into account the particular investment objectives, financial situations, or needs of individual clients. It is not an offer or a solicitation of an offer to buy or sell any financial instruments or to participate in any particular trading strategy. Target prices are inherently impreci

[中间内容因长度限制已省略]

written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau  
Group Chief Economist and Global Head of Research

<table><tr><td>Pam Finelli
COO and Head of Fixed Income Research</td><td>Steve Pollard
Global Head of Company Research and Sales</td><td>Jim Reid
Global Head of Macro and Thematic Research</td><td>Tim Rokossa
Head of European Company Research</td></tr><tr><td>Matthew Barnard
Head of Americas
Company Research</td><td>Debbie Jones
Global Head of Sustainability and Data Innovation, Research</td><td>Robin Winkler
Head of German Macro Research</td><td>Sameer Goel
Global Head of EM &amp; APAC Research</td></tr><tr><td>Francis Yared
Global Head of Rates Research</td><td>George Saravelos
Global Head of FX Research</td><td>Peter Hooper
Vice-Chair of Research</td><td>Nilendra de-Mel
Head of APAC &amp; Middle East Product Development</td></tr></table>

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce Centre</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip Streets</td><td>60329 Frankfurt am Main Germany</td><td>1 Austin Road West, Kowloon, Hong Kong</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Sydney, NSW 2000 Australia</td><td>Tel: (49) 69 910 00</td><td>Tel: (852) 2203 8888</td><td>Japan Tel: (81) 3 6730 1000</td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr><tr><td>DB AG</td><td>DB Securities Inc.</td><td>DB AG</td><td></td></tr><tr><td>21 Moorfields London EC2Y 9DB United Kingdom Tel: (44) 20 7545 8000</td><td>The DB Center 1 Columbus Circle New York, NY 10019 Tel: (1) 212 250 2500</td><td>Filiale Singapur One Raffles Quay, South Tower Singapore 048583 Tel: (65) 6423 8001</td><td></td></tr></table>
"""
