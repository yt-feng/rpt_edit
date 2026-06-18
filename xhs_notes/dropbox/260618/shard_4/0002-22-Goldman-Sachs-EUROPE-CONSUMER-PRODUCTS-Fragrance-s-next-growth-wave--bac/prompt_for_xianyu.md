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
# EUROPE CONSUMER PRODUCTS

# Fragrance's next growth wave: back to blockbusters

As fragrance growth normalises, performance will depend less on category tailwinds and more on the ability to create new blockbuster pillars. L'Oréal (Buy) remains the execution benchmark, but we see clear re-rating potential in Puig (Buy) and Interparfums (Buy).

Fragrance is an offer-driven category, with demand disproportionately shaped by new formats, scents and activations that drive trial. Growth was easier to achieve in the post-Covid cycle as the consumer base expanded and usage frequency increased. We still expect penetration gains, but as category growth normalises to $3.5\%$ in Q1 and competition intensifies (6,000 launches in 2025 versus 2,500 in 2019), growth will increasingly depend on launches that can become new pillars. Over the next three years, we expect Puig to launch blockbusters for Rabanne and Jean Paul Gaultier and to scale La Bomba; Interparfums to build new pillars across its four largest brands alongside the debut of Longchamp; and L'Oréal potentially to introduce a new Armani pillar and to develop the Kering Beauty franchise.

Blockbusters have long been a durable growth engine, even before the recent supercycle. At L'Oréal, fragrance sales rose 8% in 2019, supported by three launches including Libre, which six years later became the world's leading women's fragrance, overtaking Chanel. Earlier in the mid-2010s, L'Oréal launched another wave of blockbusters, notably La Vie Est Belle, which helped drive double-digit growth in women's fragrance in 2014 and over 9% growth in 2015, and still anchors Lancôme today. Puig followed a similar playbook, with Good Girl surpassing 3% market share within six years of launch. Meanwhile, Interparfums has built Jimmy Choo into a franchise generating over €200m in sales through a steady rollout of new pillars. Search interest in La Bomba and Paradigme tracks ahead of comparable past launches, suggesting newness continues to resonate with consumers.

We do not believe this is fully reflected in valuations. As fragrance growth normalises, we expect a step up in launch activity to support near-term sell-in and extend the medium-term growth runway. In our view, Puig and Interparfums, trading at 13x and 16x CY27 P/E, do not fully reflect that opportunity, leaving scope for re-rating if execution remains consistent. While some of L'Oréal's premium at 26x P/E is justified by unparalleled execution and a more diversified category footprint, the gap remains wide versus history. Looking ahead, we expect Puig's CMD on 28 October to outline its runway in women's fragrance and plans to reinvigorate Rabanne, while L'Oréal's 1 December CMD is set to focus on its AI agenda.

## Aron Adamski

+44(20)7774-6224

aron.adamski@gs.com

GS International

## Olivier Nicolai

+44(20)7774-2895

olivier.nicolai@gs.com

GS International

## Rebecca Ayo-Adebanjo

+44(20)7552-2213 | rebecca.ayo-adebanjo@gs.com

GS International

## Sam Darbyshire, CFA

+44(20)7051-9112

sam.darbyshire@gs.com

GS International

## Tom Hulls

+44(20)7774-7641|tom.hulls@gs.com

GS International

## Srikar Medisetti

+1(332)245-7675

srikar.medisetti@gs.com

GS India SPL

## Fragrances in 6 Key Charts

Exhibit 1: Beauty market growth rate has accelerated post Covid  
L'Oréal estimate of global beauty industry sales growth, 2010-25  
![](images/e642bea11288f7de1b520f3bfce1d668f80279ea7fa4eb612071684ae89516ed.jpg)

<details>
<summary>bar chart</summary>

| Year | Value (%) |
|---|---|
| 2010 | 4.2 |
| 2011 | 4.6 |
| 2012 | 4.6 |
| 2013 | 3.8 |
| 2014 | 3.6 |
| 2015 | 3.9 |
| 2016 | 4.0 |
| 2017 | 4.8 |
| 2018 | 5.7 |
| 2019 | 5.6 |
| 2020 | -8.2 |
| 2021 | 8.0 |
| 2022 | 5.9 |
| 2023 | 8.0 |
| 2024 | 4.5 |
| 2025 | 3.5 |
Beauty market has experienced +4.5% average growth over 2009-19; +5.5% average growth between 2021-25
</details>

Source: Company data

Exhibit 2: Premium fragrances gained share of beauty market post Covid  
Global beauty industry breakdown by category, 2010-2025  
![](images/bdc2bb3907fbbf47d09b271f2b6bbc1b033a80be000bb737f461d3d9f158a034.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Dark Blue (%) | Light Blue (%) | Red (%) | Green (%) |
|---|---|---|---|---|
| 2010 | 37 | 26 | 7 | 9 |
| 2015 | 38 | 25 | 8 | 9 |
| 2019 | 41 | 23 | 9 | 6 |
| 2025 | 40 | 23 | 8 | 12 |
</details>

Source: Euromonitor

Exhibit 3: We think cohort expansion drove beauty and fragrance growth acceleration  
Beauty: average entry age by category (USA)  
![](images/debaf156c745717d74829c8d6d26fb26f2ffc654a718273ffe0cd065774068c8.jpg)

<details>
<summary>line chart</summary>

| Category | Fragrance | Skincare | Makeup (girls only) |
|---|---|---|---|
| 1 | 13.0 | 14.0 | 14.0 |
| 2 | 12.5 | 13.5 | 13.5 |
| 3 | 11.5 | 13.5 | 13.0 |
| 4 | 11.5 | 12.0 | 13.0 |
</details>

<table><tr><td>Teens of 2000s34-43 years old today</td><td>Teens of 2010s23-33 years old</td><td>Teens of early 2020s19-23 years old</td><td>Today&#x27;s teens13-18 years old</td></tr></table>

Source: Boston Consulting Group

Exhibit 4: Largest six players account for two-thirds of premium fragrance sales  
Global premium fragrances breakdown by company, 2025  
![](images/2d6d1a16cc7ed933a5fb0ac3297ec074ea943f211eb3d55ce00985bede1848e2.jpg)

<details>
<summary>pie chart</summary>

| Brand | Percentage (%) |
| :--- | :--- |
| L'Oréal | 17 |
| LVMH | 12 |
| Coty | 11 |
| Puig | 9 |
| Chanel | 7 |
| Estée Lauder | 6 |
| Interparfums | 4 |
| Other | 34 |
</details>

Source: Euromonitor

Exhibit 5: Interparfums is only exposed to fragrances, while Puig and L'Oréal are more diversified  
Revenue mix from fragrances, FY25  
![](images/e93850adf7e10f76ae2e60a306aef52ef098b7b2136327d610892ec62cbccb7a.jpg)

<details>
<summary>bar chart</summary>

| Company | Percentage (%) |
| :--- | :--- |
| Interparfums | 100 |
| Puig | 72 |
| Coty | 69 |
| Estee Lauder | 17 |
| L'Oréal | 15 |
</details>

Source: Company data

Exhibit 6: Newness continues to resonate, with interest in fresh blockbusters tracking ahead of past launches  
Indexed searches for Good Girl vs La Bomba in first 12 months  
![](images/9f74c16a3de0d881aadeb68a17f0727c1b0b5bcc42eb50e80561fc18ed9cfd4c.jpg)

<details>
<summary>line chart</summary>

| Time Point | Good Girl | La Bomba |
|---|---|---|
| T + 0 | 90 | 90 |
| T + 1 | 290 | 190 |
| T + 2 | 370 | 350 |
| T + 3 | 280 | 670 |
| T + 4 | 410 | 390 |
| T + 5 | 280 | 410 |
| T + 6 | 285 | 610 |
| T + 7 | 270 | 230 |
| T + 8 | 240 | 220 |
| T + 9 | 240 | 260 |
| T + 10 | 220 | 340 |
| T + 11 | 215 | 390 |
| T + 12 | 215 | 290 |
</details>

Source: Google Trends (https://www.google.com/trends)

## Blockbusters have long been a durable growth engine

Blockbusters have long been a durable growth engine. At L'Oréal, fragrance sales rose 8% in 2019, supported by three launches including Libre, which six years later became the world's leading women's fragrance, overtaking Chanel. Meanwhile, Prada scaled from under €100m in sales in 2021 to more than €700m, driven by the Paradoxe and Paradigme launches. Earlier, L'Oréal's mid-2010s blockbuster wave, notably La Vie Est Belle, helped drive double-digit growth in women's fragrance in 2014 and over 9% growth in 2015, and still anchors Lancôme today. Looking ahead, the CEO of L'Oréal Luxe USA recently indicated that H2 26 will bring new product launches.

Exhibit 7: Even before the recent fragrance supercycle blockbusters have long been a durable growth engine L'Oréal fragrance organic sales growth, FY10-25  
![](images/666e02f4f42bb00a218cfdcef2cdd757339d7b7fc6a5439f38adba0544c63a25.jpg)

<details>
<summary>bar chart</summary>

| Fiscal Year | Growth Rate (%) |
|---|---|
| FY10 | 3.8 |
| FY11 | 3.8 |
| FY12 | 5.6 |
| FY13 | 3.6 |
| FY14 | 6.7 |
| FY15 | 6.2 |
| FY16 | 1.6 |
| FY17 | 2.1 |
| FY18 | 7.8 |
| FY19 | 8.4 |
| FY20 | -15.4 |
| FY21 | 34.5 |
| FY22 | 22.8 |
| FY23 | 16.9 |
| FY24 | 14.1 |
| FY25 | 10.4 |
Cohort expansion and usage frequency increase alongside new launches: Prada Paradoxe and YSL MYSLF
</details>

Source: Company data, GS Global Investment Research

Puig followed a similar playbook: Good Girl surpassed 3% market share within six years, while 1 Million reached 1% in its first year and continued building over the next decade. Meanwhile, Interparfums built Jimmy Choo into a €200m-plus franchise through a steady stream of new pillars, including I Want Choo, which grew 27% in 2025 despite being four years old. Montblanc's launch of Explorer likewise drove nearly 30% revenue growth and still underpins the franchise today. More recently, Coty's Goddess launch helped drive Burberry to more than 30% retail sales growth in 2024, with the franchise still ranking among the top 20 women's fragrances.

Exhibit 8: Good Girl surpassed $3\%$ share in six years Good Girl: women's fragrance market share, 2022 vs 2016  
![](images/5bc734cda574070180ef43162add06833fe65eae28493bc31e9c71733624f7c8.jpg)

<details>
<summary>bar chart</summary>

| Year | Percentage (%) |
|---|---|
| 2016 | 0.4 |
| 2022 | 3.2 |
Good Girl has built its position over time
</details>

Source: Circana

Exhibit 9: Jimmy Choo scaled through new pillars Jimmy Choo and Montblanc net sales in EURm, 2011-25  
![](images/9716f2d030b21f2f89ab6d32435db6c0f31c368d24c6ccc7910f116fc24de657.jpg)

<details>
<summary>bar chart</summary>

Jimmy Choo and Montblanc scaled through a disciplined pillar-and-flanker playbook
| Year | Jimmy Choo | Montblanc |
| :--- | :--- | :--- |
| 2011 | 29 | 31 |
| 2015 | 83 | 88 |
| 2019 | 104 | 141 |
| 2025 | 228 | 193 |
</details>

Source: Company data

## Blockbusters will drive the next wave of fragrance growth

Growth was relatively easy in the post-Covid period, as the consumer base expanded and usage frequency increased. Looking ahead, we still see room for further penetration gains, but as category growth normalises and competition intensifies, performance is likely to increasingly depend on launches that can evolve into new pillars. In prestige fragrance, brands typically introduce a new blockbuster every three to five years, while annual flankers help keep core franchises relevant and aligned with shifting consumer preferences. Against that backdrop, over the next three years we expect:

L'Oréal could introduce a new Armani pillar, one of its largest fragrance franchises, with no major launch since My Way in 2020. Valentino has been successfully driven by Born in Roma since 2019, but we would expect the brand to broaden that platform over the next three years. Lancôme also screens as a credible candidate for a new blockbuster, having not launched a major new pillar since Idole in 2019. We also expect L'Oréal to develop the Kering Beauty fragrance portfolio (Bottega Veneta, Balenciaga), and ultimately Gucci by FY28 at the latest.  
Puig is set to launch a women's blockbuster at Jean Paul Gaultier in H2 26 as it looks to narrow the gap between its feminine and stronger masculine positions. In men's, flanker extensions have helped propel Le Male to top global rankings, although we would expect a new pillar closer to FY28. Rabanne should introduce a new pillar in FY27 to reinvigorate the brand following no major men's launch since Phantom in FY21. We also expect Carolina Herrera to build the recently launched La Bomba through flankers, with potential for a men's extension, given the brand's women's blockbusters have historically been followed by masculine launches.  
Interparfums is set to build out new pillars across its largest brands, including Jimmy Choo, Coach, Montblanc, and Lacoste, alongside the launch of Longchamp.  
Coty plans to launch a Swarovski fragrance in 2027, while focusing its prestige strategy on a set of key growth bets next year. At the same time, it is increasing marketing support behind Burberry and Hugo Boss and sharpening its mass-market portfolio around core brands and priority markets.

A key uncertainty around blockbuster launches is whether they can bring new consumers into the brand, rather than simply cannibalising existing pillars. Puig has suggested that La Bomba is attracting a different consumer from the traditional Good Girl audience, which we would attribute to its distinct scent profile.

Mists are also a recruitment opportunity. Coty has said the category resonates with the youngest Gen Z consumers, who do not yet engage meaningfully with traditional fragrances, and aligns with the scent-layering trend. The economics are attractive too, with gross margins comparable to the Prestige division's 71% level in FY25. The category is gaining traction, with L'Oréal expanding Valentino and Lancôme into mists, Puig recently launching the format at Penhaligon's and Byredo, and Interparfums at DKNY. While still dominated by non-fragrance players such as L'Occitane, Bath & Body Works, and Victoria's Secret, we see clear scope for traditional fragrance players to gain share as the category develops.

Exhibit 10: We think there's scope for multiple prestige fragrance blockbusters over the coming years  
Selected blockbuster launches of L'Oréal, Puig and Interparfums

<table><tr><td>Women&#x27;s launch</td><td>Men&#x27;s launch</td><td>BLOCKBUSTER ≥ 5 YRS AGO</td><td>RECENT BLOCKBUSTER</td></tr><tr><td colspan="4">L&#x27;Oréal Group</td></tr><tr><td>Yves Saint Laurent</td><td>Armani</td><td>Lancôme</td><td>Valentino</td></tr><tr><td rowspan="2">Managed in-house prior to 2008</td><td>Acqua di Gio (1996)</td><td>Tresor (1990)</td><td rowspan="3">Managed by Puig prior to 2018</td></tr><tr><td>Code (2004)</td><td>Poeme (1995)</td></tr><tr><td>Black Opium (2014)</td><td>Acqua di Gioia (2010)</td><td>Miracle (2000)</td></tr><tr><td>Y (2017)</td><td>Si (2013)</td><td>Hypnôse (2005)</td><td>Born in Roma (2019)</td></tr><tr><td>Libre (2019)</td><td>You (2017)</td><td>La Vie Est Belle (2012)</td><td>Born in Roma (2019)</td></tr><tr><td>MYSLF (2023)</td><td>My Way (2020)</td><td>Idôle (2019)</td><td>Voce Viva (2020)</td></tr><tr><td>Ralph Lauren</td><td>Prada</td><td>Mugler</td><td>Viktor &amp; Rolf</td></tr><tr><td>Big Pony (2010)</td><td></td><td></td><td>Under L&#x27;Oréal management since 2002</td></tr><tr><td>Big Pony 2 (2012)</td><td rowspan="2">Managed by Puig prior to 2019</td><td rowspan="3">No blockbusters since the brand was acquired in 2020</td><td>Flowerbomb (2005)</td></tr><tr><td>Polo Red (2013)</td><td>Spicebomb (2012)</td></tr><tr><td>Ralph&#x27;s Club (2021)</td><td></td><td>Bonbon (2014)</td></tr><tr><td>Polo Earth (2022)</td><td>Paradoxe (2022)</td><td></td><td>Good Fortune (2022)</td></tr><tr><td>Polo Est. 67 (2024)</td><td>Paradigme (2025)</td><td></td><td></td></tr></table>

<table><tr><td colspan="4">Puig Brands</td></tr><tr><td>Rabanne</td><td>Carolina Herrera</td><td>Jean Paul Gaultier</td><td>Nina Ricci</td></tr><tr><td>1 Million (2008)</td><td>212 (1997)</td><td>Classique (1993)</td><td rowspan="2">Acquired by Puig in 1988</td></tr><tr><td>Lady Million (2010)</td><td>212 Men (1999)</td><td>Le Male (1995)</td></tr><tr><td>Invictus (2013)</td><td>CH (2007) &amp; CH Men (2009)</td><td>Scandal (2017)</td><td>Nina (2006)</td></tr><tr><td>Olympéa (2015)</td><td>Good Girl (2016)</td><td>Le Beau &amp; La Belle (2019)</td><td>L&#x27;Extase (2015)</td></tr><tr><td>Phantom (2021)</td><td>Bad Boy (2019)</td><td>Scandal Pour Homme (2021)</td><td>Luna (2016)</td></tr><tr><td>Fame (2022)</td><td>La Bomba (2025)</td><td>Divine (2023)</td><td>Vénus (2024)</td></tr></table>

<table><tr><td colspan="4">Interparfums SA</td></tr><tr><td>Coach</td><td>Jimmy Choo</td><td>Montblanc</td><td>Lacoste</td></tr><tr><td>Managed by Esteé</td><td>Signature Women (2011)</td><td>Managed by P&amp;G</td><td></td></tr><tr><td>Lauder prior to 2015</td><td>Flash (2013)</td><td>prior to 2010</td><td></td></tr><tr><td>Signature Women 

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
