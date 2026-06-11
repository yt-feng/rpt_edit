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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/ad68987b2900d56da48f106f3649a9427b41aa868f5d97cd55bc2b337c594156.jpg)

<details>
<summary>line chart</summary>

| Date | Stock Price | Hang Seng Index | Rating | Price target |
| --- | --- | --- | --- | --- |
| Mar 25, 2026 | 81 | 130 |  |  |
| Jun 2023 | 80 | 130 |  |  |
| Sep 2023 | 84 | 130 |  |  |
| Dec 2023 | 80 | 130 |  |  |
| Mar 2024 | 81 | 130 |  |  |
| Jun 2024 | 84 | 130 |  |  |
| Sep 2024 | 88 | 130 |  |  |
| Dec 2024 | 93 | 130 |  |  |
| Mar 2025 | 98 | 130 |  |  |
| Jun 2025 | 103 | 130 |  |  |
| Sep 2025 | 109 | 130 |  |  |
| Dec 2025 | 113 | 130 |  |  |
| Mar 2026 | 162 | 130 |  |  |
| Jun 2026 |  |  |  |  |
| Oct 9 |  |  |  |  |
| Nov 2026 |  |  |  |  |
| Dec 2026 |  |  |  |  |
| Jan 2027 |  |  |  |  |
| Feb 2027 |  |  |  |  |
| Mar 2027 |  |  |  |  |
| Apr 2027 |  |  |  |  |
| May 2027 |  |  |  |  |
| Jun 2027 |  |  |  |  |
| Jul 2027 |  |  |  |  |
| Aug 2027 |  |  |  |  |
| Sep 2027 |  |  |  |  |
| Oct 2027 |  |  |  |  |
| Nov 2027 |  |  |  |  |
| Dec 2027 |  |  |  |  |
| Jan 2028 |  |  |  |  |
| Feb 2028 |  |  |  |  |
| Mar 2028 |  |  |  |  |
| Apr 2028 |  |  |  |  |
| May 2028 |  |  |  |  |
| Jun 2028 |  |  |  |  |
| Jul 2028 |  |  |  |  |
| Aug 2028 |  |  |  |  |
| Sep 2028 |  |  |  |  |
| Oct 2028 |  |  |  |  |
| Nov 2028 |  |  |  |  |
| Dec 2028 |  |  |  |  |
| Jan 2029 |  |  |  |  |
| Feb 2029 |  |  |  |  |
| Mar 2029 |  |  |  |  |
| Apr 2029 |  |  |  |  |
| May 2029 |  |  |  |  |
| Jun 2029 |  |  |  |  |
| Jul 2029 |  |  |  |  |
| Aug 2029 |  |  |  |  |
| Sep 2029 |  |  |  |  |
| Oct 2029 |  |  |  |  |
| Nov 2029 |  |  |  |  |
| Dec 2029 |  |  |  |  |
| Jan 21 |  |  |  |  |
| Feb 21 |  |  |  |  |
| Mar 21 |  |  |  |  |
| Apr 21 |  |  |  |  |
| May 21 |  |  |  |  |
| Jun 21 |  |  |  |  |
| Jul 21 |  |  |  |  |
| Aug 21 |  |  |  |  |
| Sep 21 |  |  |  |  |
| Oct 21 |  |  |  |  |
| Nov 21 |  |  |  |  |
| Dec 21 |  |  |  |  |
| Jan 22 |  |  |  |  |
| Feb 22 |  |  |  |  |
| Mar 22 |  |  |  |  |
| Apr 22 |  |  |  |  |
| May 22 |  |  |  |  |
| Jun 22 |  |  |  |  |
| Jul 22 |  |  |  |  |
| Aug 22 |  |  |  |  |
| Sep 22 |  |  |  |  |
| Oct 22 |  |  |  |  |
| Nov 22 |  |  |  |  |
| Dec 22 |  |  |  |  |
| Jan 23 |  |  |  |  |
| Feb 23 |  |  |  |  |
| Mar 23 |  |  |  |  |
| Apr 23 |  |  |  |  |
| May 23 |  |  |  |  |
| Jun 23 |  |  |  |  |
| Jul 23 |  |  |  |  |
| Aug 23 |  |  |  |  |
| Sep 23 |  |  |  |  |
| Oct 23 |  |  |  |  |
| Nov 23 |  |  |  |  |
<

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
