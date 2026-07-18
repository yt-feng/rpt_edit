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
European Chemicals

Air Products & Chemicals Inc

Rating

Outperform

Price Target

APD

345.00 USD

![](images/8843be6b478a25988e951b1608b7ae259628945757ec3aa17625abc9d082dc8e.jpg)

James Hooper
+44 20 7676 6995
james.hooper@bernsteinsg.com

![](images/594f47407c968099c09d62751ff1f54dc613507b9e723606f2067232259821a1.jpg)

Sebastien Afoy
+44 207 762 1032
sebastien.afoy@bernsteinsg.com

Specialist Sales

![](images/0f413310f7575b6bc621b28d7723dcad58ff9079d14d66d1a3f6954af313eee7.jpg)

![](images/ed195831e79a35d2693752a4406bd8985081a763425941c65de74ce6da905014.jpg)

James Brady
+44 20 7762 5272
james.brady@bernsteinsg.com

Steve Song
+1 917 344 8401
steve.song@bernsteinsg.com

# Air Products: Sustainable above-consensus EPS growth, even including NEOM

Air Products has the lowest valuation of the industrial gas majors, and also the highest recent EPS growth. This makes it attractive on paper - hence we write this report. In our view, growth can be at least in line with management's plan and sell side consensus, and therefore the punishment of the multiple will become increasingly unjustified as APD continues following the industrial gas model and delivering results. We rate APD Outperform with a PT of \$345.00.

We think the base business can deliver the +HSD EPS growth promised by management sustainably. This EPS growth framework was based on roughly 3% contributions each from pricing and productivity, base volumes, and projects, plus an additional 1% from share buybacks once the balance sheet deleverages. We see the numerical contributions a little differently, but we are confident that APD can deliver 9–10% annual EPS growth through 2030, supported by ongoing cost initiatives, attractive exposure to electronics and space, and easing helium headwinds.

Our conservative c. -1% per annum NEOM EPS headwind doesn't spoil the party. We have built our own proprietary NEOM model, available on request. Assuming that APD / Yara (if the agreement completes) can market 75% of the volumes with a green premium, we expect a c. -\$0.20 / 1% annual headwind to EPS over 2027-29, which turns positive from 2030 as the TotalEnergies offtake commences. We add this NEOM headwind to our model and still forecast EPS ahead of consensus over 2027-2029.

We believe the valuation multiple gap versus industrial gas peers is unfair. Thanks to APD's culture change, we believe they will continue to follow the industrial gas strategy diligently, and therefore deliver commensurate returns. If they do so, the case for the current valuation gap versus Linde, and particularly Air Liquide (c. 20% vs. c. 5% historical average) looks less strong. An additional catalyst would be increased capital return, possibly in connection with any cash inflows after the Darrow cancellation.

<table><tr><td>Close Date</td><td>16 Jul 2026</td></tr><tr><td>APD Close Price (USD)</td><td>297.29</td></tr><tr><td>Price Target (USD)</td><td>345.00</td></tr><tr><td>Upside/(Downside)</td><td>16%</td></tr><tr><td>52-Week Range</td><td>314.87/229.11</td></tr><tr><td>SPX</td><td>7,533.77</td></tr><tr><td>FYE</td><td>Sep</td></tr><tr><td>Div Yield</td><td>2.4%</td></tr><tr><td>Market Cap (USD) (M)</td><td>66,201</td></tr><tr><td>EV (USD) (M)</td><td>86,108</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>20.4</td><td>5.5</td><td>11.1</td><td>1.3</td></tr><tr><td>SPX (%)</td><td>10.1</td><td>0.3</td><td>8.6</td><td>20.3</td></tr><tr><td>Relative (%)</td><td>10.3</td><td>5.2</td><td>2.6</td><td>(19.0)</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.  
Price Performance, 1YR

![](images/8225d270de0418e45ca8a6283036960f4c44d3d4aa13f6a2a27701b21ee288d0.jpg)

## Investment Implications

We rate Air Products Outperform. We add the NEOM impact to the outer years of our model, cutting EPS in 2027 through 2029 but raising 2030 EPS by \$0.84. Our price target remains \$345.00.

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>APD (USD)</td><td>12.07</td><td>13.28</td><td>14.50</td><td>EBIT (M)</td><td>2,865</td><td>3,162</td><td>3,506</td><td>--</td><td>Adjusted P/E (x)</td><td>24.6</td><td>22.4</td><td>20.5</td></tr><tr><td>OLD</td><td>--</td><td>--</td><td>14.64</td><td></td><td></td><td></td><td></td><td></td><td>EV/EBITDA (x)</td><td>17.0</td><td>15.9</td><td>14.7</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

## DETAILS

## PM SUMMARY

The quest for double-digit EPS growth. As per our December 2025 Long View, the industrial gas stocks tend to work well when they are producing double-digit EPS growth. Soon after his appointment in 2025, Air Products (APD) CEO Eduardo Menezes set out a 5-year roadmap for returning APD to double-digit EPS growth (Exhibit 1). A 40+-year veteran of the industrial gas sector through a decorated career at Praxair and subsequently Linde, Menezes sought to simplify the Air Products strategy, in line with the density and discipline model first made famous at Praxair (see The Bernstein Industrial Gases Primer: How the industry structure can support long-term outperformance). When explaining this strategy, Menezes has used the 3+3+3+1 framing. We quote Menezes to explain further:

"I'm internally trying to make it very simple to our people so they remember that, as I say that the equation is very simple. It's 3 plus 3 plus 1. So $3\%$ on that price plus productivity minus inflation I talked about, $3\%$ from new projects, and $3\%$ from growth on the volumes, on industrial production and market share or whatever, and $1\%$ on share buyback. Those are the exact numbers, not really, right? So it's a little plus or minus $1\%$ there. So normally we try to get a little more than $3\%$ on price and productivity. The contribution from projects is a little lumpy. So normally $2\%$ to $3\%$ . And the industrial production is something we can't control. But normally industrial gases, I tell people that I'm in this industry for 40 years. And when I started the largest customers were the steel customers, 20 years ago became the chemical and refining customers. Today our largest customers are the electronic customers, right, the chip manufacturers, right? So the industry evolves and, of course, the opportunities for the usage of industrial gases, it's always changing and improving. So I think we with that profile, we have everything to do in our base volume a little bit better than industrial production. So that's the mindset we need to have, and that's the numbers. In the first few years for our products, with the cash situation that we have, we cannot afford to do the buyback of shares. So -- But we hope after the wave of these projects, that will be part of our capital deployment."

Air Products CEO Eduardo Menezes, Competitor conference

Give or take $\pm$ a percentage point here and there, we summarise this as:

• 3% productivity and price

\- 3% base volumes

• 3% new project volumes

• 1% buyback when the balance sheet is less stressed

This EPS growth framework reminds us of Linde's 8–12% EPS long term growth range. This range was established during the March 1, 2019 business update following the merger with Praxair, and it was intended to define the company's long-term ambition for adjusted EPS growth. The medium-term framework is roughly split in two: about half of the growth is expected to come from pricing and productivity (including mix improvement, margin expansion, and cost initiatives), while the other half is driven by capital deployment (new projects coming onstream and share buybacks). At that time, CEO Eduardo Menezes was serving as Executive Vice President of Linde plc for EMEA, where he was responsible for implementing this framework. Linde EMEA today has the highest margins in the Linde group.

![](images/4128bfd9b2ae10123c1b193b6799e458c5bd1f458b42987a215bd2c659889eaa.jpg)

## EXHIBIT 1: Air Products' 5-year strategic roadmap

![](images/c373173fcad7f775c8e8a78981b1a07363d137311300685412a6b47d1867fba8.jpg)  
Non-GAAP financial measure. Management is unable to reconcile, without unreasonable efforts, the Company's forecasted range of adjusted operating margin, return on capital employed or adjusted EPS to a comparable GAAP range.  
Source: APD 3QFY25 Earnings Presentation

We believe this is the right overall strategy... As per our recent primer (The Bernstein Industrial Gases Primer: How the industry structure can support long-term outperformance), we see the Praxair density and discipline approach that all three of Linde, Air Liquide and Air Products are now following as key to the sector-wide value creation seen over the last decade or so. We therefore support the strategy pivot, led by Mantle Ridge Capital, Menezes and Board Vice-Chair Dennis H. Reilley. We also believe the company have identified the key levers for execution and that they are the right way to go about approaching the strategy - controlling costs, maintaining capital discipline for new projects, optimising the existing footprint and maintaining the value creation framework which has been so successful for the broader industrial gas industry.

... although the components could be more like 5.5+1.5+2.5+1%. Starting from our FY26E estimates, we analysed the individual contribution of each component of EPS growth and summarise our findings in Exhibit 2. We expect pricing and productivity to contribute around +5.5% to EPS growth. For base volumes, while we anticipate improvements in line with our primer, we remain cautious and assume no more than a +1.5% contribution to EPS. However, we see strong support from project-driven growth, particularly in Electronics, which comprises a significant part of our 4% volume growth forecast for the Americas and Asia. We also see a long-term opportunity in space, even though it is a small business today (see The Long View: The Industrial Gas space opportunity - rocket fuel for growth).

## As a mitigating factor, we model NEOM as a c.\$20c / -1% EPS drag through 2027-2029, before contributing

positively once the TotalEnergies offtake begins in 2030. We have made a detailed model for the NEOM project, both of the JV and Air Products' offtake, which is available on request. We expect the JV to make a typical industrial gas 10.6% IRR for the project, and therefore a positive contribution to profitability. However, the ability of APD to generate a return on the offtake depends on their ability (and Yara's if an agreement is reached) to sell the volumes for a green premium. With the trajectory for green hydrogen demand and regulation uncertain in the near-term, as our base case we model that APD / Yara sell 75% of the volumes as a green premium, with the other 25% at a grey price from our ammonia supply / demand model. This leads to an average annual EPS headwind of c. \$0.20 across 2027-29. Once the TotalEnergies hydrogen offtake kicks in, which we believe has more conventional industrial gas economics, NEOM turns to a net positive on EPS under the same 75-25% green-grey split as less of the volume is sold at a grey price. We model the breakeven % as 85% green, and if APD / Yara can sell all the volumes with a green premium, then average EPS upside is c. \$0.35 / 2.5% per annum. Our NEOM model is available upon request.

Even factoring a small headwind from NEOM, we see higher EPS growth than consensus through the rest of the decade. This could lead to 13.5% compounding share price returns. We model higher EPS growth than consensus for

APD, even though we adjust our model to include a headwind from NEOM (Exhibit 3). If we are right, we believe the stock can re-rate closer to industrial gas peers, in particular Air Liquide. A 25x P/E multiple on our 2029 EPS of \$17.31 implies 13.5% annual returns and for reference Air Liquide trades at 26.2x at time of writing. We also see risk-reward skewed positively. In the bull case we could see 12% compounding EPS growth from 2027 (1%-point better base volumes, 2%-point more project growth from semis and space, no NEOM headwind) valued at 27x, close to Air Liquide all-time highs, which delivers a 19.4% 3-year return CAGR. And the bear case: a return to the historical $25^{th}$ percentile valuation of 19x P/E with 6% compounding EPS (1%-point lower productivity, base volumes and project growth) achieves a share price of \$300, effectively flat to the shares at time of writing (Exhibit 4).

Can Air Products execute this? This is still a question investors ask. Air Products has a challenging recent track record, marked by project cost overruns and, at times, questionable capital allocation decisions. We believe that any successful turnaround will need to be as much cultural as operational. We have conviction in Air Products' cultural change (see Bernstein SDC: Air Products Takeaways and Quick Take: Air Products cancels Darrow & 3QFY26 update), and this underpins our Outperform rating. We deliberately use the word "if" throughout this report, as execution remains uncertain. That said, this uncertainty also creates the valuation opportunity. If Air Products can maintain its current trajectory, then +HSD EPS compounding, combined with a narrowing of the valuation gap relative to peers, could result in significant shareholder value creation.

EXHIBIT 2: We see strong contribution from pricing and productivity, and from NEOM when the offtake with TotalEnergies start to contribute

APD EPS growth by contribution factor (%) - 2026/2030E  
![](images/4f8c2181c89fa4da11c25fb91e07753292815650e663e14239baf8f980c9fc64.jpg)  
Source: Company information, Bernstein analysis and estimates

EXHIBIT 3: We sit above consensus on EPS growth through 2028  
![](images/046e93a721a8398f0a9986e73854ebaf511132bacfa596a32052d43f2a17d67d.jpg)  
\*2030 consensus is an average of 4 values including 2 null values and our estimates Source: Company information, Bloomberg, Bernstein analysis and estimates

EXHIBIT 4: We see a path to very solid share price returns from APD  
![](images/6a6c8824bc4128d4ca45ad7dff7b384c1dabab07e11a1fef837f0f68b50e0c4e.jpg)  
Source: Company information, Bernstein analysis and estimates

## 1.5% FROM BASE VOLUME GROWTH

There is a correlation between IP growth and industrial gases' underlying growth. As per our long view (see The Bernstein Industrial Gases Primer: How the industry structure can support long-term outperformance), organic growth for the gas majors' tends to track and modestly outpace the world's IP growth (Exhibit 5). Particularly, we observe a reasonable correlation with IP growth and volume growth for Air Liquide and Linde, as Air Products has been more of an outlier in recent years (Exhibit 6 and Exhibit 7). As Air Products refocus away from the megaprojects, however, we would expect this relationship to hold across all three major players.

The outlook for IP growth remains subdued in the near term, but we see some improvements. Based on the latest data from our forecasts, IP growth is currently trending at around 2%, indicating a gradual recovery (Exhibit 8). As highlighted in our primer, a shift in base volumes from negative to positive territory would help to return to approximately 5% organic growth, a level we view as attractive for the sector over the long term.

That said, achieving volume growth of 2% could be challenging in the context of the Middle East conflict. The current situation remains uncertain and even if there is a near-term resolution, which would be supportive, any normalisation is likely to be gradual. As such, we remain cautious on base volumes (see Chemicals: Specialty or Commodity, with potentially to

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
