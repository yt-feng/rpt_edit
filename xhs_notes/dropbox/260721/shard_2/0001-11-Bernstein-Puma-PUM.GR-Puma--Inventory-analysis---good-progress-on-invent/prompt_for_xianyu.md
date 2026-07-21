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
European General Retail

Puma

Rating
Outperform

Price Target

PUM.GR

## 35.00 EUR

![](images/6966b9aa9caf41cda73f0abb563e91f81e4679d1923d6ec6bb9070751513b1b7.jpg)

William Woods
+44 20 7676 6806
william.woods@bernsteinsg.com

![](images/c9567e95764465e522a2014d79bf909a79a24438512837934db8833599a49ef0.jpg)

![](images/65adcb5f4067ae3b9752d467ea96b609b47d82bf49c67946b0773206e000fe5d.jpg)

Richard Trainor
+44 20 7762 1050
richard.trainor@bernsteinsg.com

![](images/67f425027bc096f0a3c2138cda9a7afbd3a035e569db07338b5cb09fd20693a8.jpg)

Alice Buckley
+44 20 7676 6739
alice.buckley@bernsteinsg.com

Rhea Gudiwala
+44 20 7676 7293
rhea.gudiwala@bernsteinsg.com

## Puma: Inventory analysis - good progress on inventory purr-ge

Puma has been clearing its inventory since its H1-26 results as a key part of its turnaround strategy. We refresh our analysis from Feb -26 (see note here) to track Puma's progress 1 year later. Into the Puma's H1-26 print on $31^{\text{st}}$ July (preview here), we expect continued positive commentary on Puma's inventory clearance, but think it will be more important to now start hearing about the path to brand revival and product innovation pipeline once inventory is in a good place.

1) SKU count continues to decline across DTC and wholesale channels, reflecting solid inventory clearance progress, particularly in the UK. Puma's UK DTC SKU count is down almost 50% from the Jul-25 peak. Meanwhile, wholesale partners have seen SKU rationalization, particularly at retailers such as JD Sports and Size?, as Puma tries to regain control of its brand perception with a more targeted assortment.

2) The US remains behind the UK in the clearance cycle, but progress through wholesale channels is encouraging. SKU count on Puma's US DTC platform has continued to rise versus Feb-26, suggesting Puma is still buying back excess inventory. Plus, SKU counts across key US partners have fallen, implying Puma is successfully consolidating inventory and the next stage will be to clear this stock through its own channels, mirroring the UK trajectory.

3) Puma is increasingly focusing on assortment quality, with weaker franchises being cut and key growth franchises emphasised. Across both DTC and wholesale channels, Puma has narrowed assortments and removed/marked-down less popular franchises, e.g. Mostro continues to be heavily discounted, while the core Speedcat assortment is narrower, but there are newer variations (e.g., ballets, mules and wedges) instead.

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>31.0</td><td>4.0</td><td>36.8</td><td>33.3</td></tr><tr><td>EDME (%)</td><td>8.0</td><td>0.6</td><td>6.2</td><td>17.5</td></tr><tr><td>Relative (%)</td><td>23.1</td><td>3.4</td><td>30.6</td><td>15.8</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Close Date</td><td>17 Jul 2026</td></tr><tr><td>PUM.GR Close Price (EUR)</td><td>28.48</td></tr><tr><td>Price Target (EUR)</td><td>35.00</td></tr><tr><td>Upside/(Downside)</td><td>23%</td></tr><tr><td>52-Week Range</td><td>30.31/15.30</td></tr><tr><td>EDME</td><td>1,587.83</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>NA</td></tr><tr><td>Market Cap (EUR) (M)</td><td>4,325</td></tr><tr><td>EV (EUR) (M)</td><td>6,347</td></tr></table>

Price Performance, 1YR

![](images/2c776f8e77e089136f0cf6f716bf09303d95f25b0f7fbf96452790877a349b53.jpg)

## Investment Implications

We rate Puma Outperform with a target price of €35, based on current market multiples and an average of a PE (14x) and EV/EBIT (13x) applied to our NTM+2 estimates.

Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>PUM.GR (EUR)</td><td>(4.36)</td><td>(1.42)</td><td>1.23</td><td>Revenues (M)</td><td>7,296</td><td>6,958</td><td>7,793</td><td>--</td></tr><tr><td></td><td></td><td></td><td></td><td>EBIT (M)</td><td>(369.50)</td><td>(6.62)</td><td>374.07</td><td>--</td></tr><tr><td></td><td></td><td></td><td></td><td>FCF (M)</td><td>(892.30)</td><td>82.99</td><td>60.84</td><td>--</td></tr><tr><td></td><td></td><td></td><td></td><td>Revenues growth (%)</td><td>(17.3)</td><td>(4.6)</td><td>12.0</td><td>--</td></tr><tr><td></td><td></td><td></td><td></td><td>EBIT Margin (%)</td><td>(5.1)</td><td>(0.1)</td><td>4.8</td><td>--</td></tr></table>

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Adjusted P/E (x)</td><td>(6.5)</td><td>(20.1)</td><td>23.1</td></tr><tr><td>Reported P/E (x)</td><td>(6.5)</td><td>(20.1)</td><td>23.1</td></tr></table>

## DETAILS

## PROGRESS TO DATE

\- DTC shows good progress in reducing SKU count in the UK, with numbers down almost -50% since peaks in Jul-25, when management initially announced the strategic turnaround, and progress continues to look strong. Management at Q1-26 results highlighted they saw better-than-expected sell-through during Q1 on inventory they had previously written off. We see SKU count come down more slowly through Q2 (Exhibit 2) as the remainder of the inventory is of lower quality and likely reflects the unpopular SKUs that are much more difficult to clear. The US lags the UK in the inventory clearance cycle, as SKU count on Puma's US DTC platform continues to rise (+7% vs. Jul-25), indicating Puma is likely still in the phase of buying bank inventory from its wholesale partners, and has yet to clear this excess via its own channels.

\- SKU count has come down considerably across most retail partners since Jul-25, reflecting a good cadence of inventory buyback by Puma. By retailer, Footlocker US appears to be the furthest ahead in the inventory clearance cycle, with SKU count coming down c. -80% from Jul-25 to Jan-26 (Exhibit 27), before ticking back up, suggesting the bulk of the low quality SKU's have been sold, and the uptick in SKUs could reflect a broadening of the assortment with more desirable SKUs. Similarly, the SKU count at Finish Line has come down all the way down (Exhibit 30), and we would expect this to start inflecting again over the next 3-6 months as Puma improves its decision-making on SKU allocation to retailers. On the other hands, Dick's Sporting Goods seems further behind on this curve with SKU count reduction of c. -20% (Exhibit 24), although this is on the highest base given Dick's is one of the biggest wholesale partners for Puma in the US. This all points to promising inventory clearance either via the wholesale channel, or the buyback in order for Puma to clear via its own distribution channels.

\- In the UK, we see similar trends, with Footlocker's SKU count down c. -50% since the start of 2025 (Exhibit 15), suggesting good progress. The next step would be to better consolidate the SKU count and work on refining the assortment. For Sports Direct, which we view as a less attractive wholesale partner, clearance appears to be a little slower, with SKU count starting to tick back up and going slightly above the c. 9,000 SKUs in Jul-25 (Exhibit 18). We would highlight this remains of the most stuffed retailers Puma works with and therefore continue to expect slow progress.

\- When we break down pricing, specifically depth and breadth of discounting to look at Puma's DTC approach to selling excess inventory (Exhibit 1 and Exhibit 8), there is a key difference between the UK and the US, whereby markdown depth in the UK is greater than markdown breadth, whereas we see the opposite in the US (i.e., markdown breadth is greater than markdown depth). This suggests that in the UK, Puma's assortment has fewer, less desirable SKUs and therefore less of a need to discount broadly, with a focus instead on a higher markdown % to encourage purchases.

\- In the UK, markdown breadth has taken a step-up on Puma DTC since our last update in Feb-25, although the level of this remains reasonably constant, with the assortment seeing markdowns of c. -40%. Similarly, in the US, markdowns have increased as a proportion of the assortment, climbing to and average of 60% in the last 12 weeks vs. an average of 53% since 2025 (until Q2-26).

\- Across the wholesalers, the discounting picture has change slightly, where markdown breadth is decreasing, particularly with US retail partners such as Footlocker, Finish Line and Academy Sports now discounting across a much smaller proportion of their assortment (c. 15-20% vs. 50-60% previously) as the inventory buyback progresses. In the UK, this is slightly more varied as Footlocker now discounts across <20% of the assortment, but retains the same level of discount (c. -40%), whilst Sports Direct sees limited change with c. 90% of SKUs being marked-down.

## FRANCHISE BREAKDOWN

Illustratively, we compare Puma's DTC assortment and discounting on its website compared to its distribution partners to gauge a perspective of what SKU count and discounting looked like in Oct-25/Feb-26 vs. Jul-26 across key Puma franchises in lifestyle, football and running.

Looking at Puma's DTC assortment ([REFERENCE NOT FOUND] ; excluding outlets), the proportion of shoes being discounted has come up from $8\%$ in Feb-26 to $26\%$ in Jul-26. We think broadly reflects the next leg of the inventory clearance to get rid of all the more difficult to move, less desirable stock. As a result of which, greater discounting is needed.

\- At an individual franchise level, within lifestyle, Mostros have seen the highest proportion of SKUs being discounted ( $>80\%$ , with a markdown of c. $50 - 60\%$ ), likely due to the greater need to clear this franchise, which is arguably the least accessible to a broad-based audience in terms of fashionability (Exhibit 11). Across the rest of the lifestyle franchise, markdown have broadly come down (as % of SKUs), with only one Palermo and one Speedcat with a discount on it. However, we note that the number of Speedcat SKUs has come down considerably (c. $-60\%$ ) as there has been a narrowing of the original range, and then supplemented by other models of the Speedcat such as the ballets, mules and wedges, which we have excluded as they weren't part of our original comparison base. We think this is a good way for Puma to develop its brand heat by building on a franchise which continues to gain traction, but adding new versions to ensure newness. Overall, the lifestyle segment of Puma's assortment looks more appealing, with another less popular franchise (VS1) no longer available on the platform.

\- Looking at football, discounting has gone up. A greater proportion of football shoes are being discounted (almost 40% of all boots), which suggests this could be the next key segment to focus the inventory clearance on as good progress appears to have been made in lifestyle. Plus, the number of football boots SKUs has come up 12%, likely reflecting additional SKUs which have been bought back from retail partners. By franchise, Ultra sees the greatest breadth of discounting, followed by Future and King, reflecting the same trend as we saw in Feb-26 and therefore suggests the clearance momentum continues.

\- The picture for running shoes is similar - the total number of SKUs has gone up (c. +25%), with markdowns on c. 17% of the assortment (up vs. no promotions on running shoes in our last update). Running is a key segment for Puma to grow in and drive brand heat, as there has been considerable innovation in this space. We note that the markdowns are on older versions of various shoes rather than newer arrivals, which is positive as it suggests the newly developed shoes have good momentum and the discounting is likely on shoes that have been purchased from retail partners.

Across other retailers, the picture looks more mixed, and we think Puma is at different stages of its inventory management/buyback from its partners.

\- For example, if we look at Footlocker, who only sell lifestyle shoes, 25% of Speedcat SKUs are on sale, but none of the Suedes have markdowns. This is a continuation of the trend seen in Feb-26, although breadth of Speedcat markdowns has come up. We think this reflects a ramp up in the inventory clearance, as Puma works to ensure there is a very select assortment with its retail partners.

\- At JD Sports, there has been a significant reduction in the lifestyle segment of the assortment, with two further franchises being pulled from the site (Rider and Mostro) as these are less popular and do not drive sufficient Puma brand heat, alongside not being as aligned with JD's fashionability proposition. For Speedcats, the number of SKUs has come down from 8 to 2, and both of these are being marked down. However, this is because they have been replaced by the Speedcat ballets (16 SKUs), which have been growing in popularity and are arguably more fashionable. We consider JD to be a higher quality retailer and strong partner to help build Puma's brand heat and longer term brand equity in the lifestyle segment

\- In football, markdown breadth has taken a step-up as the SKU count has been rationalized (c. -55% since Feb-26) as this is less of a JD focus, and we think a good indication of Puma's brand strength will be reflected by its Lifestyle collection with JD rather than football, as it is not a specialist retailer.

\- Looking at Size?, we see a similar trend to JD Sports, where markdowns have climbed as a proportion of the assortment, but broadly reflecting the rationalization of the SKU count (c. -80%). This suggests Puma's clearance is working well and indicates a good cadence in inventory buyback, to get rid of undesirable SKUs and better control the Puma brand narrative with its partners.

EXHIBIT 1: Puma UK - Markdown Breadth and Markdon Depth %  
Puma UK - Markdown Breadth and Markdown Depth (%)  
![](images/95ee3b870e0ee373ce89d1c54571da4d1605e20048a614510e6da7e285c0270c.jpg)  
Source: Exabel, Bernstein analysis

EXHIBIT 2: Puma UK - SKU count  
![](images/d509033064bb12fad22ec33391cc1300d224fb310c2eb23ff35e1f2b096d8302.jpg)  
Source: Exabel, Bernstein analysis

EXHIBIT 3: Puma UK - Average Price (£)  
![](images/ddddf9c39ac5d29756b07134ac48e5059a5dbdfbac8a08616fbba1bb8f9579d1.jpg)  
Source: Exabel, Bernstein analysis

DTC (UK)  
EXHIBIT 4: Puma DTC SKU count by franchise

<table><tr><td colspan="6">DTC</td></tr><tr><td>Date</td><td>Category</td><td>Franchise</td><td>Total SKUs</td><td>Discounted SKU count</td><td>% discounted</td></tr><tr><td rowspan="14">16/10/25</td><td rowspan="8">Lifestyle</td><td>Speedcat</td><td>82</td><td>10</td><td>12%</td></tr><tr><td>Palermo</td><td>46</td><td>18</td><td>39%</td></tr><tr><td>Mostro</td><td>53</td><td>1</td><td>2%</td></tr><tr><td>H-street</td><td>7</td><td>0</td><td>0%</td></tr><tr><td>Inhale</td><td>17</td><td>16</td><td>94%</td></tr><tr><td>Rider</td><td>19</td><td>9</td><td>47%</td></tr><tr><td>Suede</td><td>24</td><td>3</td><td>13%</td></tr><tr><td>VS1</td><td>4</td><td>0</td><td>0%</td></tr><tr><td rowspan="3">Football</td><td>Future</td><td>94</td><td>17</td><td>18%</td></tr><tr><td>Ultra</td><td>95</td><td>17</td><td>18%</td></tr><tr><td>King</td><td>34</td><td>12</td><td>35%</td></tr><tr><td rowspan="3">Running</td><td>Deviate</td><td>38</td><td>0</td><td>0%</td></tr><tr><td>Velocity</td><td>18</td><td>0</td><td>0%</td></tr><tr><td>Magmax</td><td>16</td><td>0</td><td>0%</td></tr></table>

## FOOTLOCKER (UK)

EXHIBIT 5: Puma franchise SKU count on Footlocker site

<table><tr><td colspan="6">Footlocker</td></tr><tr><td>Date</td><td>Category</td><td>Franchise</td><td>Total SKUs</td><td>Discounted SKU count</td><td>% discounted</td></tr><tr><td rowspan="14">16/10/25</td><td rowspan="8">Lifestyle</td><td>Speedcat</td><td>18</td><td>6</td><td>33%</td></tr

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
