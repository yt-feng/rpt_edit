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
June 21, 2026 06:00 AM GMT

# Sunday Start | What's Next in Global Macro

# New Chair, New Chapter

Kevin Warsh's first meeting as Fed Chair marked a new chapter. Chair Warsh intentionally gave little guidance on the path of monetary policy; he has said that reducing “forward guidance” is central to his philosophy. He highlighted important forthcoming changes, but as with the policy rate, he did not specify the likely path.

The market's expectations for a rate hike this year were reinforced by the statement and Warsh's press conference. The blunt statement that “[t]he Committee will deliver price stability” seems clear, but (again...by design) the path was not laid out. Before determining when the Fed will hike rates and by how much, consider the following. Chair Warsh did not write down his own projection for the policy rate. The median FOMC participant expects only one hike this year, but with the addition of that one dot, the median could have been no hikes.

Moreover, that policy path was plotted alongside a forecast of 3.3% core inflation for 2026. But the boost to prices from tariffs is largely complete, so we expect notable disinflation for the remainder of the year. Oil prices are sharply lower, so the risk of “second-round” inflation from energy seems to have receded markedly. The FOMC’s inflation forecast is plausible, but not the most likely. If inflation materially undershoots, the fact that the median participant expected to cut rates next year presents a puzzle. Why hike rates only once if inflation undershoots and you expect to cut rates anyway?

The task forces the Chair laid out represent bigger changes for the Fed. On the balance sheet, little guidance was given, but Warsh's advocacy for a smaller balance sheet is established. I have been part of Fed staff work groups laying out options for the implementation of policy in the past. There is a clear path to a notably lower balance sheet that could allay many, if not all, concerns of those who prefer the status quo. Simply halving the Treasury's account at the Fed would reduce the balance sheet by roughly a half trillion, with literally no effect on markets. Paying substantially less on some portion of reserves than on the reverse repo facility (and thereby Treasury bills) could reduce bank demand for reserves, so a smaller supply could still be “ample.” Changes to liquidity regulation would further dampen that demand. Ultimately, I suspect the balance sheet will decline by more than many expect, but I also suspect the market implications will be less important than most fear. Lower bank demand for reserves met by an increase in bills as Treasury refunds the debt the Fed sheds should have little net effect. The clear exception is if the Fed becomes an active seller of MBS.

Less clear are the implications of the task force on inflation. The Chair reaffirmed the 2% inflation target, but the TIPS market already confronts a basis between the PCE measure of inflation, which the Fed targets, and CPI. Could there be an additional disconnect? Will the study lead to moving the goal posts? We have few hints for now.

MS & CO. LLC

Seth B Carpenter

Chief Global Economist

Seth.Carpenter@morganstanley.com

+1 212 761-0370

The other notable change is communications. The statement was overhauled, much shorter, and rearranged. That change, however, is not unprecedented. Until 1994, the Fed did not issue post-meeting statements, and even once it started, it did not do so after every meeting. The length and content of the statement have evolved significantly since then, getting longer and then shorter, only to grow again. The reduction or elimination of “forward guidance” is also less momentous than it appears. Economists have long argued that its true value is at the effective lower bound. The shift may help communication, because while policymakers view the dot plot and their speeches as conditional on the data, to the extent markets take utterances as commitments, we get miscommunication.

How different will the Fed be a year from now? Very different, I suspect, in many aspects of the Chair's communications. I also suspect the size of balance sheet could be very different. But when it comes to monetary policy through rates, I am less convinced the change will be as stark.

Enjoy your Sunday.

Send Us Feedback

## What I'm Reading This Week

US Economics and Fixed Income Strategy: June FOMC Reaction: Hawkish Today, Reforms Tomorrow (18 Jun 2026)

U.S. Data Pulse: CPI: May CPI: Tariff push might be near completion (10 Jun 2026)

Global Technology: Chipflation – Navigating A Memory Crisis (2 Jun 2026)

Global Economic Briefing: Reshoring? Not Quite Yet (9 Jun 2026)

## What We Are Watching This Week

MONDAY, JUNE 22

Euro area consumer confidence: We expect consumer confidence to rebound a touch in June, at -18.5 from -19.0 previously, albeit still a low level.

## TUESDAY, JUNE 23

Euro area PMIs: We expect EA composite PMI to rebound to 50.2 in June from 48.5 in May. The data is collected in the second half of the month and is thus likely to show improved sentiment on the back of US-Iran agreement and the recent fall in oil prices.

Hungary Base Rate: We expect the NBH to ease its base rate by 25bp to 6% at its upcoming June core meeting. Further ahead, we see the policy rate falling to 5.50% in end-2026 and 4.50% in end-2027. While we see risks of a more front-loaded easing cycle, we believe the NBH would remain cautious. We expect it to retain its data-driven approach, given uncertainties around domestic fiscal and regulatory policy, and the outlook for external monetary conditions.

Argentina 1Q26 GDP: We forecast 1Q26 GDP growth at 1.9% y-o-y, mainly supported by exports.

US Factory surveys: After Empire State and Philadelphia Fed factory surveys, we are expecting the manufacturing ISM index rises to 54.3 from 54.0, suggesting continued momentum in manufacturing growth. The S&P measure is important to the forecast. Just as important will be the question of pass-through of fast-rising input prices to final prices. We've found the S&P prices received index to correlate better with core goods consumer inflation than other measures. So far, prices paid measures for May remained elevated, but the prices received indexes were less conclusive: The Empire measure remained high, but the Phila. Fed measure retreated.

## WEDNESDAY, JUNE 24

German ifo: We expect ifo business climate to move up to 85.3 in June from 84.9 in May, on the back of the agreement between the US and Iran.

US New home sales: The drop in new home sales last month surprised us. We expect a modest 1.3% m/m rise in May to a still low 630k. May inputs were mixed, with a pickup in homebuilder confidence and mortgage apps but a slight decline in starts. So far, real residential investment is tracking little changed (about a 0.5% q/q annual rate) in 2Q, reflecting weakness in new home sales and housing starts and some offset from existing home sales,

US Current account balance: A wider deficit in goods likely led the current account deficit up in 1Q. At 2.8% of GDP, it would be 0.4 pct pt wider than in 4Q but still much narrower than 3.7% in 2025, 4.0% in 2024, and 3.3% in 2023.

## THURSDAY, JUNE 25

Mexico Banxico Meeting: We expect Banxico to remain on hold and keep rates unchanged at 6.50%, while inflation risks still remain tilted to the upside.

Brazil IPCA-15: We expect June IPCA-15 at 0.38% m-o-m, driven by a decelerating but still resilient food inflation and lower fuel prices, partially offset by higher electricity tariffs.

US Personal Income and Spending: We expect real personal spending rose 0.3% m/m with goods up 0.7% and services up 0.2%. With this forecast, we track 2Q real consumption up 2.9% q/q saar. The May retail sales print was stronger than we expected. We continue to expect later drag on goods from the oil shock, but the data suggest upside risk. Nominal spending rises 0.8% m/m in May. We expect nominal personal income rose 0.4% m/m with labor compensation also up 0.4%. Real disposable personal income is down 0.1% m/m and the saving rate falls further to 2.4%.

US PCE Prices: We expect May core PCE inflation at 0.36% m/m and headline at 0.48% m/m. Including our forecast for historical revisions (Jan +3bp, and April -1bp), the 3-month and 6-month annualized core PCE pace as of April comes to 3.58% and 4.20% (vs. 3.74% and 3.83% in April). The y/y rate is expected to be 3.44% in May (vs 3.31% in April).

US Durable goods orders: Orders probably fell sharply in May because of a drop in aircraft orders. But we expect continued rapid increase in underlying orders, driven by decent ongoing increase in volume plus increased price pressures.

US Jobless claims: Claims have picked up over the past month. Levels are still low and layoffs limited. But they are signalling slightly faster layoffs and slower re-employment in June than in the prior several months and some modest slowing in payroll growth.

US GDP: We forecast a 0.1 pt downward revision to 1Q real consumption (to a 1.3% q/q annual rate) as prices are revised slightly higher. Headline GDP likely is again reported at a 1.6% q/q annual rate — not quite rounding down to a 1.5%.

## FRIDAY, JUNE 26

US Trade in goods: We forecast a widening deficit on increased consumer goods import volumes. Retail sales have been strong enough to suggest stronger.

US University of Michigan consumer sentiment: Our summary of long-run inflation expectations has moved up only little, in contrast to the surge in the Michigan measure. In the preliminary estimate for June, long-run inflation expectations in this survey retreated sharply to 3.4% from 3.9% in May.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS & Co. LLC and/or MS C.T.V.M. S.A. and/or MS México, Casa de Bolsa, S.A. de C.V. and/or MS Canada Limited and/or MS & Co. International plc and/or MS Europe S.E. and/or RMB MS Proprietary Limited and/or MS MUFG Securities Co., Ltd. and/or MS Capital Group Japan Co., Ltd. and/or MS Asia Limited and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS) and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 24-0813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105), Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Disclosures

MS is not acting as a municipal advisor and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of Section 975 of the Dodd-Frank Wall Street Reform and Consumer Protection Act.

MS does not provide individually tailored investment advice. MS has been prepared without regard to the circumstances and objectives of those who receive it. MS recommends that investors independently evaluate particular investments and strategies, and encourages investors to seek the advice of a financial adviser. The appropriateness of an investment or strategy will depend on an investor's circumstances and objectives. The securities, instruments, or strategies discussed in MS may not be suitable for all investors, and certain investors may not be eligible to purchase or participate in some or all of them. MS is not an offer to buy or sell or the solicitation of an offer to buy or sell any security/instrument or to participate in any particular trading strategy. The value of and income from your investments may vary because of changes in interest rates, foreign exchange rates, default rates, prepayment rates, securities/instruments prices, market indexes, operational or financial conditions of companies or other factors. There may be time limitations on the exercise of options or other rights in securities/instruments transactions. Past performance is not necessarily a guide to future performance. Estimates of future performance are based on assumptions that may not be realized. If provided, and unless otherwise stated, the closing price on the cover page is that of the primary exchange for the subject company's securities/instruments.

The fixed income research analysts, strategists or economists principally responsible for the preparation of MS have received compensation based upon various factors, including quality, accuracy and value of research, firm profitability or revenues (which include fixed income trading and capital markets profitability or revenues), client feedback and competitive factors. Fixed Income Research analysts', strategists' or economists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

With the exception of information regarding MS, MS is based on public information. MS makes every effort to use reliable, comprehensive information, but we make no representation that it is accurate or complete. We have no obligation to tell you when opinions or informa

[中间内容因长度限制已省略]

DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
