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
## HONG KONG BANKS

# Addressing FAQs on Hong Kong deposits and Mainland China cross-border investment

In short: Shares in HSBC and STAN have underperformed the SX7P by 5%/7% since 21 May (at time of writing), in our view reflecting investor concerns of a slowdown in Hong Kong deposit flows, and potentially more limited engagement with Mainland China clients. In our view, this underperformance does not correspond with the potential earnings impact from measures and changes already announced, but could more likely be a reflection of uncertainty regarding potential future policy changes. While we take no view on the final outcome of recently announced regulations and await further details — as a sensitivity, even in a scenario where Group net new money were to slow down by 10% (as a proxy for the share of NNM originating from onshore mainland China), even assuming a \~300bp margin on these flows (HIBOR currently at 2.7%), this would equate to only \~1%/2% of PBT for HSBC/STAN, on 2025 numbers. Following on from our earlier note, we address recent investor FAQs on Hong Kong deposits and cross-border investment below.

## Recap: What measures have been announced so far?

1. On 22 May, the China Securities Regulatory Commission announced regulatory controls on online brokers and related fines, while the Hong Kong Monetary Authority issued a circular, aimed at strengthening account opening procedures and compliance requirements, reinforcing existing rules around investment accounts and the source of funds. Standard Chartered's CFO highlighted at our conference last week (see full transcript here) that their existing policies were directionally aligned with these circulars, while there were several incremental action items including closing legacy zero balance accounts and gaining client attestations regarding sources of funds. Overall, while the additional attestations may add a layer of friction, we do not anticipate a material impact for either HSBC or STAN. Indeed, per press reports of 9th June, the HKMA has indicated that for Hong Kong-based banks, the necessary system upgrades have been completed, with account opening services having continued in a smooth manner.

2. On 1 June, China's State Council released a decree regulating cross-border investment. Our economists highlight that the timing likely relates to the government's recent blocking of the Meta-Manus deal, while specifically focussing on establishing frameworks for regulating cross-border technology transfers, supporting Chinese companies going global, and managing operational

## Chris Hallam

+44(20)7552-2958

chris.hallam@gs.com

GS International

## Melissa Kuang, CFA

+65-6889-2869

melissa.kuang@gs.com

GS (Singapore) Pte

## Benjamin Caven-Roberts

+44(20)7552-7066 | benjamin.d.caven-

roberts@gs.com

GS International

## Sachin Nayar

+44(20)7051-2598

sachin.x.nayar@gs.com

GS International

## Wayne Wang

+65-6889-2866

wayne.q.wang@gs.com

GS (Singapore) Pte

and geopolitical risks associated with Chinese businesses and assets abroad. The primary concern of policymakers, our economist argues, revolves around monitoring and managing cross-border technology and capital flows in an increasingly complex geopolitical environment, rather than to reduce capital outflows. The relevant angle for banks, however, may centre upon one specific article (#33), which stipulates that investment in overseas financial markets shall be governed by the regulations, with detailed rules to be formulated separately.

We do not yet have insight onto what form these rules may take — however, we note that the share of NNM which comes directly from onshore sources in mainland China (i.e., not generated offshore to begin with) accounts for the vast minority of NNM flows for HSBC and STAN, in our view limiting the ultimate earnings impact.

## What could the financial impact be on HSBC and Standard Chartered?

Looking specifically at deposits, based on comments from HSBC and Standard Chartered, we understand that (as a rough proxy) for a typical mainland Chinese resident who holds an account in Hong Kong, \~90% of the deposit flow comes from “offshore” sources (e.g. Singapore, or elsewhere in Hong Kong), while only \~10% comes from a mainland China bank account. In 2025, total net new money for HSBC was c.\$86bn and c.\$52bn for STAN. At our recent conference, STAN’s CFO flagged that \~30% of their net new money was from Global Chinese, with the vast majority of that money already sitting offshore.

Quantifying potential headwinds: As a result of the information outlined above, assuming that \~10% of Group NNM is from onshore sources in mainland China — were we to assume as an adverse scenario that this future NNM flow stopped entirely, this 10% reduction in NNM would equate to c.\$9bn/\$5bn for HSBC/STAN, all else equal.

☐ For each 100bp margin earned on this net new money, this equates to 0.3%/0.7% of 2025 PBT for HSBC/STAN — as a result, even assuming a 300bp margin (with HIBOR at 2.7% currently), this would equate to \~1%/2% of PBT for HSBC/STAN p.a.

\- With regard to insurance and investment products, we currently do not consider there to be any impact as they are currently out of scope or in line with pre-existing rules, and a more restrictive approach to either product set would not necessarily align with a) the focus of regulating cross-border technology transfers, or b) the desire to support RMB internalisation, and c) the continued development of Hong Kong as a hub for outbound and inbound investment.

For context, as highlighted in our prior note, wealth income for Standard Chartered and HSBC accounts for roughly one third of operating income. For HSBC, wealth fees from its disclosed HK segment (which likely excludes insurance) contribute to approximately one fifth of total wealth fees and c.2-3% of group operating income (as per their HK divisional disclosure), while for STAN, Hong Kong wealth contributes c.40% of total wealth income. While HSBC and STAN note that a significant proportion of new-to-bank clients are non-resident in Hong Kong, net new money is increasingly sourced from global Chinese clients (with offshore wealth).

## Valuation and key risks

We value HSBC using a target multiple of 12.0x applied 75%/25% to 2027/28E estimates to arrive at 12-month target prices of GBp1,700, while using a 2-stage dividend discount model for 0005.HK to arrive at a 12-month price target of HK\$165. We are Buy rated (HSBA.L on Conviction List). Risks to our rating and price target include: 1) Weaker-than-expected Banking NII, including faster-than-expected Fed rate cuts, or a widening gap between HIBOR and Fed rate; 2) Slower-than-expected non-NII growth, including a potential slowdown in global trade or increased competition from peers; 3) Reversal/pause of positive operating efficiency trajectory if simplification efforts are impacted adversely.

We value STAN using a target multiple of 10.25x applied 75%/25% to 2027/28E estimates to arrive at 12-month target prices of 2,260p, while using a 2-stage dividend discount model for 2888.HK to arrive at a 12-month price target of HK\$242. We are Buy rated. Downside risks to our view and price target include reversal/pause of positive jaws delivery, slower-than-expected non-interest income growth, lower-than-expected net interest income growth.

## Disclosure Appendix

## Reg AC

We, Chris Hallam, Melissa Kuang, CFA, Benjamin Caven-Roberts, Sachin Nayar and Wayne Wang, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Chris Hallam GS International, Melissa Kuang, CFA GS (Singapore) Pte, Benjamin Caven-Roberts GS International, Sachin Nayar GS International, Wayne Wang GS (Singapore) Pte.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for HSBC Holdings and Standard Chartered Bank is/are relative to the other companies in its/their coverage universe: BDO Unibank, BOC Hong Kong (Holdings), Bangkok Bank, Bank Central Asia, Bank Mandiri, Bank Negara Indonesia, Bank Rakyat Indonesia, Bank of East Asia, Bank of Philippine Islands, DBS Group, HSBC Holdings, Kasikornbank, Krung Thai Bank, Oversea-Chinese Banking Corp., SCB X PCL, Standard Chartered Bank, TMBThanachart Bank PCL, United Overseas Bank

The rating(s) for HSBC and Standard Chartered is/are relative to the other companies in its/their coverage universe: ABN Amro Bank, AIB Group, Alpha Bank, BBVA, BNPP, BPER Banca, Banco Comercial Portugues, Banco Santander, Bank of Ireland Group, Bankinter, BARC Plc, CaixaBank SA, Credit Agricole SA, DNB, Danske Bank, DB, Eurobank SA, HSBC, ING Groep NV, Intesa Sanpaolo, Julius Baer Group, KBC Group, Lloyds Banking Group, NOBA Bank Group, National Bank of Greece, Natwest Group, Nordea, Piraeus Bank SA, SEB, Shawbrook Group, SG, Standard Chartered, Svenska Handelsbanken, Swedbank, UBS Group, Unicaja Banco SA

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Standard Chartered (1,811p) and Standard Chartered Bank (HK\$189.30)

GS has received compensation for investment banking services in the past 12 months: HSBC (1,311.4p), HSBC (ADR) (\$89.34), HSBC Holdings (HK\$135.30), Standard Chartered (1,811p) and Standard Chartered Bank (HK\$189.30)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: HSBC (1,311.4p), HSBC (ADR) (\$89.34), HSBC Holdings (HK\$135.30), Standard Chartered (1,811p) and Standard Chartered Bank (HK\$189.30)

GS has received compensation for non-investment banking services during the past 12 months: HSBC (1,311.4p), HSBC (ADR) (\$89.34), HSBC Holdings (HK\$135.30), Standard Chartered (1,811p) and Standard Chartered Bank (HK\$189.30)

GS had an investment banking services client relationship during the past 12 months with: HSBC (1,311.4p), HSBC (ADR) (\$89.34), HSBC Holdings (HK\$135.30), Standard Chartered (1,811p) and Standard Chartered Bank (HK\$189.30)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: HSBC (1,311.4p), HSBC

(ADR) (\$89.34), HSBC Holdings (HK\$135.30), Standard Chartered (1,811p) and Standard Chartered Bank (HK\$189.30)

GS had a non-securities services client relationship during the past 12 months with: HSBC (1,311.4p), HSBC (ADR) (\$89.34), HSBC Holdings (HK\$135.30), Standard Chartered (1,811p) and Standard Chartered Bank (HK\$189.30)

GS has managed or co-managed a public or Rule 144A offering in the past 12 months: HSBC (1,311.4p), HSBC (ADR) (\$89.34) and HSBC Holdings (HK\$135.30)

GS makes a market in the securities or derivatives thereof: HSBC (1,311.4p), HSBC (ADR) (\$89.34), HSBC Holdings (HK\$135.30), Standard Chartered (1,811p) and Standard Chartered Bank (HK\$189.30)

GS International acts as corporate broker to: Standard Chartered (1,811p) and Standard Chartered Bank (HK\$189.30)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within t

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
