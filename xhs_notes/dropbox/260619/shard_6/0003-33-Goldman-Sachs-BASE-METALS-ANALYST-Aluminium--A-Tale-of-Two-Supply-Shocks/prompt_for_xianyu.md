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
BASE METALS ANALYST

# Aluminium: A Tale of Two Supply Shocks

Middle East outages keep the aluminium market tighter for longer, even if the Strait reopens. Since our last update, industry feedback and company announcements point to a slower recovery in Middle East production than we had initially assumed. Even if the Strait of Hormuz reopens under the announced interim deal, smelters cannot immediately return to full capacity as damaged potlines need repairs and curtailed capacity must be restarted gradually. Therefore, we nudge higher our Q3 2026/average 2027 LME aluminium price forecasts to \$3,300/\$2,950/t from \$3,200/\$2,750/t previously (Exhibit 1), but remain below forwards at \$3,400/\$3,250/t, as stronger Indonesia and China supply growth — helped by high smelter margins (Exhibit 4) — keeps our medium-term bearish view intact.  
Middle East supply losses persist into 2027. We downgrade Middle East output by \~660kt in 2026 and \~1Mt in 2027, as we now assume damaged capacity restarts in early 2027 rather than H2 2026. We now expect Bahrain output to return to pre-conflict levels by mid-2027 and the UAE by end-2027. Recent precedent points to around a one-year period before output can be fully restored: following the April 2025 Iberian grid outage, Alcoa completed the San Ciprián restart in mid-2026. This leaves the global aluminium market in a 720kt deficit/590kt surplus in 2026/2027 vs. a 570kt deficit/1.3Mt surplus prior, with lower Middle East output partly offset by higher Indonesia and China production (Exhibit 2). This is the tale of two supply shocks: a near-term Middle East shock that tightens the 2026/2027 balance and supports near-term prices, set against a structural China-backed supply wave, led by Indonesia, that increasingly offsets the disruption over time and keeps us bearish further out (Exhibit 7).  
- Indonesia drives medium-term supply growth. We raise our Indonesian primary aluminium production forecast to 1.7Mt in 2026 and 2.9Mt in 2027 from 1.6Mt and 2.5Mt previously (Exhibit 9), reflecting faster ramps at Adaro, Taijing Morowali and Juwan Weda Bay, as well as the inclusion of Harita Danantara Inalum from 2027 (Exhibit 9). Recent data support the ramp, with Indonesian output up around $89\%$ YoY YTD, suggesting projects are progressing broadly in line with the faster supply path. We also have more confidence that power availability is not a binding constraint for the 2026 projects. Expert feedback suggests producers are prioritising fast ramp-ups while margins remain high, supported by captive or dedicated power arrangements and some reallocation

Lavinia Forcellese

+44(20)7774-9243

lavinia.forcellese@gs.com

GS International

Aurelia Waltham

+44(20)7051-2547

aurelia.waltham@gs.com

GS International

Samantha Dart

+1(212)357-9428

samantha.dart@gs.com

GS & Co. LLC

Daan Struyven

+1(212)357-4172

daan.struyven@gs.com

GS & Co. LLC

of power from nickel to aluminium projects in industrial parks. This does not fully offset the Middle East loss in 2026, but Indonesian supply growth underpins our surplus forecast from 2027 onwards, reinforcing our medium-term bearish view once Middle East production starts to recover.

China adds to the supply offset. We raise our China primary aluminium production forecast to 45.6Mt in 2026 and 46.3Mt in 2027, from 45.2Mt and 45.9Mt previously, as strong industry margins support restarts, selected replacement projects and some estimated overproduction above the headline cap (Exhibit 10). Recent data suggest China output has already moved above the headline 45Mt capacity cap on a run-rate basis (Exhibit 11). Expert feedback suggests the YTD strength could reflect unauthorized overproduction, continued operation of old capacity under capacity swap programmes and short-term potline intensification, while the production hit from recent environmental inspections and reported curtailments appears relatively small. This means China can provide another partial offset to lower Middle East output in 2026/27 alongside Indonesia.

■ Two-sided risks around Middle East supply recovery. Risks to our Middle East supply recovery assumption are two-sided, although the announced interim deal to reopen Hormuz has lowered the likelihood of a more severe disruption beyond announced curtailments (Exhibit 12). A slower restart of damaged Middle East capacity would remove around 500kt of 2027 supply versus our base case, keeping the 2027 market fairly balanced and prices around \$3,250/t. A faster restart would add around 600kt of 2027 supply, lifting the surplus toward 1.2Mt and bringing prices closer to \$2,750/t.

We close our short Dec-26 LME aluminium trade for a potential loss of \~\$610/t, and roll to a short Dec-27, where our forecast sits furthest below the forward and best expresses our structural surplus view. We also reiterate our long Dec-27 copper vs short Dec-27 aluminium trade (+\$1,965/t since November), where the remaining upside is now concentrated in the aluminium leg. The key risk to both is a lengthier Middle East conflict or slower restart of disrupted capacity, keeping aluminium higher for longer and delaying the move to our forecast surplus.

## A Tale of Two Supply Shocks

Exhibit 1: We Raise our 2027 Price Forecast to \$2,950 But Our Forecast Stays Well Below the Forwards  
![](images/f2e006c3e0b79a58c80a44f2b0d13d24e340b00b7dd246942d2de36c52473890.jpg)

<details>
<summary>line chart</summary>

LME Aluminium Price
| Year | Aluminium Price ($/t) | GS Forecast New ($/t) | GS Forecast Prior ($/t) | Futures ($/t) |
|---|---|---|---|---|
| 2022 | 3500 | 3500 | 3500 | 3500 |
| 2023 | 2500 | 2500 | 2500 | 2500 |
| 2024 | 2300 | 2300 | 2300 | 2300 |
| 2025 | 2600 | 2600 | 2600 | 2600 |
| 2026 | 3100 | 3100 | 3100 | 3100 |
| 2027 | 3600 | 3300 | 3300 | 3300 |
| 2028 | 3100 | 2800 | 2700 | 3100 |
| 2029 | 3100 | 2750 | 2700 | 3100 |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 2: We Expect the Global Aluminium Market to Shift into a Smaller Surplus in 2027 Than Previously Forecast on Lower Middle East Supply  
![](images/01da3d335a7b29038ecd5410cff009bb19f712be77729a478099f06c00f8a6a0.jpg)

<details>
<summary>bar chart</summary>

Global Aluminium Market Balance
| Year | New (kt) | Mar-26 (kt) |
|---|---|---|
| 2023 | 500 | |
| 2024 | 150 | |
| 2025 | -300 | |
| 2026E | -700 | -500 |
| 2027E | 600 | 1300 |
| 2028E | 2050 | 1800 |
| 2029E | 2200 | 1950 |
| 2030E | 850 | 150 |
</details>

Source: CRU, Wood Mackenzie, SMM, GS Global Investment Research

Exhibit 3: We Expect a Larger Q3 Deficit Before the Market Returns to Surplus in Q4  
![](images/b598a5280ec833e18f1236de37ebba0ba4e4c66cf36e05828bba214854cb479b.jpg)

<details>
<summary>bar chart</summary>

Primary Aluminium Market Balance
| Quarter | New (kt) | Mar-26 (kt) |
| :--- | :--- | :--- |
| Q1 | 700 | 800 |
| Q2 | -1200 | -1250 |
| Q3 | -500 | -400 |
| Q4 | 200 | 150 |
</details>

Source: CRU, Wood Mackenzie, SMM, GS Global Investment Research

## High Smelter Margins Support Stronger Supply Growth

Exhibit 4: Aluminium Production Margins Are Approaching the 2022 Highs  
![](images/0db0cfb8038c3164bb4302b09696597d90ba463a6631c9be8cfcdfb430766ed6.jpg)

<details>
<summary>line chart</summary>

| Year | Min-max range | Average (quarterly-reporting companies only) |
|------|---------------|-----------------------------------------------|
| 2018 | ~5%           | ~10%                                          |
| 2019 | ~-5%          | ~0%                                           |
| 2020 | ~10%          | ~15%                                          |
| 2021 | ~-5%          | ~15%                                          |
| 2022 | ~55%          | ~30%                                          |
| 2023 | ~-15%         | ~5%                                           |
| 2024 | ~-5%          | ~10%                                          |
| 2025 | ~10%          | ~15%                                          |
| 2026 | ~55%          | ~25%                                          |
</details>

Source: Company filings, GS Global Investment Research

Exhibit 5: Low Inventory Cover Supports Higher Smelter Margins  
![](images/38d19163100c5fd9dc690d215984a3c408c98dcf41257a3a54ed98efd3fa7ab1.jpg)

<details>
<summary>line chart</summary>

Aluminium Inventories as Days of Consumption
| Quarter | Aluminium Inventories as Days of Consumption |
|---|---|
| 1Q 2018 | 68 |
| 2Q 2018 | 65 |
| 3Q 2018 | 60 |
| 4Q 2018 | 58 |
| 1Q 2019 | 55 |
| 2Q 2019 | 50 |
| 3Q 2019 | 47 |
| 4Q 2019 | 45 |
| 1Q 2020 | 65 |
| 2Q 2020 | 63 |
| 3Q 2020 | 60 |
| 4Q 2020 | 55 |
| 1Q 2021 | 50 |
| 2Q 2021 | 48 |
| 3Q 2021 | 47 |
| 4Q 2021 | 48 |
| 1Q 2022 | 50 |
| 2Q 2022 | 48 |
| 3Q 2022 | 47 |
| 4Q 2022 | 48 |
| 1Q 2023 | 50 |
| 2Q 2023 | 48 |
| 3Q 2023 | 49 |
| 4Q 2023 | 48 |
| 1Q 2024 | 50 |
| 2Q 2024 | 48 |
| 3Q 2024 | 49 |
| 4Q 2024 | 48 |
| 1Q 2025 | 50 |
| 2Q 2025 | 47 |
| 3Q 2025 | 46 |
| 4Q 2025 | 48 |
| 1Q 2026 | 50 |
| 2Q 2026 | 45 |
| 3Q 2026 | 41 |
| 4Q 2026 | 43 |
| 1Q 2027 | 44 |
| 2Q 2027 | 44 |
The chart displays the percentage of inventory consumed by aluminium inventories over time (in days). The x-axis represents time periods from Q1 of each year, and the y-axis represents the percentage of inventory consumed. There is no label for the data series. The values are estimated based on the visual scale.
</details>

![](images/86e983dd56156dfc5eef322a68f7e6c7c426f9ebfc241a7233ccef61f77b5a9a.jpg)

<details>
<summary>scatter plot</summary>

| Year       | Smelter Margins (%) | Inventories As Days Of Consumption |
|------------|---------------------|------------------------------------|
| 2004-2024  | ~30                 | ~45                                |
| 2025       | ~15                 | ~48                                |
| 2026       | ~45                 | ~42                                |
| 2027       | ~35                 | ~45                                |
</details>

Total stocks include visible liquid inventories, including LME, SHFE, CME, Japan port stocks and China social inventories, as well as producer inventories, government stockpiles and estimated unreported inventories. RHS observations are quarterly. Data from 2004–2024, excluding the period from Q4 2009–Q4 2011 when LME warehouse queues impacted prices.  
Source: Bloomberg, CRU, GS Global Investment Research

## A China-Backed Supply Wave Offsets the Middle East Shock Over Time

Exhibit 6: Two Supply Shocks: Middle East Output Falls, Indonesia Supply Catching Up  
![](images/1c81517ff8103d1c377fa277028a39548f58a583c97c6f37f801c5736c9fbc8a.jpg)

<details>
<summary>line chart</summary>

Aluminium Production Share
| Quarter | Indonesia (%) | Middle East (%) |
|---|---|---|
| Q2 2025 | 1.0 | 9.3 |
| Q3 2025 | 1.0 | 9.3 |
| Q4 2025 | 1.0 | 9.3 |
| Q1 2026 | 1.5 | 8.8 |
| Q2 2026 | 2.0 | 5.3 |
| Q3 2026 | 2.5 | 5.3 |
| Q4 2026 | 2.8 | 5.1 |
| Q1 2027 | 3.0 | 5.8 |
| Q2 2027 | 3.5 | 6.5 |
| Q3 2027 | 3.8 | 7.1 |
| Q4 2027 | 4.0 | 7.9 |
</details>

Source: CRU, SMM, GS Global Investment Research

Exhibit 7: We Expect Indonesia and China Production Growth to Partly Offset Middle East Losses  
![](images/76d478b9c79ca046fb703e7c176cd340efe18938e28eb60470d56e5d5a6dca9c.jpg)

<details>
<summary>stacked bar chart</summary>

Global Primary Aluminium Production YoY Growth
| Year | Total (kt) | China (kt) | Indonesia (kt) | Rest of World (kt) | Middle East (kt) |
|---|---|---|---|---|---|
| 2025 | 1400 | 800 | 100 | 100 | 1400 |
| 2026 | -200 | 1000 | 700 | 100 | -200 |
| 2027 | 3500 | 600 | 1100 | 900 | 1800 |
| 2028 | 3100 | -100 | 800 | 1100 | 1600 |
| 2029 | 2200 | -150 | 1000 | 900 | 300 |
| 2030 | 800 | 0 | 300 | 400 | 800 |
</details>

Source: CRU, SMM, GS Global Investment Research

## Indonesia Drives Medium-Term Supply Growth

Exhibit 8: We Raise Our Indonesian Primary Aluminium Production Forecast to 1.7Mt in 2026 and 2.9Mt in 2027  
![](images/e36ea62e47e265440f1a871161adeae9510b411d0d784210b4dcc835088dc6d5.jpg)

<details>
<summary>bar chart</summary>

Indonesia Primary Aluminium Production
| Year | New (Mt) | Mar-26 (Mt) |
|---|---|---|
| 2025 | 0.8 | 0.8 |
| 2026E | 1.7 | 1.5 |
| 2027E | 2.9 | 2.4 |
| 2028E | 3.8 | 3.3 |
| 2029E | 4.9 | 4.1 |
| 2030E | 5.2 | 4.3 |
</details>

Source: CRU, GS Global Investment Research

Exhibit 9: We Include Harita Group Smelter from 2027 in Our Base Case  
![](images/95f49045a734bcc6be8479821306274780c8bc54e6d8b26be734307fa049558c.jpg)

<details>
<summary>stacked bar chart</summary>

Indonesia Primary Aluminium Production, Million Tonnes
| Year | Inalum (Mt) | Tsingshan+Huafon (Mt) | Tsingshan+Xinfa Weda Bay (Mt) | Tsingshan+Xinfa Morowali (Mt) | Adaro (Mt) | Harita+Innovation Global (Mt) | Nanshan Indonesia (Mt) |
|---|---|---|---|---|---|---|---|
| 2021 | 0.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 2022 | 0.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 2023 | 0.3 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 2024 | 0.3 | 0.2 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 |
| 2025E | 0.4 | 0.3 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 |
| 2026E | 0.4 | 0.4 | 0.3 | 0.2 | 0.2 | 0.1 | 0.1 |
| 2027E | 0.4 | 0.5 | 0.6 | 0.4 | 0.4 | 0.2 | 0.2 |
| 2028E | 0.4 | 0.5 | 0.7 | 0.5 | 0.6 | 0.4 | 0.3 |
| 2029E | 0.4 | 0.5 | 0.8 | 0.6 | 1.1 | 1.1 | 0.5 |
| 2030E | 0.4 | 0.5 | 1.1 | 1.1 | 1.3 | 1.4 | 0.6 |
Indonesia: Total production; Malaysia: Indonesia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Indonesia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Malaysia: Indonesia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia;

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
