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
Rating Market-Perform

Price Target

HON

264.00 USD (243.00 OLD)

# HON 2Q26 Post Earnings: The "show me" story is looking increasingly credible; raising TP to 264.

Recap of results: Top line organic growth was up 4% vs. expectations to be flat, and adjusted operating margin was largely in line with expectations at 19%. EPS of \$1.95 is \~7% ahead of consensus. Organic growth for all three segments came in better than expected (BA 9% vs. 6.5% consensus, PAT at -1% vs. -7.5% consensus, IA at 4% vs. 0.5% consensus). Segment operating margins also came in better than expected (\~20 - 30 bps depending on the business unit). Guidance was marginally raised as well for the full year; organic growth is up to 3 - 4% (vs. 2 - 3% earlier), segment margins are up to 20.3% at the midpoint (vs. \~20.0% earlier), and the EPS guidance midpoint is \$8.20 vs. \$8.10 in earlier.

Outlook commentary: We have received a lot of questions on Honeywell's 4 - 6% organic growth numbers for the back half of 2026. We think this is conservative, and reflects some amount of contingency; while we're modelling in this range, we think it's quite likely that Honeywell beats it. BA has printed mid-single consistently and there's no structural reason for that to slow down. Management has displayed high confidence that PAT will grow. Short-cycle industrial inflection will support at least some part of IA which came in well above expectations as well. All of these point to organic growth pushing at the high end of management's guide (if not higher). The only other big question we get is on the bridge for IA to go from \~17% margins to 22% by 4Q. We think about half of that comes from the spin of PSS / WWS which have been dilutive while the other half comes from operating leverage / self-help. Some of this is at risk if IA growth slows, but we do not anticipate that to be the case.

## Investment Implications

We continue to rate Honeywell Market-Perform with a \$264 target price. Based on updates per guidance, we use an NTM + 1 EPS of \$11.24 (Earlier \$10.19) at a 20x (unchanged from earlier) forward PE multiple. We then add \~\$39 per share (unchanged from earlier) of value from their stake in QNT (assuming a QNT TP of \$94 per Bernstein coverage). We believe our choice of multiple is conservative.

<table><tr><td>Close Date</td><td></td><td></td><td colspan="2">29 Jul 2026</td></tr><tr><td>HON Close Price (USD)</td><td></td><td></td><td colspan="2">241.12</td></tr><tr><td>Price Target (USD)</td><td></td><td></td><td colspan="2">264.00</td></tr><tr><td>Upside/(Downside)</td><td></td><td></td><td colspan="2">9%</td></tr><tr><td>52-Week Range</td><td></td><td></td><td colspan="2">260.15/195.77</td></tr><tr><td>SPX</td><td></td><td></td><td colspan="2">7,316.15</td></tr><tr><td>FYE</td><td></td><td></td><td colspan="2">Dec</td></tr><tr><td>Div Yield</td><td></td><td></td><td colspan="2">1.2%</td></tr><tr><td>Market Cap (USD) (M)</td><td></td><td></td><td colspan="2">76,421</td></tr><tr><td>EV (USD) (M)</td><td></td><td></td><td colspan="2">102,500</td></tr><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>17.9</td><td>5.8</td><td>1.2</td><td>10.1</td></tr><tr><td>SPX (%)</td><td>6.9</td><td>(1.7)</td><td>5.0</td><td>14.8</td></tr><tr><td>Relative (%)</td><td>11.0</td><td>7.5</td><td>(3.8)</td><td>(4.7)</td></tr><tr><td colspan="5">Source: Bloomberg, Bernstein estimates and analysis.</td></tr></table>

Price Performance, 1YR  
![](images/d4c0fbadb1f350bea07b59f7b938f8605393cbcc785c53f65fe083b82ff17752.jpg)

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>HON (USD)</td><td>6.46</td><td>8.37</td><td>10.55</td></tr><tr><td>OLD</td><td>--</td><td>8.26</td><td>10.02</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Adjusted P/E (x)</td><td>37.3</td><td>28.8</td><td>22.8</td></tr></table>

## DETAILS

## OVERVIEW

We were relatively skeptical on Honeywell's ability to deliver on the promise of growth and margins at Investor Day. After this print, we are much less skeptical. If the next few quarters are anything like 2Q26, we would expect the stock to see some re-rating. Remember, the P/E ratio you see is artificially inflated; you need to look at it ex-QNT which adds \~\$20 - 30 per share of value in which case the stock starts looking far more reasonable.

Top line organic growth was up 4% vs. expectations to be flat, and adjusted operating margin was largely in line with expectations at 19%. EPS of \$1.95 is \~7% ahead of consensus. Organic growth for all three segments came in better than expected (BA 9% vs. 6.5% consensus, PAT at -1% vs. -7.5% consensus, IA at 4% vs. 0.5% consensus). Segment operating margins also came in better than expected (\~20 - 30 bps depending on the business unit). Guidance was marginally raised as well for the full year; organic growth is up to 3 - 4% (vs. 2 - 3% earlier), segment margins are up to 20.3% at the midpoint (vs. \~20.0% earlier), and the EPS guidance midpoint is \$8.20 vs. \$8.10 in earlier.

## THOUGHTS ON THE BACK HALF (WITH CALLBACK COMMENTARY WOVEN IN)

We do think there is some level of conservatism in 2H26, especially on growth at 4 - 6%. While we have modelled this in line with guidance for now, we'd be looking for any signals from management on increased growth or accelerated margin expansion that could strengthen the story. There is certainly some contingency baked into that number from management, and short of a major escalation in the Middle East or a short-cycle collapse in industrials we think they are well poised on growth. Our segment level perspectives have been detailed below.

BA: This is the least cyclical and most stable pf Honeywell's business units. BA effectively start each year with a clean slate and drive orders and conversion from there, so it is dependent on sales performance in the Q. Generally, the team has done a great job and sustained HSD organic growth. We see no real tailwinds here that would cause growth to drop below HSD, it is largely just the uncertainty of needing to wait for orders to flow in that keeps guidance conservative. Margin expansion is also relatively straight line; we see it going from 27% today to \~29% in the next 2 - 3 years with sequential improvement.

IA: This is where we have been most impressed operationally. Honeywell is expected to reach 22% margins by 4Q26, and 25% as the mid-term target. While the market is extremely skeptical of this, management also seems to be extremely confident. We break the margin expansion into two pieces; near-term (teens to 22%) and mid-term (22% to 25%). In the near-term, we anticipate roughly half the expansion to come from the divestment of PSS and WWS which have been dilutive. The remaining half comes from a mix of “self-help” and operating leverage from growth. Short-cycle inflection (which affects a part of IA) also supports this outlook. In the mid-term, management said they expect to see the remaining margin expansion to be front-weighted (i.e., the journey from 22% to 25% happens more in FY27 than in FY28/FY29). While growth is guided LSD for the back half, we do think commercial excellence and positive short-cycle movement are all tailwinds, and MSD organic in 2H26 is not an unreasonable assumption.

PAT: In our call back (as with the earning call), management displayed a high degree of confidence in their ability to meet HSD organic growth in the back half of the year. Our understanding is that this is driven more by a recovery in catalyst volumes, while the strong LNG orders numbers provide a tailwind over the next two years. While we continue to think that oil capex is challenged, the positive inflection from gas and catalysts will likely more than offset any growth drag from refining. Margins are going to be less attractive for PAT in the near-term; there is expected to be a lot of projects in 2H26 which are dilutive, as well as the integration of Johnson Matthey which will also create near-term margin pressure. We are modelling weakness in the remainder of 2026, with an inflection in the back half of FY27/early FY28.

Forge: The one piece we thought we'd get more color on is Forge (Honeywell's digital / AI platform). The current target is 15% revenue growth on \~\$1B of annualized software revenues; we do think this seeks low given the high double digit (and in some case triply digit) YoY growth numbers in terms of connected assets we saw at their investor day. It seems like there is still some flux around the pricing strategy, but we think there's potential for this growth number to be higher long-term depending on how well Honeywell can execute. We'd love to see a bit more color in future prints.

EXHIBIT 1: HON Cons. vs reported

<table><tr><td>Group ($m)</td><td>2Q&#x27;25 Reported</td><td>2Q&#x27;26 Reported</td><td>2Q&#x27;26 VA Cons.</td><td>YoY change</td><td>Beat / Miss vs VA Cons.</td><td>% Beat / Miss</td></tr><tr><td>Revenue Remain co.</td><td>5,018</td><td>5,187</td><td>4,978</td><td>+3.4%</td><td>BEAT</td><td>+4.2%</td></tr><tr><td>Organic growth</td><td></td><td>4.0%</td><td>0.2%</td><td>400 bps</td><td>BEAT</td><td>383 bps</td></tr><tr><td>Segment profit Remain co.</td><td>904</td><td>985</td><td>943</td><td>+9.0%</td><td>BEAT</td><td>+4.4%</td></tr><tr><td>Operating margin</td><td>18.0%</td><td>19.0%</td><td>18.9%</td><td>100 bps</td><td>BEAT</td><td>5 bps</td></tr><tr><td>Adj. EPS ($) Remain co.</td><td>1.77</td><td>1.95</td><td>1.82</td><td>+10.2%</td><td>BEAT</td><td>+7.4%</td></tr></table>

<table><tr><td>Segments ($m)</td><td>2Q&#x27;25 Reported</td><td>2Q&#x27;26 Reported</td><td>2Q&#x27;26 VA Cons.</td><td>YoY change</td><td>Beat / Miss vs VA Cons.</td><td>% Beat / Miss</td></tr><tr><td colspan="7">Industrial Automation</td></tr><tr><td>Revenue</td><td>1,577</td><td>1501</td><td>1,457</td><td>-5%</td><td>BEAT</td><td>+3.0%</td></tr><tr><td>Organic growth</td><td>0.0%</td><td>4.0%</td><td>0.5%</td><td>400 bps</td><td>BEAT</td><td>350 bps</td></tr><tr><td>Segment operating Income</td><td>257</td><td>258</td><td>247</td><td>0%</td><td>BEAT</td><td>+4.5%</td></tr><tr><td>Segment operating Margin</td><td>16.3%</td><td>17.2%</td><td>16.9%</td><td>90 bps</td><td>BEAT</td><td>25 bps</td></tr><tr><td colspan="7">Building Automation</td></tr><tr><td>Revenue</td><td>1,826</td><td>2002</td><td>1,954</td><td>10%</td><td>BEAT</td><td>+2.5%</td></tr><tr><td>Organic growth</td><td>8.0%</td><td>9.0%</td><td>6.5%</td><td>100 bps</td><td>BEAT</td><td>250 bps</td></tr><tr><td>Segment operating Income</td><td>479</td><td>542</td><td>524</td><td>13%</td><td>BEAT</td><td>+3.5%</td></tr><tr><td>Segment operating Margin</td><td>26.2%</td><td>27.1%</td><td>26.8%</td><td>87 bps</td><td>BEAT</td><td>29 bps</td></tr><tr><td colspan="7">Process Automation</td></tr><tr><td>Revenue</td><td>1,613</td><td>1679</td><td>1,549</td><td>4%</td><td>BEAT</td><td>+8.4%</td></tr><tr><td>Organic growth</td><td>6.0%</td><td>-1.0%</td><td>-7.5%</td><td>-700 bps</td><td>BEAT</td><td>650 bps</td></tr><tr><td>Segment operating Income</td><td>386</td><td>371</td><td>342</td><td>-4%</td><td>BEAT</td><td>+8.4%</td></tr><tr><td>Segment operating Margin</td><td>23.9%</td><td>22.1%</td><td>22.1%</td><td>-183 bps</td><td>BEAT</td><td>0 bps</td></tr></table>

Source: Visible Alpha, Company reports, Bernstein analysis

## EXHIBIT 2: HON three year financial targets

## 2026 Investor Day | Three-year financial targets

Organic growth: 4% - 6%
\~15% annual recurring
software revenue growth

Segment margin: \~24% \~60 bps average annual segment margin expansion

Adjusted EPS: \~\$12.00
10%+ annual adj. EPS growth

Free Cash Flow: >\$3B
90%+ conversion

Durable growth acceleration

Operational excellence

Strategic capital deployment

Clear roadmap for shareholder value creation

Honeywell Technologies

2Q 2026 Earnings – July 23, 2026

Source: Company presentation

2Q 2026 Earnings – July 23, 2026

![](images/3ef3babccc8712fc2a335ee3b2ebb231c432c273bd47d74e84cdb06d31c56d59.jpg)  
EXHIBIT 3: HON orders acceleration

## Honeywell Technologies | 2Q 2026 orders growth acceleration

\- Double-digit short-cycle orders growth in all segments, driving total orders up $16\%$ organically

\- PA&T orders up 24% organically driven by surging LNG and gas processing demand globally

\- BA up $13\%$ organically from resilient demand and share gains led by growth in Fire and focus growth verticals (data centers, healthcare and hospitality)

• IA orders up 10% organically, with double-digit growth in Europe, Middle East and China

\- Orders grew over 50% organically in the Middle East, driven by large awards in Process Technology

\- \$5.7B in orders with book-to-bill above 1.1x; continued backlog growth (+9%) supports 2H organic growth outlook of 4% to 6%

## Broad-based, double-digit order growth across all segments

Source: Company presentation

## EXHIBIT 4: HON revised guidance

## Honeywell Technologies | Revised 2026 Guidance

<table><tr><td></td><td>Prior 2026 Guidance</td><td>2026 Guidance</td><td>3Q26 Guidance</td><td>4Q26 Guidance</td><td>Commentary</td></tr><tr><td> $Sales^1$ Organic growth*</td><td>$19.9B - $20.2B2% - 3%</td><td>$19.8B - $20.0B3% - 4%</td><td>$4.9B - $5.0B4% - 6%</td><td>$5.0B - $5.1B4% - 6%</td><td>· Raising full-year organic growth, segment margin and adjusted EPS estimates· BA strength continues across both products and solutions with double-digit growth across data centers, hospitality and healthcare</td></tr><tr><td>Segment Margin* Expansion</td><td>19.8% - 20.3%220 - 270 bps2</td><td>20.1% - 20.5%250 - 290 bps2</td><td>20.0% - 20.7%240 - 310 bps2</td><td>22.0% - 22.7%400 - 470 bps2</td><td>· PA&amp;T growth to inflect in 3Q as project activity and catalyst shipments accelerate, supported by robust backlog</td></tr><tr><td>Adjusted EPS* Growth</td><td>$7.90 - $8.3022% - 28%2</td><td>$8.05 - $8.3525% - 29%2</td><td>$2.05 - $2.2021% - 29%2</td><td>$2.28 - $2.4325% - 33%2</td><td>· Core IA growth accelerates through the second half led by products· Margin expansion led by IA and BA, with tailwinds from stranded costs elimination and divestitures</td></tr><tr><td>Free Cash Flow *3</td><td>~$2.0B</td><td>~$2.0B</td><td></td><td></td><td>· Below the line tailwind year-over-year from lower net interest expense driven by accelerated debt paydown</td></tr></table>

■ Building Automation ■ Process Automation

EXHIBIT 5: HON Revenue \$bn  
![](images/0e9ee70a04a580f1c596ef15ec6e48f7862387573bfaa9288398c5eb0d1506a9.jpg)  
Source: Company reports, Bernstein estimates and analysis

EXHIBIT 6: HON revenue per segment \$bn  
![](images/6489722de390227dc33dbbe7cd1cb4d597acba20a429db07a31c907f93a4f9df.jpg)  
- Industrial Automation  
Source: Company reports, Bernstein estimates and analysis  
EXHIBIT 7: HON Gross profit & GP margin \$bn

![](images/7819c8f5fd9983b66b9fc65f48ccf301b99a8899ab2044e0f25e06554ef20b4f.jpg)  
Source: Company reports, Bernstein estimates and analysis  
EXHIBIT 8: HON EBIT & EBIT margin % \$bn

![](images/d9552d3f65d036fe931315194248987a28facdc8ca323f2650caa6c58a1b3846.jpg)  
Source: Company reports, Bernstein estimates and analysis

EXHIBIT 9: HON EBIT per segment \$bn  
![](images/ee2bc53c29adfc11a2d70d01d9b17d87b487506c3bfae472a226558f35a5c169.jpg)  
Source: Company reports, Bernstein estimates and analysis

EXHIBIT 10: HON Net Income & Net Income margin % \$bn

EXHIBIT 11: HON Adj. EPS (\$)  
![](images/73701852fb1bbc50940ffca18e1467ad2ff30b5abc700feb7bffcb888ccf7216.jpg)  
Source: Company reports, Bernstein estimates and analysis

![](images/ddac56e92daf0c3cde305c569ffccb4d0d7377a9d888ea39e50ddc6050a68da7.jpg)  
Source: Company reports, Berns

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
