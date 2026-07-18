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
U.S. Medical Devices
Abbott Laboratories

Rating

Outperform

Price Target

ABT

117.00 USD (110.00 OLD)

![](images/765dfa582f2cb9f103abb75f9b29c5e23eddaf9bb2f7c22607b52e50e7faefc8.jpg)

Lee Hambright
+1 917 344 8429
lee.hambright@bernsteinsg.com

![](images/b5f3c504e18f7bdf01a1112434163cb225c07a9a07d08672ebf6059d375c1bc9.jpg)

Adam Chow
+1 212 845 7820
adam.chow@bernsteinsg.com

Specialist Sales

![](images/80fd0f8d2168c801c1866583ead97def7c15457e1f7d9201b2ba336fee2782da.jpg)

Christian Moore
+1 917 344 8555
christian.moore@bernsteinsg.com

# Abbott 2Q26: EPS beat and raise on in-line sales, and a vehement defense of medtech market health

EPS beat and raise on in-line sales. Revenue grew 4.8% on a comparable basis to \$12.59bn, just ahead of consensus (\$12.54bn) by 0.4%. All segments came in above consensus: Medical Devices (8.4% growth, 0.6% beat), Diagnostics (2.9% growth, 1.6% beat), Established Pharmaceuticals (8.7% growth, 1.2% beat). Nutrition sales declined 3.6%, but beat consensus 0.9% with recovery better than internal expectations. Adj EPS of \$1.31 was modestly ahead of consensus (\$1.28) by 3 cents (2.6%), driven primarily by a 50bps beat on gross margin (58.0%). ABT held FY26 sales guidance at 6.5%-7.5% comparable growth and raised EPS guidance by 4.5 cents (after a 3-cent beat in Q2).

2H acceleration driven by 4 segments. After acceleration from 3.7% comparable growth in Q1 to 4.8% in Q2, ABT sees acceleration to \~8.7% comparable growth in the second half, driven by (1) Nutrition, (2) Electrophysiology, (3) Core Lab, and (4) Cancer Diagnostics.

Vehement defense of medtech markets. After Tuesday's pre-release from HCA highlighted Q2 declines in inpatient and outpatient procedure volumes (see our take), investors have been keen to get company perspectives on procedure trends. On Wednesday, JNJ said they saw no sign of a slowdown in underlying procedure markets. Yesterday, ABT doubled-down on this view, claiming both that (1) they also saw no signs of slowdown and, (2) fears were grounded in the “flawed assumption” that declining enrollment in ACA or Medicaid are impactful to medtech markets. With added encouragement from in-line surgical volumes at UNH (Wilkes), Medtech stocks rallied on Thursday.

## Investment Implications

We rate ABT Outperform with a price target of \$117 (up from \$110) using a target P/E multiple of 19x (up from 18x to reflect increasing confidence in growth forecast) against our forward Q5-Q8 EPS estimate of \$6.16 (up from \$6.09). For more, see our 4Q25 and 1Q26 recaps. Updated model: ABT

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>ABT (USD)</td><td>5.14</td><td>5.52</td><td>5.88</td></tr><tr><td>OLD</td><td>--</td><td>5.48</td><td>5.95</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>Revenues (M)</td><td>44,328</td><td>50,212</td><td>54,591</td><td>11.0%</td></tr><tr><td>Organic Sales Growth (%)</td><td>6.4</td><td>7.8</td><td>8.6</td><td>--</td></tr><tr><td>Gross Profit (M)</td><td>25,326</td><td>27,510</td><td>29,987</td><td>8.8%</td></tr><tr><td>Adj. Operating Margin (%)</td><td>23.2</td><td>24.0</td><td>24.7</td><td>--</td></tr><tr><td>Operating Earnings (M)</td><td>10,379</td><td>11,583</td><td>12,945</td><td>11.7%</td></tr><tr><td>Adjusted Net Income (M)</td><td>9,040</td><td>9,670</td><td>10,254</td><td>6.5%</td></tr></table>

<table><tr><td>Close Date</td><td>16 Jul 2026</td></tr><tr><td>ABT Close Price (USD)</td><td>98.83</td></tr><tr><td>Price Target (USD)</td><td>117.00</td></tr><tr><td>Upside/(Downside)</td><td>18%</td></tr><tr><td>52-Week Range</td><td>137.49/81.97</td></tr><tr><td>SPX</td><td>7,533.77</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>2.6%</td></tr><tr><td>Market Cap (USD) (M)</td><td>172,143</td></tr><tr><td>EV (USD) (M)</td><td>199,172</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>(21.1)</td><td>9.1</td><td>(18.8)</td><td>(25.0)</td></tr><tr><td>SPX (%)</td><td>10.1</td><td>0.3</td><td>8.6</td><td>20.3</td></tr><tr><td>Relative (%)</td><td>(31.2)</td><td>8.8</td><td>(27.4)</td><td>(45.3)</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.  
Price Performance, 1YR

![](images/93aef1274d53cf40155ab420742c5af33652f800b21b57c74957b837cbd443a3.jpg)

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Adjusted P/E (x)</td><td>19.2</td><td>17.9</td><td>16.8</td></tr><tr><td>PEG Adjusted (x)</td><td>1.9</td><td>2.4</td><td>2.6</td></tr><tr><td>EV/EBITDA (x)</td><td>14.8</td><td>16.1</td><td>13.7</td></tr><tr><td>Div Yield (%)</td><td>4.2</td><td>2.3</td><td>2.4</td></tr><tr><td>EV/FCF (x)</td><td>18.4</td><td>27.5</td><td>19.4</td></tr><tr><td>EV/Sales (x)</td><td>4.5</td><td>4.0</td><td>3.6</td></tr></table>

## DETAILS

## Vehement defense of the health of underlying medtech markets

Over the past few months, hospital commentary has stoked fears that utilization growth could slow in 2H26, driven in part by declining enrollment in ACA plans and cuts to Medicaid. When HCA pre-released 2Q26 revenue on Tuesday—highlighting a 2.3% decline in same-facility inpatient surgery volumes and a 3.4% decline in same-facility outpatient surgery volumes—these fears boiled over, and medtech stocks dropped 3%-7% (see our takeaways from HCA's pre-release).

Flawed assumption. Abbott CEO Robert Ford characterized medtech procedure volume fears as having been driven by "a flawed assumption." Ford made the case that medtech and diagnostics businesses are less impacted by changes in ACA and Medicaid. ABT has seen no sign of procedure growth slowdown and does not expect any material impact in 2H26. Management emphasized that Medicare drives medtech surgical procedures, with two-thirds of Abbott's U.S. cardiovascular business coming from Medicare.

"...I think it's less of a concern for the companies... in the markets that we're operating in. I think there's a couple reasons for that. I think some of the concern for the decline in volumes is tied to... challenges with the ACA, lower enrollment rates or disenrollment rates in Medicaid. I think that's a flawed assumption,..., as it relates to the medtech and diagnostic space. If you go back to when the ACA was implemented, really the pharma companies... predominantly benefited from new patients coming into the market, we didn't see that in medtech or in diagnostics. We didn't see a spike in demand when the ACA and the expansion of Medicaid happened. I think it's logical here to assume that if we didn't see the benefit, I don't think we're going to see the downside, if that truly is what's happening. I think one reason for that is that it's not Medicaid that is a driver of medtech surgical procedures in the U.S. It's actually Medicare. Medicare is by far the largest U.S. payer as it relates to devices. For us, it's over two-thirds of our U.S. cardio business. I think that's one reason. The other reason that I believe it's not a concern, at least right now we're not seeing it, is that not all healthcare products are the same here. Demand for high acuity life-saving products is very inelastic. In the U.S., we treat people with serious acute medical conditions, and the system doesn't save lives of only those people with insurance. That's why we didn't see the impact of expansion of ACA and Medicaid into the business, because those patients were already being treated. If you look at our portfolio, it's really tied, and maybe this is a little bit more of an Abbott side, we're really tied to a lot of major chronic conditions like diabetes, cardiovascular, cancer, and this is less likely to forego insurance. I think that's one reason."

Dx as a barometer. Management positioned Abbott's Diagnostics business as a forward-looking barometer for procedural demand, emphasizing that in their Hospital Labs business—which focuses on instruments and reagents for hospital and in-hospital testing—management saw strong growth of 13%, indicating strong future demand.

"...our diagnostic business [...] provides us, I think, a forward-looking into the healthcare environment and the healthcare system. Our instruments are located across the world, across the country, all in the States here in the U.S. Testing volumes in the U.S. have held up very well. Not seeing a decline, including in the States that we've seen the highest level of ACA disenrollment. We've gone as deep as looking at it from that perspective. Our U.S. Core Lab business has accelerated growth in the last 2 quarters. Our print here is about $7.5\%$ this quarter. If you unpack that, we've got a couple different segments in our U.S. Core Lab business,..., labs, and then specifically hospital labs. This is our business for selling instruments and reagents specifically for hospital and in-hospital testing. That business was up $13\%$ in this quarter. I think if I look at the diagnostic system as a forward-looking barometer there, we're not seeing that. We're seeing strong demand for our U.S. cardio business. I'd argue that our U.S. cardio business is performing better than it's ever been. We're seeing that same similar strong, stable demand internationally, both in developed and emerging markets. I feel very good about overall healthcare markets and especially our markets. [...], and I think the demand is, right now, we don't see it as a concern."

## Confidence in H1 to H2 growth acceleration driven by 4 things

Management expressed strong confidence that Q2 momentum would continue and drive accelerating sales and earnings growth in 2H26. CEO Robert Ford broke down the majority of that growth as coming from four buckets: (1) Nutrition, (2) Electrophysiology, (3) Core Lab, and (4) Cancer Diagnostics.

"...I think Q2 results showed that we've got momentum that's building. [...] The lift in the second half, 80% of that lift, I'm going to call it trajectory shift, is really coming from four areas: nutrition, electrophysiology, core lab, and cancer diagnostics. Each of these four businesses are entering with a lot of momentum and line of sight to the drivers of the business. [...], nutrition is tracking slightly ahead of expectations. Several of our strategies, whether it's pricing, new product launches, commercial execution, that's all being done very well by the team. EP, we've got a lot of great launch activity, a lot of good feedback on our new products. I expect the second half of the market to really show that growth acceleration that we've been forecasting. In our Core Lab business,..., our businesses have performed very well across the world. We obviously had the challenge of the VBP in China, where we had a pretty sizable portion of our international business decline for at least five quarters, around 30%. We're still forecasting a decline in the China business, but much, much lower, mid-single digits. That allows some of the other businesses that have continued to do very well, and actually accelerate to kind of overpower that China impact. Cancer diagnostics, very good trajectory there, especially with new Cologuard users. They're exceeding our expectations. I've learned a lot about these care gap programs. I've got confidence in them. We've got a lot of work around them, and I'm confident in that. It's really those four businesses that represent the significant shift. Obviously, all the other businesses have got to continue to do well, and they've got all their strategies. If I were to kind of really focus on what's going to drive that second half, it's these four areas here, and they're actually going into Q3 with a lot of good momentum, some of them a little bit ahead of what we thought we would be at. We feel good about that second quarter acceleration."

## EPS beat and raise on in-line sales

In-line sales. 2Q26 sales grew 4.8% on a comparable basis to \$12.59bn, just ahead of consensus (\$12.54bn) by 0.4%. FX had a favorable YoY impact of 0.8% on sales. Medical Devices grew 8.4% comparable to \$5.9bn and beat consensus by 0.6%. Bright spots included Electrophysiology (13.4% comparable, 1.3% beat), Rhythm Management (9.5% comparable, 1.8% beat), Heart Failure (8.7% comparable, 1.2% beat), and Vascular (5.1% comparable, 1.4% beat). Key weak spots were Structural Heart (5.7% comparable, -2.7% miss) and Neuromodulation (1.2% comparable, -1.7% miss). Diabetes Care grew 9% to \$2.2bn, much slower than the high-teens/low-20s pace investors had come to expect over the past few years, but a step up from 7.4% in 1Q26 and ahead of 2Q26 consensus by 0.8%. Diagnostics grew 2.9% to \$3.09bn, 1.6% above consensus (\$3.04bn). Core Lab is moving along with 3.2% growth (1.3% beat), while Cancer Diagnostics came in below consensus (13.3% comparable, 1.1% miss). Combined Rapid and Molecular Diagnostics sales declined 8.0% to \$755mn (1% miss) on lower respiratory virus testing as a result of a weaker than normal season that concluded during Q2. Nutrition sales declined 3.6% to \$2.14bn and were a touch ahead of consensus (\$2.12bn). And Established Pharmaceuticals grew 8.7% to \~\$1.50bn, ahead of consensus (\$1.48bn).

EPS beat. Adj EPS of \$1.31 was modestly ahead of consensus (\$1.28) by 3 cents (2.6%). Adjusted gross margin was 58.0% of sales (\~50bps above consensus). The improvement was broad-based, reflecting favorable business mix within the legacy Abbott portfolio and from the addition of Exact Sciences, as well as the continued operational improvements and disciplined execution of margin expansion initiatives. Adjusted R&D was 6.9% of sales and adjusted SG&A was 28.6% of sales. Adj operating margin was 22.6% (\~30bps above consensus.)

FY26 organic growth guide reaffirmed; adj EPS guidance raised by 4.5 cents. Abbott maintained FY26 comparable growth guidance at 6.5%-7.5% and raised full-year 2026 adjusted diluted EPS guidance range to \$5.45 to \$5.60 vs previous range of \$5.38 to \$5.58, a 4.5-cent raise at the midpoint after a 3-cent beat in Q2.

EXHIBIT 1: ABT maintained FY26 organic growth guidance and nudged FY26 EPS guidance up by 4.5c (\~1%)

<table><tr><td>Abbott Labs (ABT)Date Provided:</td><td>1/22/2026</td><td>4/16/2026</td><td>7/16/2026</td><td>Pre-Event Consensus</td><td>Pre-Event BERNe</td><td>Bernstein Forecast</td></tr><tr><td>For Period:</td><td>FY26</td><td>FY26</td><td>FY26</td><td>FY26</td><td>FY26</td><td>FY26</td></tr><tr><td>Comparable Growth (total)</td><td>6.5% - 7.5%</td><td>6.5% - 7.5%</td><td>6.5% - 7.5%</td><td>6.5%</td><td>7.0%</td><td>6.6%</td></tr><tr><td>FX Impact (%)</td><td>1.0%</td><td>1.0%</td><td>1.0%</td><td></td><td>0.9%</td><td>0.6%</td></tr><tr><td>Adjusted tax rate</td><td>15% - 16%</td><td>15% - 16%</td><td>-</td><td>15.5%</td><td>15.4%</td><td>15.2%</td></tr><tr><td>EPS (adj)</td><td>$5.55 - $5.80</td><td>$5.38 - $5.58</td><td>$5.45 - $5.60</td><td>$5.48</td><td>$5.48</td><td>$5.52</td></tr></table>

Source: Company reports; Bloomberg; Bernstein estimates & analysis

## Medical Device sales grew 8.4% comparable, roughly in-line (0.6% beat)

Sales growth in the quarter was led by double-digit growth in Electrophysiology and HSD growth in Rhythm Management, Diabetes Care, and Heart Failure.

In Electrophysiology, sales grew 13.4% to \$861mn (1.3% beat), accelerating from 12.5% YoY in Q1. U.S. EP sales grew 15.9% to \$420mn, as Abbott launched their next-generation PFA catheter (Volt 2.0) in the U.S. in May, with expectations to transition from limited market to full market release in Q3. OUS EP sales grew 11.1% to \$441mn on the expanding international rollout of Volt and TactiFlex Duo. Management affirmed confidence that EP would be able to 

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
