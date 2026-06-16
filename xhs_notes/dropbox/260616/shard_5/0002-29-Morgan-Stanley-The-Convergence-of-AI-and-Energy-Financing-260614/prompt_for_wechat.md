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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

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
# Sunday Start | What's Next in Global Macro

# The Convergence of AI and Energy Financing

A few weeks ago, we outlined a framework for financing the unprecedented scale of capex for AI infrastructure across multiple channels in equity and credit markets, touching on potential constraints (see The New Architecture of AI Infrastructure Financing). After spending more time with clients and industry participants, it has become increasingly clear that these constraints are not peripheral frictions – they are central to this entire AI infrastructure buildout and require a rethink of both the scale and structure of this financing. In this week’s Start, we outline the constraints and their impact on the pace and magnitude of investment as well as their implications.

One of the most serious constraints sits upstream from data centers, in power. The scale of power demand tied to AI is colliding with structural limits in both generation and grid infrastructure in the US and globally, as detailed in a recent report (see Flexible Power – The Next Wave of Growth in AI). In several regions, data centers are no longer marginal additions to load, but are among the largest and fastest-growing sources of incremental power demand. Yet the systems required to support that demand—the generation capacity, transmission networks, and equipment supply chains needed to support it—face much longer timelines.

A few data points illustrate the bottlenecks. As reported by IndustrialSage, power transformer lead times now average 128 weeks, with generator step-up transformers at 144 weeks, versus a pre-COVID norm of just 12–16 weeks. Berkeley Lab noted that the interconnection backlog—the delay between building new energy projects and connecting them to the grid—exceeded 2x installed US capacity in early 2025. It is likely longer today.

This dynamic is reshaping how we think about the AI infrastructure buildout. Power is no longer a secondary consideration but a co-equal constraint on data center development that must be secured up front. Developers are already prioritizing sites based on power availability and exploring integrated solutions that bring generation and compute closer together. While these limits may catalyze innovation in how power is sourced, contracted, and delivered, they reinforce the sobering reality that scaling AI infrastructure is likely to take longer and be more sequential and capital-intensive than headline data center capex projections alone suggest.

With power availability emerging as a roadblock, the financing needs of AI infrastructure and the energy complex are converging, blurring the traditional boundaries between them. “Off-grid” power solutions—ranging from fuel cells and gas turbines to energy storage—along with “time-to-power” strategies such as repurposing Bitcoin mining sites, have become central to the build-out. Recent transactions across both investment-grade and high-yield markets reflect this

MS & CO. LLC

## Vishwanath Tirupattur

Strategist

Vishwanath.Tirupattur@morganstanley.com

+1 212 761-1043

## Stephen C Byrd

Equity Analyst

Stephen.Byrd@morganstanley.com

+1 212 761-3865

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

convergence. Increasingly, AI players themselves are acquiring, contracting, or financing these assets rather than treating them as separate, utility-led investments. In effect, the AI build-out is collapsing what were once distinct capital pools into a more integrated and interdependent funding model.

Beyond power, broader structural constraints spanning labor, natural resources, and public policy are emerging. On labor, there is a projected shortfall of roughly 300,000 electricians in the US over the next decade, with more than a fifth of the existing workforce already aged 55 or older and nearing retirement. Water is emerging as a parallel constraint: S&P analysis suggests that 43% of data centers globally are located in regions of high water stress, raising questions about the sustainability and scalability of further build-out in key hubs. At the same time, bipartisan opposition to new data center development is building. Draft legislation in New York State would impose a moratorium on new projects, a recent order from Texas Governor Abbott directs regulators to ensure incremental data center demand does not raise costs for other users, and a growing number of projects have been rejected at the local level. More broadly, 14 state legislatures are now considering some form of moratorium on data centers.

These structural constraints are challenging the industry's ability to deliver compute capacity at the pace and scale implied by current demand trajectories. The risk of a structural imbalance between supply and demand for compute is growing. In that environment, scarcity becomes a defining feature of the market, reinforcing pricing power for those with access to scaled, reliable capacity – the emerging “merchants of compute.” Importantly, at this stage of the cycle, demand appears relatively inelastic, particularly from enterprise use cases, with higher prices unlikely to slow adoption materially. If anything, this dynamic may further shift usage toward higher-value applications, where the economics of compute remain compelling even at elevated price points.

Enjoy your Sunday.

Send Us Feedback

## What I'm Reading This Week

Global Thematics: Thematics + Mathematics

Global Technology: Chipflation – Navigating A Memory Crisis

Asia Economics - The Viewpoint: Why boosting India's manufacturing is more important than ever

US Economics: Why didn't the unemployment rate fall more? And will labor supply growth be sufficient?

What We Are Watching This Week

MONDAY, JUNE 15

US Industrial Production: Industrial production is expected to have slipped 0.1% m/m in May. Motor vehicle output was likely a slight drag, and we forecast stalled nonauto manufacturing output. This looks like a temporary pause: growth has been solid, and the factory surveys do not suggest a change in trend.

US NAHB: National Assoc. of Homebuilders builder confidence index has risen from mid-2025 lows but remains unusually depressed.

US Empire manufacturing: The May ISM manufacturing PMI was stronger than expected. Both the national and regional surveys show strong production and demand, while employment remained soft. We also see price deceleration in some areas and acceleration in others. We expect the manufacturing sector to remain resilient in June, and we initiate our June ISM manufacturing PMI tracking estimate at 53.8.

Japan Index of Tertiary Industry Activity: We expect that the index of tertiary industry activity in April increases at +0.6% MoM.

Euro area industrial production: We expect EA Industrial production to stall in April (0.2%M after 0.2%M in March), in line with softer business surveys

## TUESDAY, JUNE 16

US Housing Starts: Single-family starts are running high relative to permits. We expect further payback in May, with a slight decline to 915k. The housing market index rose slightly in May but remains weak; we expect just a slight pickup in single-family permits to 895k. We expect multifamily permits to be unchanged but to start declining after a strong April.

Japan BoJ MPM: We expect a rate hike to 1.0% at June MPM (June15-16). We also expect the BoJ to maintain JGB purchase amounts from April 2027.

Germany ZEW expectations: ZEW expectations for the next six months are expected to edge up in June (-5.0 from -10.2) as oil prices have receded in the past weeks.

China growth indicators: We expect industrial production growth to pick up to 4.5%Y (vs. 4.1% in Apr). YTD FAI growth likely slipped to -3.1%Y (vs. -1.6% in Apr). Retail sales growth may have dropped to -0.5%Y (vs. 0.2% in Apr).

Australia RBA Cash Rate: We expect the RBA Board will leave the cash rate on hold at 4.35% at its 16 June meeting, following three consecutive hikes. The statement is still likely to lean hawkish as inflation pressures are broadening and the Board will remain alert to de-anchoring risk.

## WEDNESDAY, JUNE 17

US Retail Sales: We forecast that headline retail sales rose 0.5%m/m for the month of May, boosted by another strong month of sales at gasoline stations. We expect that control group retail sales were up 0.2%m/m, auto sales rose 0.4%, and sales at restaurants were up 0.5%. Sales of building materials are expected to have decelerated in May (-0.3%). For the control group, growth in nominal labor market income is supportive, and credit/debit card transactions May data show some recovery after a very soft April. We estimate the growth of control group prices for May is -0.1%.

US Pending Home Sales: Pending home sales have risen the past few months, and the recent pickup in existing home sales in May brought the two measures back in-line. Home sales overall are still within their low range of the past few years.

US FOMC Meeting: Chairman Warsh's first. We expect the Fed to hold rates unchanged in June, with no dissents. In the statement, we expect new recognition of faster payroll gains. We also expect the FOMC to drop the easing bias, instead saying something like "in considering any adjustments to the target range..." In the SEP, we expect the median dot to show no cuts this year, one cut in 2027, and one cut in 2028. First press conferences can be uneven. There's a greater chance of miscommunication and subsequent correction, in our view. We expect Warsh to describe an uncertain economic outlook, to point out that heightened uncertainty argues for patience in policymaking, and to say that the FOMC believes the current stance of policy is appropriate. How much guidance he is willing to give is an important question, as he has leaned against guidance in commentary in the past.

Japan Core Machinery Orders: We forecast core machinery orders increase by +1.5% MoM in April.

Japan Custom Clearance Trade Balance: The trade balance is expected to be -590.0 billion yen in May.

UK Inflation: We see headline CPI inflation at 3.0%Y, with core rounding up to 2.7%Y, and RPI inflation coming in at 3.3%Y. The upswing in headline inflation is down to services - more precisely, air fares, which we model at 14%M. Accommodation, we think, should provide a decent counter to air fares, with what we estimate to be \~10bp drag on services inflation. Base effects in travel categories and in VED, in sum, will push up on May inflation, in a reversal of April dynamics.

Sweden Riksbank Rates Decision: We expect Riksbank to remain on hold next week. The policy rate path could bring the possibility of tightening forward to 3Q26. On projections, we expect to see lower growth and inflation in 2026, and a higher inflation path in 2027.

Brazil BCB Meeting: We expect BCB to cut rates 25bp to 14.25%. In the statement, we anticipate a more hawkish tone on inflation (BCB inflation forecast up to 3.7%) while still keeping a dovish bias on the activity outlook. We expect BCB to signal a pause for August, reflecting a deterioration in the external environment that led markets to price higher global interest rates. We now expect a higher Selic at 14.00% (vs 13.00% previously) by year-end and 11.00% (from 10.50%) next year.

## THURSDAY, JUNE 18

Czech Republic Repo Rate: In what is very likely to be a close call, we expect the CNB to leave its key policy rate unchanged at 3.50% but see a subjective probability of 45% for the MPC to decide to raise it by 25bp to 3.75%.

US Jobless Claims: The four-week average of jobless claims has risen 10k from a month ago. Some of the rise looks like distortion from seasonal factors: the sum of state claims has not risen as much and it diverged similarly last year at this time. We do not yet forecast retracement.

Indonesia BI Monetary Policy Meeting: We expect BI to hike rates by another 25bps as part of its drive to strengthen currency stability. We think that the decision will hinge on currency trends in the coming days. Unless the currency appreciates meaningfully in the days before the meeting, we still see a rate hike as the central scenario.

The Philippines BSP Monetary Policy Meeting: We expect BSP to hike rates by another 25bps. Headline and core measures of inflation remain elevated and while energy prices have come off, we think further rate hikes are needed to anchor inflation expectations and ensure that inflation returns closer to target over time.

Taiwan CBC Monetary Policy Meeting: We expect no change at the June meeting while concerns around stronger inflation may be noted. We see CBC not in any urgency to move the rate given the stable housing market and the overall benign inflation level relative to other economies.

UK Labor Market Data: After a level shift higher in March, we expect the jobless rate to remain at 5.0% in the three months to April, before rounding up to 5.1% in the next month's reading. We forecast a revised April payrolls change at -10k and May at -25k. In addition, we see vacancies as slipping to just below 700k in the three months to May. On earnings, the AWE data suggests compositional effects are as negative as -0.5pp but there is a decent degree of uncertainty around the data. Mindful of this, we model the private sector regular AWE growth in April just about rounding down to 2.9%3M/Y, with whole economy ex-bonus pay growth coming in at 3.3%3M/Y. We see total pay growth at 4.0%3M/Y, as some of the recent strength in bonuses as measured by AWE cools.

Norway Norges Bank Rates Decision: We expect Norges Bank to remain on hold after delivering its 2Q rate hike in May. Inflation came broadly in line, and economic activity has been a touch weaker. However, due to rising inflationary pressures (indicators and commodity prices), we expect a further upward revision of policy rate path upwards in 3Q.

UK BoE Rates Decision: We expect unchanged messaging, and a 7:2 vote for rates on hold.

## FRIDAY, JUNE 19

Japan Nationwide CPI: Our forecasts for the May nationwide CPI are: All items +1.4% YoY, All items less fresh food: +1.4%YoY, All items less fresh food and energy: +1.9%YoY.

## Disclosure Section

Mortgage Backed Securities (MBS) and Collateralized Mortgage Obligations (CMO)

Principal is returned on a monthly basis over the life of the security. Principal prepayment can significantly affect the monthly income stream and the maturity of any type of MBS, including standard MBS, CMOs and Lottery Bonds. Yields and average lives are estimated based on prepayment assumptions and are subject to change based on actual prepayment of the mortgages in the underlying pools. The level of predictability of an MBS/CMO's average life, and its market price, depends on the type of MBS/CMO class purchased and interest rate movements. In general, as interest rates fall, prepayment speeds are likely to increase, thus shortening the MBS/CMO's average life and likely causing its market price to rise. Conversely, as interest rates rise, prepayment speeds are likely to decrease, thus lengthening average life and likely causing the MBS/CMO's market price to fall. Some MBS/CMOs may have "original issue discount" (OID). OID occurs if the MBS/CMO's original issue price is below its stated redemption price at maturity, and results in "imputed interest" that must be reported annually for tax purposes, resulting in a tax liability even though interest was not received. Investors are urged to consult their tax advisors for more information. Government agency backing applies only to the face value of the CMO and not to any premium paid.

The information and opinions in MS were prepared or are disseminated by MS & Co. LLC and/or MS C.T.V.M. S.A. and/or MS México, Casa de Bolsa, S.A. de C.V. and/or MS Canada Limited and/or MS & Co. International plc and/or MS Europe S.E. and/or RMB MS Proprietary Limited and/or MS MUFG Securities Co., Ltd. and/or MS Capital Group Japan Co., Ltd. and/or MS Asia Limited and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS) and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 24-0813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105), Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity ratin

[中间内容因长度限制已省略]

ia; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Raquel Kanner; Vishwanath Tirupattur.

© 2026 MS
"""
