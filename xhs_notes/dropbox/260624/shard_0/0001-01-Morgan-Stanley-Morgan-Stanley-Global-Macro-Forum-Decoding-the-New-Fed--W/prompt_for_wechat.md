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
## MS Global Macro Forum

## Decoding the New Fed: What the Fed Said, What Markets Heard

June 22, 2026

Vishwanath Tirupattur – Chief Fixed Income Strategist | Strategist

Seth Carpenter – Chief Global Economist

Matthew Hornbach – Global Head of Macro Strategy | Strategist

Jay Bacow – Co-Head of Securitized Products Research | Strategist

Michael Wilson – Chief Investment Officer and Chief US Equity Strategist | Strategist

MS & CO. LLC

Marina Zavolock – Chief European Equity Strategist | Strategist

MS & CO. INTERNATIONAL PLC+

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Seth Carpenter

Chief Global Economist

MS

Matthew Hornbach Global Head of Macro Strategy

MS

Jay Bacow Co-Head of Securitized Products Research

## Sell Mortgage Basis vs Rates

The mortgage index is relatively tight, and hasn't traded much tighter outside of QE periods

![](images/64454be978090ea3514e92bfd64e406a432674dbfd0e2ba395d3e32d263aa07e.jpg)  
Furthermore, vol is not particularly low and could rise amid lack of forward guidance

![](images/6a795c6dfea48b41b02366172025eb6414154055ebd330f7940d2ad07396ac0b.jpg)  
Source: MS, Bloomberg

We're Also Concerned About Cap Risk, but Net Supply is Running Low, Which Should Mitigate Too Much Widening

Into higher rates/Fed hiking cap risk may become a concern

![](images/208bb17719bc6f74863e854da2ab4d2f63d20366fdb7ca157e17a34fbc8efe38.jpg)  
Net issuance through May is running at similarly low levels as previous years and may drop at this rate level/securitization rate

![](images/bd780f50244a01da461f33cf6d0b00efd6a6a95752004b1651f6e67bef744434.jpg)  
Source: MS, eMBS

MS

Michael Wilson  
Chief Investment Officer and Chief US Equity Strategist

MS

Marina Zavolock

Chief European Equity Strategist

## Fed Policy vs SoH Reopening Trade

Correlations to SoH reopening align with Fed policy sensitivities  
European Sectors: Combined score sensitivity to SoH reopening  
![](images/611d2865ddbc7b6aeeb09ad18b25f098848ee88398614da0dfca86594133eff4.jpg)

## Performance of stocks most positively exposed to SoH reopening

SoH Reopening Top 50 Screens: Relative performance vs MSCI Europe YTD (LC)  
![](images/0654bc072a0ec63a016601360e3c05cb24b2dcd5b1f29e5e612ae6d6b708dcd1.jpg)

## Fed Policy vs SoH Reopening Trade

Top vs bottom performance has been more pronounced

SoH Reopening Screens: Top 50 vs bottom 50 relative performance YTD (LC)

![](images/07096651496215c1f988bb7eaa049e0bc559d56c8613dc491ca5e1db4e9090ca.jpg)

European equities are stuck in a seasonal lull similar to post 'Liberation Day'  
Stoxx 600 Performance Around Market Troughs (rebased, EUR)  
![](images/805801d509b157a072035b918ba97b0cb682e7be62f0785a9a00bae989843fa1.jpg)

## Fed Policy vs SoH Reopening Trade

Stock market breadth is recovering at a slow pace...

MSCI Europe performance breadth: % of stocks outperforming the market  
![](images/7623559ff5cf73bb1fae998725540d982acf2cd49572cc66aec6d250acbb23ff.jpg)  
Mutual Fund & ETF Flows into European & US Equities (USDbn)

## ... As are flows into European equities

![](images/66252fadc487dba4356e42bf430a98a4b923ecd8826171b1ab6cfc39c1993a77.jpg)

Source: EPFR, MS; Note: The EPFR data and charts displayed here must not be extracted and republished (whether internally or externally). Such use will violate the terms of MS's contract with EPFR which only covers named users.

Vishwanath Tirupattur

Chief Fixed Income Strategist

## Key Takeaways

\- New chair, new Chapter: Chair Warsh intentionally gave little guidance on the path of monetary policy, noting that reducing “forward guidance” is central to his approach. Even as he highlighted that “[t]he Committee will deliver price stability” the path was not laid out, by design. How different will the Fed be a year from now? Likely very different, in many aspects of the Chair’s communications as well as the size of balance sheet. But when it comes to monetary policy through rates, the change is unlikely to be as stark.

\- Signaling from markets and higher volatility: The chair's remarks suggest higher interest rate volatility and greater signaling qualities of macro markets. Despite Chair Warsh explaining his desire to avoid conveying anything that seemed like forward guidance, the market took Warsh's lack of pushback to current pricing as a reason to price even closer to the dots. We continue to recommend investors stay in SFRZ6M7 curve flatteners given the risk of the Fed following market pricing and a subsequent flattening of the SOFR curve.

\- Tactically underweight mortgages: Higher levels of longer-term volatility from reduced forward guidance, bear flattening leading to reduce demand from banks and the potential for FX hedging costs staying elevated motivate move to underweight FNCL 5.5s vs rates on a tactical basis. We like trades that are somewhat long vol – short mortgages, long 15s/30s, long agency multifamily vs single family, and long specified pools vs TBA.

\- View from equity markets: Chair Warsh's move away from forward guidance and toward greater reliance on market signals will improve the quality and timing of Fed's decision-making. Ultimately, earnings remain the primary driver of this bull Market. The breadth and resilience of earnings has offset the multiple contraction YTD and will likely soften any further blows from tighter monetary policy or uncertainty due to less Fed guidance and/or market challenges of the new Chair.

## MS

## Live Trades, Risk, and Rationale

<table><tr><td>Trade</td><td>Entry Date</td><td>Rationale</td><td>Risks</td></tr><tr><td>Short FNCL 5.5s vs Tsy tactically</td><td>6/17/2025</td><td>Market underpriced for Fed hikes, mortgages perform poorly in that scenario, bank and GSE demand could wane</td><td>Mortgage valuations cheap to competing assets, risk assets outperform, Fed cuts</td></tr><tr><td>Replace index exposure with multifamily</td><td>6/17/2025</td><td>Less negative carry way to short MBS, bank demand for multifamily still strong</td><td>Multifamily spreads near tights due to positive technicals</td></tr><tr><td>Long DW5/FNCL 5.5</td><td>6/17/2025</td><td>Long vol, 15yr issuance should dry up amid higher rates, 15s reasonable OAS</td><td>give liquidity, carry</td></tr><tr><td>Buy 250-350k 5.0 vs roll</td><td>5/29/2025</td><td>Cheap/fair vs TBA OAS likely near wides of possible range given technicals of worsening TBA deliverable</td><td>5.0 roll goes special</td></tr><tr><td>Buy seasoned 5.0 and 5.s vs roll</td><td>5/1/2025</td><td>Pick OAS vs TBA, take advantage of pools seasoning vs deliverable</td><td>Roll goes special</td></tr></table>

<table><tr><td>Trade</td><td>Entry Date</td><td>Rationale</td><td>Risks</td></tr><tr><td>Maintain SFRZ6M7 curve flattener</td><td>5/22/2026</td><td>We think SFRZ6M7 curve flatteners offer a compelling way to express the view that market pricing places too much weight on hawkish Fed tail risks, in response to the oil shock, and the allure of an AI-driven industrial activity renaissance. This relative value expression allows investors to exploit a substantial insurance premium against rate hikes, removes outright duration beta, while not requiring a near-term dovish pivot by the Fed.</td><td>The main risk is if fiscal stimulus arrives before the mid-term elections, which would justify currently elevated levels of near-term inflation expectations.</td></tr></table>

Source: MS, Bloomberg

## MS

## History of recommendations

<table><tr><td colspan="4">SFRZ6M7 Flattener</td><td colspan="7"></td></tr><tr><td>Instrument</td><td>Identifier</td><td>Maturity</td><td>Trade</td><td>Entry Date</td><td>Entry Level</td><td>Exit Date</td><td>Exit Level</td><td>Target/ Objective</td><td>Stop/Re-assess</td><td>Size of Trade or Unit/Notional</td></tr><tr><td>SFRZ6</td><td>SFRZ6 Comb Comdty</td><td></td><td>SFRZ6M7 Flattener</td><td>19-Jun-2026</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SFRM7</td><td>SFRM7 COMB COMDTY</td><td></td><td>SFRZ6M7 Flattener</td><td>19-Jun-2026</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: MS

## Definition of terms

Buy/Long: The analyst expects the total or excess return (depending on the nature of the recommendation) of the instrument or issuer that is the subject of the investment recommendation to be positive over the relevant time period.

Sell/Short: The analyst expects the total or excess return (depending on the nature of the recommendation) of the instrument or issuer that is the subject of the investment recommendation to be negative over the relevant time period.

Selling protection or Buying Risk: The analyst expects that the price of protection against the event occurring will decrease over the relevant time period.

Buying protection or Selling Risk: The analyst expects the price of protection against the event occurring will increase over the relevant time period.

Pay: The analyst expects that over the specified time period the variable rate underlying the swap agreement that is the subject of the investment recommendation will increase.

Receive: The analyst expects that over the specified time period the variable rate underlying the swap agreement that is the subject of the investment recommendation will decrease.

Unless otherwise specified, the time frame for recommendations included in the MS Fixed Income Research reports is 1 - 3 months and the price of financial instruments mentioned in the recommendation is as at the date and time of publication of the recommendation.

When more than one issuer or instrument is included in a recommendation, analyst expects one part of the trade to outperform the other trade or combination of other trades included in the recommendation on a relative basis.

For important disclosures related to the proportion of all investment recommendations over the past 12 months that fit each of the categories defined above, and the proportion of issuers corresponding to each of those categories to which MS has supplied material services, please see the MS disclosure at https://ny.matrix.ms.com/eqr/article/webapp/b83487c0-2db9-11f1-b3c0-bb95a716ade2?ch=rp&sch=sr&sr=1

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Vishwanath Tirupattur, Seth Carpenter, Matthew Hornbach, Jay Bacow, Michael Wilson, Marina Zavolock.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from United States of America.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: United States of America.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

(as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

## Disclosure Section (Cont.)

<table><tr><td rowspan="2">Stock Rating Category</td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment Services Clients (MISC)</td></tr><tr><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of Rating Category</td><td>Count</td><td>% of Total Other MISC</td></tr><tr><td>Overweight/Buy</td><td>1542</td><td>42%</td><td>465</td><td>51%</td><td>30%</td><td>707</td><td>43%</td></tr><tr><td>Equal-weight/Hold</td><td>1571</td><td>43%</td><td>369</td><td>40%</td><td>23%</td><td>723</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>0</td><td>0%</td><td>0%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>551</td><td>15%</td><td>86</td><td>9%</td><td>16%</td><td>201</td><td>12%</td></tr><tr><td>Total</td><td>3,667</td><td></td><td>920</td><td></td><td></td><td>1632</td><td></td></tr></table>

Data include common stock and ADRs currently assigned ratings. Investment Banking Clients are companies from whom MS received investment banking compensation in the last 12 months. Due to rounding off of decimals, the percentages provided in the "% of total" column may not add up to exactly 100 percent.

## Analyst Stock Ratings

Overweight (O). The stock's total return is expected to exceed the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months. Equal-weight (E). The stock's total return is expected to be in line with the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Not-Rated (NR). Currently the analyst does not have adequate conviction about the stock's total return relative to the average total retu

[中间内容因长度限制已省略]

 by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

## MS

## Disclosure Section (Cont.)

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations. The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income

research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are neither Equity Research Analysts/Strategists nor Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity or fixed income securities: Diego Anzoategui

dr2206

The Americas  
1585 Broadway  
New York, NY 10036-8293  
United States  
+1 212 761 4000

Europe  
20 Bank Street, Canary Wharf  
London E14 4AD  
United Kingdom  
+44 (0)20 7425 8000

Japan  
1-9-7 Otemachi, Chiyoda-ku  
Tokyo 100-8104  
Japan  
+81 (0) 3 6836 5000

Asia/Pacific  
1 Austin Road West  
Kowloon  
Hong Kong  
+852 2848 5200
"""
