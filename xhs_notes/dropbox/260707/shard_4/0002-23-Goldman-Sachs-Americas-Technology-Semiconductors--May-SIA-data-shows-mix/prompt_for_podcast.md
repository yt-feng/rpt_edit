你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Americas Technology: Semiconductors: May SIA data shows mixed seasonality after a strong start to year

## Mixed seasonality in May after a strong start to the year

Shipments of integrated circuits units (ex. memory) decreased 2% month over month in May, below typical seasonality, according to data from Semiconductor Industry Association (SIA). Many segments shipped at below-seasonal levels for the month, although NAND, MPUs, and MCUs all saw above-seasonal M/M unit growth. Despite mixed seasonality, overall shipments are now tracking 2% above long-term demand on a three-month moving average basis (vs. 1% below trend in April). Improving trends over the past few months are consistent with companies' constructive commentary, particularly for analog where shipments are now running \~4% above trend. Performance by sub-segment was as follows.

IC ex. Memory: Units were 2.7% above trend vs. 1.7% below in April.

■ Analog: Units were 4.3% above trend, better than 0.3% above trend in April.

■ MCU: Units were 23.7% below trend, better than 27.2% below trend in April.

Exhibit 1: M/M % change in revenue, units and ASPs vs. historical levels

<table><tr><td></td><td colspan="3">Revenue</td><td colspan="3">Units</td><td colspan="3">ASPs</td></tr><tr><td>May 2026</td><td>M/M Rev % Chg</td><td>Hist. M/M % Chg</td><td>Y/Y % Chg</td><td>M/M Unit % Chg</td><td>Hist. M/M Unit % Chg</td><td>Y/Y Unit % Chg</td><td>M/M ASP % Chg</td><td>Hist. M/M ASP %</td><td>Y/Y ASP % Chg</td></tr><tr><td>Total Semiconductors</td><td>16%</td><td>6%</td><td>119%</td><td>-3%</td><td>0%</td><td>13%</td><td>19%</td><td>6%</td><td>94%</td></tr><tr><td>Discretes</td><td>-3%</td><td>1%</td><td>9%</td><td>-5%</td><td>-3%</td><td>4%</td><td>2%</td><td>4%</td><td>5%</td></tr><tr><td>Integrated Circuits</td><td>18%</td><td>7%</td><td>132%</td><td>0%</td><td>3%</td><td>23%</td><td>18%</td><td>7%</td><td>88%</td></tr><tr><td>DRAM</td><td>28%</td><td>25%</td><td>309%</td><td>14%</td><td>25%</td><td>-2%</td><td>12%</td><td>2%</td><td>319%</td></tr><tr><td>NAND</td><td>41%</td><td>17%</td><td>377%</td><td>21%</td><td>19%</td><td>-12%</td><td>17%</td><td>0%</td><td>445%</td></tr><tr><td>ICs ex. Memory</td><td>2%</td><td>1%</td><td>38%</td><td>-2%</td><td>1%</td><td>21%</td><td>4%</td><td>1%</td><td>14%</td></tr><tr><td>MPU</td><td>5%</td><td>2%</td><td>31%</td><td>4%</td><td>1%</td><td>7%</td><td>1%</td><td>2%</td><td>23%</td></tr><tr><td>MCU</td><td>-3%</td><td>-2%</td><td>20%</td><td>2%</td><td>-1%</td><td>14%</td><td>-4%</td><td>-1%</td><td>5%</td></tr><tr><td>DSP</td><td>3%</td><td>-3%</td><td>-1%</td><td>-8%</td><td>3%</td><td>-11%</td><td>12%</td><td>-1%</td><td>11%</td></tr><tr><td>Analog</td><td>-8%</td><td>-2%</td><td>11%</td><td>-4%</td><td>2%</td><td>22%</td><td>-4%</td><td>-3%</td><td>-9%</td></tr><tr><td>Logic</td><td>7%</td><td>3%</td><td>26%</td><td>0%</td><td>0%</td><td>10%</td><td>7%</td><td>2%</td><td>15%</td></tr></table>

## Source: SIA, GS Global Investment Research

Stock implications: We expect shipments to stabilize above trend in the near term given the duration of below-trend shipments over the past four years, which is consistent with more constructive company commentary on the normalization of demand and customer inventory levels. We continue to prefer Microchip, NXP, and Analog Devices as we focus on companies which had shipped furthest below trend in

James Schneider, Ph.D.
+1(212)357-2929 |
jim.schneider@gs.com
GS & Co. LLC

Khalil Fenina
+1(212)357-6392 |
khalil.fenina@gs.com
GS & Co. LLC

Anmol Makkar
+1(212)357-1366 |
anmol.makkar@gs.com
GS & Co. LLC

Luya You
+1(212)902-5297 | luya.you@gs.com
GS & Co. LLC

the downturn.

IC Units ex. Memory

IC units ex. Memory relative to trend are shown below (see Exhibit 2).

IC units ex. Memory 3 months average (units in millions)  
Exhibit 2: IC units ex. Memory are \~3% above trend as of May  
![](images/c2f54175ca540f6f6c473f7523e92d009ac88f8515aa3a7e10c74e86683e4421.jpg)  
Source: SIA, GS Global Investment Research  
Exhibit 3: IC units ex. memory were down \~2% M/M, worse than typical history
M/M % change in units

![](images/cd08a0fe3698074ad6565865240aee2519beaac6091bb0c8c951535b4334ac05.jpg)  
Source: SIA, GS Global Investment Research

## Analog

Analog units relative to trend are shown below (see Exhibit 4).

Exhibit 4: Analog units are roughly 4% above trend as of May
Analog units 3 months average (units in millions)

![](images/f62066a0e99e08bc8ea7472292b111b5122c554162092951020195d3d48facbe.jpg)  
Source: SIA, GS Global Investment Research  
Exhibit 5: Analog units were down \~4% M/M, worse than typical history
M/M % change in units

![](images/08f9a8a21d5712d12f031d99471f25d64b54005f4d693ebffb0c018168906bec.jpg)  
Source: SIA, GS Global Investment Research

## Microcontrollers (MCU)

MCU units relative to trend are shown below (see Exhibit 6).

Exhibit 6: MCU units are \~24% below trend as of May
MCU units 3 months average (units in millions)  
![](images/7b33dc37e86dd9d8586aaedd9a3f7a37b248a219b98b6e00275b76826a225490.jpg)  
Source: SIA, GS Global Investment Research

Exhibit 7: MCU units were up \~2% M/M, above typical history
M/M % change in units  
![](images/88d0f9a2ff3b516e134ba4ae9b9f04c6ddba1b26e5f73f888ad1c73e81d24d48.jpg)  
Source: SIA, GS Global Investment Research

## Memory

DRAM revenues were up 28% M/M, slightly above typical M/M seasonality, driven by very strong ASPs. NAND revenues were up 41% M/M, far above typical M/M seasonality.

Exhibit 8: DRAM units were up 14% M/M, below typical seasonality  
![](images/c5f74b9332c1e82e57c929a5092a36692429f0b29ba1ab4614a2162f7a730663.jpg)  
Source: SIA, GS Global Investment Research

Exhibit 9: NAND units were up 21% M/M, slightly above typical seasonality
NAND units (in thousands) and ASP (\$)  
![](images/0d870f1a1ecd880717317fb7e4a4d2372a88006893f4b93cf0b6e47cebe4b729.jpg)  
Source: SIA, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, James Schneider, Ph.D., Khalil Fenina, Anmol Makkar and Luya You, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: James Schneider, Ph.D. GS & Co. LLC, Khalil Fenina GS & Co. LLC, Anmol Makkar GS & Co. LLC, Luya You GS & Co. LLC.

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

## Rating and pricing information

Analog Devices Inc. (Buy, \$377.16), Microchip Technology Inc. (Buy, \$84.64) and NXP Semiconductors NV (Buy, \$273.36).

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an

officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details, a copy of the annual compliance audit report and other relevant information and disclosures can be found at this link:

https://www.goldmansachs.com/worldwide/india/research-analyst. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the financial circumstances, investment profiles or risk profiles of clients. GS assumes no responsibility for any investmen

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
