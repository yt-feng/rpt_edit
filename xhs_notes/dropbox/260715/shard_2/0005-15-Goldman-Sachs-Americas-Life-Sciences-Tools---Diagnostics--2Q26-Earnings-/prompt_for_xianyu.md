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
# Americas Life Sciences Tools & Diagnostics: 2Q26 Earnings Preview: GS Tools Tracker and China Stimulus Tracker Updates

## Executive Summary

Year to date, Tools saw underperformance versus the broader market (return of -9% vs S&P 500 +10%), as 1Q performance for several names came in line with guides that were previously expected to be conservative. The Tools space is yet again in a position where organic growth needs to show sequential improvement throughout the year in order to meet/beat full year guides for several names in our coverage. We continue to be focused on several factors which we believe could drive end market improvements and sequential growth including 1) CDMO demand driven by onshoring trends to offset tariff (TMO, A), 2) bioprocessing equipment which could potentially see an inflection late 2026/early 2027 (DHR), 3) respiratory testing headwinds rolling off in 2Q26 (DHR, WAT), 4) improved clinical stage biotech funding which could start to flow through to spending in 2H26 (TMO), 5) continued investment in downstream Pharma manufacturing (WAT, A, MTD), and 6) industrial strength driven by semiconductors and cyclical patterns (A, BRKR). We remain cautious on the potential recovery in US Academic & Government and while we are encouraged by recent strength in preclinical biotech funding, we believe this will take time to be reflected in spending patterns.

Evie Koslosky
+1(212)357-1694 | e.v.koslosky@gs.com
GS & Co. LLC

Grey Smith
+1(212)934-1193 | grey.smith@gs.com
GS & Co. LLC

Recent investor conversations revolved around the magnitude and timing of the ongoing recovery, where focus for the quarter is on management commentary of end market health and assessing if the current growth rates reflect a fundamentally broken long-term growth algorithm or a temporary post-pandemic aftermath. We continue to believe the current valuations represent attractive entry points for several names in our space as growth will likely accelerate from here, albeit at an uncertain pace. In this note, we update our GS Tools Tracker which observed a slight acceleration in growth in 2Q26 relative to 1Q26, and in a separate note we update our GS China Stimulus Tracker.

## Charts We Are Watching

Exhibit 1: Continued bifurcation of end market growth according to the GS Tools Tracker in 2Q26  
![](images/c79135063ffd11a795273c9b65ef8363c27ade25c4ac7a617198ba1b0e14eca0.jpg)  
Source: GS Global Investment Research

Exhibit 2: mAb Sales by volume tracking above average historical growth in recent months  
![](images/44544a3434376b849fd92dff7d32bdb39a4c43a261c3c3e195566ff5fc1f0f9b.jpg)  
KG = Kilograms  
Source: IQVIA, GS Global Investment Research

Exhibit 3: Preclinical Biotech VC Funding Accelerated in 2Q26
YoY Growth  
![](images/361bfcfeb9ec6f892529864145ad8990aaa73e0f11963e074f47f7bad91fba4e.jpg)  
Source: Biopharma Dive

Exhibit 4: Average Tools Multiples have Expanded Since 1Q Earnings
12 month Tools Group and S&P 500 EV/EBITDA  
![](images/881c0a485c0e8d05c8f47b3fc18d27b6d5409ab2e2e80cda6233f4fd22ea0376.jpg)  
Source: FactSet

## GS Tools Tracker Update

## What is the GS Tools Tracker?

The GS Tools Tracker is a proprietary market growth model which compiles 17 quarterly datasets in the 4 distinct Tools end markets (Biopharma, Industrial, Clinical Diagnostics, and Academic/Government), then weights the datasets according to their relevance to each end market, to help determine growth estimates by end market. It then weights the end markets growth by Tools aggregate exposure to provide a total market growth estimate on a quarterly basis. The growth fluctuates quarter to quarter, in line with Tools company revenue growth, but has a long term average growth rate of \~5%, in line with market growth rate estimates from management teams in the space. Generally, Biopharma is the fastest growing end market in the Tool Tracker with a long term average growth rate in the HSD range, with Industrial at LSD, Clinical Dx at LSD and academic at MSD. We acknowledge certain dynamics will not be accounted for in the tracker including ex-US academic funding, clinical diagnostic menu expansion/pricing, and biosimilar drug volume uplift, but we view the tracker as a tool to help orient investors and provide a dashboard-type view of the market as a whole. Overall the GS Tools Tracker has shown an 86% correlation with average Tools revenue growth and is correct 80% of quarters in determining acceleration or deceleration in growth.

For more information on our GS Tools Tracker and our previous update, please see our Life Science Tools initiation note here.

Exhibit 5: GS Tools Tracker vs Average Organic Growth  
![](images/4a4bb677486b2ad4c9a3bff406817d4738b55a4284b81324f6910c4b25f5f1da.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 6: End Market Data Set Composition

<table><tr><td>End Market</td><td>Data Set</td></tr><tr><td>Biopharma</td><td>Pharma R&amp;DBiotech R&amp;DCchina R&amp;DCchina CapexPharma CapexBiotech CapexBiotech IPOBiotech VC funding</td></tr><tr><td colspan="2"></td></tr><tr><td>Academic/Gov</td><td>National Institutes of Health OutlaysNational Science Foundation Outlays</td></tr></table>

Source: Company data, GS Global Investment Research

<table><tr><td>End Market</td><td>Data Set</td></tr><tr><td>Industrial</td><td>New orders of durable goodsPMISemi CapexChina GDP</td></tr><tr><td colspan="2"></td></tr><tr><td>Clinical Dx</td><td>Hospital AdmissionsLH Dx volumeRoutine Testing Volumes</td></tr></table>

Exhibit 7: Tools Tracker Biopharma Growth
4Q Rolling Average  
![](images/d8e31e5290d9e3c39eac7467fad54da669a7b654947478d4dfb839322aac0c39.jpg)  
Source: GS Global Investment Research

Exhibit 8: Tools Tracker Industrial Growth
4Q Rolling Average  
![](images/b3bf26fb7ce6aa25765fd9ac4a850ddc72c6879e2c7a6ecc273d7a9ad5c0541a.jpg)  
Source: GS Global Investment Research

Exhibit 9: Tools Tracker Clinical Diagnostics Growth
4Q Rolling Average  
![](images/f82353bd6284add028caa4528db74059f4d91f2955a938d079aa5e8592b225f9.jpg)  
Source: GS Global Investment Research

Exhibit 10: Tools Tracker Academic & Government Growth
4Q Rolling Average  
![](images/c04e6432efa94e5b68721eb72824a078e96fecd16ddcdcf152c42c8bbda487bb.jpg)  
Source: GS Global Investment Research

## GS Tools Tracker 2Q26 Update

The GS Tools Tracker compiles 17 distinct data sets to help inform our market growth estimates both historically and one-quarter forward. We update our data as of the date of this report and include key insights within each end market below. We note that some datasets are based on GSe or have not yet released data for the last month of the quarter, so our market growth estimate for 2Q26 may be subject to change.

Broadly this quarter we observed a slight acceleration in underlying market data trends in 2Q26 over 1Q26, largely driven by step-ups in both the Industrial and Academic (albeit still negative) end markets with clinical roughly flat and biopharma down \~2% sequentially, off a strong 1Q. While this is largely in line with guidance set forth by several companies in the space, which called for acceleration in growth in 2Q26, we view the two quarters in a row of our end market tracker signaling an acceleration as an encouraging sign for the Tools companies as we enter the second half of 2026 to drive organic growth profiles. While idiosyncratic factors remain for each company, the health in the underlying end markets seem to continue inching higher. For more detail, please see the end market takeaways below, and reach out to our team for underlying data.

Biopharma: According to our tracker, 2Q showed low double digit growth in the Biopharma end market, driven by broad based strength in the majority of datasets we track, although decelerating slightly against a strong 1Q26. The acceleration was led by biotech R&D, China Capex, and Biotech Capex. We note our Biotech VC and IPO data remained elevated for the third quarter in a row which according to our estimates, takes \~1 year+ to show up in biotech capex spending, aligning with recent management commentary (Exhibit 11).

Exhibit 11: Biotech Capex tends to lag funding by >1 year
4Q Rolling Average  
![](images/22b795848c2b9dea660bd1184171085b8aba01e22511c90f48699dd10ac10122.jpg)  
Source: GS Global Investment Research, Pitchbook, Dealogic

Industrial: The industrial end market grew at the high end of high single digits according to our tracker, accelerating above 2Q and continued to remain well above the historic average of \~LSD%. The \~3pt acceleration in the end market was largely driven by a sequential step up in PMI and semi capex offset by weaker new orders of durable goods. We continue to view the industrial end market as favorable for our Tools coverage given the cyclical upswing, however call out recent macro uncertainty as a key risk. We believe, according to historical patterns, there is still room left to grow in the current cycle as we have not seen the industrial growth rate reach mid-teens which is the high water mark informed by historical patterns. We call out Agilent's CAM segment as a key beneficiary, which has tracked closely with our Industrial tracker historically.

Clinical Diagnostics: Clinical accelerated in the quarter vs 1Q and returned to slightly positive growth driven by sustained lower routine testing volumes while hospital admissions accelerated by \~1ppt. We note that our clinical tracker is largely US based, and thus reimbursement dynamics in China would not be reflected in this growth estimate.

Academic/Gov: According to our tracker, the academic end market remains well below historic averages, with funding outlays for the National Science Foundation (NSF) posting negative growth for the 4th quarter in a row, while National Institutes of Health (NIH) posted a slight acceleration in outlays off 1Q but still in the LSD growth range. We note our data in this end market is US based, and China stimulus/European dynamics would not be included. While our tracker is focused on funding outlays, we have observed continued uncertainty surrounding academic funding as many researchers face multi-year grant dynamics, degradation in PhD

admissions, and continuing conversations centering around hesitancy to spend funding on larger capital equipment, despite funding starting to come through.

Overall, this led to an acceleration in growth in 2Q26 over 1Q26, and while we recognize there are certain dynamics that the Tools Tracker will not pick up on, we view this as an encouraging sign for the Tools end markets, especially given investor debate on the ability for tools companies to durably reaccelerate growth into the 2H and exiting 2026. Macro related headwinds, including those in the Middle East could be a risk to our data, given we believe most companies in our coverage have \~LSD exposure to the region, which is not well-represented in our Tools Tracker.

## GS China Stimulus Tracker

## What is the GS China Stimulus Tracker?

We track China stimulus orders for TMO, DHR, A, WAT, and BRKR for instruments including (but not limited to) Liquid Chromatography, Gas Chromatography, Mass Spectrometry. Since the launch of China's equipment renewal stimulus in March 2024, we have tracked over 1,100 instrument orders across our China exposed instrument companies under coverage and include our most recent update to our data below.

For more information on our China Stimulus Tracker and the 2Q26 update, see our separate note here.

## GS China Stimulus Tracker 2Q26 Update

In 2Q26, leveraging our China equipment renewal bidding tracker, we tracked 65 total orders, a decline of (-57%) YoY across TMO, DHR, A (3Q26 for A), WAT, and BRKR. We think BRKR should be the most insulated from the lack of broader stimulus-related order growth this quarter as 2Q26 orders show \~55% YoY growth versus other Tools companies being down. Please see a more detailed breakdown of our data below:

## Charts:

Exhibit 12: Waters (WAT) instrument split by quarter  
![](images/3fe39b101f4aefee7bb6501acbc4687ca10e03778e1ca2bd3110434f7756b4a2.jpg)  
Source: Data compiled by GS Global Investment Research, ChinaBidding

Exhibit 13: Agilent (A) instrument split by quarter  
![](images/6d5ad639fdfe463eed0f5606f69967c37ed2f9a36f866f63eb433b2eb4e22774.jpg)  
\*3Q26 QTD represents May 1, 2026 - July 5, 2026  
Source: Data compiled by GS Global Investment Research, ChinaBidding

Exhibit 14: Thermo Fisher Scientific (TMO) instrument split by quarter  
![](images/acdf3b13012aea1a9cfc271df6e146c14d4ab37132b15b53c31dfc42ae29bc44.jpg)  
Source: Data compiled by GS Global Investment Research, ChinaBidding

Exhibit 15: Danaher (DHR) instrument split by quarter  
![](images/685212a4ca5b3efb7e4fd1279846423551389c8f988e44ef31187c75f1656799.jpg)  
Source: Data compiled by GS Global Investment Research, ChinaBidding

Exhibit 16: Bruker (BRKR) instrument split by quarter  
![](images/967af4befc64444bca9bca82078c6bb681cf9c0e93a902812698592364e7360c.jpg)  
Source: Data compiled by GS Global Investment Research, ChinaBidding

Exhibit 17: 2Q26 vs. 2Q25 tenders awarded by company  
![](images/1d42e51bb25ee68b4ac2dd6af63afdb85a82340c31fc82309923b3fb4b371037.jpg)  
\*A 3Q26E (reflects May 1, 2026 - July 5, 2026) / 3Q25A  
Source: Data compiled by GS Global Investment Research

Exhibit 18: 1Q26 vs. 1Q25 tenders awarded by company  
![](images/6ef14c6adb4386799d5e0b993957f918b5064a4707cd8be200055b5792884d78.jpg)  
\*A 2Q26E (reflects February 1st - April 5th) / 2Q25A  
Source: Data compiled by GS Global Investment Research

Exhibit 19: 4Q25 vs. 4Q24 tenders awarded by company  
![](images/9ec7ebca501a26255fc9e83149f9edfbe2a75f67dd095e6a5d89c4e72e5745fb.jpg)  
\*A 1Q26A (reflects November 1st - December 31st) / 1Q25A  
Source: Data compiled by GS Global Investment Research, ChinaBidding

Exhibit 20: 3Q25 vs. 3Q24 tenders awarded by company  
![](images/79f14de6f67b5c21dd4db2c005f36bd7f5bcf8f602bb6cc50a0d39cf3eb312e8.jpg)  
\*A 4Q25A/4Q24A  
Source: Data compiled by GS Global Investment Research, ChinaBidding

Exhibit 21: Mass spectrometer imports into China  
![](images/d24cf9ba924a0f87deafee99ca98bbe35b886ed320683434a81099523dc4305c.jpg)  
Source: Data compiled by GS Global Investment Research, ChinaBidding

Exhibit 22: Liquid chromatography imports into China  
![](images/8fba9eda28be7b8b75f8054034c58f8e188ac33741b9b15e3c6549c27baa24e4.jpg)  
Source: Data compiled by GS Global Investment Research, ChinaBidding

Life Science Tools: 2Q26 earnings calendar and single stock outlooks

Exhibit 23: Upcoming Earnings Calendar

<table><tr><td>Company</td><td>Date</td></tr><tr><td>A*</td><td>TBA</td></tr><tr><td>BRKR</td><td>TBA</td></tr><tr><td>DHR</td><td>7/21/2026</td></tr><tr><td>MTD</td><td>7/30/2026</td></tr><tr><td>RVTY</td><td>8/4/2026</td></tr><tr><td>TMO</td><td>7/23/2026</td></tr><tr><td>WAT</td><td>8/4/2026</td></tr></table>

\*Agilent reporting 3Q26

Source: Company data, GS Global Investment Research

Life Science Tools Previews

## Thermo Fisher Scientific (TMO) — Buy

For 2Q26, we expect top line organic growth of 3.1% with revenues/EPS of \$11.73bn/\$5.70, compared to FactSet consensus of \$11.71bn/\$5.72.

## Quarter

Guidance: TMO reiterated its 2026 organic revenue growth guidance of 3-4% and raised its adj operating margin expansion to 70 bps up from 50bps. The company continues to expect 2026-2027 organic growth of 3-6%. For 2Q26, TMO set expectations for organic growth at \~3%, which includes steady underlying end market trends plus the normalization of prior-quarter headwinds (selling days, CDMO contract phasing). YoY growth is expected by management to improve sequentially as the \~100 bps headwind from one less selling day in 1Q does not

repeat, and Pharma Services (CDMO) revenue phasing becomes less of a d

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
