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
U.S. SMID-Cap Software
Datadog Inc

Rating

![](images/1e8f4d0c90163c6bf73122040ae33f2c85aaefe8b188f44c096178b826368669.jpg)

![](images/a50d51230bcb18a15a789aeb57c4ed5d88360f9b891a1f17f954f07c60d4191a.jpg)

Market-Perform (Outperform OLD)

Luwei Yang
+1 917 344 8342
luwei.yang@bernsteinsg.com

Price Target

DDOG

226.00 USD (180.00 OLD)

# Datadog (DDOG): raising our model, but tactical downgrade

Datadog continues to impress us with their speed and completeness of their vision around both observability and the broader requirements for a VP of Product Operations. Their recent DASH conference made us incremental bullish about their AI for Datadog / Datadog for AI story and line of sight for areas such as cybersecurity — they could end up becoming another large revenue pillar. Overall we reiterate our optimism that Datadog is both an AI winner and has decreasing risk from disruption as new technology horizons emerge (e.g., “Born in AI headless”?). We raise our model’s ex-AI growth duration a few % points.

We raise our Born-in-AI revenue expectations (particularly Q4+). Our model post Q1 implied the future “Born-in-AI” growth (outside their largest customer) after this year would slow to effectively \~40% YoY growth. But with the newest AI Lab customers (added in Q4 and Q1) this seems much too low. While there probably isn’t a 1:1 relationship with the AI Lab revenue and Datadog (e.g., pricing increases drive AI labs, Datadog tends to discount more with scale), we anticipate at most price is \~½ the lab’s growth. Based on the labs' expectation of 100%+ revenue CAGR over the next few years, we raise Datadog’s participation. We will need to refine this over time as we learn more, but this feels like a more fair expectation.

<table><tr><td>Close Date</td><td>2 Jul 2026</td></tr><tr><td>DDOG Close Price (USD)</td><td>260.36</td></tr><tr><td>Price Target (USD)</td><td>226.00</td></tr><tr><td>Upside/(Downside)</td><td>(13)%</td></tr><tr><td>52-Week Range</td><td>278.71/98.01</td></tr><tr><td>SPX</td><td>7,483.24</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>NA</td></tr><tr><td>Market Cap (USD) (M)</td><td>92,686</td></tr><tr><td>EV (USD) (M)</td><td>89,213</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>91.5</td><td>4.0</td><td>94.6</td><td>67.8</td></tr><tr><td>SPX (%)</td><td>9.3</td><td>1.3</td><td>7.8</td><td>19.2</td></tr><tr><td>Relative (%)</td><td>82.1</td><td>2.7</td><td>86.9</td><td>48.6</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

DOWNGRADE on Q3+ earnings caution vs. more exuberant investor expectations: demand signals slowing in both enterprise and some AI Labs. Not only do we start lapping tough comps in Q4, but as we've discussed in several other notes, we are seeing demand signals flat lining ex-AI (\~85% of revenue) that causes ex-AI growth to peak in Q3, and potentially regress -100-200bps in Q4. We also re-highlight signals AI Labs are seeing growth plateau — our QoQ into Q3 "Born-in-AI" expectations are low relative to recent growth trends. All together, Q4 could see -500bps growth rate regression, falling to \~29% YoY. This would be a disappointment vs. recent investor conversations where some expect high 30% to 40%+ peak growth, and 30%+ growth into next year.

Price Performance, 1YR  
![](images/055741c9829d3d17545b2966daa402a7d3980208f62fc36f038421f184e368df.jpg)

## Investment Implications

Raised modeled Datadog revenue growth a few hundred bps over the next decade. Applying our 50/50 multiples (higher \~16x NTM Revenue vs. 14x before), and DCF (11% WACC, 3% terminal growth) we raise our PT to \$226 and downgrade to Market-Perform.

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>DDOG (USD)</td><td>2.05</td><td>2.69</td><td>3.37</td></tr><tr><td>OLD</td><td>--</td><td>2.66</td><td>3.24</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>Cost of Goods Sold (M)</td><td>686.96</td><td>928.45</td><td>1,164</td><td>--</td></tr><tr><td>FCF (M)</td><td>914.72</td><td>1,296</td><td>1,747</td><td>--</td></tr><tr><td>Operating Earnings (M)</td><td>768.04</td><td>1,086</td><td>1,420</td><td>--</td></tr><tr><td>Revenues (M)</td><td>3,427</td><td>4,543</td><td>5,654</td><td>28.4%</td></tr></table>

<table><tr><td>Valuation Metrics</td><td>25A</td><td>26E</td><td>27E</td></tr><tr><td>EV/EBIT (x)</td><td>N/M</td><td>623</td><td>246</td></tr><tr><td>Adjusted P/E (x)</td><td>126.8</td><td>97.0</td><td>77.2</td></tr><tr><td>EV/FCF (x)</td><td>97.5</td><td>68.8</td><td>51.1</td></tr><tr><td>EV/Sales (x)</td><td>26.0</td><td>19.6</td><td>15.8</td></tr></table>

## DETAILS

## BORN-IN-AI MODEL EXPECTATIONS (\~15% OF Q2 REVENUE)

“Largest AI customer” (OpenIA?) rationalizes \$170MM ARR, but remaining base grows 65% this year (decelerating to 45% and 36% in +1 and +2 years). [we believe it is OpenAI, so use them in our model discussion here] Previously we have discussed our model where OpenAI would rationalize \~\$170MM ARR in Q3 off a contracted \$210MM+ ARR. Specifically we anticipate they will move “Business metrics” to Chronosphere and Logs to Clickhouse. But the rest of the platform, \~\$40MM ARR estimated, should still grow with the underlying scale of the company.

How fast should we grow that remaining \$40MM ARR? Relative to Q3 last year, when they implemented their prior contract, we thought it seemed likely that OpenAI would grow ARR at least 200%. Even after our previously noted signals of slowing growth (Exhibit 1) that still seems possible (or near it) given they'd already grown \~100% by February/March. With that said, we believe a material portion of their growth this year will be from increased pricing and ads [NOTE: OpenAI has reportedly talked about massive price cuts to compete even more heavily for token share — we will watch how this impacts the setup / demand / scale as the reality evolves]. The company discussed hitting \$2.5B in advertising revenue this year as recently as April, and we'll assume this is attainable within the growth noted above. And from a pricing standpoint we have industry benchmarks from the "Token Price Index" that suggest real world prices are up \~85% since the contract went into place. To further validated this, we watched revenue per engagement on their web interface as a proxy, and noticed that also skyrocketed into Q1 (Exhibit 2) — we think this does miss revenue from Codex and their API, so is not a complete revenue picture. So, while we anticipated overall YoY growth to be high for OpenAI, the effective scale growth would be lower from a Datadog revenue standpoint.

Based on our pricing, ads and demand flattening estimates, we get a mid-point underlying demand growth to Datadog of 65% this year. We use that to scale up the remaining \~\$40MM ARR by Q4 of this year. There is some upside potential if demand recovers or more of OpenAI's ARR growth proven to be driven by usage instead of pricing (if they bring prices down, for instance). This is something we will need to watch and improve with our read-through signal.

We will assume the incremental added this year will continue to get larger in future (\~15% YoY), leading to 45% and 36% growth rates in +1 and +2 years. This includes some pricing pressure on Datadog itself, as the contract scale grows.

EXHIBIT 1: MAU for the ChatGPT mobile app has slowed down in its growth after a huge increase last Q2

ChatGPT Mobile App Global MAU (indexed to Q3'23)

![](images/3d91af991559f88cc762b900d6e1ce2cb83d6d27ec99af23a945b15b736ee124.jpg)  
Source: SensorTower, Bernstein analysis

EXHIBIT 2: Anthropic's revenue per engaged visit to its website has stalled QoQ in Q2'26, indicating most of its revenue growth was driven by increased usage which would benefit Datadog  
![](images/f39c38590e3f74452ccd245dce531744f8ab4d0462a349e43c784a3dcefa018d.jpg)  
OpenAI and Anthropic's revenue figures estimated based on monthly ARR disclosures  
Source: Similarweb, the Information, Bernstein estimates and analysis

“Large new AI lab landed Q4” massive 125-150%+ QoQ in Q2, but less in Q3/Q4, growth halves next year to 65%, and closer to 45-50% in +2 years. [we believe to be Anthropic, so use them in our model here] Anthopic’s QoQ revenue growth into Q2 is expected to be 125%+, and based on their reported ARR it would be \~150% (Exhibit 3). Like OpenAI we would normally not want to read this through 1:1 as some is pricing, but we also have indications from their web metrics that seem to suggest pricing may be a less meaningful driver of revenue growth QoQ into Q2 (Exhibit 2). But looking to H2, right now there seems to be some stalling in growth (Exhibit 4), which is consistent with some prior periods of digestion after new model releases, so we are slowing their growth towards the rate they’ve commonly seen for a few quarters after hyper growth periods (10-15% QoQ). In future years we would anticipate the growth rate to come down, just like our OpenAI model does. We have them coming down by half in ‘27 and reaching 45-50% in ‘28.

EXHIBIT 3: Anthropic's revenue growth has mostly followed the trajectory of its website traffic growth  
![](images/856cb8491569da5cab0a3075c2567fcd7c83ebba96c1f21fe6fc0b93eb70762b.jpg)  
Source: Similarweb, the Information, Bernstein estimates and analysis

EXHIBIT 4: The engaged visits to claude.ai website surged in March/April but has slowed down in its month-over-month growth in June  
![](images/368f666267a24ff55f93b63cb8fdd0609db02731fa1d6b0e0b6a7f73c4baa3c7.jpg)  
Source: Similarweb, Bernstein estimates and analysis

Rest of “Born in AI” grows net new QoQ by \~25% in ‘27 and \~20% in ‘28. In Q1 we estimate Datadog had roughly \$55-60MM in “Born-in-AI” revenue ex-OpenAI and ex-Anthropic. This upcoming Q2 we add \$7-12MM contribution from the couple new AI Labs (a “7-figure” and an “8-figure” ARR deal announced in Q1). On top of this we anticipate a large \$20-25MM incremental bump up, as the “rest” tends to follow the same tailwinds as OpenAI and Anthropic step-ups (possibly because this aligns to budget willingness, models finally making the companies that use them more viable, etc.). Looking further forward is hard to know for sure, but we do notice they’ve been adding on average a couple \$MM to net new scale each quarter, and we continue this trend through 2028.

## EX-AI REVENUE MODEL (\~85% OF Q2 REVENUE)

Q2 revenue growth was already signaled by the strong Q1 web metric results (they look +1 quarter, as we've discussed in our deep dives on the methodology). The bigger question is Q3 revenue signal based on Q2, and as we've discussed before (here) we have been watching our web metric signal growth flat line since early May (Exhibit 5) — this pattern seems to have continued into the $1^{\text{st}}$ week of July (the latest data before publishing this note). This flatlining seems consistent with channel checks that suggest there are capacity constraints to new workloads (further supported by reports that new datacenter capacity has been relatively flat since H2 last year — Exhibit 6) as well as some pausing to address cybersecurity risks in existing deployed applications post Mythos/Glasswing warnings (i.e., fix backlog of maintenance/bug fixes). With that said, Q2 results (that signal +1 quarter) started strong enough that Q3 will likely be near steady or slightly increased growth rates (it is also helped by the fact -1 year was a relatively easy comp).

The bigger risk of deceleration is looking toward Q4 revenue. We still need to watch for Q3 web metric and channel check results to know the setup for sure, but the -1 year was very very strong in Q4, so anything less than that would create a headwind. For now, we are assuming a “normal” growth quarter, which would cause a step-down. We note that the week-to-week run rate we are seeing right now is below “normal”, so it would require the run rate to actually get better just to get to our model.

EXHIBIT 5: Web metric data suggests workloads moving to the cloud have stagnated since early May – channel checks back this up, pointing to near term hyperscaler capacity constraints, cyber hardening, and tokenmaxxing impacts

AWS SSO Web Metrics: % change relative to March average

![](images/fadc29698ea07a9878353505f283cd0e427f3a13213f4edf0188aa135e92bc1a.jpg)  
AWS SSO = awsapps.com
Source: Similarweb, Bernstein analysis  
Month over Month Active Data Center
Capacity Added (in MW)

EXHIBIT 6: After a surge in new active data center capacity coming online in Q4 last year, the pace of active data center capacity being added has slowed down in 2026 – hyperscalers near net 0.

![](images/c398730ac54e3d946e65fd42eb15c098af95956bd1e518d728803ce00fbb55af.jpg)  
Source: Aterio, Bernstein analysis

## UPSIDE FROM HERE IS HARD TO IMAGINE IN THE FACE OF PEAKING AND THEN REGRESSING GROWTH IN H2 AND INTO 2030.

It is frustrating to us, given our bullish long term view on Datadog, when we hit a patch of expectations that exceed our own bullish expectations. In this note we are raising our own model throughout its duration by a few hundred bps (Exhibit 7), and even bringing up some of the Born-in-AI expectations, but are only reaching a price target near recent trading levels (Exhibit 8). This gives us pause and forced our hands on a downgrade to Market-Perform, as we could imagine this price level being rational over the coming year (with some up and downside risk to it that we discuss below).

Messy between here and +1 year? Even worse, in between here and a year from now there could be incremental friction/noise as we move through a near term “natural” air pocket in growth (Exhibit 9) — Product Led Growth cloud consumption companies rarely offer the smooth growth profiles of traditional application vendors, as the underlying demand environment swings them around. It is quite normal for there to be periods of hyper adoption and digestion, or slower periods from other impacts like capacity constraints and other near term priorities. The long term average will look good, but the market seems to historically over-react to these near term swings (Exhibit 10). We worry this time could be more of the same.

+1 year will likely lap the near term air pocket, and be back in a better setup relative to current valuation. Once this air pocket passes, and investors see the company re-accelerate we would anticipate our price target would be a roughly natural level to return to.

EXHIBIT 7: Our updated model raises Datadog's YoY revenue growth rates by 1-2% in the next 4 quarters and 3-4% longer term

DDOG YoY Revenue Growth Rate (previous estimates vs. updated model)

![](images/3a900d2e6667bdc316f4cb602c0e3ffe177e74340f53fb099fb9942e04a1edc4.jpg)  
Source: Company reports, Bernstein estimates and analysis  
EXHIBIT 8: The current P/Sales multiple for Datadog is significantly disconnected from the “core” regression of Growth SaaS companies, implicitly suggesting investors expect a much higher revenue growth expectation than our model  
Cloud SaaS multiple regression: Price/NTM Sales vs. Ro40 (Jun 30th)

![](images/2b39aea347355f7f00483d35e4c645fed29aaa4e79019132e4e47fb8a74dd035.jpg)  
Outliers (high = DDOG, NET, CRWD, FROG; low = NOW, TEAM, WK) are excluded from the regression line  
All datapoints based on Bloomberg consensus except for DDOG (BERN) which uses Bernstein's PT and model  
Source: Bloomberg, Bernstein estimates and analysis

EXHIBIT 9: Near-term acceleration in Datadog's revenue growth has been driven by both the expansion in the AI-native cohort and an increase of enterprise workloads running on Cloud. But the gr

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
