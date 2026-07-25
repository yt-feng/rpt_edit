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
# Energy, Utilities & Mining Pulse: Investors Asking: Where Do We See the Most Positive/Negative 2027 Consensus Revisions?

As exemplified by the sharp outperformance of Refiners compared to Natural Gas this year, Natural Resources equities generally trade with a high correlation to forward consensus revisions. Accordingly, we ask our senior analyst team to identify one Buy-rated stock where there is upside to 2027 FactSet consensus EPS/EBITDA and one Neutral/Sell rated stock where there is downside to 2027 FactSet consensus EPS/EBITDA.

Stocks where we are above consensus: MPC, TLN, LB, SHLS, and NUE

Stocks where we are below consensus: APA, CEG, CQP, SEDG, and CLF

## Oil & Gas:

Among Integrated Oil & Refiners, we highlight Marathon Petroleum Corp. (MPC) where we see \~7% upside to consensus EPS estimates in 2027. As highlighted in our recent top picks across Natural Resources report, our constructive view is driven by the company's exposure to the structurally tighter PADD 5 environment, growing export optionality on the Gulf Coast, low-cost operations, and growing midstream earnings contributions. In addition to the robust refining backdrop, we highlight the company's yield flexibility projects, as well as a continued focus on strong operational execution. Given these considerations, we believe the company is well positioned to generate strong cash flow, ultimately supporting an attractive capital return yield and per share profitability. We note on our updated estimates, we see the stock trading at a \~12%/\~9% FCF yield in 2026/2027.

For a stock where we are more than 5% below consensus on 2027 EBITDA, we flag APA as a Sell-rated stock within our E&P coverage where our estimates for 2027 EBITDA are 6% below consensus. We seek more clarity around the company's outlook for its net gain on oil and gas purchases and sales in 2027+, as we have seen local Waha pricing tighten relative to Gulf Coast natural gas pricing. On the future outlook for Waha pricing, we continue to seek more clarity on timelines regarding new Permian takeaway pipeline capacity coming online in 2H26/2027. Our lower estimates relative to consensus are also impacted by our mid-cycle Brent oil price estimate of \$75/bbl in 2027, which is \~2% lower than the consensus Brent oil price estimate for APA. Following APA's year-to-date outperformance among our international/diversified E&P coverage, we see 10% downside to shares at current levels and a 10% FCF yield on 2027 estimates relative to peers at 11% (peers include OXY, MUR, TALO).

Neil Mehta
+1(212)357-4042 | neil.mehta@gs.com
GS & Co. LLC

Brian Lee, CFA
+1(917)343-3110 | brian.k.lee@gs.com
GS & Co. LLC

John Mackay
+1(212)357-5379 |
john.mackay@gs.com
GS & Co. LLC

Carly Davenport
+1(212)357-1914 |
carly.davenport@gs.com
GS & Co. LLC

Nick Cash
+1(212)357-6372 | nick.cash@gs.com
GS & Co. LLC

Alexa Petrick
+1(917)343-9472 |
alexa.petrick@gs.com
GS & Co. LLC

Olivia Foster
+1(801)212-7314 | olivia.foster@gs.com
GS & Co. LLC

## Utilities:

Among Buy-rated stocks in power/utilities, we see the most upside consensus risk to Talen (TLN). Here, we see 7% upside to consensus EBITDA estimates for 2027. This is driven by (1) recently completed M&A and execution on asset integration/performance, and (2) upside to power prices in 2027 where the forward curve has recently started to firm to the mid \$60s/MWh range across nodes in PJM. We believe if power prices continue to firm, or spark spreads otherwise expand, there could be further upside from running marginal units more to capture the upside. More broadly, we see potential catalysts for shares from improved regulatory clarity in PJM, where the RBP filing is expected by the end of the month, as well as incremental large load PPA signings. We also see valuation as attractive with shares trading at a 10% FCF yield on our 2027 numbers.

For a Neutral/Sell rated stock where we see downside to 2027 consensus estimates, we would highlight Neutral rated CEG, where we are 2% below consensus EBITDA. We believe this is driven by slightly softer Texas power prices vs. PJM, as well as higher fuel costs and O&M expenses, which could be attributed to stronger synergy realizations from the Calpine transaction being priced into consensus estimates. Our Neutral view on CEG is predicated on less leverage to EBITDA upside from incremental PPAs and valuation despite a strong fundamental business highly levered to nuclear power assets.

## Midstream:

We highlight LB as the stock with the most significant upside to 2027 consensus revisions, driven by strong produced water growth and commercial momentum. We forecast +41% annual EBITDA growth for 2027 (vs. 33% for 2026) and up +7% vs. consensus, underpinned by ramping minimum volume commitment (MVC) volumes from affiliate WBI’s kraken and Speedway I pipelines – with management guiding to Speedway I online by mid-2026 and ramping through 2027. Our model also assumes robust third-party volume growth and a broader pick up in Permian produced water activity. Beyond water, we expect solid organic growth from commercial execution across both legacy and newly acquired acreage. We see this support revenue per acre growth from \$696/acre in 2026 to \$921/acre in 2027, though still well below LB’s \$1,159/acre average on its pre-2024/ legacy vintage. Additional upside risk to our estimates could come from faster commercial conversion and stronger Speedway I volumes, especially as WBI’s commercial progress on Speedway Phase II signals incremental demand that can be absorbed by Speedway I’s open capacity (ahead of Speedway II in-service). Overall, we expect further insight into customer project ramp timing and the ability to increase its revenue accretion support upward estimate revisions from here.

We flag CQP as a Sell-rated stock where we see -4% downside to 2027 consensus EBITDA estimates. We estimate EBITDA will be down 8% YoY, reflecting lower blended margins across the Sabine Pass (SPL) footprint as well as higher sequential maintenance activities. On the former, we expect a larger portion of SPL volumes in 2027 to be sold under long-term sale-and-purchase agreements (largely due to contracts startups at CMI throughout 2026 tied to the Corpus Christi Stage 3 project) which brings the blended EBITDA margin per volume lower YoY. On the latter, while we are still awaiting details on the timing of the next major maintenance turnarounds, our model contemplates a turnaround on Sabine Pass Trains 5 and 6 in 2027, resulting in higher opex and lower volumes YoY. Risks to our estimate include the timing of major

maintenance, better than expected production at SPL, and/or better than expected optimization upstream and downstream of CQP's footprint.

## Clean Technology:

We highlight SHLS as a Buy-rated stock that maintains more than 5% upside to 2027 consensus EPS. In particular, our revenue and EBITDA forecasts remain 1% and 5% above FactSet consensus estimates, respectively, while our adj. EPS forecast of \$0.60 is 17% above consensus at \$0.52. We highlight that our 2027 EBITDA margins of 22.2% remain \~75bps above consensus, and view some discrepancies in interest/other expenses as driving further separation from our EPS forecast. We highlight that SHLS anticipates delivering \$628mn over the next four quarters, up from \$603mn at the end of 2025, and see the potential for management to raise the low-end of its 2026 revenue guidance, which would be supportive of future revenue growth potential. We believe the improvement in revenue, which is being further supported by continued traction expanding its product portfolio and entering new geographies, can drive some margin expansion from economies of scale. Importantly, our \~200bps yoy adj. EBITDA margin expansion in 2027 is only \~30bps above consensus forecasts.

We point to SEDG as a Sell-rated stock that has more than 5% downside to 2027 consensus EPS. We note that our 2027 adj. EPS of \$1.10 remains 30% below consensus at \$1.57. Importantly, our 2027 revenue forecast is \~3% below consensus, and recent industry data has suggested that SEDG has lost some inverter market share in the US as a result of RUN shifting away from its affiliate channel, and two large installers that were heavily exposed to SEDG encountering some operational issues, including the bankruptcy of Freedom Forever. We attribute most of the delta on EPS as a result of our higher opex forecast, as consensus anticipates opex declining by \~11% yoy in 2026 and remaining flat in 2027, as compared to our view where opex declines by \~7% in 2026 and increases by 2% yoy in 2027 to support the continued revenue growth and new product launches such as its solid state transformer product. In aggregated, we believe estimates remain elevated and anticipate will contract over the near-term.

## Metals & Mining:

We highlight NUE as a Buy-rated stock that has \~4% upside vs. 2027 consensus EBITDA. Within the steel commodity and macro backdrop, we are more bullish than consensus with mid-cycle HRC prices of \$1,000 vs. Visible Alpha consensus of \$950. Our upside to consensus estimates includes higher commodity prices, muted scrap costs and higher volumes within the mills segment being slightly offset by start-up costs associated with the West Virginia mill which is set to begin ramping production in 2027 which is set to have a higher value-added product mix. Furthermore, we believe incremental upside will be driven by plate prices which we believe will remain tighter for longer compared to HRC prices. Lastly, we believe there is incremental upside NUE's towers and structures businesses which will have three facilities producing by the end of 2027. Despite guidance of \~\$150mn across the three facilities running at mid-teens margins, we believe there is incremental margin capture for the towers and structures business as NUE will be vertically integrated compared to competitors that import tariffed product and achieve high-teens margins. As a result, we believe NUE can achieve towers and structures margins in the mid-20s.

We flag CLF as a stock where we are (4%) below consensus on 2027 EBITDA. Despite the positive rate of change on commodity increases, CLF maintains a large portion of fixed price contracts which only reset between 1-3 years. Furthermore, CLF has a large, fixed cost basis as a blast furnace operator. As a result, the company is less exposed to the pricing leverage other mills across our coverage experience while also having a higher cost basis. Additionally, given the large automotive exposure, we believe inflation, higher rates and lower consumer sentiment could weight on US automotive production, which has already been depressed. As a result, volume upside may be limited in 2027 as well. Furthermore, we believe the chunkier cost-cutting initiatives that have been undertaken over the past 3-4 years have likely been exhausted, resulting in improvements to cost profile likely being limited.

## Editor's Choice Charts

Exhibit 1: Energy, Utilities & Mining sub-sector performance
Past 90 days (4/23/2026-7/22/2026)

![](images/546589ea7ae447e1bf03af349054b4d1756d0dbdd5bbb8d18a4dafc5477d2757.jpg)  
Source: FactSet, GS Global Investment Research

Exhibit 2: We believe E&Ps are reflecting a cost of capital above 10%  
![](images/953bf64dc04023e80e7ed7d91794e14b8769fc931879b5d562426f2090e3d962.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 3: Combined Oil Flows from Saudi Arabia and Sudan via Bab-al-Mandab Rose to 4mb/d in 2026Q2 (Amid Redirection Mostly via the East-West Pipeline and the Yanbu Port)  
![](images/4f65060372123e439742bbee41a5a213a8600c11c77880370db55f1e52132567.jpg)  
In a scenario with Hormuz, Bab-al-Mandab, and Suez shipping frictions; includes Saudi Arabia and Sudan.  
Source: Kpler, GS Global Investment Research

Exhibit 4: CPC Oil Exports Appear to Decline Following Strikes Amid Russia-Ukraine Escalation  
![](images/7ed3ae5a616479b1983781a6811235073ed31fba466dd5d25a771523461679e5.jpg)  
The Caspian Pipeline Consortium (CPC) transports Kazakh and Russian oil to Russia's Novorossiysk port, from where it is exported to the rest of the world. The CPC Terminal is the loading point at the port for this oil.  
Source: Kpler, GS Global Investment Research

## Sector in Context

Exhibit 5: Valuations of E&P stocks reflect WTI oil prices slightly below the five-year strip Historical WTI price implied in covered E&Ps and forward oil futures, \$/bbl

![](images/2a9f27addbb92fdf4b0d08aaa01ed63cbb209c590cde1b3e90dbc35e56123461.jpg)  
Source: FactSet, GS Global Investment Research

Exhibit 6: Gas-focused E&Ps are broadly implying \~\$3.55/MMBtu long-term gas price vs. our mid-cycle view of \$3.50/MMBtu, 2026/2027/2028 gas futures at \~\$3.56/\$3.36/\$3.63 per MMBtu

Henry Hub gas price implied by our FCF Yield-analysis of covered gas producers, vs. 2026/2027/2028
Henry Hub gas futures

![](images/06d9060da4a15d6ea679f15fbf0755c4f72cc7518a0c1aa49b24e7fb5d0ee3da.jpg)  
Source: FactSet, GS Global Investment Research

Exhibit 7: Historically, Utilities trade at a P/E multiple premium to the S&P when the 10-year UST remains below \~3%, however, the relationship weakens in times of negative real rates

Utility P/E multiple premium / discount to the S&P in different UST 10-year yield environments

![](images/a9b5918d8a43b92fab99436f70c68f88576e47d48167ae2e200bed2b71cf3802.jpg)  
Source: Company data, GS Global Investment Research

## Conversations we are having with investors

## E&P

MGY. MGY has been a stock in focus this week with investors following the company's recently announced plans on July 20 to acquire WildFire Energy, LLC for \$4.06 bn. Investor conversations have centered around the outlook for the pro forma accretion potential stemming from the pending WildFire transaction, as well as MGY's outlook on taking on additional debt following the company's proposed offering of \$500 mn Senior Notes on July 22. Those more constructive on MGY note the potential operational efficiencies the company can drive for the pro forma business, including the potential for extending lateral lengths toward the 10,000-15,000 ft range discussed by management. Those more cautious on MGY have noted the recent \$1.1 bn equity offering pricing announced on July 21 and seek more clarity on the company's outlook to optimize the pro forma cost structure. Investor conversations on MGY have also focused on the company's outlook for a pro forma oil cut of \~54%, as many investors seek more clarity on the potential for realized oil pricing tailwinds from legacy WildFire assets' exposure to incremental Gulf Coast liquids pricing.

EQT. Following the company's reporting of 2Q26 earnings on July 21, EQT has been a name in focus this week with investors following outperformance on 2Q26 production. The company reported total production of 6.97 Bcfe/d for the quarter relative to FactSet consensus at 6.65 Bcfe/d. Investors have noted the company's commentary around compression projects driving a shallower base decline rate, as many investors begin to focus on the potential for incremental efficiencies to the maintenance capital program in 2027+ as a result of EQT's organic growth projects. Those more constructive on EQT note the company's announcements for incremental power and LNG agreements alongside 2Q26 earnings. On the 10-year power supply deal with CPV Shay, investors have been focused on the premium pricing structure linked to PJM pricing as well as the potential for a 2031 start-up as was messaged by EQT. On the 5-year LNG offtake agreement with an undisclosed large integrated Asian energy company, investors have noted EQT's expectation for a \$45 mn uplift to 2028 FCF at recent strip pricing. Given the ongoing pressure in the U

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
