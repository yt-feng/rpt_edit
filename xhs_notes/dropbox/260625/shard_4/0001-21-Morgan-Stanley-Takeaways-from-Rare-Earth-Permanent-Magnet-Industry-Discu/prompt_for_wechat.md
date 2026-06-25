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
June 23, 2026 07:54 AM GMT

Australia Materials | Asia Pacific

# Takeaways from Rare Earth Permanent Magnet Industry Discussion

We hosted a discussion with an expert with $\sim 35$ years in the rare earth permanent magnet industry, focussing on the build-out of ex-China magnet capacity, rare earth intensity reduction, China-related supply risk, rare earth substitution risk, and implications for NdPr, Dy and Tb demand.

## Key Takeaways

Ex-China NdFeB capacity is scaling: US \~28ktpa by 2028, Europe \~3.6ktpa and Japan \~6.8ktpa+ from established producers.

Sees US capacity in 2028 more than covering current NdFeB imports (\~8.5ktpa) if executed, but qualification, metal/alloy supply and cost will decide output.

\- NdPr substitution remains difficult; total rare earth content in NdFeB only fell from \~32% to \~30.5% over two decades.

Dy/Tb use has fallen much more materially, with HREE demand reduced by 50%+ in some applications through Grain Boundary Engineering and design changes.

Sees China's rare earth controls as a national security issue given military use. Although defence demand may be <500tpa this complicates commercial approvals.

Ex-China rare earth magnet capacity is growing: The expert expects that US Neodymium Iron Boron (NdFeB) capacity could reach \~28ktpa by 2028, based on announced projects and expansion from proven US manufacturers, including MP Materials (covered by Carlos De Alba), e-VAC / Vacuumschmelze and Noveon Magnetics (not covered), with broader potential US capacity of \~35ktpa when including funded and potential projects, and potential growth to \~50-55ktpa beyond 2028. This compares with current US bulk magnet imports of \~8.5ktpa from China, Vietnam and Europe, suggesting that, if executed, announced US capacity could more than sufficiently cover current US usage. However, customer qualification, metal/alloy availability, yield, process control and cost competitiveness remain challenges and will determine utilisation.

Western bottlenecks sit in metal/alloy supply and process control: The expert highlighted oxide-to-metal conversion and strip-cast alloy production as key missing links in the US supply chain. Magnet manufacturing also requires process control, automation, QA systems, trained labour, and customer qualification. For experienced companies, the expert estimated \~3 years from factory design to full output; for start-ups, the timeline could be closer to \~6 years.

MS AUSTRALIA LIMITED+

Rahul Anand, CFA

Equity Analyst

R.Anand@morganstanley.com

+61 2 9770-1136

Michael A Stancliff

Research Associate

Michael.Stancliff@morganstanley.com

+61 2 9770-9253

Asia Summer School 2026

![](images/02e86cb9fc5f0a1360f9417ffe18b1fce81f77171c9d39fde583a26649fa10ac.jpg)

AUSTRALIA MATERIALS

Asia Pacific

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Continued

NdFeB intensity reduction is mainly about HREEs, not total rare earth content: Total rare earth content in NdFeB magnets has only declined modestly over the past two decades, according to the expert, from \~32% to \~30.5%. Most of the improvement has come from reducing Dysprosium (Dy) and Terbium (Tb) use, where grain boundary diffusion, grain boundary engineering, smaller grain size, and lower application temperatures have cut heavy earth rare element (HREE) demand by 50% or more in some applications.

NdPr substitution looks more limited: The expert framed Neodymium-Praseodymium (NdPr) as more structurally embedded in NdFeB magnet chemistry. Pr substitution has helped broaden usable supply, while Ce/La-substituted grades have grown into a lower-cost product family. However, these grades fill a performance gap between NdFeB and lower-performance magnets, such as ferrite and alnico, rather than replacing high-performance NdFeB.

Rare-earth-free magnets remain application-specific: The expert does not expect a broad shift away from NdFeB. Ferrite, alnico and iron-nitride serve selected applications, but NdFeB retains a strong price-performance position. Iron-nitride is still under development and appears more relevant for lower-temperature applications. The more likely outcome is differing growth rates across magnet types and motor technologies, rather than broad displacement of NdFeB.

For wind generation, substitution depends on capital cost, maintenance and turbine architecture: The expert noted that wind generation began with induction systems and has also trialled ferrite magnets. In the West, induction systems can still be commercially attractive. NdFeB permanent magnet generators carry higher upfront cost but can reduce maintenance costs, with permanent magnet systems operating at lower speeds and potentially eliminating or simplifying the gearbox. The expert estimated NdFeB magnets in a wind generator can represent \~4–5% of total system cost, vs. \~2–2.5% for older induction-based systems. In the US, only \~1–2% of installed wind power generators uses NdFeB magnets, Europe is somewhat higher, while China may be 30-50%, or more.

China controls are already changing OEM sourcing behaviour: The expert viewed China's rare earths related export controls as partly aimed at protecting its industry position, alongside geopolitical considerations. China exports magnets directly and embedded in finished products, such as appliances, fans and other equipment, making controls commercially and politically sensitive, according to the expert. Customers are already moving toward non-China producers for immediate supply and approval processes, the expert said. Western defence industry demand for NdFeB magnets is small, potentially <500tpa, but often intermingles with commercial and industrial applications, which can complicate approvals.

Military and high-temperature applications remain sensitive: The expert highlighted aircraft generators, sensors and non-critical motors as areas where rare earth magnets are used, including Samarium-Cobalt (SmCo) and NdFeB. SmCo remains relevant in elevated-temperature and demanding aerospace / defence applications, while NdFeB is used more broadly where high magnetic performance is required. This makes end-use sensitivity

important under dual-use controls.

China pricing has pressured Western production: China-made magnets have historically been priced well below US, Japanese and European levels. In the expert's view, Chinese suppliers were often competing with each other for market access and share, rather than only competing against Western producers. In the early 2000s, Chinese pricing was around 75% of US selling prices, which made Western production difficult, particularly when US producers were already close to break-even. A competitive Western industry therefore requires a manufacturing cost base that can support viable pricing.

Western producers can close the quality gap faster than the cost gap: The expert argued that Western producers could reach Chinese magnet quality within about three years, but are unlikely to reach Chinese low production costs in the near term. China's advantage reflects lower costs across many manufacturing stages and decades of process learning. The expert estimated domestic NdFeB magnets may be \~50% more expensive than China-sourced magnets.

End-market demand is nuanced: US wind demand for permanent magnets remains limited, given low offshore wind activity and minimal permanent magnet use in onshore wind. In EVs, the expert cited NdFeB magnet weight at \~12g/kW of rated motor power, or slightly above 2kg per battery electric light-duty vehicle, while hybrids use roughly half the magnet weight. Emerging areas such as mobile robots may add demand, but many applications use very small magnets, which may be attractive on a \$/gram basis without requiring thousands of tonnes of magnet output.

Please note that the expert is not a member of MS's Research department. Unless otherwise indicated, their views are their own and may differ from the views of the MS department and from the views of others within MS. We make no claim that the expert's representations are accurate or complete.

This report references export controls and/or entities that may be subject to export control restrictions. Readers are solely responsible for ensuring that their investment or trade activities are carried out in compliance with applicable laws.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Rahul Anand, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: BHP Group Ltd, Boss Energy Ltd, Fortescue Metals Group Ltd., IGO Ltd, Iluka Resources Ltd, Lynas Rare Earths, Paladin Energy Ltd, PLS Group Ltd, Rio Tinto Limited, Sandfire Resources Ltd, South32 Ltd. Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Nickel Industries, Whitehaven Coal Ltd.

Within the last 12 months, MS has received compensation for investment banking services from Nickel Industries, Whitehaven Coal Ltd.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from BHP Group Ltd, Fortescue Metals Group Ltd., IGO Ltd, Iluka Resources Ltd, Lynas Rare Earths, Mineral Resources Limited, Nickel Industries, Paladin Energy Ltd, PLS Group Ltd, Rio Tinto Limited, Sandfire Resources Ltd, South32 Ltd, Whitehaven Coal Ltd.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Nickel Industries, Rio Tinto Limited, South32 Ltd. Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: BHP Group Ltd, Fortescue Metals Group Ltd., IGO Ltd, Iluka Resources Ltd, Lynas Rare Earths, Mineral Resources Limited, Nickel Industries, Paladin Energy Ltd, PLS Group Ltd, Rio Tinto Limited, Sandfire Resources Ltd, South32 Ltd, Whitehaven Coal Ltd.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Nickel Industries, Rio Tinto Limited, South32 Ltd.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

(as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment ServicesClients (MISC)</td></tr><tr><td>Stock RatingCategory</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of RatingCategory</td><td>Count</td><td>% of Total OtherMISC</td></tr><tr><td>Overweight/Buy</td><td>1542</td><td>42%</td><td>465</td><td>51%</td><td>30%</td><td>707</td><td>43%</td></tr><tr><td>Equ

[中间内容因长度限制已省略]

 Stanley Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Australia Materials

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/22/2026)</td></tr><tr><td colspan="3">Rahul Anand, CFA</td></tr><tr><td>BHP Group Ltd (BHPB.L)</td><td>O (09/19/2024)</td><td>3,238p</td></tr><tr><td>BHP Group Ltd (BHGJ.J)</td><td>O (09/19/2024)</td><td>ZAc 70,399</td></tr><tr><td>BHP Group Ltd (BHP.AX)</td><td>O (09/19/2024)</td><td>A$60.34</td></tr><tr><td>Boss Energy Ltd (BOE.AX)</td><td>O (01/16/2026)</td><td>A$1.16</td></tr><tr><td>Deterra Royalties Ltd (DRR.AX)</td><td>O (01/16/2026)</td><td>A$4.53</td></tr><tr><td>Fortescue Metals Group Ltd. (FMG.AX)</td><td>U (01/16/2026)</td><td>A$19.60</td></tr><tr><td>IGO Ltd (IGO.AX)</td><td>U (07/15/2025)</td><td>A$7.94</td></tr><tr><td>Iluka Resources Ltd (ILU.AX)</td><td>O (05/22/2025)</td><td>A$8.13</td></tr><tr><td>Lynas Rare Earths (LYC.AX)</td><td>E (04/14/2026)</td><td>A$18.62</td></tr><tr><td>Mineral Resources Limited (MIN.AX)</td><td>++</td><td>A$66.63</td></tr><tr><td>Paladin Energy Ltd (PDN.AX)</td><td>O (10/08/2025)</td><td>A$9.83</td></tr><tr><td>PLS Group Ltd (PLS.AX)</td><td>E (04/14/2026)</td><td>A$5.53</td></tr><tr><td>Rio Tinto Limited (RIO.AX)</td><td>E (04/09/2025)</td><td>A$175.99</td></tr><tr><td>Sandfire Resources Ltd (SFR.AX)</td><td>U (12/16/2024)</td><td>A$20.71</td></tr><tr><td>South32 Ltd (S32.AX)</td><td>O (12/16/2024)</td><td>A$4.15</td></tr><tr><td>South32 Ltd (S32J.J)</td><td>O (12/16/2024)</td><td>ZAc 4,876</td></tr><tr><td>Whitehaven Coal Ltd (WHC.AX)</td><td>O (04/14/2026)</td><td>A$8.27</td></tr><tr><td colspan="3">Shannon J Sinha</td></tr><tr><td>Nickel Industries (NIC.AX)</td><td>E (04/09/2025)</td><td>A$0.96</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
