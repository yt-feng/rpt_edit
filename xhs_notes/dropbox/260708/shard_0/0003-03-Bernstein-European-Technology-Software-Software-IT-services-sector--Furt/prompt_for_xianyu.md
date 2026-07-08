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
# European Technology/Software

# Software/IT services sector: Further recovery, less euphoria

![](images/a30594934ef38bc114ae5d0c5cabcbf20c1537dc1477b0ccbebda858c19a964e.jpg)

Derric Marcon

+33 1 58 98 06 30

derric.marcon@bernsteinsg.com

![](images/523573b3ce43ea3ab87b6ebb9fffaf9ac4a9c7f188267a9b6a7d2b9ccd4c37c9.jpg)

Richard Nguyen

+33 1 42 13 54 22

richard.nguyen@bernsteinsg.com

Specialist Sales

![](images/c8902dc519df6b4690b04241b70729a18db23d6e225a520d054178f8ef2cb4df.jpg)

Kiran Shah, CFA

+44 20 3547 1533

kiran.shah@bernsteinsg.com

On Tuesday after market close, we attended the semi-annual meeting of France's trade association of software and IT service companies (Numeum). The organisation presented the results of a survey conducted among its members in April/May covering 413 companies and CIOs, $43\%$ of which were IT service providers, $29\%$ software vendors and $28\%$ CIOs. As usual, it engaged an industry research firm—in this case Xerfi—to conduct the survey and forecast growth through 2026 for the various market segments it tracks.

Still recovering but less so than initially anticipated. First, we note that this survey was conducted when the Middle East conflict was very much in the foreground and GDP growth forecasts for France had already begun to be revised down (10bp drop between late March and late April). The survey also reflects the very low morale among small firms, spanning both software vendors and IT service providers. For small IT service firms, challenges include the trend among clients to consolidate and narrow down their lists of preferred suppliers, the shift toward nearshore and offshore delivery models, and the need to invest in new technologies. For small software vendors, difficulties centre on the capacity to invest and the need to avoid being hit by rising operating costs associated with AI-powered tools. For these reasons (economic climate and the weight of small businesses' responses to the survey), we are not overly concerned by the slightest hint of optimism emerging from the poll compared to six months ago. For once, the main downward revision relates to the software segment (from +8.4% to +6.2%), while IT services firms' growth is projected to remain in the low single digits. Numeum anticipates higher growth in 2H than 1H for all segments. See details in Exhibit 1 and Exhibit 2.

‘SaaSpocalypse’ not a reality but a foreboding. While software vendors are not seeing their existing business being disrupted by new entrants—with no increase observed in churn and no proliferation of ‘software factories’ springing up to replace established software—those surveyed believe that decision-makers are taking longer to make choices due to the technological upheaval caused by AI. They also express more concern about the future than we had anticipated. For software vendors still in the early stages of AI adoption, the road ahead appears long—both to monetise new features and evolve technology stacks to match the capabilities of AI-native companies. One statistic in particular struck us: 22% of CIOs believe that agentic AI could replace or reduce certain software expenditures. The word ‘certain’ is crucial here, as it likely refers to applications that are less central to core business operations. This echoes a study by the consulting firm Bain highlighting its ability—within the context of M&A processes—to identify applications that could be 80% rewritten in just ten days using AI.

Continued on next page...

## ... continued from previous page

Bringing IT services back in-house is certainly an option, but not because of AI. In the survey, members highlight the possibility of in-sourcing IT services activities. This option has always existed, but it tends to gain traction during periods of rapid, profound innovation as companies seek to internalise the knowledge associated with these new technologies. In other words, it is not AI driving this move to insource but rather the pace of innovation and technological disruption.

AI: a source of additional business, but no margin boost. Whether for software vendors or IT service providers, the productivity gains observed and projected are substantial, yet neither group anticipates a significant improvement in profitability —for various reasons, primarily the passing on of gains to clients and the need to shoulder additional costs.

Energy efficiency/green IT: no longer a priority. Unfortunately, faced with technological disruption and the need to evolve information systems and remain competitive, energy efficiency and Green IT rank as a priority in 2026 for only 22% of the CIOs surveyed—well behind cybersecurity, compliance, the optimisation of unavoidable costs, and generative AI.

EXHIBIT 1: Numeum market growth forecasts by segment (yoy %)

<table><tr><td rowspan="2"></td><td colspan="3">2023</td><td colspan="3">2024</td><td colspan="3">2025</td><td colspan="2">2026e</td></tr><tr><td>Dec 2022 forecast</td><td>Jun 2023 forecast</td><td>Dec 2023 actual</td><td>Dec 2023 forecast</td><td>Jun 2024 forecast</td><td>Dec 2024 actual</td><td>Dec 2024 forecast</td><td>Jun 2025 forecast</td><td>Dec 2025 forecast</td><td>Dec 2025 forecast</td><td>Jun 2026 forecast</td></tr><tr><td>IT services</td><td>+3.7%</td><td>+4.2%</td><td>+4.1%</td><td>+3.3%</td><td>+3.3%</td><td>+0.7%</td><td>+0.9%</td><td>-2.1%</td><td>-1.8%</td><td>+1.4%</td><td>+1.0%</td></tr><tr><td>Outsourced engineering services</td><td>+5.6%</td><td>+5.9%</td><td>+5.5%</td><td>+4.6%</td><td>+4.6%</td><td>+1.0%</td><td>+1.3%</td><td>-2.5%</td><td>-2.5%</td><td>+1.0%</td><td>+0.2%</td></tr><tr><td>Software</td><td>+9.4%</td><td>+9.4%</td><td>+10.3%</td><td>+9.5%</td><td>+9.5%</td><td>+8.2%</td><td>+9.0%</td><td>+8.2%</td><td>+8.2%</td><td>+8.4%</td><td>+6.2%</td></tr><tr><td>French IT services/software market</td><td>+5.9%</td><td>+6.3%</td><td>+6.5%</td><td>+5.8%</td><td>+5.8%</td><td>+3.5%</td><td>+4.1%</td><td>+1.8%</td><td>+2.0%</td><td>+4.3%</td><td>+3.0%</td></tr></table>

Source: Numeum data and estimates

EXHIBIT 2: Market growth set to accelerate in 2H26

<table><tr><td></td><td>1H26</td><td>FY26e</td></tr><tr><td>IT services</td><td>+0.8%</td><td>+1.0%</td></tr><tr><td>Outsourced engineering services</td><td>-0.2%</td><td>+0.2%</td></tr><tr><td>Software</td><td>+6.0%</td><td>+6.2%</td></tr></table>

Source: Numeum data and estimates

## INVESTMENT IMPLICATIONS

## No changes in rating and PT.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">7 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">EV/Adj EBIT (x)</td></tr><tr><td>ClosingPrice</td><td>PriceTarget</td><td>Curr.</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td><td></td></tr><tr><td>ATE.FP (Alten)</td><td>O</td><td>EUR</td><td>55.95</td><td>135.00</td><td>(45.5)%</td><td>EUR</td><td>4.91</td><td>7.07</td><td>7.72</td><td>5.6</td><td>5.2</td><td>4.9</td></tr><tr><td>ATO.FP (Atos)</td><td>U</td><td>EUR</td><td>34.40</td><td>43.00</td><td>(4.3)%</td><td>EUR</td><td>(50.11)</td><td>(1.73)</td><td>3.25</td><td>(7.5)</td><td>7.9</td><td>5.8</td></tr><tr><td>AUB.FP (Aubay)</td><td>O</td><td>EUR</td><td>55.50</td><td>66.00</td><td>(7.8)%</td><td>EUR</td><td>3.06</td><td>3.57</td><td>3.76</td><td>13.1</td><td>11.0</td><td>10.4</td></tr><tr><td>CAP.FP (Capgemini)</td><td>O</td><td>EUR</td><td>93.82</td><td>208.00</td><td>(50.6)%</td><td>EUR</td><td>12.86</td><td>13.00</td><td>13.95</td><td>7.3</td><td>7.2</td><td>6.7</td></tr><tr><td>GIB/A.CN (CGI)</td><td>U</td><td>CAD</td><td>95.74</td><td>141.00</td><td>(53.3)%</td><td>CAD</td><td>8.28</td><td>8.82</td><td>9.72</td><td>11.6</td><td>10.9</td><td>9.8</td></tr><tr><td>IDR.SM (Indra)</td><td>O</td><td>EUR</td><td>51.38</td><td>66.00</td><td>19.7%</td><td>EUR</td><td>2.48</td><td>2.53</td><td>3.10</td><td>20.7</td><td>20.3</td><td>16.6</td></tr><tr><td>OVH.FP (OVHcloud)</td><td>O</td><td>EUR</td><td>16.80</td><td>19.00</td><td>38.9%</td><td>EUR</td><td>(0.01)</td><td>0.13</td><td>0.41</td><td>8.7</td><td>8.1</td><td>7.1</td></tr><tr><td>REY.IM (Reply)</td><td>M</td><td>EUR</td><td>96.80</td><td>120.00</td><td>(50.5)%</td><td>EUR</td><td>7.13</td><td>7.71</td><td>8.13</td><td>8.6</td><td>7.8</td><td>7.4</td></tr><tr><td>SOP.FP (Sopra Steria)</td><td>O</td><td>EUR</td><td>152.00</td><td>242.00</td><td>(43.8)%</td><td>EUR</td><td>16.47</td><td>16.87</td><td>18.84</td><td>7.9</td><td>7.7</td><td>7.0</td></tr><tr><td>74SW.FP (74Software)</td><td>O</td><td>EUR</td><td>37.20</td><td>55.00</td><td>(23.1)%</td><td>EUR</td><td>2.25</td><td>2.84</td><td>3.43</td><td>12.7</td><td>11.5</td><td>10.1</td></tr><tr><td>EDME</td><td></td><td></td><td>1,606.65</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,503.85</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended CAP.FP, GIB/A.CN, IDR.SM valuation is Adjusted P/E (x); OVH.FP valuation is EV/Adj EBITDA (x); Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

This research publication covers six or more companies. For valuation methodology and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RISKS

This research publication covers six or more companies. For risks and other company disclosures:

Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 500 Banks And Financial Services Index (BEBANKS) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 500 Insurance Index (BEINSUR) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within +/-10 pp

\- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as ‘Feature’ (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) c

[中间内容因长度限制已省略]

 you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
