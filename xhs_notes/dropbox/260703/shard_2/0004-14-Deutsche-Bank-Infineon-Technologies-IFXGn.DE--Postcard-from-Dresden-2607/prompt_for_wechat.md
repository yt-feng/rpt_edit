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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`DB`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份DB研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Company Infineon Technologies

Rating Buy

Europe
Germany

Bloomberg
IFX GR

Reuters
IFXGn.DE

Exchange
GER

Technology Semiconductors

Ticker
IFXGn

ADR
IFNNY

ISIN
US45662N1037

Steep capacity ramp to drive accelerating growth in '27 and beyond - reiterate Buy

# Postcard from Dresden

We visited Infineon's new Dresden 4 fab today ahead of the official opening ceremony on July 2nd. A tour of the cleanroom as well as meetings with Infineon's COO Alexander Gorski and the local operational team reaffirm our view that the company has substantial growth potential from 2027 onwards as more capacity becomes available. A fast ramp at Dresden 4 plays an important role here but we are also incrementally positive on capacity in Villach as well as Kulim and foundry partners. Demand for Infineon's AI products remains strong and we see scope for the company to substantially lift its FY27 AI revenue target of E2.5b on the back of capacity expansion as well as pricing - likely with FY26 results in November (and not with FQ3 in August), in our view. Pricing also remains a positive driver with a second round of price increases now communicated that goes way beyond just AI products and should therefore be more meaningful on a group level than the last increase, in our view. We reiterate our bull case for close to 20% revenue growth in FY27e driving mid-20s margins if the capacity ramp across Dresden/Villach/Kulim remains on track. We also reiterate our Buy rating with Infineon remaining one of our top picks in European Tech and global Semis.

## Steep capacity ramp at Dresden 4 could fill the fab in 2-3 years

Our most important take away from this field trip is the planned pace of the Dresden ramp with our conversations indicating 2-3 years until full utilization which would be twice as fast compared to what we consider a normal ramp. About 50 of 1000+ tools are already moved into Dresden 4 with first wafers out ahead of the official opening ceremony tomorrow and an AI-enhanced fab design as well as ramp plan that makes this accelerated ramp possible. Equipment is ordered and scheduled for delivery to a large extent out to 2028 and despite lengthening equipment lead times across the industry, we believe tool availability will not put an accelerated ramp at risk. This could add E2b+ per year to Infineon's capacity and hence revenues over the next 2-3 years, i.e. low-to mid-teens percentages of today's revenues which we deem as very meaningful. The company commented that it sees supply bottlenecks for AI power over the coming 2-3 years and potentially beyond across the industry and we also believe that demand for this capacity is very likely to materialize.

Date
1 July 2026

## Company Update

Price at 30 Jun 2026 (EUR) 81.67
Price Target (EUR) 90.00
52-week range (EUR) 88.00 - 31.28

## Valuation & Risks

Johannes Schaller
Associate Director of Equity Research - Germany
+49-69-910-31731

Nicolas Herms
Research Analyst
+49-69-910-13052

Robert Sanders
Research Analyst
+44-20-754-58394

Nooshin Nejati
Research Analyst
+49-69-910-61797

Yusuf Jamal
Research Associate

Kunal Gupta
Research Associate

![](images/4f65b042870292b85e1005238f84fefb334bfdd6b7d34b0ce3548eeff9e88655.jpg)

<table><tr><td>Performance (%)</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Absolute</td><td>0.7</td><td>114.9</td><td>126.1</td></tr><tr><td>DJ (.STOXXE)</td><td>3.5</td><td>12.9</td><td>19.7</td></tr><tr><td colspan="4">Source: DB</td></tr></table>

Infineon can double revenues without building another fab, driving margins and FCF medium-term

In terms of CapEx, we found comments by Infineon's COO encouraging that the company can grow to E30b of annual revenues (close to double of today's runrate) without building an additional fab. We see this driven by E5b plus from Dresden 4 with upside from pricing (especially in AI) and mix, E5b from Villach (300mm conversion) and Kulim (excl. Kulim 3.2) as well as \~E4b from foundry with ESMC playing an important role (DBe potentially E3b). Importantly, Infineon's backend can scale with the front-end capacity expansion above, supported by its new large scale site in Bangkok. This confirms our view that the company's FCF and margin profile should meaningfully improve over the coming years, taking into account that \~40% of e.g. Dresden 4 for is building CapEx and only \~60% for tools.

## Appendix 1

Important Disclosures

\*Other information available upon request

<table><tr><td colspan="4">Disclosure checklist</td></tr><tr><td>Company</td><td>Ticker</td><td>Recent price*</td><td>Disclosure</td></tr><tr><td>Infineon Technologies</td><td>IFXGn.DE</td><td>81.67 (EUR) 30 Jun 2026</td><td>1, 2, 7, 8, 14, 15, 24, 26</td></tr></table>

\*Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Important Disclosures Required by U.S. Regulators

Disclosures marked with an asterisk may also be required by at least one jurisdiction in addition to the United States. See Important Disclosures Required by Non-US Regulators and Explanatory Notes.

1. Within the past year, DB and/or its affiliate(s) has managed or co-managed a public offering for this company, for which it received fees.

2. DB and/or its affiliate(s) may act as a market maker or liquidity provider in the financial instruments issued by this company.

7. DB and/or its affiliate(s) has received compensation from this company for the provision of investment banking or financial advisory services within the past year.

8. DB and/or its affiliate(s) expects to receive, or intends to seek, compensation for investment banking services from this company in the next three months.

14. DB and/or its affiliate(s) has received compensation from this company within the past year for non-investment banking related services.

15. This company has been a client of DB Securities Inc. within the past year during which time it received investment banking services.

## Important Disclosures Required by Non-U.S. Regulators

Disclosures marked with an asterisk may also be required by at least one jurisdiction in addition to the United States. See Important Disclosures Required by Non-US Regulators and Explanatory Notes.

1. Within the past year, DB and/or its affiliate(s) has managed or co-managed a public offering for this company, for which it received fees.

2. DB and/or its affiliate(s) may act as a market maker or liquidity provider in the financial instruments issued by this company.

24. DB and/or its affiliate(s) is or has been over the previous 12 months party to an agreement with the company relating to the provision of services set out in Sections A and B of Annex I of Directive 2014/65/EU, or has over the previous 12 months been obliged or entitled (as applicable) to pay or receive compensation relating to the provision of services set out in Sections A and B of Annex I of Directive 2014/65/EU.

26. Within the preceding 12 months, DB and/or its affiliate(s) has received compensation for the provision of investment banking services or is currently providing or has provided investment banking services to this company.

For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst(s) about the subject issuer and the securities of the issuer. In addition, the undersigned lead analyst(s) has not and will not receive any compensation for providing a specific recommendation or view in this report. Johannes Schaller.

Historical recommendations and target price: Infineon Technologies (IFXGn.DE) (as of 06/30/2026)

![](images/7de1884a33c33168beaf475b851e34412f81b5476ae4d3f3c3b6186e7a24a847.jpg)

Current Recommendations
Buy
Hold
Sell
Not Rated
Suspended Rating

<table><tr><td>1.</td><td>10/24/2023</td><td>Buy, Target Price Change EUR 40.00, Current Price EUR 29.07 Johannes Schaller</td><td>7.</td><td>06/20/2025</td><td>Buy, Target Price Change EUR 42.00, Current Price EUR 34.22 Johannes Schaller</td></tr><tr><td>2.</td><td>05/07/2024</td><td>Buy, Target Price Change EUR 44.00, Current Price EUR 36.39 Johannes Schaller</td><td>8.</td><td>07/09/2025</td><td>Buy, Target Price Change EUR 44.00, Current Price EUR 37.91 Robert Sanders</td></tr><tr><td>3.</td><td>08/06/2024</td><td>Buy, Target Price Change EUR 40.00, Current Price EUR 29.74 Johannes Schaller</td><td>9.</td><td>02/04/2026</td><td>Buy, Target Price Change EUR 48.00, Current Price EUR 40.31 Johannes Schaller</td></tr><tr><td>4.</td><td>11/13/2024</td><td>Buy, Target Price Change EUR 38.00, Current Price EUR 29.40 Johannes Schaller</td><td>10.</td><td>04/14/2026</td><td>Buy, Target Price Change EUR 52.00, Current Price EUR 44.46 Robert Sanders</td></tr><tr><td>5.</td><td>02/04/2025</td><td>Buy, Target Price Change EUR 42.00, Current Price EUR 34.50 Johannes Schaller</td><td>11.</td><td>05/06/2026</td><td>Buy, Target Price Change EUR 70.00, Current Price EUR 59.23 Johannes Schaller</td></tr><tr><td>6.</td><td>04/08/2025</td><td>Buy, Target Price Change EUR 38.00, Current Price EUR 25.30 Robert Sanders</td><td>12.</td><td>05/28/2026</td><td>Buy, Target Price Change EUR 90.00, Current Price EUR 80.11 Johannes Schaller</td></tr></table>

Equity rating dispersion and banking relationships  
![](images/ae73a022e6a946b37edf2ad7db314d8f66e9b1354e0870d30003880e999ee220.jpg)  
Equity Rating and Dispersion Key

The Equity Rating Dispersion Chart depicts the following:

The proportion of recommendations that are rated "buy", "sell" and "hold" over the previous 12 months. This is shown for securities issued in the stated region e.g. "Europe Universe". See rating definitions below. This is represented by the "Companies Covered" bars in the chart. The percentage value displayed above the bar is the proportion as a percentage. E.g. 50% above the "buy" / "Companies Covered" bar means that 50% of DB's equity research covered companies over the past 12 months have a "buy" rating.

Next to each of the three respective bars showing the proportion of "buy", "sell" and "hold" recommendations we provide two additional bars to show:

\- The proportion of "buy", "sell" or "hold recommendations where DB and or/Affiliates provided MIFID Investment or Ancillary Services in the past 12 months. This is represented in the "MIFID Investment and Ancillary Services" bar. The percentage value displayed above the bar shows the proportion of Companies Covered with the given rating where DB has also provided MIFID Investment and Ancillary Services in the past 12 months. E.g. 50% above the "Cos. w/ MIFID Investment and Ancillary Services" bar means 50% of the Companies Covered with the rating stated have also received MIFID Investment and Ancillary Services from DB.

\- The proportion of "buy" (or "sell" or "hold") recommendations where DB and or/Affiliates has provided Investment Banking services in the past 12 months for which it has received compensation. The percentage value displayed above the bar shows the proportion of Companies Covered with the stated rating where DB has also provided Investment Banking services in the past 12 months. E.g. 50% above the "Cos. w/ Investment Banking relationship" bar means 50% of the Companies Covered with the rating stated also have an Investment Banking Relationship with DB.

Buy: Based on a current 12-month view of TSR, we recommend that investors buy the stock.

Sell: Based on a current 12-month view of TSR, we recommend that investors sell the stock.

Hold: We take a neutral view on the stock 12-months out and, based on this time horizon, do not recommend either a Buy or Sell.

TSR = Total Shareholder Return. Percentage change in share price from current price to projected target price plus projected dividend yield

Newly issued research recommendations and target prices supersede previously published research.

## Additional Information

The information and opinions in this report were prepared by DB AG or one of its affiliates (collectively 'DB'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, DB makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. DB neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of DB in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a DB analyst, DB may act as principal for its own account or as agent for another person.

DB may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within DB, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. DB issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communication may differ from recommendations contained in others, whether as a result of differing time horizons, methodologies, perspectives or otherwise. DB and/or its affiliates may also be holding debt or equity securities of the issuers it writes on. Analysts are paid in part based on the profitability of DB AG and its affiliates, which includes investment banking, trading and principal trading revenues.

Opinions, estimates and projections constitute the current judgment of the author as of the date of this report. They do not necessarily reflect the opinions of DB and are subject to change without notice. DB provides liquidity for buyers and sellers of securities issued by the companies it covers. DB analysts sometimes have shorter-term trade ideas that may be inconsistent with DB's existing longer-term ratings. Some trade ideas for equities are listed as Catalyst Calls on the Research Website (https://research.db.com/Research/), and can be found on the general coverage list and also on the covered company's page. A Catalyst Call represents a high-conviction belief by an analyst that a stock will outperform or underperform the market and/or a specified sector over a time frame of no less than two weeks and no more than three months. In addition to Catalyst Calls, analysts may occasionally discuss with our clients, and with DB salespersons and traders, trading strategies or ideas that reference catalysts or events that may have a near-term or medium-term impact on the market price of the securities discussed in this report, which impact may be directionally counter to the analysts' current 12-month view of total return or investment return as described herein. DB has no obligation to update, modify or amend this report or to otherwise notify a recipient thereof if an opinion, forecast or estimate changes or becomes inaccurate. Coverage and the frequency of changes in market conditions and in both general and company-specific economic prospects make it difficult to update research at defined intervals. Updates are at the sole discretion of the coverage analyst or of the Research Department Management, and the majority of reports are published at irregular intervals. This report is provided for informational purposes only and does not take into account the particular investment objectives, financial situations, or needs of individual clients. It is not an offer or a solicitation of an offer to buy or sell any financial instruments or to participate in any particular trading strategy. Target prices are inherently imprecise and a product of the analyst's judgment. The financial instruments discussed in this report may not be suitable for all investors, and investors must make their own informed investment decisions. Prices and availability of financial instruments are subject to change without notice, and investment transactions can lead to losses as a result of price fluctuations and other factors. If a financial instrument is denominated in a currency other than an investor's currency, a change in exchange rates may adversely affect the investment. Past performance is not necessarily indicative of future results. Performance calculations exclude transaction costs, unless otherwise indicated. Unless otherwise indicated, prices are current as of the end of the previous trading session and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Data is also sourced from DB, subject companies, and other parties. Artificial intelligence tools may be used in the preparation of this material, including but not limited to assist in fact-finding, data analysis, pattern recognition, content drafting and editorial corrections pertaining to research material.

The DB Department is independent of other business divisions of the Bank. Details regarding our organizational arrangements and information barriers

[中间内容因长度限制已省略]

out prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South Tower,Singapore 048583TeL: +65 6423 8001</td></tr></table>

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

## International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
