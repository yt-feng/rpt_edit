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
First Read

# Electronic Components Sector Update Asia marketing feedback

## Interest in the sector remains high

We had 28 investor meetings in Hong Kong and Singapore on 7-10 July. Interest in the electronic components sector remained remarkably high. While many investors were bullish on sector fundamentals for MLCCs, compared with our Asia and US marketing trips in March and April, we also heard some more cautious views due to higher share-price valuations and the recent increase in share price volatility. Compared with our previous trip, we had the impression that more investors agreed with our preference for Murata Mfg. over Taiyo Yuden given Murata Mfg.'s higher visibility for medium-term growth driven by Al. Regarding Ibiden, the majority of investors had bullish opinions of fundamentals, although some investors voiced concerns regarding its elevated valuation.

## Feedback on our Rohm rating upgrade

We upgraded our rating on Rohm from Neutral to Buy right before the Asia marketing trip (link). Although we were asked some questions regarding the timing of this upgrade given the strong appreciation of its share price so far this year, we had the impression that most investors agreed with our view that Rohm's intrinsic value (excluding its Toshiba common shares) remains underappreciated and there is substantial earnings upside. On the other hand, some investors are favouring Kioxia over Rohm because Rohm's share price is influenced by movements in its indirectly held stake in Kioxia.

## Other stocks we discussed

Hirose Electric, TDK, MinebeaMitsumi and Kyocera were among the stocks most frequently discussed. For Hirose Electric, many investors voiced expectations for a recovery in industrial equipment demand and noted the potential of newly consolidated SER (a manufacturer of probe pins for semiconductor testing). While multiple investors said that upside for TDK and MinebeaMitsumi is limited, we had lengthier discussions regarding their business opportunities in data centres. For Kyocera, many investors wanted to better understand the factors behind its recent share price strength, while we also heard some expectations for upside to fundamentals.

## Valuation: Stock picks

In particular, we recommend Murata Mfg. (6981) and Rohm (6963), which supply components with tight supply-demand conditions in AI data centres.

Equities

Japan

Electric Components & Equipment

Shingo Hirata, CFA

Analyst

shingo.hirata@ubs.com

+81-3-5208 6224

## Valuation Method and Risk Statement

Risk factors for the sector include (1) sudden fluctuations in macro factors (such as individual consumption in the US), (2) sudden swings in financial markets (including the US stock market) and (3) changes in base material costs (including petrochemicals and metals).

Rohm: Our price target for Rohm is based on PER. Downside risk factors include a sales slowdown due to weakness in semiconductor demand alongside a slowdown in the macro economy, a loss of market share or price declines as a result of stiffer competition, profit erosion because of a stronger yen, and deterioration in competitiveness. Production declines in autos, smartphones, game equipment, and personal computers also present risk. Upside risks include structural reforms exceeding expectations, increased demand, and the securing of orders in growth areas such as AI.

Murata Manufacturing: Our price target is based on PER. We believe the main risk factors are: (1) an unexpected reduction in demand for core products as a result of a slowdown in the US economy, (2) sudden volatility in the equity or forex markets, (3) diffusion of technology (for large-capacitance ceramic capacitors, etc.) to Asian enterprises, (4) further progress with the shift of high frequency circuits to IC with improvements in semiconductor technology, and (5) a reduction in the competitive advantage of ceramic capacitors as the performance of other capacitors improves.

## Required Disclosures

This document has been prepared by UBS Japan Co., Ltd., an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 13 July 2026 12:46 AM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

UBS Global Research: Global Equity Rating Definitions

<table><tr><td>12-Month Rating</td><td>Definition</td><td>Coverage $^{1}$ </td><td>IB Services $^{2}$ </td></tr><tr><td>Buy</td><td>FSR is &gt; 6% above the MRA.</td><td>55%</td><td>24%</td></tr><tr><td>Neutral</td><td>FSR is between -6% and 6% of the MRA.</td><td>40%</td><td>21%</td></tr><tr><td>Sell</td><td>FSR is &gt; 6% below the MRA.</td><td>6%</td><td>21%</td></tr></table>

Source: UBS. Rating allocations are as of 30 June 2026.  
1: Percentage of companies under coverage globally within the 12-month rating category.

2: Percentage of companies within the 12-month rating category for which investment banking (IB) services were provided within the past 12 months.

KEY DEFINITIONS: Forecast Stock Return (FSR) is defined as expected percentage price appreciation plus gross dividend yield over the next 12 months. In some cases, this yield may be based on accrued dividends. Market Return Assumption (MRA) is defined as the one-year local market interest rate plus 5% (a proxy for, and not a forecast of, the equity risk premium). Under Review (UR) Stocks may be flagged as UR by the analyst, indicating that the stock's price target and/or rating are subject to possible change in the near term, usually in response to an event that may affect the investment case or valuation. Equity Price Targets have an investment horizon of 12 months.

EXCEPTIONS AND SPECIAL CASES:UK and European Investment Fund ratings and definitions are: Buy: Positive on factors such as structure, management, performance record, discount; Neutral: Neutral on factors such as structure, management, performance record, discount; Sell: Negative on factors such as structure, management, performance record, discount. Core Banding Exceptions (CBE): Exceptions to the standard +/-6% bands may be granted by the Investment Review Consultation (IRC). Factors considered by the IRC include the stock's volatility and the credit spread of the respective company's debt. As a result, stocks deemed to be very high or low risk may be subject to higher or lower bands as they relate to the rating. When such exceptions apply, they will be identified in the Company Disclosures table in the relevant research piece.

Research analysts contributing to this report who are employed by any non-US affiliate of UBS LLC are not registered/qualified as research analysts with FINRA. Such analysts may not be associated persons of UBS LLC and therefore are not subject to the FINRA restrictions on communications with a subject company, public appearances, and trading securities held by a research analyst account. The name of each affiliate and analyst employed by that affiliate contributing to this report, if any, follows.
UBS Japan Co., Ltd.: Shingo Hirata, CFA.

Company Disclosures

<table><tr><td>Company Name</td><td>Reuters</td><td>12-month rating</td><td>Price</td><td>Price date</td></tr><tr><td>Murata Manufacturing $^{28b}$ </td><td>6981.T</td><td>Buy</td><td>¥9,860</td><td>10 Jul 2026</td></tr><tr><td>Rohm $^{28a}$ </td><td>6963.T</td><td>Buy</td><td>¥5,600</td><td>10 Jul 2026</td></tr></table>

Source: UBS Global Research; LSEG Eikon. All prices as of local market close. Ratings in this table are the most current published ratings prior to this report. They may be more recent than the stock pricing date.
28a. UBS holds a long position of 0.5% or more of the listed shares of this company.
28b. UBS holds a short position of 0.5% or more of the listed shares of this company.

Unless otherwise indicated, please refer to the Valuation and Risk sections within the body of this report. For a complete set of disclosure statements associated with the companies discussed in this report, including information on valuation and risk, please contact UBS LLC, 11 Madison Avenue, New York, NY 10010, USA, Attention: Investment Research.

Rohm (¥)  
![](images/e98029895a810c5350a8950685a030c080d7bae43727338ca7a57d44041b99f7.jpg)

<table><tr><td>Date</td><td>Stock Price (¥)</td><td>Price Target (¥)</td><td>Rating</td></tr><tr><td>2023-04-10</td><td>2600</td><td>3500.0</td><td>Buy</td></tr><tr><td>2023-07-12</td><td>3323</td><td>4350.0</td><td>Buy</td></tr><tr><td>2023-09-11</td><td>2898</td><td>4100.0</td><td>Buy</td></tr><tr><td>2023-11-16</td><td>2713</td><td>3800.0</td><td>Buy</td></tr><tr><td>2024-03-29</td><td>2429</td><td>3500.0</td><td>Buy</td></tr><tr><td>2024-06-05</td><td>2022</td><td>3150.0</td><td>Buy</td></tr><tr><td>2024-10-29</td><td>1740</td><td>2700.0</td><td>Buy</td></tr><tr><td>2024-11-15</td><td>1440</td><td>1500.0</td><td>Neutral</td></tr><tr><td>2025-03-29</td><td>1494</td><td>1570.0</td><td>Neutral</td></tr><tr><td>2025-06-18</td><td>1661</td><td>1790.0</td><td>Neutral</td></tr><tr><td>2025-09-12</td><td>2075</td><td>2200.0</td><td>Neutral</td></tr><tr><td>2026-07-02</td><td>5211</td><td>-</td><td>No Rating</td></tr><tr><td>2026-07-03</td><td>5950</td><td>8300.0</td><td>Buy</td></tr></table>

Source: UBS Global Research; LSEG Eikon as of 10-Jul-2026. All prices as of local market close. Ratings as of date shown.

![](images/1f13911fc94adea80df7a84c8f5c3644a8107ba0f6b1526f9856ab2958d8e794.jpg)

<table><tr><td>Date</td><td>Stock Price (¥)</td><td>Price Target (¥)</td><td>Rating</td></tr><tr><td>2023-04-10</td><td>2570</td><td>3333.33</td><td>Buy</td></tr><tr><td>2023-07-11</td><td>2670</td><td>3450</td><td>Buy</td></tr><tr><td>2024-01-23</td><td>3112</td><td>3550</td><td>Buy</td></tr><tr><td>2024-07-02</td><td>3364</td><td>3900</td><td>Buy</td></tr><tr><td>2024-09-19</td><td>2666</td><td>3600</td><td>Buy</td></tr><tr><td>2025-01-28</td><td>2515</td><td>3300</td><td>Buy</td></tr><tr><td>2025-04-24</td><td>2141</td><td>3100</td><td>Buy</td></tr><tr><td>2025-05-30</td><td>2132</td><td>2960</td><td>Buy</td></tr><tr><td>2025-09-25</td><td>2800</td><td>3400</td><td>Buy</td></tr><tr><td>2025-11-28</td><td>3213</td><td>3900</td><td>Buy</td></tr><tr><td>2026-03-05</td><td>3808</td><td>5400</td><td>Buy</td></tr><tr><td>2026-06-12</td><td>8556</td><td>13200</td><td>Buy</td></tr></table>

Source: UBS Global Research; LSEG Eikon as of 10-Jul-2026. All prices as of local market close. Ratings as of date shown.

Additional Prices: Ibiden, ¥20300 (10 Jul 2026); MinebeaMitsumi, ¥4381 (10 Jul 2026); TDK, ¥3389 (10 Jul 2026); Hirose Electric, ¥27685 (10 Jul 2026); Kyocera, ¥3720 (10 Jul 2026); Taiyo Yuden, ¥14730 (10 Jul 2026); Source: UBS. All prices as of local market close.

## Company profile and fee and risk statement under the Japanese Financial Instruments & Exchange Law

Company Name etc: UBS Japan Co., Ltd., Financial Instruments & Exchange Firm, Kanto Local Financial Bureau (Kinsho) No.2633

Associated Memberships: Japan Securities Dealers' Association, the Financial Futures Association of Japan, and Type II Financial Instruments Firms Association

UBS Japan Co., Ltd. will receive a brokerage fee based on an individual contract and no standard upper limit or calculating method. For the trading of domestic stocks, consumption tax is added to the fee. For the trading of foreign stock, fee on the foreign stock exchange or foreign tax may be charged in addition to the domestic fee and tax. Those amounts may vary depending on the jurisdiction. There is a risk that a loss may occur due to a change in the price of the stock in the case of trading stocks, and that a loss may occur due to the exchange rate in the case of trading foreign stocks. There is a risk that a loss may occur due to a change in the price or performance of the properties in the portfolio in the case of trading REITs.

UBS Japan Co., Ltd. will only receive the purchasing amounts for trading unlisted bonds (JGBs, municipals, government guaranteed bonds, corporate bonds) when UBS Japan Co., Ltd. is the counterparty. There is a risk that a loss may occur due to a change in the price of the bond caused by the fluctuations in the interest rates, and that a loss may occur due to the exchange rate in the case of trading foreign bonds.

For the detailed information of commissions and risks associated with individual financial instrument transactions, please carefully read the documents provided prior to the execution of the contracts or other materials for customers, etc. before executing any transaction. If you need any clarification, please consult with our sales person in charge.

The Disclaimer relevant to Global Wealth Management clients follows the Global Research Disclaimer. The Disclaimer relevant to CS Wealth Management follows the Global Wealth Management Disclaimer.

## UBS Global Research Disclaimer

This document has been prepared by UBS Japan Co., Ltd., an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

Any opinions expressed in this document may change without notice and are only current as of the date of publication. Different areas, groups, and personnel within UBS may produce and distribute separate research products independently of each other. For example, research publications from UBS CIO are produced by UBS Global Wealth Management. UBS Global Research is produced by UBS Investment Bank. Research methodologies and rating systems of each separate research organization may differ, for example, in terms of investment recommendations, investment horizon, model assumptions, and valuation methods. As a consequence, except for certain economic forecasts (for which UBS CIO and UBS Global Research may collaborate), investment recommendations, ratings, price targets, and valuations provided by each of the separate research organizations may be different, or inconsistent. You should refer to each relevant research product for the details as to their methodologies and rating system. Not all clients may have access to all products from every organization. Each research product is subject to the policies and procedures of the organization that produces it.

## This document is provided solely to recipients who are expressly authorized by UBS to receive it. If you are not so authorized you must immediately destroy the document.

UBS Global Research is provided to our clients through UBS Neo, and in certain instances, UBS.com and any other system or distribution method specifically identified in one or more communications distributed through UBS Neo or UBS.com (each a system) as an approved means for distributing UBS Global Research. It may also be made available through third party vendors and distributed by UBS and/or third parties via e-mail or alternative electronic means.

All UBS Global Research is available on UBS Neo. Please contact your UBS sales representative if you wish to discuss your access to UBS Neo. Where UBS Global Research refers to "UBS Evidence Lab Inside" or has made use of data provided by UBS Evidence Lab and you wou

[中间内容因长度限制已省略]

 Republic of Türkiye are allowed to purchase or sell the financial instruments traded in financial markets outside of the Republic of Türkiye. Further to this, pursuant to article 9 of the Communiqué on Principles Regarding Investment Services, Activities and Ancillary Services No. III-37.1, investment services provided abroad to residents of the Republic of Türkiye based on their own initiative are not restricted. United Arab Emirates (UAE) / DIFC / Abu Dhabi: UBS is not licensed in the UAE by the Central Bank of the UAE nor by the Emirates' Securities and Commodities Authority and does not undertake banking activities in the UAE. This document is provided for your information only and does not constitute financial advice. DIFC: UBS AG Dubai Branch is regulated by the DFSA in the DIFC. This material is strictly intended for Professional Clients and/or Market Counterparties only as classified under the DFSA rulebook. It should not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
