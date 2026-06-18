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
# Oil Tracker: 70% of Pre-War Hormuz Flows Might Become the New 100%

\- Spot Brent futures prices slipped below \$80/bbl this week as the US and Iran reached an interim deal that would lift the US blockade and reopen the Strait of Hormuz right after the deal is signed, with the US and Iran reportedly signing the Memorandum of Understanding Wednesday night electronically.

☐ The interim deal reportedly includes a waiver for exports of Iranian oil and petrochemicals and for related financial and transportation services, potentially unlocking over 50mb of Iranian oil on water overhang for immediate delivery.  
☐ We now assume that Persian Gulf exports normalize to pre-war levels by end of July and Persian Gulf crude production recover by October and see risks to the Mideast supply outlook as two-sided, but skewed to the downside on net.

☐ We estimate that this normalization in Gulf exports to pre-war levels might be achieved with a 13mb/d increase in Hormuz flows from current levels to around 70% of pre-war levels (Exhibit 3).

We estimate average visible Hormuz flows at 1.3mb/d over the 7 days, Gulf of Oman flows (which might be linked to “dark” Hormuz crossings) at 1.6mb/d, and redirections via Yanbu, Fujairah, and Ceyhan at 7.5mb/d.

☐ We do not see ship availability as a binding constraint on the recovery of flows as we estimate 860mb of empty tanker capacity within the Strait or within 5 days of navigation (Exhibit 6).

However, many shipowners reportedly remain cautious about clear guidelines for transit, and we see shippers' risk aversion as a potential constraint on the flows, along with Iran's geopolitical goals over the upcoming 60-day nuclear deal negotiations.

The IEA estimates in its latest Oil Market Report a Q2 deficit of 3.1mb/d, below our estimate of a 5.0mb/d deficit, given larger Q2 demand destruction of 5.5mb/d vs. GS at 4.9mb/d, peaking in May at 6.1mb/d (Exhibit 1).

☐ Across products, IEA demand loss estimates are concentrated in petrochemical feedstocks, consistent with our analysis.

\- The IEA downgraded LPG and ethane demand by -1.7mb/d or -11% (vs. February expectations) and naphtha demand by -1.1mb/d or 15%.

Yulia Zhestkova Grigsby

+1(646)446-3905

yulia.grigsby@gs.com

GS & Co. LLC

Filippo Cuscito

+44(20)7051-9073

filippo.cuscito@gs.com

GS International

Alexandra Paulus

+1(212)902-7111

alexandra.paulus@gs.com

GS & Co. LLC

Daan Struyven

+1(212)357-4172

daan.struyven@gs.com

GS & Co. LLC

☐ Across regions, demand losses are the largest in Asia and Middle East, as the IEA downgraded China total oil demand by -2.2mb/d or -13%, Asia ex China by -1.5mb/d or -7%, and Middle East demand by -10%.

☐ The IEA revised up its Persian Gulf production losses, with total liquids production from Iran, Iraq, Kuwait, Qatar, Saudi Arabia, and UAE declining in Q2 by 18.9mb/d from its February level.

\- The IEA keeps its assumption that Hormuz flows recovery starts in 2026Q3 and will take several months.

☐ The IEA also released their first 2027 balance and expects an average global surplus of 5.0mb/d (vs. GS at 3.2mb/d) on strong 7.9mb/d YoY supply growth and some lingering demand weakness.

While China accounts for $40\%$ of estimated global oil demand destruction at about 2mb/d, China crude imports dropped more sharply by 4.2mb/d YoY.

☐ Taking into account recent China crude net imports, production, and crude throughput, we estimate crude stock draws at 1.6mb/d in May vs. 0.3mb/d draws in visible stocks (Exhibit 2).

☐ This -1.3mb/d difference is likely driven by either meaningful invisible crude destocking (e.g. underground SPR) and/or even lower crude demand (lower refinery runs) than official data implies.

☐ Lower China oil demand would be consistent with weaker China April-May economic activity and our estimates of a 23% year-over-year drop in China gasoline and other retail oil products sales volumes in May (Exhibit 18).

## Charts of the Week

Exhibit 1: IEA Revises Down May World Oil Demand by 6.1mb/d in Latest Oil Market Report vs. the February Pre-War Estimates

<table><tr><td colspan="4">IEA May Demand Forecast Revisions (June vs. February Oil Market Report), mb/d</td></tr><tr><td>Total World Oil Deman</td><td colspan="3">-6.1</td></tr><tr><td colspan="2">by Product</td><td colspan="2">by Geography</td></tr><tr><td>LPG and Ethane</td><td>-1.7</td><td>China</td><td>-2.2</td></tr><tr><td>Diesel and Gasoil</td><td>-1.2</td><td>Asia ex China</td><td>-1.5</td></tr><tr><td>Naphtha</td><td>-1.1</td><td>Middle East</td><td>-1.0</td></tr><tr><td>Motor Gasoline</td><td>-0.8</td><td>Europe</td><td>-0.8</td></tr><tr><td>Jet Fuel and Kerosene</td><td>-0.5</td><td>Rest of World</td><td>-0.6</td></tr><tr><td></td><td></td><td>US</td><td>0.0</td></tr></table>

Source: IEA, GS Global Investment Research

Exhibit 2: China Implied Estimated Stock Draws Exceeded Visible Draws by 1.3mb/d in May, Suggesting Either Meaningful Invisible Strategic Destocking or Lower Crude Demand (i.e. Lower Refinery Runs)

<table><tr><td colspan="5">China Oil Balances, mb/d</td></tr><tr><td></td><td colspan="2">May</td><td colspan="2">May-March Average</td></tr><tr><td></td><td>Crude</td><td>Refined Products</td><td>Crude</td><td>Refined Products</td></tr><tr><td>1) Domestic Production</td><td>4.3</td><td>12.7</td><td>4.4</td><td>13.5</td></tr><tr><td>2) Net Imports</td><td>6.8</td><td>-0.1</td><td>8.4</td><td>0.0</td></tr><tr><td>3) Demand</td><td>12.7</td><td>12.5</td><td>13.5</td><td>12.9</td></tr><tr><td>4) Implied Change in Stocks: (1) + (2) - (3)</td><td>-1.6</td><td>0.2</td><td>-0.8</td><td>0.7</td></tr><tr><td>5) Visible Change in Stocks</td><td>-0.3</td><td>-0.1</td><td>0.2</td><td>0.1</td></tr><tr><td>Estimated Invisible Stock Changes: Implied Minus Visible Gap: (4) - (5)</td><td>-1.3</td><td>0.3</td><td>-1.0</td><td>0.6</td></tr></table>

We combine estimates of domestic production from the IEA, net imports and visible changes in stocks from Kpler and Oilchem, crude demand (i.e. refinery runs) from NBS, and refined products demand from S&P Global Market Intelligence.

Source: China National Bureau of Statistics, Kpler, S&P Global Market Intelligence, Oilchem, GS Global Investment Research

## 1) Persian Gulf Exports

Exhibit 3: Normalization in Oil Exports From Gulf Producers to Their Pre-War Level May Be Achieved With a 12.7mb/d Increase in Hormuz Flows From Current Levels  
![](images/1de4d3c3f54b727d06781d50728805b8d12d9e060f46d1f815cd8cc944f561fb.jpg)

<details>
<summary>bar chart</summary>

Estimating Mid June Hit to Oil Flows from Persian Gulf Countries
| Flow | Non-Hormuz Flows (mb/d) | Pre-War Flows (mb/d) | Total (mb/d) |
| :--- | :--- | :--- | :--- |
| Strait of Hormuz | -1.3 | 20.0 | 23.1 |
| Gulf of Oman | -1.6 | 22.0 | 24.0 |
| Yanbu (Saudi) | -4.6 | 21.0 | 23.5 |
| Fujairah (UAE) | -2.7 | 20.0 | 23.5 |
| Botas Ceyhan | -0.2 | 20.0 | 23.5 |
| Net Hit | 12.7 | 20.0 | 13.0 |
</details>

Yanbu is on the west coast of Saudi Arabia, bordering the Red Sea and connected to Saudi eastern oil fields via the East-West pipeline. Fujairah lies east (outside) of the Strait of Hormuz and is connected to Abu Dhabi's onshore fields via the Abu Dhabi Crude Oil Pipeline (ADCOP). The Gulf of Oman connects the Strait to the Arabian Sea (southeast). The Kirkuk-Ceyhan pipeline allows northern Iraqi crude to be pumped through Turkey to the Mediterranean sea.

Source: Kpler, S&P Global Commodities at Sea, GS Global Investment Research

Exhibit 4: We Estimate That 1.3mb/d of Visible OECD SPR Releases Have Reduced the Estimated Hit to Global Commercial Oil Stocks Since March by 1.3mb/d to 4.3mb/d  
![](images/fb4e15950b2f32345fdde7a8b20f2d9980f672627831eb7b4b05090b1dc9310e.jpg)

<details>
<summary>bar chart</summary>

Average Hit to Global Commercial Oil Stocks Since March 1 mb/d
| Category | Value (mb/d) |
|---|---|
| Global Oil Estimated Inventory Draws | 5.5 |
| OECD SPR Release | 1.3 |
| Non-OECD SPR Release | 0.0 |
| Global Commercial Oil Estimated Inventory Draws | 4.3 |
</details>

![](images/1af7848618397fcf1221bf3ed46f63906944d56c25b9949df935badc2429a499.jpg)

<details>
<summary>line chart</summary>

| Date       | Change Since March 1 (mb) | Change Over Last 30 Days (mb/d) |
| ---------- | ------------------------- | -------------------------------- |
| March 1    | -137                      | -1.3                             |
| Last 30    | -0.8                      | -0.8                             |
</details>

We estimate global oil inventory draws from latest GS oil balance.  
Source: Kpler, GS Global Investment Research

Exhibit 5: The Estimated Total Hit to Oil Flows from the Persian Gulf Is Currently at 14.8mb/d (4-Day Moving Average)  
![](images/e47fa528659110ea8d15a49aa41cb1512ce359e9d2a62a411969bb739d221c6b.jpg)

<details>
<summary>bar-line hybrid</summary>

Estimated Oil Flows From Persian Gulf Countries Percent of Normal
| Month | Strait of Hormuz (mb/d) | Strait of Hormuz (mb/d) | Yanbu, Fujairah, Gulf of Oman, Botas Ceyhan (mb/d) |
|---|---|---|---|
| Mar Avg | 1.5 | 20.0 | 7.3 |
| Apr Avg | 2.5 | 2.8 | 9.8 |
| May Avg | 2.0 | 2.0 | 8.8 |
| Jun 03 | 2.0 | 1.5 | 14.5 |
| Jun 04 | 1.5 | 1.5 | 3.5 |
| Jun 05 | 1.5 | 1.5 | 16.0 |
| Jun 06 | 2.5 | 2.5 | 8.2 |
| Jun 07 | 1.0 | 1.0 | 13.8 |
| Jun 08 | 3.0 | 2.8 | 12.5 |
| Jun 09 | 2.5 | 2.5 | 11.3 |
| Jun 10 | 1.5 | 1.5 | 7.8 |
| Jun 11 | 2.5 | 2.5 | 15.2 |
| Jun 12 | 1.5 | 1.5 | 16.0 |
| Jun 13 | 0.5 | 0.5 | 6.0 |
| Jun 14 | 2.0 | 2.0 | 10.8 |
| Jun 15 | 1.0 | 1.0 | 8.8 |
| Jun 16 | 1.0 | 1.0 | 7.8 |
Percent of Normal
Latest Total (4DMA): 8.3 mb/d
Latest Total % of Normal (4DMA): 36%
Latest Additional Flows (4DMA): 7.2 mb/d
Increase vs 2025 Average: 4.1 mb/d
Normal flows are assumed to be 20 mb/d for Strait of Hormuz and 2025 average for Yanbu (1.4 mb/d), Fujairah (1.7 mb/d), Gulf of Oman (0.0 mb/d), and Botas Ceyhan (0.0 mb/d).
</details>

![](images/41584e9068b56ffc816290001471c6f2e5399f4ecf271b9b479ae30918b054a8.jpg)

<details>
<summary>bar-line hybrid</summary>

Estimated Hit to Persian Gulf Oil Exports
| Month | Strait of Hormuz (mb/d) | Redirections (mb/d) | Total, 4-Day Moving Average (mb/d) | Latest Level Total (4DMA) (mb/d) |
|---|---|---|---|---|
| Mar Avg | 18.5 | -2.0 | 16.0 | 15.5 |
| Apr Avg | 17.5 | -3.5 | 13.5 | 13.0 |
| May Avg | 18.0 | -3.0 | 14.5 | 14.0 |
| Jun 03 | 18.0 | -10.5 | 7.5 | 7.0 |
| Jun 04 | 0.0 | 20.0 | 14.5 | 20.0 |
| Jun 05 | 18.5 | -12.0 | 7.0 | 6.5 |
| Jun 06 | 17.5 | -2.5 | 15.0 | 15.0 |
| Jun 07 | 19.0 | -9.5 | 9.5 | 9.0 |
| Jun 08 | 17.0 | -6.0 | 11.0 | 11.0 |
| Jun 09 | 17.5 | -5.5 | 12.0 | 12.0 |
| Jun 10 | 18.0 | -3.0 | 12.5 | 15.5 |
| Jun 11 | 18.0 | -9.5 | 8.0 | 8.0 |
| Jun 12 | 18.5 | -12.0 | 7.0 | 7.0 |
| Jun 13 | 20.0 | -2.5 | 12.5 | 17.5 |
| Jun 14 | 18.0 | -5.0 | 12.0 | 12.5 |
| Jun 15 | 19.5 | -4.5 | 14.5 | 14.5 |
| Jun 16 | 19.5 | -3.5 | 15.5 | 15.5 |
Hit is calculated relative to normal flows. Redirections include Yanbu, Fujairah, Gulf of Oman, and Botas Ceyhan flows.
</details>

Source: S&P Global Commodities at Sea, Kpler, GS Global Investment Research

Exhibit 6: We Estimate That Empty Oil Tankers Within the Strait or Within 5 Days of Navigation Have the Capacity to Load 861 Million Barrels  
Oil Tanker Capacity on Both Sides of Hormuz  
![](images/bc8db960bad79a1bbf72b50c350e9ee2d6442c45294db5dc04e8e8b24e31bcce.jpg)

<details>
<summary>line chart</summary>

| Date       | Loaded (mb) | Empty (mb) |
| ---------- | ----------- | ---------- |
| March      | 350         | 300        |
| April      | 300         | 150        |
| May        | 300         | 120        |
| June       | 280         | 110        |
| July       | 241         | 114        |
</details>

![](images/594f42a932fee5933ca22c1c3c4a0a6f9713fcca64ce6a6bf35a0b3196c7cf40.jpg)

<details>
<summary>line chart</summary>

| Date       | Ceasefire (mb) | Loaded (mb) | Empty (mb) |
| ---------- | -------------- | ----------- | ---------- |
| Apr        | 650            | 496         | 747        |
</details>

We consider vessels in: Arabian Sea, Gulf of Oman, Yemeni waters.  
Source: Kpler, GS Global Investment Research

Exhibit 7: 28% of the Hit to Persian Gulf Crude/Condensate Exports Is Currently Being Offset, With Contributions From Higher Exports from the US/Americas Ex US/Russia of 16pp/8pp/5pp  
Global Oil Exports vs. 2025 Average  
![](images/ed965688bf4f05d63f95f99bf81bac8f29c0558888ad91665f60ca7ed93db5ce.jpg)

<details>
<summary>area chart</summary>

| Month    | Total (mb/d) | Rest of World (mb/d) | Persian Gulf (mb/d) | Russia (mb/d) | Americas Ex US (mb/d) | United States (mb/d) |
|----------|--------------|----------------------|---------------------|---------------|------------------------|----------------------|
| Feb 2026 | -1           | 0                    | 0                   | 0             | 0                      | 0                    |
| Mar      | 2            | 1                    | 1                   | 0             | 0                      | 0                    |
| Apr      | -6           | 1                    | -4                  | 0             | 0                      | 0                    |
| May      | -4           | 3                    | -8                  | 1             | 1                      | 1                    |
| Jun      | -6           | 2                    | -10                 | 1             | 1                      | 1                    |
</details>

![](images/2a587d875725edf7faba4d4f7b7b77c7f171a2fe1ae32bb2d53bbb1112457a09.jpg)

<details>
<summary>area chart</summary>

| Month    | Total | Rest of World | Persian Gulf | Russia | Americas Ex US | United States |
| -------- | ----- | ------------- | ------------ | ------ | -------------- | ------------- |
| Feb 2026 | 1.0   | 0.5           | 0.3          | 0.1    | 0.1            | 0.1           |
| Mar      | -0.5  | -0.3          | -0.2         | 0.1    | 0.1            | 0.1           |
| Apr      | -4.0  | -5.0          | -1.0         | 0.1    | 0.1            | 0.1           |
| May      | -5.0  | -5.5          | -1.5         | 0.1    | 0.1            | 0.1           |
| Jun      | -4.5  | -5.0          | -1.5         | 0.1    | 0.1            | 0.1           |
</details>

Refined products include LPG.  
Source: Kpler, GS Global Investment Research

## 2) Inventories

Exhibit 8: China Landed Visible Inventories Have Drawn by 0.5mb/d Over the Last 14 Days  
Global Visible Total Oil Inventories, Change Since Feb 27  
![](images/2be2f22b8a4de1dc27992c1acd1bd5e2803b0e5a50a4d84b53661bef398cdd95.jpg)

<details>
<summary>line chart</summary>

| Date    | China | India | Middle East | Asia ex China ex India | Rest of World |
|---------|-------|-------|-------------|--------------------------|---------------|
| Feb     | -10   | 0     | 0           | 0                        | -30           |
| Mar     | 0     | 0     | 0           | 0                        | 0             |
| Apr     | 20    | -10   | 10          | -50                      | -70           |
| May     | 40    | -20   | 20          | -80                      | -120          |
| Jun     | 10    | -10   | -10         | -100                     | -200          |
</details>

![](images/9c6916864018869f9b47b8ce416cde0c1bebb473fd9231f3d5c1845fc2fd8170.jpg)

<details>
<summary>line chart</summary>

| Date       | Floating Storage from Persian Gulf (mb) | Floating Storage from Rest of World (mb) | Oil in Transit from Iran and Russia (mb) | Oil in Transit from Rest of World (mb) |
| ---------- | ---------------------------------------- | ------------------------------------------ | ---------------------------------------- | -------------------------------------- |
| Feb 15     | -10                                      | 0                                          | 10                            

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be

supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
