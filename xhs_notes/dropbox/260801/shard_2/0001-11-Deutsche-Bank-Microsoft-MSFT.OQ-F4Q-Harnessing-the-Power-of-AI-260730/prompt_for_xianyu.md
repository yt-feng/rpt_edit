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
Rating Buy

## Company Microsoft

North America
United States

Reuters
MSFT.OQ

Bloomberg
MSFT US

Date
30 July 2026

<table><tr><td>Rating</td><td>Buy</td></tr><tr><td>Price target (USD)</td><td>550.00</td></tr><tr><td>Price at 29 Jul 26</td><td>390.54</td></tr><tr><td>52-week range</td><td>542.07 – 1.46</td></tr></table>

TMT
Software

Valuation & Risks

## F4Q - Harnessing the Power of AI

Microsoft reported very strong F4Q results that underscore its full-stack advantage in the AI era, with strong evidence of monetization up through the application layer featuring M365 Commercial Cloud acceleration including Copilot reaching 30mn seats from 20mn last quarter. Another clear message is that the future is very much multi-model and the frontier is about every firm having the flexibility and choice to control its destiny; Microsoft enables this with the broadest model catalog in the cloud and associated scaffolding and guardrails enterprises require. The quarter evidenced that production AI applications rely on harnesses, context, memory and action space, architected in a way that any given model at any given time is swappable. Aligning with the durable role Microsoft plays, we found it interesting that mgmt. framed its success and various growth metrics ex the contribution from frontier model companies.

Azure +43% y/y @cc exceeded \~40-41% investor expectations, driven by efficiency gains across the CPU/GPU fleet and process improvements that enabled earlier delivery of new capacity which was quickly monetized. Results also benefited from stronger than expected GitHub Copilot consumption revenue following the June business model change to consumption pricing. Very impressively, Azure was guided to accelerate in F1H and +45% y/y @cc in F1Q, which implies \$2.8bn net adds (+65% y/y) and is consistent with commentary implying accelerating demand. With CapEx continuing to climb in F1H and more weighted toward short-lived assets in recent quarters, this looks supportive for elevated Azure growth rates to persist for multiple quarters to come.

For the full year, mgmt. reiterated total company guidance for double-digit topline and EBIT growth, with operating margins down <1pt y/y. This was slightly better than the -1pt y/y decline we previewed despite guidance for sharper FY27 revenue declines in high margin Windows (-high-teens % y/y), M365 Commercial Products (-MSD %) and Server Products (-MSD %). Factoring in updated guidance, our FY27 GM estimate eases only a slight \~10bps to 65.8% which we believe supports our view that Microsoft has a number of levers to help partly offset margin headwinds from mix shift and higher component costs as we laid out in our Margins under the Microscope report. As for CapEx, the lease reclassification impact from useful life changes on long-lived assets creates some noise, but on a like-for-like basis we understand there is no change to prior CY26 investment plans. Beyond that, mgmt. essentially held off on giving a view on F2H plans outside the expectation for FY27 FCF overall to remain positive.

Brad Zelnick
Research Analyst
+1-212-250-8563

Bhavin Shah, CFA
Research Analyst
+1-212-250-6775

Yash Kejriwal
Research Associate
+1-212-250-1203

We come away reaffirmed in our view that Microsoft is poised to continue compounding EPS at a mid-teens+ rate for multiple years to come on the back of increasingly tangible AI monetization across its full-stack. Accelerating Azure and M365 growth along-side resilient operating margins should build confidence in the returns on CapEx and R&D investment going into the business and Microsoft's position as a key facilitator of enterprise wide AI value creation. We maintain our Buy rating and target price of \$550, which implies \~25x our updated CY27E EPS.

## What We Liked / What We're watching on the Quarter

## Revenue/Bookings

(+) F4Q revenue of \$90.0bn was 3.2% above the midpoint of guidance, with upside across all segments. On a constant currency basis, growth accelerated to 17% y/y @cc vs +15% last quarter. From a full year perspective, growth ticked up 1pt to +16% y/y @cc with a revenue base that now exceeds \$331bn.

(+) Commercial Bookings grew 11% y/y @cc. When adjusted for Azure commitments from OpenAI, commercial bookings reportedly grew 18% y/y driven by strong execution in core annuity sales motions vs guidance for healthy growth on a growing expiry base. Commercial RPO ended the quarter +84% y/y at \$678bn with all sequential growth driven by commitments from customers other than frontier model providers. Total Commercial RPO was noted to have a weighted avg duration of 2.3yrs (including OpenAI), down from 2.5yrs last quarter, with 30% expected to be recognized in the next 12 months (up +37% y/y).

## Business Lines

(+) Azure growth of +43% y/y @cc was 3.5pts above the guidance midpoint (39.5%) and likely above buyside expectations. Upside was driven by efficiency gains across the CPU and GPU fleet, process improvements to enable earlier delivery of new capacity, and stronger than expected GitHub Copilot consumption. We underscore that while the outperformance was incredibly strong, results continue to be limited by supply constraints as mgmt. works toward balancing increasing Azure demand with growing needs across 1P services, increasing allocation to R&D teams, and replacement of end-of-life equipment. Demand continues to exceed supply across workloads, customer segments, and geographic regions.

(+) M365 Commercial Cloud +14% y/y @cc came in at the high end of guidance +13-14% on a reported basis. When adjusted for 1x rev rec benefit in the prior year, M365 Commercial Cloud grew +16% and accelerated from +15% in F3Q. Growth was again driven by a combination of seat growth (+6% y/y) and ARPU expansion which was led by Copilot, E5, and early E7 traction. M365 Copilot was now reported to exceed 30m paid seats vs >20m reported last quarter with net paid seat adds >2x q/q against guidance for "net paid seat adds to increase sequentially".

(+) Server Products declined -1% y/y @cc and was relatively unchanged on a reported basis, ahead of guidance that called for a MSD% decline on the back of continued mix shift to cloud partially offset by higher purchasing of licenses running in multi cloud environments.

(+) LinkedIn ticked up to +10% y/y @cc vs +9% in F3Q primarily driven by growth in Marketing Solutions.

(-) Dynamics 365 growth eased to +12% y/y @cc and grew in line with expectations for LDD% growth. Mgmt. noted bookings growth within ERP to remain healthy while CRM moderated with longer sales cycles.

(=) Search and News Advertising revenue (ex-TAC) +9% y/y @cc came in line with guidance for high single digit growth (flat sequentially as growth rates normalize).

(+) High margin Windows OEM + Devices revenue of -7% y/y was much better than guidance for mid-to-high teens decline attributable to lower PC market demand and a tough prior year comp partially offset by OEM and channel partners continuing to build inventory because of increasing component prices.

## Margins/EPS/CapEx

(+) Operating margin of 45.1% was +1.1pts above the implied guidance midpoint (44.0%) and +0.2pts y/y, benefiting from revenue and gross margin outperformance. Gross margin of 67.2% exceeded guidance of 66.2%, though was down -1.4pts y/y on continued investments in AI infrastructure and growing AI product usage, partially offset by efficiency gains in Azure and M365 Commercial Cloud.

(=) OpEx of \$19.9bn came in \~2.7% above the guidance midpoint (\$19.35bn) and grew 10% primarily driven by continued investments in R&D compute capacity, talent, and data to support product development. Adjusted for 1x charges (\$0.5bn net impact), primarily those tied to Xbox and the VRP, OpEx screens roughly in line with the guidance midpoint in our view. Despite gross margin headwinds, operating margins expanded >1pt on a full year basis to 46.8%. Total company headcount was noted to be down 2% y/y exiting FY26.

(+) Non-GAAP EPS of \$4.74 was in line with consensus, though benefited by \$2.0bn (\$0.27 EPS impact) from discrete items.

(+) Capex (inclusive of capital leases) rose by \$9.1bn sequentially to \~\$41.0bn in F4Q, in line with guidance to be >\$40bn with impact from higher component pricing. Roughly two-thirds was spent on short-lived assets, in line with last quarter and consistent with mgmt.'s messaging around capex mix shift.

## What We Liked / What We're watching on the Guide

(+) F1Q revenue guidance of \$90.4bn at the midpoint came in above Street (\$89.9bn); PBP and IC segment revenue guidance was ahead of consensus while MPC is guided below and declining y/y. FX is anticipated to be a <1pt headwind to revenue in the quarter. From a full year perspective, mgmt. expects another year of DD% revenue growth with a <1pt headwind from FX.

(+) F1Q Azure guidance of +45% y/y @cc was 4pts ahead of consensus \~41% and implies a 2pt acceleration from F4Q levels. Demand is still expected to remain ahead of supply and mgmt. remains focused on delivering infrastructure efficiencies to help bridge the gap between demand and supply. Despite a strong C1H26, mgmt. continues to expect C2H growth to accelerate.

(+) F1Q M365 Commercial Cloud guidance for +16% y/y @cc in line with F4Q when normalized for in-period rev rec benefit in the prior year comp. Beyond F1Q, mgmt. guided M365 Commercial Cloud revenue to accelerate through FY27, contributors to which include premium SKU momentum and increased monetization opportunity from adding usage based billing products.

(+) At midpoints, guidance for F1Q OM to remain relatively flat y/y in the 48.0% to 49.0% range, \~1pt above Street. Guidance embeds gross margins of 67.1% at the midpoint that are down 1.9pts y/y and OpEx growth of +7.5%. On a full year basis, op. income is expected to grow DD% once again with OpEx growing in the MSD-HSD% range calling for full year operating margins to tick down less than 1pt.

(+) From a CapEx perspective, CY26 CapEx was reset to \~\$175bn (vs. \~\$190bn previously), though the change is primarily accounting-driven following the extension of datacenter and office building useful lives from 15 to 25 years. The update shifts more future datacenter leases from finance to operating leases, the latter of what is generally not included in CapEx thus reducing reported CapEx without changing underlying investment levels. Consistent with that, management reiterated that CY26 investment expectations are unchanged and guided to >\$50bn of CapEx in F1Q reinforcing continued infrastructure investment to support demand. From a full year perspective, mgmt. did not give more direction beyond saying FY27 CapEx is expected to grow y/y. Microsoft is expected to be FCF positive in FY27.

(+) In other parts of the business, M365 Commercial Products as well as Server Products are expected to decline in the MSD% range for the full year as they lap higher transactional purchasing from the timing of product launches. Windows OEM and Devices is also expected to be impacted by lower PC market demand driven by high component prices in addition to already elevated inventory levels and comps that benefitted from W10 EOS, following which Windows OEM and Devices are expected to decline in the HDD% range for the full year.

## Estimate Revisions and Valuation

Incorporating F4Q results, guidance and our latest thoughts on the business we increase FY27/28 revenue estimates to \$388.5/\$459.4bn from \$384.2/\$448.0bn and non-GAAP EPS estimates to \$19.46/\$23.15 from \$19.45/\$22.75, respectively. We reiterate our \$550 TP, implying a P/E of \~25x our CY27E Non-GAAP EPS. We use a DCF to arrive at our target price. Our DCF is based on a WACC of 9.1%, a risk-free rate of 4.0% and an equity risk premium of 5.3%. We use a terminal growth rate of 3.5%, based on GDP growth. Downside risks to our Buy rating include: (1) Increased competition for AI and public cloud; (2) Further deterioration of the macro environment; and (3) Expectations for continued growth at large scale.

Figure 1: Key Charts

![](images/a6d1320b974cb2be2af2988eee8c3c97c838ca0c564565c57e557c8c8e9a5e2a.jpg)

![](images/a900dcfc4e5954b8754ce160707b8c66446abb9a0ccfd786dbc794006df264de.jpg)

![](images/5f989ef06db70f48fbabf40ead61922b8a9c3cc6fc74e2556947978205cc80a3.jpg)  
Source: Company Reports, DB Estimates

![](images/93ac3d9a68e67675f8cc794911f7b7cb9e2c79e009dc70529975e55023b6c05f.jpg)

Figure 2: F4Q26 Summary

<table><tr><td colspan="6">Microsoft (MSFT)In $mn except EPS</td></tr><tr><td rowspan="2"></td><td colspan="5">4Q26E</td></tr><tr><td>Actual</td><td>DBe</td><td>Actual vs. DBe</td><td>Cons.</td><td>Company guidance</td></tr><tr><td colspan="6">Income Statement</td></tr><tr><td>Productivity &amp; Business Process</td><td>37,847</td><td>37,171</td><td>+1.8%</td><td>37,235</td><td>37,000 - 37,300</td></tr><tr><td>Y/Y Growth</td><td>+14.3%</td><td>+12.3%</td><td></td><td>+12.5%</td><td></td></tr><tr><td>M365 Comm Cloud Y/Y Growth - CC</td><td>+14.0%</td><td>+13.5%</td><td></td><td>+13.8%</td><td>+13% - +14%</td></tr><tr><td>Intelligent Cloud</td><td>39,306</td><td>38,095</td><td>+3.2%</td><td>38,127</td><td>37,950 - 38,250</td></tr><tr><td>Y/Y Growth</td><td>+31.6%</td><td>+27.5%</td><td></td><td>+27.6%</td><td></td></tr><tr><td>Azure Y/Y Growth - CC</td><td>+43.0%</td><td>+39.5%</td><td></td><td>+39.5%</td><td>+39% - +40%</td></tr><tr><td>More Personal Computing</td><td>12,854</td><td>12,105</td><td>+6.2%</td><td>12,106</td><td>11,750 - 12,250</td></tr><tr><td>Y/Y Growth</td><td>-4.4%</td><td>-10.0%</td><td></td><td>-10.0%</td><td></td></tr><tr><td>Total Revenue</td><td>90,007</td><td>87,371</td><td>+3.0%</td><td>90,007</td><td>86,700 - 87,800</td></tr><tr><td>Y/Y Growth</td><td>+17.7%</td><td>+14.3%</td><td></td><td>+17.7%</td><td></td></tr><tr><td>Gross Profit</td><td>60,482</td><td>57,839</td><td>+4.6%</td><td>60,482</td><td>57,100 - 58,400</td></tr><tr><td>GM (%)</td><td>67.2%</td><td>66.2%</td><td></td><td>67.2%</td><td></td></tr><tr><td>Operating Income</td><td>40,603</td><td>38,487</td><td>+5.5%</td><td>40,603</td><td>37,700 - 39,100</td></tr><tr><td>OM (%)</td><td>45.1%</td><td>44.1%</td><td></td><td>45.1%</td><td></td></tr><tr><td>Y/Y Growth</td><td>+18.3%</td><td>+12.1%</td><td></td><td>+18.3%</td><td></td></tr><tr><td>Non-GAAP Net Income</td><td>35,286</td><td>31,017</td><td>+13.8%</td><td>35,286</td><td></td></tr><tr><td>Net margin (%)</td><td>39.2%</td><td>35.5%</td><td></td><td>39.2%</td><td></td></tr><tr><td>Non-GAAP EPS</td><td>$4.74</td><td>$4.17</td><td>+13.6%</td><td>$4.74</td><td></td></tr><tr><td colspan="6">Operating Metrics</td></tr><tr><td>Operating Cash Flow</td><td>55,441</td><td>49,028</td><td>+13.1%</td><td>55,441</td><td></td></tr><tr><td>Y/Y Growth</td><td>+30.0%</td><td>+15.0%</td><td></td><td>+30.0%</td><td></td></tr><tr><td>Capital Expenditures (incl. cap leases)</td><td>41,002</td><td>41,938</td><td>-2.2%</td><td>41,000</td><td></td></tr><tr><td>Levered Free Cash Flow (ex-cap leases)</td><td>19,639</td><td>14,080</td><td>+39.5%</td><td>19,639</td><td></td></tr><tr><td colspan="6">Source: DB estimates, Company data, Bloomberg Finance LP</td></tr></table>

Figure 3: Estimates Summary

<table><tr><td colspan="14">Microsoft (MSFT)In $mn except EPS</td></tr><tr><td rowspan="2"></td><td colspan="5">1Q27E</td><td colspan="4">FY27E</td><td colspan="4">FY28E</td></tr><tr><td>New Estimates</td><td>Old Estimates</td><td>New vs. Old</td><td>Cons.</td><td>Company guidance</td><td>New Estimates</td><td>Old Estimates</td><td>New vs. Old</td><td>Cons.</td><td>New Estimates</td><td>Old Estimates</td><td>New vs. Old</td><td>Cons.</td></tr><tr><td colspan="14">Income Statement</td></tr><tr><td>Productivity &amp; Business Process</td><td>36,855</td><td>36,654</

[中间内容因长度限制已省略]

t DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau
Group Chief Economist and Global Head of Research

<table><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre</td><td>Tower</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,</td><td>Minato-ku, Tokyo 106-</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Kowloon,</td><td>0041</td></tr><tr><td>Australia</td><td></td><td>Hong Kong</td><td>Japan</td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td>Tel: (852) 2203 8888</td><td>Tel: (81) 3 6730 1000</td></tr></table>

DB AG
21 Moorfields
London EC2Y 9DB
United Kingdom
Tel: (44) 20 7545 8000

DB Securities Inc.

The DB Center
1 Columbus Circle
New York, NY 10019
Tel: (1) 212 250 2500

DB AG
Filiale Singapur
One Raffles Quay, South Tower
Singapore 048583
Tel: (65) 6423 8001
"""
