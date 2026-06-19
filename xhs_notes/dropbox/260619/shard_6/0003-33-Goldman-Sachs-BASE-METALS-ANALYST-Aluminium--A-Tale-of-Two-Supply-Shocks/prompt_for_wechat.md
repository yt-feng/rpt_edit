你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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
Indonesia: Total production; Malaysia: Indonesia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Indonesia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Indonesia: Malaysia; Malaysia: Indonesia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Malaysia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indonesian Indonesia; Malaysia: Indian Ocean & Coastal Oceans (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) (Mt) - Indonesia, China, India, Japan, South Korea, Singapore, Philippines, Vietnam, Thailand, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Singapore, Philippines, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladesh, Bangladeshi Islands & Palau & Kiribati & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto & Kanto / Kazakhstan / Kazakhstan / Pakistan / Iran / Nepal / Bhutan / Sri Lanka / Sri Lanka / Nepal / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka/ Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / Sri Lanka / S

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
