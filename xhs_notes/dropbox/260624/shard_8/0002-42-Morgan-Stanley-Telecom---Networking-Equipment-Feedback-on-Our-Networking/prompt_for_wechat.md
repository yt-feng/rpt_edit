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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
June 22, 2026 04:24 AM GMT

# Telecom & Networking Equipment | North America

# Feedback on Our Networking & Optical Notes: Some Healthy Debate

Found healthy backing to our networking note highlighting inference opportunity, particularly with ANET, a thesis we think has more momentum. Optical, which lacks firm data points, has had more recent debates, with clearest story remaining in GLW; more powerful stories into FQ4 EPS around LITE/COHR.

## Key Takeaways

■ Found the most support for our networking note, which points to continued momentum with ANET / CSCO.

■ Optical conversations picking up given concerns around CPO/NPO timing, laser competition, training vs. inference in scale-across.

\- Cleanest setup remains with GLW, LITE / COHR becoming more interesting into earnings, still more risk off CIEN for now.

Focus turns to networking as optical has a few more debates. In general, we have found that our networking conversations coming out of our note a couple of weeks back were positive, pointing to more support for ANET / CSCO over the next month into earnings. This is counter to our recent optical discussions, which have moved from a demand-discovery conversation around incremental content (highlighted in our Insight earlier this year) to a margin-durability debate as timing of incremental content, capacity coming online and overall switches in capacity investments between training and inference come to the forefront. More specifically, 1) the timing / form of CPO / NPO (discussed in our note earlier in the month), 2) reports of Source Photonics' capacity expansion, and 3) the inference / training argument we made in our networking note potentially changing some estimates on the scale-across side of optical. Given more spot market data points with other AI trades like memory, we expect volatility to continue in optical in near term, leaving our preference for networking names (ANET/CSCO). We expect against all these discussion points in optical, that GLW remains the cleanest story over the next month ahead of earnings, LITE / COHR to become more interesting into earnings in early August.

Optical long term margin stories start to differ in conversations. Demand for optical isn't really the question for many investors, as demand conditions remain strong. Where there tends to be more debate is around margins, particularly since there is not as much of a spot market vs. other AI trades like memory. In order of importance, we list recent conversation points that have set the framework for differing margin conversations:

MS & CO. LLC

Meta A Marshall

Meta.Marshall@morganstanley.com +1 212 761-0430

Antonio Jaramillo

Research Associate

Antonio.Jaramillo@morganstanley.com +1 212 761-4438

## TELECOM & NETWORKING EQUIPMENT

North America

Industry View In-Line - 1) (+: GLW) Fujikura (covered by Yu Shirakawa) raising full year outlook last Thursday, noting stronger demand, better pricing, milder effects of hydrogen shortages. While we have repeatedly held that the spot pricing commentary out of Asia for fiber is too aggressive for GLW, who has preferred LTAs over price taking, the meaningful raise to Fujikura's full year outlook (+47% to OP) is a positive for GLW.

\- 2) (-: LITE / COHR) Suzhou Dongshan Precision Manufacturing (SHE: 002384) noting they would invest \$1.2bn to build out additional laser capacity through their Source Photonics business. We would note Source Photonics is a relatively small player in the laser market, but as capacity came out it would be more likely to challenge CW market vs. EMLs, but could weigh on longer term margin expectations in the near term.

\- 3) (-: CIEN) With our networking note highlighting inference opportunities vs. training, how competitive the pricing will be in scale-across optical coming into question.

\- 4) (=: LITE / COHR) CPO Timing / Architecture. As we argued in our note from a couple of weeks ago, additional optical content in scale-up is more important than the form factor it takes.

## More on Source Photonics' Capacity Expansion and Competitive Implications.

The biggest incremental data point we heard last week was around the capacity expansion with Source Photonics. Suzhou Dongshan Precision's filing indicates Source Photonics and its subsidiaries plan a \$1.2B optical chip and module expansion funded with self-raised capital and aimed at downstream AI demand. Industry feedback suggests Source Photonics had already been discussed as potentially expanding capacity by 5-6x before the announcement, although we would treat that as channel context rather than official guidance. We think LITE / COHR price action in response to the Source Photonics headline is likely exaggerated, as Source Photonics is a relatively small competitor. Checks suggest Source Photonics is not coming up meaningfully in competitive discussions, with the market dominated by LITE, COHR, Sumitomo, Broadcom. Their expansion is likely to be more impactful to the CW laser side vs. EML.

Exhibit 1: Networking stocks have lagged Optical YTD, but momentum has started to shift, with Networking up 6.7% over the last month vs. a 10% decline for Optical.

<table><tr><td colspan="5">Optical Communications Stock Performance</td></tr><tr><td></td><td>1Y</td><td>YTD</td><td>1 Month</td><td>1 Week</td></tr><tr><td>AAOI</td><td>590.2%</td><td>364.3%</td><td>(10.8%)</td><td>(4.3%)</td></tr><tr><td>CIEN</td><td>474.6%</td><td>83.1%</td><td>(26.6%)</td><td>(4.0%)</td></tr><tr><td>COHR</td><td>379.8%</td><td>111.1%</td><td>3.2%</td><td>1.2%</td></tr><tr><td>FN</td><td>115.5%</td><td>26.0%</td><td>(18.5%)</td><td>(6.1%)</td></tr><tr><td>GLW</td><td>290.8%</td><td>123.4%</td><td>0.6%</td><td>8.8%</td></tr><tr><td>LITE</td><td>848.0%</td><td>130.6%</td><td>(10.2%)</td><td>(7.8%)</td></tr><tr><td>Average</td><td>449.8%</td><td>139.7%</td><td>(10.4%)</td><td>(2.0%)</td></tr></table>

Source: Factset

<table><tr><td colspan="5">Networking Stock Performance</td></tr><tr><td></td><td>1Y</td><td>YTD</td><td>1 Month</td><td>1 Week</td></tr><tr><td>ANET</td><td>96.7%</td><td>29.5%</td><td>10.2%</td><td>3.9%</td></tr><tr><td>CLS</td><td>175.5%</td><td>26.0%</td><td>1.4%</td><td>(5.2%)</td></tr><tr><td>CSCO</td><td>84.4%</td><td>56.9%</td><td>(0.7%)</td><td>(1.3%)</td></tr><tr><td>FFIV</td><td>34.3%</td><td>51.0%</td><td>(2.1%)</td><td>(2.7%)</td></tr><tr><td>HPE</td><td>169.5%</td><td>99.2%</td><td>26.5%</td><td>(1.3%)</td></tr><tr><td>KEYS</td><td>128.2%</td><td>79.0%</td><td>4.9%</td><td>3.7%</td></tr><tr><td>Average</td><td>114.8%</td><td>56.9%</td><td>6.7%</td><td>(0.5%)</td></tr></table>

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Meta A Marshall.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

The analyst or strategist (or a household member) identified below owns the following securities (or related derivatives): Antonio Jaramillo - Arista Networks(common or preferred stock); Meta A Marshall - Corning Inc(common or preferred stock).

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Arista Networks, Axon Enterprise Inc, Ciena Corporation, Cisco Systems Inc, Coherent Corp, Corning Inc, F5 Inc, Keysight Technologies Inc, Lumentum Holdings Inc, Motorola Solutions Inc, Zebra Technologies Corporation.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Lumentum Holdings Inc.

Within the last 12 months, MS has received compensation for investment banking services from Coherent Corp, Corning Inc, Lumentum Holdings Inc, Motorola Solutions Inc, Zebra Technologies Corporation.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Arista Networks, Axon Enterprise Inc, Ciena Corporation, Cisco Systems Inc, Coherent Corp, Corning Inc, F5 Inc, Keysight Technologies Inc, Lumentum Holdings Inc, Motorola Solutions Inc, Zebra Technologies Corporation.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Cisco Systems Inc, Coherent Corp, Corning Inc, Motorola Solutions Inc, Zebra Technologies Corporation.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Arista Networks, Axon Enterprise Inc, Ciena Corporation, Cisco Systems Inc, Coherent Corp, Corning Inc, F5 Inc, Keysight Technologies Inc, Lumentum Holdings Inc, Motorola Solutions Inc, Zebra Technologies Corporation.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Axon Enterprise Inc, Cisco Systems Inc, Coherent Corp, Corning Inc, Motorola Solutions Inc, Zebra Technologies Corporation. MS & Co. LLC makes a market in the securities of Ciena Corporation, F5 Inc, Keysight Technologies Inc.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

(as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment ServicesClients (MISC)</td></tr><tr><td>Stock RatingCategory</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of RatingCategory</td><td>Count</td><td>% of Total OtherMISC</td></tr><tr><td>Overweight/Buy</td><td>1542</td><td>42%</td><td>465</td><td>51%</td><td>30%</td><td>707</td><td>43%</td></tr><tr><td>Equal-weight/Hold</td><td>1571</td><td>43%</td><td>369</td><td>40%</td><td>23%</td><td>723</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>0</td><td>0%</td><td>0%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>551</td><td>15%</td><td>86</td><td>9%</td><td>16%</td><td>201</td><td>12%</td></tr><tr><td>Total</td><td>3,667</td><td></td><td>920</td><td></td><td></td><td>1632</td><td></td></tr></table>

Data include common stock and ADRs currently assigned ratings. Investment Banking Clients are companies from whom MS received investment banking compensation in the last 12 months. Due to rounding off of decimals, the percentages provided in the "% of total" column may not add up to exactly 100 percent.

## Analyst Stock Ratings

Overweight (O). The stock's total return is expected to exceed the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Equal-weight (E). The stock's total return is expected to be in line with the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Not-Rated (NR). Currently the analyst does not have adequate conviction about the stock's total return relative to the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Underweight (U). The stock's total return is expected to be below the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Unless otherwise specified, the time frame for price targets included in MS is 12 to 18 months.

## Analyst Industry Views

Attractive (A): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be attractive vs. the relevant broad market benchmark, as indicated below.

In-Line (I): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be in line with the relevant broad market benchmark, as indicated below. Cautious (C): The analyst views the performance of his or her industry coverage universe over the next 12-18 months with caution vs. the relevant broad market benchmark, as indicated below. Benchmarks for each region are as follows: North America - S&P 500; Latin America - relevant MSCI country index or MSCI Latin America Index; Europe - MSCI Europe; Japan - TOPIX; Asia - relevant MSCI country index or MSCI sub-regional index or MSCI AC Asia Pacific ex Japan Index.

## Important Disclosures for MS Smith Barney LLC Customers

Important disclosures regarding any material conflict of interest that can reasonably be expected to have influenced MS Smith Barney LLC's choice of a third-party research provider or the subject company of a third-party research report, are available on the MS Wealth Management disclosure website at www.morganstanley.com/online/researchdisclosures. For MS specific disclosures, you may refer to https://www.morganstanley.com/eqr/disclosures/webapp/generalresearch.

Each MS report is reviewed and approved on behalf of MS Smith Barney LLC. This review and approval is conducted by the same person who reviews the research report on behalf of MS. This could create a conflict of interest.

## Other Important Disclosures

A member of Research who had or could have had access to the research prior to completion owns securities (or related derivatives) in the Cisco Systems Inc. This person is not a research analyst or a member of research analyst's household.

MS policy is to update resear

[中间内容因长度限制已省略]

d by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Telecom & Networking Equipment

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/18/2026)</td></tr><tr><td colspan="3">Meta A Marshall</td></tr><tr><td>Arista Networks (ANET.N)</td><td>O (10/31/2023)</td><td>$169.67</td></tr><tr><td>Axon Enterprise Inc (AXON.O)</td><td>O (12/03/2024)</td><td>$423.40</td></tr><tr><td>Ciena Corporation (CIEN.N)</td><td>E (10/10/2025)</td><td>$428.22</td></tr><tr><td>Cisco Systems Inc (CSCO.O)</td><td>O (04/08/2024)</td><td>$119.54</td></tr><tr><td>Coherent Corp (COHR.N)</td><td>E (12/13/2023)</td><td>$389.57</td></tr><tr><td>Corning Inc (GLW.N)</td><td>E (06/13/2024)</td><td>$194.92</td></tr><tr><td>F5 Inc (FFIV.O)</td><td>E (04/12/2022)</td><td>$385.49</td></tr><tr><td>Keysight Technologies Inc (KEYS.N)</td><td>E (10/10/2025)</td><td>$363.67</td></tr><tr><td>Lumentum Holdings Inc (LITE.O)</td><td>E (05/12/2021)</td><td>$850.00</td></tr><tr><td>Motorola Solutions Inc (MSI.N)</td><td>O (12/17/2025)</td><td>$395.17</td></tr><tr><td>Zebra Technologies Corporation (ZBRA.O)</td><td>E (12/02/2024)</td><td>$235.98</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
