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
# Australian and New Zealand Inflation Monitor: Further Indirect Effects From Higher Oil Prices Expected in May

In Australia, headline CPI increased by $0.4\%$ mom in April, though year-over-year inflation decelerated 40bp to $4.2\%$ yoy. Compositionally, a seasonal rebound in garments and holiday travel was partly offset by declines across fuel and urban transport, owing to a temporary reduction in the fuel excise tax and public transport subsidies.

Looking ahead to the May data, we expect headline CPI to fall $0.4\%$ mom, which would leave year-over-year inflation unchanged at $4.2\%$ yoy. In underlying terms, we expect monthly trimmed mean CPI to increase $0.3\%$ mom, taking the year-over-year rate 10bp higher to $3.5\%$ yoy. We flag a higher-than-usual degree of uncertainty in our forecasts this month.

In New Zealand, monthly price data covering around 50% of the CPI basket remained unchanged in May. Compositionally, a decline in fuel and airfare prices was offset by rising food prices, particularly for restaurant meals where there have been some reports of fuel surcharges.

## Australia

Australia's headline CPI increased by 0.4%mom in April, though year-over-year inflation decelerated 40bp to 4.2%yoy. Compositionally, a seasonal rebound in garments, domestic travel and international travel was partly offset by declines across automotive fuel and urban transport – owing to a temporary reduction in the fuel excise tax and public transport subsidies. Looking through the volatility in headline inflation, monthly trimmed mean rose 0.3%mom, with year-over-year growth accelerating 10bp to 3.4%yoy. In quarterly terms, our three-month-on-three-month trimmed mean measure eased 3bp to 0.84%qoq.

Looking ahead to May, we expect headline CPI to fall 0.4%mom, which would leave year-over-year inflation unchanged at 4.2%yoy. Compositionally, our forecast reflects a decline in automotive fuel (GSe: -12.5%mom), alongside lower global crude oil prices, as well as a seasonal fall in domestic airfares (GSe: -7.2%mom) following the Easter holidays. We expect the indirect pass-through of higher fuel prices to intensify in May, particularly across new dwelling purchase (GSe: +0.9%mom), restaurant meals (GSe: +0.7%mom) and takeaway meals (GSe: +0.7%mom).

In underlying terms, we expect monthly trimmed mean CPI to increase 0.3%mom, taking the year-over-year rate 10bp higher to 3.5%yoy. Our forecasts are consistent with a 0.88%qoq increase in our preferred three-month-on-three-month trimmed mean measure.

Andrew Boak, CFA

+61(2)9321-8576

andrew.boak@gs.com

GS Australia Pty Ltd

Will Maher

+61(2)9320-1013 | will.maher@gs.com

GS Australia Pty Ltd

Oscar To

+61(2)9320-1367 | oscar.to@gs.com

GS Australia Pty Ltd

We flag a higher-than-usual degree of uncertainty in this month's forecasts for two reasons: (i) the heightened volatility in fuel prices stemming from both the excise tax reduction and movements in global oil prices; and (ii) May will be the first month in which international airfares reflect the impact of the conflict, as these prices are collected two months in advance.

Exhibit 1: We expect headline CPI and trimmed mean to increase $4.2\%$ yoy and $3.5\%$ yoy respectively in May  
![](images/301553b9934b56c03c139e4890d15897fdd4bb1ff65dcd1c0ea110bb6a6f0aa8.jpg)

<details>
<summary>line chart</summary>

| Year | Headline CPI | Trimmed mean CPI |
|------|--------------|------------------|
| 2022 | ~3.5         | ~3.0             |
| 2023 | ~8.5         | ~7.0             |
| 2024 | ~3.5         | ~4.0             |
| 2025 | ~2.5         | ~3.0             |
| 2026 | ~4.5         | ~3.5             |
</details>

Source: ABS, GS Global Investment Research

Exhibit 2: May CPI forecasts

<table><tr><td>May month CPI forecasts</td><td>%mom May-26</td><td>%yoy May-26</td></tr><tr><td>Headline CPI</td><td>-0.4</td><td>4.2</td></tr><tr><td>Trimmed mean</td><td>0.3</td><td>3.5</td></tr><tr><td>Food &amp; non-alcoholic beverages</td><td>0.5</td><td>3.1</td></tr><tr><td>Alcohol &amp; tobacco</td><td>0.2</td><td>4.0</td></tr><tr><td>Clothing &amp; footwear</td><td>-1.9</td><td>6.0</td></tr><tr><td>Housing</td><td>0.3</td><td>6.3</td></tr><tr><td>New dwelling purchase</td><td>0.9</td><td>5.6</td></tr><tr><td>Rents</td><td>0.4</td><td>3.5</td></tr><tr><td>Household goods &amp; services</td><td>0.0</td><td>1.7</td></tr><tr><td>Health</td><td>-0.3</td><td>3.9</td></tr><tr><td>Transport</td><td>-3.8</td><td>3.4</td></tr><tr><td>Automotive fuel</td><td>-12.5</td><td>6.9</td></tr><tr><td>Communication</td><td>-0.5</td><td>1.5</td></tr><tr><td>Recreation &amp; culture</td><td>-0.4</td><td>5.2</td></tr><tr><td>Education</td><td>0.0</td><td>4.8</td></tr><tr><td>Insurance &amp; financial services</td><td>0.0</td><td>3.1</td></tr></table>

All figures are non-seasonally adjusted except for trimmed mean.  
Source: GS Global Investment Research

## Automotive fuel

Timely data from the Australia Institute of Petroleum suggest gasoline and diesel prices fell sharply in May, alongside lower global oil prices and the earlier temporary 3-month reduction of the excise tax (Exhibit 3).

We expect automotive fuel in the official CPI data to fall 12.5%mom in May.

Exhibit 3: Diesel and gasoline prices fell in May  
![](images/a7eee4200cf024d7f6b033699ecb1979a401241e0e95dab40d87d53cce742be2.jpg)

<details>
<summary>line chart</summary>

| Year | Diesel (cents/L) | Gasoline (cents/L) |
| --- | --- | --- |
| 2016 | 115 | 113 |
| 2017 | 125 | 123 |
| 2018 | 145 | 143 |
| 2019 | 155 | 153 |
| 2020 | 135 | 133 |
| 2021 | 145 | 143 |
| 2022 | 205 | 203 |
| 2023 | 235 | 230 |
| 2024 | 215 | 210 |
| 2025 | 195 | 190 |
| 2026 | 190 | 185 |
| 2026 (with label) | 290 | 230 |
</details>

Source: Haver Analytics, GS Global Investment Research

## Materials and chemical costs

The number of price rises announced by key plumbing and trade material suppliers continue to trend upwards, with the average price increase and number of price increases exceeding the post-COVID peak (Exhibit 4). Prices for fertiliser also remain somewhat elevated (Exhibit 5).

Exhibit 4: Key building supply companies are announcing a greater number of, and larger, price increases  
![](images/dc3732f63829bdb829df4f6ccae1bfd66a217b58c4440c7a95e0438bd0c435d9.jpg)  
Source: Reece, TradeLink, GS Global Investment Research

Exhibit 5: Fertiliser prices remain somewhat elevated  
![](images/0e7cd6073377c4cdb8e87018cb2074571cd90c7b023bd707d8d0465f62209747.jpg)

<details>
<summary>line chart</summary>

| Year | Urea (USD/tonne) | Ammonia (USD/tonne) |
|---|---|---|
| 2019 | 250 | 275 |
| 2020 | 240 | 230 |
| 2021 | 300 | 350 |
| 2022 | 950 | 900 |
| 2023 | 600 | 1050 |
| 2024 | 350 | 550 |
| 2025 | 400 | 400 |
| 2026 | 850 | 750 |
</details>

Source: Argus, GS Global Investment Research

Over time, we expect higher materials and chemical costs to pass through to higher consumer prices for food and housing, reflecting cost pressures faced by the agriculture and materials manufacturing industries (Exhibit 6).

Exhibit 6: Prices for food and housing are likely to be boosted by higher input costs  
![](images/8a6265a74d07f24a7018fb64a6d5d2f0dc91f9de006c894d6f6b8ea358d307f9.jpg)

<details>
<summary>stacked bar chart</summary>

Contribution to CPI from a 10% increase in material & chemical prices
| Category | Industrial gases (bp) | Plastics (bp) | Fertiliser (bp) | Aluminium (bp) | Organic chemicals (bp) |
|---|---|---|---|---|---|
| Food | 0.1 | 0.25 | 1.3 | 0.0 | 0.4 |
| Alcohol | 0.0 | 0.0 | 0.15 | 0.0 | 0.05 |
| Clothing | 0.0 | 0.0 | 0.1 | 0.0 | 0.0 |
| Housing | 0.25 | 0.45 | 0.25 | 0.0 | 0.4 |
| Furnishings | 0.05 | 0.45 | 0.35 | 0.0 | 0.25 |
| Health | 0.05 | 0.35 | 0.25 | 0.0 | 0.3 |
| Transport | 0.0 | 0.15 | 0.15 | 0.0 | 0.1 |
| Communication | 0.0 | 0.0 | 0.05 | 0.05 | 0.05 |
| Recreation | 0.0 | 0.15 | 0.15 | 0.05 | 0.1 |
| Education | 0.0 | 0.1 | 0.1 | 0.05 | 0.1 |
| Finance | 0.0 | 0.05 | 0.05 | 0.05 | 0.1 |
</details>

Source: GS Global Investment Research

## Airfares and holiday travel

We expect domestic travel & accommodation in the official CPI data to fall 7.2%mom in May. Alternative data on domestic airfares from the Bureau of Infrastructure and Transport Research Economics suggest prices fell a smaller 2.1%mom in April (Exhibit 7), although we acknowledge these data measure prices on the last Thursday of each month, whereas the official ABS measures prices more frequently throughout the month.

We expect international travel & accommodation prices to rise 4.7%mom. We note that price collection for international airfares occurs two months in advance, meaning that

May's data is the first to capture the impact of the conflict in the Middle East. Our forecast contrasts with the decline in international travel prices in the New Zealand already observed over May (Exhibit 8), possibly in part due to differences between the Australian and New Zealand collection methodologies.

Exhibit 7: Alternative data on airfares fell a little in May  
![](images/7f372403b10d6dbd4de2aff11d3e09f0c7d4d4378ce6722949ee459870efde48.jpg)  
Source: ABS, GS Global Investment Research, BITRE

Exhibit 8: International air transport prices in New Zealand declined in May  
![](images/0d9b1c3fd6ecb63aeb4c2d05e8b51e7c99d646851b0d129ab7a7d77dafb9fc85.jpg)

<details>
<summary>line chart</summary>

International travel prices
| Year | Australia CPI: International holiday travel and accommodation prices (%mom) | New Zealand CPI: International air transport prices (%mom) |
|---|---|---|
| 2023 | -18 | -30 |
| 2024 | 22 | 42 |
| 2025 | -15 | -15 |
| 2026 | -18 | 32 |
</details>

Source: ABS, StatsNZ, GS Global Investment Research

## Housing

Growth in SQM advertised rents picked up further in May, which will pass through to inflation in the stock of rents measured in the CPI data over time. The April CPI report showed a slight easing in rents inflation, while new dwelling inflation picked up further, reflecting the pass-through of fuel surcharges and higher material costs.

Looking ahead, we expect new dwelling inflation to accelerate further to 0.9%mom in May from higher input costs. We expect rents inflation to edge up to 0.4%mom.

Exhibit 9: Growth in advertised rents picked up further in May  
![](images/1f1f8c7f2abec7f64bf28bebb8e91a9a32260b23ad8bcb92e522415ce92e65dd.jpg)

<details>
<summary>line chart</summary>

| Year | SQM capital city average (fwd 9 months; LHS) | Monthly CPI (RHS) | Quarterly CPI (RHS) |
|------|-----------------------------------------------|-------------------|---------------------|
| 2012 | ~5                                            | ~10               | ~8                  |
| 2014 | ~-5                                           | ~5                | ~5                  |
| 2016 | ~0                                            | ~0                | ~0                  |
| 2018 | ~5                                            | ~5                | ~5                  |
| 2020 | ~-10                                          | ~-15              | ~-15                |
| 2022 | ~15                                           | ~15               | ~15                 |
| 2024 | ~25                                           | ~25               | ~25                 |
| 2026 | ~5                                            | ~5                | ~5                  |
</details>

Source: SQM, ABS, GS Global Investment Research

Exhibit 10: Housing inflation picked up further in April  
![](images/8841a266cc48ffb733530fbf7cf8e15cf08de3a800e8761468cc1d0363c96a4f.jpg)

<details>
<summary>line chart</summary>

| Year | Rents and new dwelling inflation (%3m/3m, sa) (%) | Rents and new dwelling inflation (%qoq, sa) (%) |
|---|---|---|
| 2020 | -0.1 | 0.2 |
| 2021 | 0.1 | 0.4 |
| 2022 | 2.5 | 3.8 |
| 2023 | 1.5 | 2.8 |
| 2024 | 1.4 | 1.6 |
| 2025 | 0.1 | 1.4 |
| 2026 | 1.0 | 1.1 |
</details>

Source: ABS, GS Global Investment Research

## Market services

We expect a slight acceleration in market services inflation in April, reflecting pass-through of higher oil prices. In particular, we expect restaurant meals and takeaway to each rise by $0.7\%$ mom, alongside reports of fuel surcharges in the food and hospitality industry. We expect inflation across other market services to remain little changed.

Outside of fuel-related cost impacts, measures of labour tightness included in the RBA's indicator framework suggest conditions in the labour market are close to balance and not contributing excessively to inflation (Exhibit 11).

Exhibit 11: The RBA's updated labour framework suggests to us that labour market conditions are close to balanced  
![](images/f2889f44016994371f34f114ae07f84270d6fb67c436ce78a2d937305795316d.jpg)

<details>
<summary>line chart</summary>

| Year | Range of indicators | Middle 50% of indicators | Midpoint of middle 50% range | GS wage-informative composite |
|------|---------------------|--------------------------|------------------------------|-------------------------------|
| 1990 | -                   | -                        | -                            | -                             |
| 1994 | -                   | -                        | -                            | -                             |
| 1998 | -                   | -                        | -                            | -                             |
| 2002 | -                   | -                        | -                            | -                             |
| 2006 | -                   | -                        | -                            | -                             |
| 2010 | -                   | -                        | -                            | -                             |
| 2014 | -                   | -                        | -                            | -                             |
| 2018 | -                   | -                        | -                            | -                             |
| 2022 | -                   | -                        | -                            | -                             |
| 2026 | -                   | -                        | -                            | -                             |
</details>

Source: GS Global Investment Research, ABS, Haver Analytics

## Inflation expectations

Measures of short-term inflation expectations remain well above the RBA's target band, but recently retraced from their peaks (Exhibit 12). Measures of long-term inflation expectations – which are more problematic for a central bank if they become unanchored – generally remain stable around the mid-point of the RBA's target band (Exhibit 13).

Exhibit 12: Short-term inflation expectations have retraced from their peaks but remain elevated  
![](images/d64723889ce2870680db12e2bb25471943cf8d6cfc8ee15185946395f44c3fc1.jpg)

<details>
<summary>line chart</summary>

| Year | Consumer (Melbourne Institute) | Consumer (Roy Morgan) | Market economist | Inflation swaps |
|------|----------------------------------|------------------------|------------------|-----------------|
| 2005 | ~4%                              | ~4%                    | ~3%              | ~3%             |
| 2008 | ~8.5%                            | ~4%                    | ~3%              | ~4%             |
| 2011 | ~6%                              | ~4%                    | ~3%              | ~3%             |
| 2014 | ~4%                              | ~4%                    | ~3%              | ~3%             |
| 2017 | ~4%                              | ~4%                    | ~3%              | ~3%             |
| 2020 | ~4%                              | ~4%                    | ~3%              | ~3%             |
| 2023 | ~6.5%                            | ~6%                    | ~5%              | ~5%             |
| 2026 | ~7%                              | ~7%                    | ~6%              | ~4%             |
</details>

Source: Haver Analytics, RBA, Bloomberg, GS Global Investment Research

Exhibit 13: Long-term inflation expectations generally remain anchored  
![](images/90f92575d2fd4e25c0088140467af6934fdc76d6a4ce02e6a0d3138ea0f613c0.jpg)

<details>
<summary>line chart</summary>

| Year | Inflation swaps (3-year) | Inflation swaps (10-year) | Market economists |
|------|--------------------------|---------------------------|-------------------|
| 2008 | ~4.0%                    | ~4.0%                     | ~2.5%             |
| 2011 | ~3.0%                    | ~3.0%                     | ~2.5%             |
| 2014 | ~2.5%                    | ~2.5%                     | ~2.5%             |
| 2017 | ~2.0%                    | ~2.0%                     | ~2.5%             |
| 2020 | ~0.5%                    | ~1.0%                     | ~2.5%             |
| 2023 | ~3.5%                    | ~3.0%                     | ~2.5%             |
| 2026 | ~3.0%                    | ~2.5%                     | ~2.5%             |
</details>

Source: RBA, GS Global Investment Research

## New Zealand

Selected prices covering around $50\%$ of NZ's quarterly CPI basket were little changed in the month, but year-over-year inflation in these prices accelerated 70bp to $5.6\%$ yoy. Excluding fuel, year-over-year inflation also increased 100bp to $3.0\%$ yoy.

Compositionally, petrol (-3.8%mom) and diesel prices (-11.4%mom) fell alongside lower global energy prices. Domestic (-11.4%mom) and international airfares (-5.5%mom)

also declined following a seasonal increase in April, while rents growth turned negative (-0.1%mom) for the second time this year. However, offsetting these declines was a material rise in food prices (+1.0%mom) driven by ready-to-eat food (+0.6%mom) and restaurant meals (+0.7%mom). The latter rose at its fastest pace since mid-2023 (Exhibit 15), possibly as a result of fuel surcharges.

Exhibit 14: Growth in New Zealand monthly prices picked up in May  
![](images/d59228a67f58521ae096a1f2a1ce212f2aba334d2d1cf6f48cb64ae851890fe3.jpg)

<details>
<summary>line chart</summary>

| Date | Monthly CPI (around 50% of items) (%)yoy | Monthly CPI ex. fuel (around 45% of items) (%)yoy | Quarterly CPI (all items) (%)yoy |
|---|---|---|---|
| Oct-22 | 8.0 | 7.5 | 7.3 |
| Apr-23 | 8.5 | 9.5 | 6.8 |
| Oct-23 | 6.0 | 6.5 | 5.8 |
| Apr-24 | 1.0 | 1.5 | 2.2 |
| Oct-24 | 1.5 | 2.8 | 2.2 |
| Apr-25 | 3.0 | 4.5 | 3.0 |
| Oct-25 | 3.5 | 4.0 | 3.1 |
| Apr-26 | 5.5 | 2.0 | 3.0 |
</details>

Source: StatsNZ, GS Globa

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
