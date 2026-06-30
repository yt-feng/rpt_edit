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
June 28, 2026 10:00 PM GMT

China Economics | Asia Pacific

# China Surplus Meets EU Defense

EU-China trade tensions are building. As the secular decline in housing-related investments lifts the current account structurally, Beijing will likely manage pressure through selective concessions and countermeasures. Meaningful RMB appreciation is not the preferred adjustment channel.

EU reacts to rising trade deficit with Beijing — gradual, institutionalized, bounded: Recent EU remarks point to a tougher trade line: de-risking with an economic-security overlay beyond the 2024 EV playbook. Pressure should concentrate where the EU runs widening bilateral deficits but still has globally competitive industries — autos, machinery & electrical equipment, and chemicals.

The toolkit has widened: Beyond anti-subsidy and anti-dumping cases, the EU now uses the Foreign Subsidies Regulation in procurement, the International Procurement Instrument on reciprocity, CBAM on energy-intensive sectors, and tougher local-content rules in clean tech. This makes escalation more institutionalized and sector-specific.

China's macro backdrop may keep tensions alive: China's surplus is not just growth policy; it is the external counterpart of weak domestic demand, as housing and "old" infrastructure investment are in secular decline; meanwhile, savings remain high. Without a more decisive shift toward consumption, part of the excess saving is likely to be reflected in elevated external surpluses.

China's response is likely tactical, not transformative: However, a real consumption pivot would be costly and institutionally hard. Beijing may offer selective concessions — import commitments, market access, further cancellation of export VAT rebate, or negotiated remedies around subsidies. Frictions can be managed, not resolved.

But escalation is two-way bounded: China retains retaliation levers, including pork, dairy and brandy probes, plus market access in aviation, autos and luxury. The EU still relies on China in rare earths and clean-tech supply chains. Expect a legal escalation, not a rupture.

RMB — meaningful appreciation not warranted: We do not expect rapid RMB appreciation in the coming quarters as the housing downturn persists, while a decisive consumption-led rebalance appears unlikely. Without stronger domestic demand, rapid appreciation would mainly squeeze exporters, profits and employment, reinforcing deflationary pressure rather than resolving the underlying imbalance.

<table><tr><td colspan="2">MS ASIA LIMITED</td></tr><tr><td colspan="2">Robin Xing</td></tr><tr><td colspan="2">Chief China Economist</td></tr><tr><td>Robin.Xing@morganstanley.com</td><td>+852 2848-6511</td></tr><tr><td colspan="2">Jenny Zheng, CFA</td></tr><tr><td colspan="2">Economist</td></tr><tr><td>Jenny.L.Zheng@morganstanley.com</td><td>+852 3963-4015</td></tr><tr><td colspan="2">Zhipeng Cai</td></tr><tr><td colspan="2">Economist</td></tr><tr><td>Zhipeng.Cai@morganstanley.com</td><td>+852 2239-7820</td></tr><tr><td colspan="2">Harry Zhao</td></tr><tr><td colspan="2">Economist</td></tr><tr><td>Harry.Zhao@morganstanley.com</td><td>+852 2239-7229</td></tr></table>

Asia Summer School 2026

![](images/8b101015b536ff1448aa2feea780949aedb73d8e4bb878d0dc1a5e105a7a72a9.jpg)  
Exhibit 1: Widening EU trade deficit with China since 2021

![](images/2dae119ab1016298ec32a8badaa416e579d8b7ae5d92cd8f955a900ee96c01d0.jpg)  
Source: CEIC, MS  
Exhibit 2: Europe faces a dual headwind from China: rising competitive pressure domestically and weak export demand externally.

![](images/96aa12ae13aac0087a73292615791bcee0299d48dfa16e83e539ef756fe30e3a.jpg)  
Source: CEIC, MS

## EU-China Trade Tensions: A Primer

## Latest EU remarks on global imbalance and domestic industrial policies

Read-out of the College orientation debate on EU-China relations - 29 May 2026

\- The Commission's overarching approach remains de-risking, not decoupling.

\- China is a critical partner, and engagement and dialogue will continue. At the same time the current state of the trade and investment relationship is not sustainable.

\- As economic and security interests become ever more intertwined, both dimensions will require a more robust and coherent response.

## G7 leaders' statement on geopolitical issues - 17 June 2026

\- We reaffirm our common interest in converging with other large economies on the causes of large and persistent global imbalances and on the need to address them. We will continue these efforts within the G20 under the United States' host year and in other relevant fora.

European Council conclusions on competitiveness and global economic challenges - 19 June 2026

\- strengthen EU competitiveness and strategic autonomy, increase resilience and economic security, promote technological innovation

\- fostering Europe's industrial renewal and innovation and reducing dependencies

## Potential China-EU trade pressure points

## Our simple framework consists of two elements:

\- By-sector level and trajectory in EU trade balance with China. A large deficit with China shows where the pressure is already big; a fast-worsening balance shows where political concern is likely rising fast.

\- The overlay would be Europe's own competitiveness that it wants to defend.

The sectors most exposed to tougher EU trade actions are machinery and electrical equipment, autos, chemicals, and steel/base metals. To further categorize:

\- Competitive EU industries being challenged: Autos, machinery and electrical equipment, chemicals. This is most visible in autos, where Europe's longstanding competitiveness is being challenged by Chinese EVs. Media reports suggest the European Commission is considering additional duties on Chinese PHEVs, following the countervailing duties imposed on BEVs in 2024.

\- Overcapacity amid China's structural transition: Steel and base metals. The EU has already started to move toward broader steel protection, likely due to the sector's implications for jobs and industrial security.

Exhibit 3: EU-China trade balance by product  
![](images/e8d09889163b891bd812210bc00f4fe67c7a3fac84499e2d208f0631d79c0206.jpg)  
Source: UNComtrade, MS

Exhibit 4: EU trade balance with China is worsening over time  
![](images/52ceef914b9c573e35fb684b616fb56e7036c9ff51e3517fa626433f454b6b0f.jpg)  
Source: CEIC, MS

## How would potential tensions unfold? Navigating preferences, dependencies, and chokepoints

A gradual, institutionalized approach, rather than sudden and massive escalation: The EU appears to be adding a more systemic economic-security overlay onto the prevailing case-by-case trade defense framework. However, the overall approach, as repeatedly affirmed by EU, would remain “de-risking not decoupling” — pursued through two complementary tracks: diversifying critical supply chains away from China, and selectively restricting Chinese access to the EU single market where strategic, security or level-playing-field concerns arise.

The toolkit has expanded in recent years: Anti-subsidy and anti-dumping investigations (EVs, biodiesel, mobile cranes, tinplate); the Foreign Subsidies Regulation (FSR), now actively used to screen Chinese bids in public procurement, M&A and green-tech tenders; the International Procurement Instrument (IPI), first deployed against Chinese medical devices; Carbon Border Adjustment Mechanism covering steel, aluminum and chemicals; and hardening local-content and "Made-in-Europe" criteria in clean-tech subsidies and auto procurement.

But potential tensions will likely be bounded by the following forces:

\- Managing differences in internal interests: The Commission must assess whether measures are consistent with the broader economic interests in the EU, and consensus building takes time. Take the countervailing duties on EVs as an example: the investigation was announced by the EU in Sep-23 and only finished by Oct-24.

\- Strategic goals rely on inputs from China: For example, the EU's preferred EV transition still depends heavily on China-linked battery supply chains, where China holds a dominant position. Aggressive restrictions on Chinese autos could therefore trigger retaliation or supply-chain friction in batteries and related inputs, potentially slowing EV penetration in the EU.

\- Two-way leverage. The constraints run both ways. China retains meaningful retaliatory tools such as anti-dumping probes on EU pork, dairy and brandy; Airbus order pipelines; and discretionary market access for European firms in autos, luxury and financials.

\- Chokepoints: EU sources all of its heavy rare earth elements (REEs) and 85% of its light REEs from China, as well as 98% of its rare-earth magnets (per European Parliament). This dependency caps how far Brussels can escalate before risking self-harm.

## China's reaction function: tactical accommodation, commensurate countermeasures, no decisive rebalancing towards consumption

China's macro backdrop: excess savings amid transition of growth drivers: The surplus is not just industrial or trade policy, in our view. The property downturn has reduced demand for housing-related investment, while the scope for another round of “old” infrastructure-led stimulus looks increasingly constrained. At the same time, household confidence remains fragile and precautionary savings are still high, keeping domestic demand soft. The increasing gap between desired saving and investment is reflected in elevated external balance in recent years. Without a more decisive consumption-led rebalancing, the surplus is likely to remain relatively persistent as the economy converges to a new growth path.

China's response to EU escalation is likely to be tactical: But a decisive consumption pivot would be costly and institutionally hard, requiring a larger redistribution of income. Beijing may seek to manage frictions through selective concessions — import commitments, targeted market access, further cancellation of export VAT rebates, price undertakings, or negotiated remedies around subsidies and procurement. At the same time, China's reaction function will likely feature calibrated reciprocity: offer concessions where cost is manageable, and retaliate where leverage is high and escalation remains controllable. This points to probes or restrictions in politically sensitive European sectors — agriculture, spirits, autos, aviation, luxury goods — rather than a broad rupture.

Near-term impact manageable, but trade flows could be reoriented in the long run. We think the near-term growth impact would be modest, considering (1) potentially gradual EU enforcement, and (2) resilience of China's exports amid US trade escalations — anchored by market diversification, supply chain lengthening, and continued value-chain upgrading. In the long run, if Europe gradually tightens market access through local content rules, procurement restrictions, tariffs, and anti-dumping levies, China's potential response could be to reroute exports, accelerate offshore production, and invest more directly in Europe (subject to mutual investment treaties) to preserve market access. The result would be redistribution of trade flows and value-added, instead of a meaningful deterioration in China's trade position.

## Disclosure Section

Information and opinions in MS were prepared or are disseminated by one or more of the following, which accept responsibility for its contents: MS Asia Limited, and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105), Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Disclosures

MS is not acting as a municipal advisor and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of Section 975 of the Dodd-Frank Wall Street Reform and Consumer Protection Act.

MS does not provide individually tailored investment advice. MS has been prepared without regard to the circumstances and objectives of those who receive it. MS recommends that investors independently evaluate particular investments and strategies, and encourages investors to seek the advice of a financial adviser. The appropriateness of an investment or strategy will depend on an investor's circumstances and objectives. The securities, instruments, or strategies discussed in MS may not be suitable for all investors, and certain investors may not be eligible to purchase or participate in some or all of them. MS is not an offer to buy or sell or the solicitation of an offer to buy or sell any security/instrument or to participate in any particular trading strategy. The value of and income from your investments may vary because of changes in interest rates, foreign exchange rates, default rates, prepayment rates, securities/instruments prices, market indexes, operational or financial conditions of companies or other factors. There may be time limitations on the exercise of options or other rights in securities/instruments transactions. Past performance is not necessarily a guide to future performance. Estimates of future performance are based on assumptions that may not be realized. If provided, and unless otherwise stated, the closing price on the cover page is that of the primary exchange for the subject company's securities/instruments.

The fixed income research analysts, strategists or economists principally responsible for the preparation of MS have received compensation based upon various factors, including quality, accuracy and value of research, firm profitability or revenues (which include fixed income trading and capital markets profitability or revenues), client feedback and competitive factors. Fixed Income Research analysts', strategists' or economists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

With the exception of information regarding MS, MS is based on public information. MS makes every effort to use reliable, comprehensive information, but we make no representation that it is accurate or complete. We have no obligation to tell you when opinions or information in MS change apart from when we intend to discontinue equity research coverage of a subject company. Facts and views presented in MS have not been reviewed by, and may not reflect information known to, professionals in other MS business areas, including investment banking personnel.

MS may make investment decisions that are inconsistent with the recommendations or views in this report.

To our readers based in Taiwan or trading in Taiwan securities/instruments: Information on securities/instruments that trade in Taiwan is distributed by MS Taiwan Limited ("MSTL"). Such information is for your reference only. The reader should independently evaluate the investment risks and is solely responsible for their investment decisions. MS may not be distributed to the public media or quoted or used by the public media without the express written consent of MS. Any non-customer reader within the scope of Article 7-1 of the Taiwan Stock Exchange Recommendat

[中间内容因长度限制已省略]

ts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 14-9169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
