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
# Global Markets Daily: Hyperscaler Credit vs. Equity: More Issuance, a Higher Beta, and a Different Focus on Cash Flow

\- Heavy AI-related capex has reshaped how hyperscaler credit and equity co-move. As these firms increasingly fund investments with debt, equity values have become more tethered to fluctuating asset valuations, while structurally imposing a higher cost of credit.

Shamshad Ali  
+1(212)902-6712 | shamshad.ali@gs.com GS & Co. LLC

Credit's beta to equity returns should increase with bond maturity, given an upward-sloping term premium. While elevated yield-based demand has dampened the beta for long-duration credit in the broader market, the AI capex cycle has lifted it for hyperscaler credit—especially as spread volatility has been felt acutely in the long-end of the curve.

Credit spreads have widened alongside a deterioration in forward free cash flow yield for hyperscalers. As a result, the path ahead for credit likely hinges on some improvement in forward estimates of free cash flow generation.

That said, the manner of improvement matters more for credit vs. equity relative value. A scenario of free cash flow gains from declining capex would likely favor credit, while a scenario of rising net income and operating cash flow would likely favor equity, as investors may read it as an inflection point for additional value accrual across the AI stack (with equities more exposed to that potential upside).

Hyperscaler Credit vs. Equity: More Issuance, a Higher Beta, and a Different Focus on Cash Flow

Increasing focus on AI-related capex has driven a few themes in markets. In equities, rising capex estimates have begun to dominate future revenue generation leaving infrastructure and “picks and shovels” names such as energy providers, semiconductor and chip manufacturers more supported than the hyperscaler equities investing in capex and presumed ultimate beneficiaries. Credit markets have focused first on the scale and speed of investments, given they are increasingly funded by debt capital, and second on clarity over returns on investment that can offset the significant expenditure.

Credit is more senior to equities, has finite duration and has upside largely limited to payment of interest and repayment of principal. Historically, this has meant a departure from the longer-term terminal values increasingly dominating equity returns, as credit investors focus instead on near-term cash flow and earnings for debt service. Yet, large AI investments are increasingly changing that picture. In this Global Markets Daily, we take stock of the relationship between hyperscaler long

bonds and their equity, using a range of metrics including the beta of spread changes to equity returns. We find that hyperscaler long-end spreads have widened in tandem with the dramatic decline in cash flow yield, underperforming an evolving equity beta in periods of heavy supply. Recently, this underperformance has been more pronounced in the long-end of credit spread curves, compared to shorter tenors. Improvement in cash flow may lead to a rally in spreads, but the manner—for example, if the improved cash flow is driven by a paring back of spend, or an acceleration in

monetization/profitability—will likely matter more for credit/equity relative value.

## AI is changing the credit-equity relationship for hyperscalers

An upward-sloping credit term premium and increasing spread duration typically mean that long-duration credit co-moves more with equity prices—mechanically, a higher beta. However, the rise of liability-driven investors searching for yield, together with elevated policy rate volatility during the 2022-2023 Fed hiking cycle, has lowered long-end credit beta, predominantly through lower volatility (Exhibit 1).

Exhibit 1: Long-end credit spread beta to equity returns has moved lower in recent years, predominantly because of lower volatility

Monthly beta regressing USD IG spread changes across tenors on S&P 500, italicized decomposes beta into correlation and volatility ratios

<table><tr><td>Sample</td><td>3-5 years</td><td>7-10 years</td><td>15+ years</td></tr><tr><td>2015-2019</td><td>-2.5</td><td>-3.1</td><td>-2.6</td></tr><tr><td>correlation</td><td>-0.7</td><td>-0.8</td><td>-0.7</td></tr><tr><td>volatility ratio</td><td>2.0</td><td>2.3</td><td>2.2</td></tr><tr><td>2021-2025</td><td>-1.7</td><td>-1.9</td><td>-1.7</td></tr><tr><td>correlation</td><td>-0.6</td><td>-0.7</td><td>-0.7</td></tr><tr><td>volatility ratio</td><td>1.6</td><td>1.6</td><td>1.4</td></tr></table>

Source: iBoxx, Bloomberg, GS Global Investment Research

Heavy investment in AI has further altered the credit vs. equity relationship for these credits. Credit investors are effectively short a put option on firm solvency while equity holders are long, which helps explain why heavy investment is increasingly driving return differentials across the capital structure. As hyperscalers have committed more to investment, equity values have become more tethered to increasingly uncertain asset valuations, and, through the structural model of equity, so too has the price of credit.

AI-related spreads have therefore seen a modest rise in their beta, echoing the broader trend we’ve noted in the credit/equity relationship. Mirroring the broader trend, long-end betas have increased on the back of higher long-end spread volatility—particularly relative to the more muted front-end (Exhibit 2).

![](images/f2855cef0b83d8ed7c8f3e9590611b5d4da8168f5261a6bc006f769dfeb3dd0f.jpg)  
Exhibit 2: Long-end hyperscaler bonds have a higher beta, given the elevated volatility in back-end spreads Trailing 2-year beta of monthly changes in hyperscaler credit spreads by tenor on monthly hyperscaler equity returns  
Source: iBoxx, Bloomberg, GS Global Investment Research  
This acute widening in back-end hyperscaler spreads has coincided with an eroding forward free cash flow yield across the cohort, a signal of growing funding needs (Exhibit 3).  
Exhibit 3: Hyperscaler credit has sold off as the aggregate free cash flow yield advantage has eroded

![](images/015c1ce8451e0140c09f90f8dd818954cedc104a560a76dc0ba045725f785624.jpg)  
Source: iBoxx, Bloomberg, GS Global Investment Research

## The drivers of improving free cash flow matter

Credit has, on average, underperformed its historical equity beta this year, with the most acute underperformance recently felt in the long-end (Exhibit 4). That much of this has come during waves of new debt issuance over the past few quarters is not surprising. We anticipate more credit curve steepening for AI-related issuers, as this multi-year issuance cycle extends.

## Exhibit 4: Credit spreads have underperformed their beta to equities recently

Rolling 3-month average residual of weekly spread change time-varying beta to hyperscaler equity returns

![](images/367d9a82b2f41fccb4360d9dee099c45604474a031bc137d86d7cf8871a02ab9.jpg)  
Source: iBoxx, Bloomberg, GS Global Investment Research

Still, cross-asset investors are increasingly focused on the path from here for long-end credit and equity relative valuations, especially as hyperscaler earnings multiples are now at multi-year lows relative to the broader index. The volatility-suppressing technical for back-end hyperscaler bonds is firmly in the rear-view mirror, given heavier supply and marginally softer demand as debates around portfolio concentration take on greater importance. We think an improvement in free cash flow generation would support the case for spread tightening, but the manner of that improvement will likely drive the relative value between owning hyperscaler equity vs. credit.

Free cash flow improvement achieved by reducing capex and scaling back investment would likely depress terminal values for hyperscalers, as investors might fear that returns will not validate the investment—an outcome that would tend to favor credit. On the other hand, growth in net income and operating cash flow while investment spending remains robust could favor equities, as returns become more visible and signal an inflection point in where value is accruing across the AI stack.

## TRADE IDEAS

## Best Trade Ideas Across Assets

For pricing, charts, and a list of previous recommendations, please visit our Trade Ideas page.

1. Stay short SGD/MYR, opened January 24, 2026, at 3.13, with a target at 2.90 and a stop at 3.30, currently trading at 3.17.

2. Stay long TRY, NGN and KZT against the USD, as an equally weighted basket, opened February 18, 2026, at 0%, with a total return target of 7.5%, and a revised stop of 1.5%, currently trading at 4.8%.

3. Stay long 3y SOFR swap spread, opened 17 April 2026, at -22.6bp, with a revised target at -15bp inclusive of carry; and a revised stop at -20bp, currently trading at -18.8bp.

4. Stay short USD/EGP, opened 24 April 2026, at 0%, with a revised total return target at 12% and a revised stop at 5%, currently trading at 7.4%.

5. Stay long 5y Receivers on 3m 2s5s10s Receiver Fly (bp running), opened 09 May 2026, at 1bp, with a target at 10bp and a stop at -5bp, currently trading at 0bp.

6. 1y forward 2s10s GBP OIS steepeners, opened 29 May 2026, at 0.38, with a target at 0.55 and a stop at 0.25, currently trading at 0.29.

7. Stay short THB/INR, opened 12 June 2026, at 2.91, with a target at 2.70 and a stop at 3.05, currently trading at 2.85.

8. Stay long INR 30y bonds, opened 27 June 2026, at 7.34%, with a target at 6.90% and a stop at 7.65%, currently trading at 7.41%.

9. 2s10s NZD steepeners, opened 03 July 2026, at 72bp, with a target at 90bp and a stop at 50bp, currently trading at 73bp.

10. 2s10s CAD steepeners, opened 10 July 2026, at 53bp, with a target at 80bp and a revised stop at 50bp, currently trading at 52bp.

11. Stay short AUD/NZD, via 6m (14 Jan 2027) 1.1650 puts, opened 14 July 2026, at 1.2000, currently trading at 1.2107.

12. Stay long NIFTY Banks vs. short NIFTY Pharma, opened 15 July 2026, at 100 in local currency (INR), with a target at 115 and a stop at 90, currently trading at 99.

13. Stay short GBP/USD, opened 17 July 2026, at 1.3452, with a target at 1.3250 and a stop at 1.3400, currently trading at 1.3289.

## Disclosure Appendix

## Reg AC

I, Shamshad Ali, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Shamshad Ali GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficia

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
