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
## Global Views: Renewed Escalation vs. Lower Inflation

1. The renewed escalation in the Middle East has pushed oil prices back up, with the Brent futures path above our forecasts of \$80/barrel in 2026Q4 and \$75/barrel in 2027. The risks to these forecasts are two-sided but on net tilted upward. The swift recovery in flows prior to the most recent escalation shows that Gulf exports can rebound quickly when given a chance, which means that prices could fall sharply if the latest escalation subsides. But more attacks on tankers and Middle East infrastructure could push prices back to the \$100+ range that prevailed for much of the hot phase of the conflict.

Jan Hatzius  
+1(212)902-0394 | jan.hatzius@gs.com  
GS & Co. LLC

Exhibit 1: Oil Price Risks Are Tilted to the Upside  
![](images/9f19389d5cb8d9a490f5e662786651786a403b3a736f4fc3f215f258fd6ee175.jpg)  
Source: Bloomberg, GS Global Investment Research

2. We estimate that the US economy has grown at a trend-like $2 \frac{1}{4}\%$ pace in H1, as lower taxes on households and businesses have offset the impact of higher gas prices on the consumer. However, H2 is likely to look softer because we still expect a slowdown in real disposable cash flow to weigh on consumer spending, especially if gas prices stay high. One additional downside risk is a slowdown in the AI boom, not so much because of the direct effects on US GDP growth (which are relatively small) but because of the nearly $\frac{1}{2}$ pp contribution from the equity wealth effect to consumer spending growth.

Exhibit 2: We Still Expect US Consumer Spending to Slow in H2  
![](images/376dde1c1c377192a1bc28943e5788f1c218e44917d85192e6da186879a81e42.jpg)  
\*Both series adjusted for AI-related mismeasurement.  
\*\*Real DPI with taxes converted from accrual to cash.  
Source: GS Global Investment Research

![](images/51398969af86f1346621da0511aff37a168bb4a632488c5631883479c0c210d4.jpg)

3. The weaker-than-expected June employment report has brought our estimate of underlying US job growth down to 73k, from 130k a month earlier. And while we would not ignore a move in the unemployment rate given its proven value as a cyclical indicator, we expect the latest drop to $4.2\%$ to reverse in coming months because it was driven by a suspiciously large drop in labor force participation. Moreover, other signals such as the ongoing weakness in household job market assessments as well as depressed flows both into and out of employment still suggest that the labor market remains a tad cooler than normal. This chimes with the slowdown in our GS wage tracker to $3.4\%$ , below the $4\%$ pace that would be consistent with a $2\%$ inflation target assuming a $2\%$ productivity trend.

Exhibit 3: A Well-Balanced Labor Market  
![](images/5850b6baae57a671c721adc53d456f1d0569b610ece6e4ac40c66fa4ceb83736.jpg)  
\* We estimate underlying trend job growth as 0.75\*3-month average payroll growth + 0.25\*9-month average household employment growth; see our report "How to Read the Employment Report."

![](images/89ae05193c0da254b1258f9fa5cb3f46ae80017412091212e6cc74b4143acdc5.jpg)  
Source: US Bureau of Labor Statistics, Haver Analytics, GS Global Investment Research

4. The US inflation news has improved. We estimate that core PCE rose a benign 0.18% month-on-month and 3.3% year-on-year in June, with other measures such as core CPI (-0.02%/2.6%) and trimmed-mean PCE (0.14%/2.3%) running lower. Moreover, changes to the measurement of prices for software and accessories, portfolio management, and legal services are likely to subtract a net 0.2pp from the year-on-year rate in September. (Even with these changes, the contribution from software and accessories remains overstated because these categories are not quality-adjusted and their weight in core PCE looks excessive relative to either core CPI or price indices in other countries. The BEA's continued practice of measuring portfolio management fees in terms of dollars rather than basis points—which creates a direct link with equity prices—is arguably also a source of overstatement.) We expect year-on-year core PCE inflation to slow to near 2% in 2027, driven largely by reduced contributions from software and accessories, energy pass-through, and tariff pass-through.

Exhibit 4: Temporary Drivers of Core PCE Inflation Are Likely to Subside Next Year  
![](images/295dfd2be647552e9754da6b2cab6cc29da37b6edc7285fb93ade9055a6a562b.jpg)  
Source: Haver Analytics, GS Global Investment Research

5. Amidst the higher US core PCE numbers this year, it is worth noting how favorable the inflation news has been almost everywhere else. Core inflation in the G10 ex-US—using either the traditional ex food and energy definition or trimmed-mean measures—has continued to trend down this year and now stands at 2.1%, despite the energy price surge in March and April. This means US core PCE is an outlier to the high side, not just relative to alternative measures of underlying US inflation such as core CPI or trimmed-mean PCE but also relative to other economies with similar levels of resource utilization. This reinforces our view that core PCE overstates true underlying inflation, in part because of mismeasurement and in part because of idiosyncratic US shocks such as tariffs.

Exhibit 5: G10 Core Inflation Looks Benign (Except for US Core PCE)  
![](images/2dc110f930dc807b247de7727261590ee6d4184f6dbb09cb502215bc4767b296.jpg)  
\*\*G10 ex-US is a GDP-weighted average of CPI ex food and energy in Canada, CPI ex fresh food and energy in Japan and CPI ex food, energy, alcohol and tobacco otherwise. Note: June values are predicted using realized data for the US, Euro area, Sweden, Norway and Switzerland.  
Source: Haver Analytics, GS Global Investment Research

6. The better inflation news has effectively extinguished whatever chance there was of a rate hike at the July 28-29 FOMC meeting. Hikes at subsequent meetings are possible but would probably require significantly higher inflation and/or lower unemployment than we expect. The broader question is how the FOMC will steer market expectations whenever policy does need to be adjusted in either direction, especially if there is no longer a dot plot (or the move comes at an off-cycle meeting). To keep control of the narrative and prevent financial conditions from overshooting, we think Chairman Warsh will have little choice but to explain the committee's economic outlook and reaction function in much greater detail than in his first press conference and congressional testimony.

Exhibit 6: Our Fed Call Remains Below Market Pricing  
![](images/6e85a5a96f81558a8897f0012dd6a13ebac6212cf8f4316a39ed0fe753333c8b.jpg)  
Source: Bloomberg, GS Global Investment Research

7. The rebound in energy prices probably won't cause the ECB to hike on July 23, but it has made us more confident in our call for a second hike in September. Beyond that, however, our views diverge from market pricing as we expect the Governing Council to hold off on additional hikes (and return the deposit rate to $2\%$ in 2027). Across the Channel, we are even further below market pricing as we expect no BoE hikes this year followed by three 25bp cuts in 2027. This assumes that incoming Prime Minister Burnham will make good on his promise to stick to the fiscal rules despite tight constraints resulting from the tax pledges in the Labour Party's manifesto as well as upward pressure on departmental day-to-day spending relative to current plans.

Exhibit 7: We Have Dovish Views on the ECB and Particularly the BoE  
![](images/7791c16efb00cac60bfebe92f2f46600ae3813c041e5cc4d81d07f387156c1cf.jpg)  
Source: Bloomberg, GS Global Investment Research

8. The lower-than-expected $4.3\%$ Q2 GDP print confirms that growth in China has slowed this year. Underneath the headlines, activity remains highly bifurcated, with strength in export volumes and industrial production but continued weakness in import volumes, housing, and consumer spending. We expect policymakers to step up their easing rhetoric in the July Politburo meeting and draw on remaining fiscal buffers quickly to stabilize investment and growth. But our full-year 2026 growth estimate has drifted down to $4.6\%$ and the dependence on exports means that China is vulnerable to any renewed global growth shocks from the Middle East or elsewhere.

![](images/c20c510ca29a6c16d2333a59839168dbff6ea1b6a34f71d8e03ee577d22ee68a.jpg)  
Exhibit 8: Chinese Export Volumes Surge, But Imports and Retail Sales Stagnate  
Source: China General Administration of Customs, China National Bureau of Statistics, Haver Analytics, GS Global Investment Research

9. Although the equal-weight S&P 500 has made new highs amidst a strong start to the Q2 earnings season, a pullback in the AI trade and Middle East escalation have weighed on most cap-weighted indices. While our economic view of AI remains optimistic, we think markets are now ahead of the macro from a valuation perspective. Our equity strategists therefore recommend three themes—1) firms delivering consumer experiences, 2) firms with unusually strong sustained earnings growth, ROE and balance sheets, and 3) M&A candidates—to ride out the near-term risks. Our rates strategists think markets price too much tightening but don’t see this changing as long as Middle East escalation risks remain top of mind. Our currency strategists view the current environment as favorable for carry strategies but also expect the CNY to continue appreciating. Our credit strategists continue to expect some modest widening in spreads, due in part to the wave of AI-related debt issuance that will need to be absorbed across a range of markets. And beyond energy, our commodity strategists argue that the recent reacceleration in central bank purchases should help gold prices rebound, although they acknowledge the near-term risks from energy and rates markets.

## Jan Hatzius

## Disclosure Appendix

## Reg AC

I, Jan Hatzius, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Jan Hatzius GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Registration granted by SEBI and certification from NISM in no

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
