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
US Media & Telecom

Netflix Inc

Rating

Outperform

Laurent Yoon
+1 917 344 8502
laurent.yoon@bernsteinsg.com

Price Target

100.00 USD (110.00 OLD)

NFLX

![](images/9347dc6fe02cd13743a2f7f1d40b125e9b165cdfa22074a5fd5e4e5c7db1d62c.jpg)

![](images/a488730d9fb452973f025ecd320597f9ffafa0386a3c9cc66a5e76f300088af3.jpg)

Martin Boruchowicz
+1 917 344 8564
martin.boruchowicz@bernsteinsg.com

![](images/d23163f4a6bfc2d8872cd016b80cb8113323c22f3e4df4487454172ec5afbbaa.jpg)

Andrew Chung
+1 917 344 8302
andrew.chung@bernsteinsg.com

# NFLX Q2: More than a quarter - key debates heading into the print

There's a lot riding on Q2 as Netflix faces no shortage of near and longer-term questions—from Q2 engagement trends and potential revisions to 2026 margin guidance to the broader challenge of sustaining growth amid evolving consumer preferences and viewing behavior.

There are six (too many) key debates heading into the print:

Q2 surprise? Much of it is well-understood. WC26 likely further exacerbated seasonally softer Q2 engagement, creating an incremental headwind to subscriber growth during the quarter. The more important question is how much of the headwind is reflected in the company's 2026 outlook.

The high end of revenue guidance could be at risk. Net additions below high-teens million would likely make the upper end of Netflix's '26 revenue guidance (14%) more difficult to achieve and could create modest downside risk to EPS expectations. While it is reasonable to assume subscriber growth returns to a more normal cadence in 2H26 (ex-July headwind from WC26), it is less likely that growth can accelerate sufficiently to offset 1H headwinds.

Can advertising offset subscriber growth pressure? A softer subscriber trajectory could be mitigated by >\$3B ad revenue, providing support to both revenue and EPS. While there is no reliable third-party data source to track Netflix's ad revenue, broader market conditions continue to point to healthy CTV ad demand, which should further support Netflix's ad business momentum. Summary continues on the following page...

## Investment Implications

We maintain an Outperform rating for Netflix with a revised PT of \$100 (-10). '26 EPS adj are due to subscriber growth pressure (-3M) from WC26, while our '27 adj reflects a reacceleration in subscriber growth (+4M) driven by the anticipated ad-tier expansion into 15 new markets. We also adjusted our valuation multiple down from 29x to 26x, to reflect challenges discussed weighing on investor sentiment in the foreseeable future.

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>(18.8)</td><td>(7.3)</td><td>(16.0)</td><td>(40.9)</td></tr><tr><td>SPX (%)</td><td>9.6</td><td>1.6</td><td>8.4</td><td>20.4</td></tr><tr><td>Relative (%)</td><td>(28.4)</td><td>(8.9)</td><td>(24.5)</td><td>(61.4)</td></tr></table>

<table><tr><td>Close Date</td><td>7 Jul 2026</td></tr><tr><td>NFLX Close Price (USD)</td><td>76.18</td></tr><tr><td>Price Target (USD)</td><td>100.00</td></tr><tr><td>Upside/(Downside)</td><td>31%</td></tr><tr><td>52-Week Range</td><td>129.50/70.86</td></tr><tr><td>SPX</td><td>7,503.85</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>NA</td></tr><tr><td>Market Cap (USD) (M)</td><td>320,779</td></tr><tr><td>EV (USD) (M)</td><td>325,232</td></tr></table>

Price Performance, 1YR  
![](images/4ebe3ec2bc9773528b7c925dc2d6381ffcb86c15eaf6d387fa8911ca514e14b0.jpg)

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>NFLX (USD)</td><td>2.53</td><td>3.15</td><td>3.83</td></tr><tr><td>OLD</td><td>--</td><td>3.20</td><td>3.80</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>EBITDA (M)</td><td>13,660</td><td>16,721</td><td>19,863</td><td>--</td></tr><tr><td>Revenues (M)</td><td>45,183</td><td>51,329</td><td>57,434</td><td>--</td></tr><tr><td>EBIT (M)</td><td>13,327</td><td>16,341</td><td>19,449</td><td>--</td></tr></table>

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Adjusted P/E (x)</td><td>30.1</td><td>24.2</td><td>19.9</td></tr><tr><td>EV/EBITDA (x)</td><td>23.8</td><td>19.5</td><td>16.4</td></tr><tr><td>EV/EBIT (x)</td><td>24.4</td><td>19.9</td><td>16.7</td></tr></table>

## DETAILS

Summary continued...

Margin revision? It may not be the base case. Netflix has raised its full-year margin outlook alongside Q2 results over the past two years. If ad revenue is tracking ahead of expectations and content spending remains below \$20B budget, a 50 bps + margin increase appears achievable despite slower subscriber growth. Conversely, maintain the current guide could be interpreted as confirmation that subscriber headwinds are significant enough to warrant waiting until Q3 for greater visibility—a scenario that would likely further weigh on sentiment.

What if Netflix discontinues the engagement report? Investor concern is growing around the possibility that Netflix may stop publishing its semiannual What We Watched engagement report, following the company's decision to pull subscriber metrics. While the rationale may be understandable, eliminating the report would further weigh on already challenged sentiment in the near-term.

Engagement has become a perennial debate and likely to remain one for years as consumer preferences and viewing behavior continue to evolve. This does not imply that long-form storytelling is in decline, but it does suggest that traditional long-form platforms must continue adapting to changing viewer behavior. With increasing uncertainties around both the “what” and the “how” to get there, M&A speculation is likely to persist (and Netflix should explore options). Until investors gain greater confidence on the future state, a narrative centered on PxQ and a steady drumbeat of EPS growth may prove insufficient to sustain a premium valuation multiple.

## RECENT RELEVANT NOTES

7 Jul 2026 - US Media: The cost of growth - the return of rising content spend

30 Jun 2026 - Comcast (CMCSA): The Optionality Spin

23 Jun 2026 - Netflix: At 52-lows, we expect continued near-term volatility

4 Jun 2026 - Netflix: Messy Near-Term Narrative, but a Durable Engine

22 May 2026 - Weekend Media Blast: The Battle of 16:9 vs 9:16

20 May 2026 - State of the Media Industry (1Q26): Industry grows with steady margins - calm before the storm?

14 May 2026 - Netflix to launch AVOD-tier in 15 more countries in 2027 - more about 'Q' than \$

17 Apr 2026 - Netflix 1Q26: Streaming Growth, Buffering Margins?

1 Apr 2026 - NFLX: Deconstruction of Netflix's content spend and implications on '26 EPS

27 Mar 2026 - NFLX: Price hike secures double-digit revenue growth in '26

19 Mar 2026 - NFLX: Engagement - more nuanced than the headline

12 Mar 2026 - NFLX: What is the range of EPS upside for 2026?

4 Mar 2026 - State of the Media Industry (4Q25): Margin pressure on deck

## NETFLIX'S STOCK PERFORMANCE AND STORY HEADING INTO Q2

Netflix shares have had a rough 2026, down roughly \~19% on an absolute basis and underperforming the broader market by \~30% YTD. Coming into the year, the WBD M&A overhang kept shares pressured. When Netflix walked away from the bid, shares had a sharp recovery and steadily re-rated higher as investors refocused on the fundamentals heading into Q1. However, management's reiteration of a soft full-year outlook during Q1 sent shares lower again. The stock has drifted steadily lower over the past three months as concerns around engagement and subscriber growth pressures from the FIFA World Cup weighed on the narrative. NFLX hit a 52-week low in late June and currently trades at \~20x '27 Consensus EPS (Exhibit 1).

EXHIBIT 1: NFLX stock has underperformed the market  
NFLX vs S&P YTD share price indexed to 1/1/26  
![](images/360e62902365d1287ce72cbdd5756b99620152e4c4266002b470edf77a6b4e1d.jpg)  
Source: Bloomberg, Bernstein analysis

## FY26 GUIDANCE: RISKS AND OFFSETS

Netflix's full-year revenue guidance of 12% – 14% YoY growth rests on subscriber growth, pricing, and projected doubling of ad revenue to \~\$3B. With the March 2026 price hike now fully in effect, and advertising expectations set, hitting the top end of the guidance range likely requires net subscriber additions of roughly 20-23M for the year, implying around \~7% membership growth (Exhibit 4). The concern heading into Q2 is whether 1H subscriber growth has tracked to that pace. Engagement pressures from the FIFA World Cup, have raised questions about whether Netflix subscriber growth has been slower. Without a clear catalyst or a particularly strong content slate in the back half of the year, we view an acceleration in H2 subscriber growth to bridge any 1H shortfall as unlikely.

That said, we think advertising strength could be a factor allowing management to emphasize the top end of the guidance even if subscriber growth is tracking below expectations. The ad tier continues to demonstrate strong subscriber momentum and increasing scale + ad market tailwinds may help Netflix outperform expectations and make up for subscriber softness. And as discussed in a recent note, we believe the advertising business carries high contribution margins, and incremental revenues above the target would be highly accretive to EPS (Exhibit 2).

We also see that management has established a track record of guiding conservatively on margins and revising upward as the year progresses (Exhibit 5), and for FY26, we believe upward revisions to margins can be driven by advertising contribution and content cost timing. On the ad side, as discussed, incremental revenue above the \$3B target carries high contribution margins and flows to the bottom line.

On content, management guided full year content amortization growth of $\sim 10\%$ , front loaded into the first half, with Q2 explicitly flagged as the peak growth quarter before decelerating to mid-to-high single digits in H2. 1Q results came in on track with that envelope, though Q2 through H2 results may still yield lower than expected full year results (as discussed in a previous note). Looking at historical quarterly content allocation pattern and the timing of expenses, a Q2 content amortization growth rate in the low-to-mid-teens YoY is consistent with management's guidance and prior seasonal patterns (Exhibit 6). A result that comes in below that range or a steeper deceleration in H2 would be a direct tailwind to margins and EPS.

Overall, slower-than-expected member growth is the clearest near-term risk — if 1H subscriber trends have tracked below the implied \~20–25M net add pace, the market is likely to react negatively. However, we think the setup has meaningful positive

offsets. Stronger-than-expected advertising revenue and/or lighter content costs could allow management to reiterate full-year revenue guidance with an emphasis on the top end of the range, while also supporting an upward margin guidance revision (Exhibit 3). In that scenario, the stock has a clear path to a positive reaction off already depressed levels.

EXHIBIT 2: If subscriber growth has fallen below expectations in 1H, we believe advertising strength could still help reach the top end of revenue guidance for the year  
![](images/cc3307a2884263103e5c251d6381249c47824b9274d6c948232a15d261c4ae8d.jpg)  
Source: Bernstein analysis

EXHIBIT 3: A positive reaction for the stock can be driven by updated guidance on advertising and/or lower content costs leading to higher margins

<table><tr><td><img src="images/f5f91065f2293af7c82d9b7a2e30b524eea4edd0b9dd4b963a99ba4beb594333.jpg"/></td><td>• Slower member growth leads to slower revenue growth and lower EPS
• Even when idiosyncratic (WC2026), narrative worsens</td></tr><tr><td><img src="images/70b13e7fc567c7a179791a309e61ff78e66a042aa88ac8cff86476f0c665fc01.jpg"/></td><td>• Increasing ad scale and market tailwind could lead to higher ad revenue with higher marginal contribution</td></tr><tr><td><img src="images/bc1a801c47c650461cdbcc3e267ff4ca1065616ff202c3891c0c01f2034d80d1.jpg"/></td><td>• Membership growth headwind could be offset by advertising tailwind
• Revenue guide remains and potential for EPS upside
• But future member growth remains a question</td></tr><tr><td><img src="images/1f26d25856f7e1e367196f12859523ac54f8329b4e40d402306d5985d8d0ed6a.jpg"/></td><td>• Leads to EPS upside
• Q2 content amort expected to peak, and could provide an indication for Q3 and Q4 amort schedule</td></tr><tr><td><img src="images/347d0401736f28865c2f314920ecdcd75b06e071136bff287c598b84aa2fe29e.jpg"/></td><td>• Even with membership growth headwind, Ad growth and lower content spend would lead to higher EPS—the most favorable outcome for the quarter and the year</td></tr></table>

Source: Bernstein analysis

EXHIBIT 4: Subscriber growth is estimated to be \~7% in order to reach the high end of revenue guidance. However, there is risk to that number as sports engagement (FIFA) may be pressuring NFLX subscriber growth

Estimated ad revenue, subscriber growth, and price increase contributions to 2026 Revenue growth  
![](images/acc7197ecb91ce330d42445f87b908d665768a003bf3bbefd688cfb554e7880d.jpg)  
Source: Bernstein analysis

EXHIBIT 5: Management has made upwards revisions on margins during Q2 for the past two years  
![](images/15859dc6a4247b614281b053c365e80599ec6665ca754cb7b3e6db03836ed2c8.jpg)  
Source: Company reports, Bernstein analysis

Yearly Content Amortization Costs and Quarterly Breakdown  
EXHIBIT 6: Amortization costs are expected to grow up to 16% in Q2 based off of historical timing of content expenses and assuming the full amortization envelope guidance  
![](images/e0642c0e1d4497ced5ccea5d675102297266b156605fed6de30c1356c7f6c29a.jpg)  
Source: Company reports, Bernstein analysis

EXHIBIT 7: Over the past 3 months consensus revenue for Q2 has come down only slightly  
![](images/e21de56bb865d2f2fd4f5c9c2c61786b1bd43c7166ccfcc133aa6a1cdb165bca.jpg)  
Source: Bloomberg, Bernstein analysis

EXHIBIT 8: Over the past 3 months consensus revenue for FY26 has come down only slightly  
![](images/dbfb1d87ebd42aebaa92a578b03c505020aec3004ee9b9489ddf88c09007d31d.jpg)  
Source: Bloomberg, Bernstein analysis

EXHIBIT 9: On the other hand Q2 EPS estimates has remained flat  
![](images/5101fa8598902f6ffe553a0d328f584a9d9da81fbf9903acefd182bea419399e.jpg)  
Source: Bloomberg, Bernstein analysis

EXHIBIT 10: FY26 EPS estimates have also remained flat  
![](images/3323b433262f5e04fdd9f80a0eee7b06436427bc3bcd3effb42b70288cac401d.jpg)  
Source: Company reports, Bernstein analysis

## APPENDIX - FINANCIAL FORECASTS

## EXHIBIT 11: NFLX Financial Summary

in millions except per share and percentage data

<table><tr><td>NFLX</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>FY2025</td><td>FY2026E</td><td>FY2027E</td></tr><tr><td>GAAP INCOME STATEMENT</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>12,250</td><td>12,547</td><td>12,986</td><td>13,546</td><td>45,183</td><td>51,329</td><td>57,434</td></tr><tr><td>Cost of Revenue</td><td>5,888</td><td>6,150</td><td>6,451</td><td>6,843</td><td>23,275</td><td>25,332</td><td>27,459</td></tr><tr><td>Marketing expense</td><td>842</td><td>788</td><td>845</td><td>1,208</td><td>3,301</td><td>3,683</td><td>4,027</td></tr><tr><td>Technology and development</td><td>960</td><td>934</td><td>911</td><td>946</td><td>3,391</td><td>3,751</td><td>4,081</td></tr><tr><td>General and administrative</td><td>603</td><td>565</td><td>517</td><td>539</td><td>1,888</td><td>2,223</td><td>2,418</td></tr><tr><td>Total Expenses</td><td>8,293</td><td>8,436</td><td>8,723</td><td>9,536</td><td>31,856</td><td>34

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
