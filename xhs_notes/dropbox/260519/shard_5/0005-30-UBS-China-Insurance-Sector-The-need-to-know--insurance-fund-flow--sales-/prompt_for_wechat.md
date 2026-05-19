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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# First Read

# China Insurance Sector

The need-to-know: insurance fund flow, sales, and investor feedback on stock performance

# Sector equity exposure rose QoQ in Q126, despite weak stock market

NFRA recently released Q126 industry statistics. Insurance fund AUM was +2.5% QoQ to Rmb39.4 tn, as (1) steady cash inflow driven by solid premium growth (+6.2% YoY) was partially offset by (2) fair value loss on equity and bond investments. Equity was the fastest-growing asset class. Exposure to long-term equity stake trended up 0.2 pp QoQ to 7.8%. Stocks and securities investment funds accounted for 16% of AUM, +0.1 pp QoQ, likely reflecting the (1) bottom-fishing move, and (2) business mix shift towards PAR products. Allocation to bonds was +0.1 pp QoQ to 51%, as insurers capitalized on the rise of long-dated bond yield. Exposure to 'others' (mainly non-standard debt assets) and bank deposits declined, down 0.3 pp/0.1 pp QoQ to 18%/8.1%, extending the trends seen in previous years, as the maturity of higher-yielding assets coincided with supply shortage. In 2026, insurers generally expect interest rate to hover at a low level, according to Q1 earnings calls. Many also indicated that the current asset class allocations were at appropriate level.

# YoY growth of FYRP moderated in Q2-to-date – not a surprise

For most listed insurers, YoY growth of first-year regular premium (FYRP) moderated in Q2-to-date, not a surprise, as (1) deposit maturities/migrations were concentrated in Q1 this year, (2) insurers are preparing for bancassurance regulatory change (i.e. Circular 65) effective from Jul, and (3) comparable base is tougher in Q2. Circular 65 demands a more granular approach in reporting of expenses and cost allocation. While the rectification process facilitates a healthier industry development, it may lead to lower actual sales incentives, suppressing bancassurance sales. In Q2-to-date, CPIC outperforms in FYRP growth (UBS-e), as the insurer changes bancassurance product strategy and strives to catch up peers. China Life also fares better than most peers in sales, but we expect YoY margin expansion to narrow in rest of the year vs Q1. Ping An faces growth pressure in Q2-to-date, as the company upholds a more disciplined approach in commission consistency following regulatory scrutiny. In H2, the key debate is centered around bancassurance - regulations would be tightened after Circular 65, but the level of enforcement is uncertain following the changes of NFRA leadership.

# Investor feedback on recent share price performance

Equity market rebounds in Q2-to-date, bringing expectation for strong earnings recovery for insurers, especially life names, in Q226 – assuming a stable equity market performance in rest of the quarter. China life insurance sector (H/A), however, fell by 5.3%/8.7% over the past week, lagging Hang Seng Index/CSI300 by 2.5 pp/6.3 pp. We gather investor feedback: From fundamental perspective, some investors are concerned about the tougher comparable base for VNB from June, given the buying spree before pricing interest rate cut at end Aug-2025. Further, A-share life names underperformed H-shares by 20 pp in YTD, possibly due to (1) reduced A-share insurance exposure by 'national team', and (2) sector rotation towards tech in A-share market (CSI Tech 50 +8.8%/STAR 50 +27%; vs Hang Seng Tech: down 12%), and (3) increased holdings of insurance (H) by insurance funds (e.g. Ping An continued to invest in China Life-H).

# Stock calls: China Life (2628.HK) & Ping An (2318.HK)

We like China Life (H), given its (1) relatively high earnings sensitivity to equity price and beta, (2) above-average FYRP growth in Q2-to-date, and (3) low base for earnings in Q2. 72% of its stocks were classified as FVTPL as of 2025 (vs peers' average: 57%). We also like Ping An (H) for its (1) sustained double-digit VNB and group OPAT growth in 2026E, and (2) attractive dividend yield of 5.3% and valuation of 6.1x P/OPAT (12M FWD).

# Equities

China

Insurance

Charles Zhou

Analyst

charles.zhou@ubs.com

+852-3712 3887

Jessica Chan

Analyst

jessica.chan@ubs.com

+852-3712 2507

Dennis Bai

Analyst

dennis.bai@ubs.com

+852-3712 2473

Figure 1: China's insurance fund AUM expanded by 2.5% QoQ to Rmb39.4 tn...   
![](images/e1540e8f7ad117446e228770bf710ecb9734eb21d721c3dc4ffe5086ec4fe489.jpg)

<details>
<summary>bar</summary>

| Year | Insurance fund AUM (Rmb tn) |
| :--- | :--- |
| 2017 | 15 |
| 2018 | 16.5 |
| 2019 | 18.5 |
| 2020 | 21.5 |
| 2021 | 23.0 |
| 2022 | 25.5 |
| 2023 | 28 |
| 2024 | 33.5 |
| 2025 | 38.5 |
| Q126 | 39.5 |
+2.5%
</details>

Source: NFRA, UBS.

Figure 2: ...partly driven by solid premium growth (+6.2% YoY)   
![](images/d3a00784aba4c90ab4ac50c1794752c9bb8d7557c62ad767776a42a4d9182bc5.jpg)

<details>
<summary>bar_line</summary>

| Quarter | Premium (Rmb bn) - Life | Premium (Rmb bn) - P&C | Total YoY chg. (%) |
| :--- | :--- | :--- | :--- |
| Q124 | 1650 | 500 | 0 |
| Q224 | 950 | 450 | 0 |
| Q324 | 850 | 400 | 0 |
| Q424 | 550 | 350 | 0 |
| Q125 | 1650 | 500 | 1.5 |
| Q225 | 1100 | 450 | 12.5 |
| Q325 | 1050 | 450 | 18.5 |
| Q425 | 600 | 350 | 0.5 |
| Q126 | 1900 | 450 | 6.5 |
</details>

Source: NFRA, UBS. Premium

Figure 3: Equity was the fastest-growing asset class in Q126   
![](images/5ca2b9c4646e05f230b73bfc695527291e178df171e4cc79ca58f450644fbff9.jpg)

<details>
<summary>bar_stacked</summary>

| Quarter | Stocks (%) | Bond (%) | Long-term equity inv. (%) | Securities inv. funds (%) | Bank deposits (%) | Others (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Q124 | 7 | 50 | 8 | 10 | 13 | 29 |
| Q224 | 7 | 53 | 8 | 10 | 13 | 29 |
| Q324 | 7 | 55 | 8 | 10 | 13 | 29 |
| Q424 | 7 | 56 | 8 | 10 | 13 | 29 |
| Q125 | 8 | 57 | 8 | 10 | 13 | 28 |
| Q225 | 8 | 58 | 8 | 10 | 13 | 28 |
| Q325 | 9 | 58 | 8 | 10 | 13 | 28 |
| Q425 | 9 | 59 | 8 | 10 | 13 | 28 |
| Q126 | 9 | 60 | 8 | 10 | 13 | 27 |
</details>

Source: NFRA, UBS.

Figure 4: 72% of China Life's stocks were classified as FVTPL as of 2025 (vs peers' average: 57%)   
![](images/139fbea3cdb22f5ecd247d393beaa352a7192062e90bdf7e347a30967b001877.jpg)

<details>
<summary>bar_stacked</summary>

| Company | FVTPL (%) | FVOCI (%) |
| :--- | :--- | :--- |
| Ping An | 43 | 57 |
| China Life | 72 | 28 |
| CPIC | 62 | 33 |
| NCI | 80 | 16 |
| Taiping | 65 | 33 |
| PICC P&C | 36 | 63 |
| PICC Group | 53 | 46 |
</details>

Source: Company data, UBS.

# Valuation Method and Risk Statement

Our price target for China Life is based on appraisal value methodology.

Our price target for Ping An is based on SOTP methodology.

Investment risks for China insurance industry include: 1) equity market downturn; 2) prolonged interest rate down-cycle; and 3) worse-than-expected operating experience variance.

# Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 18 May 2026 12:26 PM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

# Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

UBS Global Research: Global Equity Rating Definitions 

<table><tr><td>12-Month Rating</td><td>Definition</td><td>Coverage $^{1}$ </td><td>IB Services $^{2}$ </td></tr><tr><td>Buy</td><td>FSR is &gt; 6% above the MRA.</td><td>54%</td><td>24%</td></tr><tr><td>Neutral</td><td>FSR is between -6% and 6% of the MRA.</td><td>40%</td><td>21%</td></tr><tr><td>Sell</td><td>FSR is &gt; 6% below the MRA.</td><td>6%</td><td>21%</td></tr></table>

Source: UBS. Rating allocations are as of 31 March 2026.   
1: Percentage of companies under coverage globally within the 12-month rating category.   
2: Percentage of companies within the 12-month rating category for which investment banking (IB) services were provided within the past 12 months.

KEY DEFINITIONS: Forecast Stock Return (FSR) is defined as expected percentage price appreciation plus gross dividend yield over the next 12 months. In some cases, this yield may be based on accrued dividends. Market Return Assumption (MRA) is defined as the one-year local market interest rate plus 5% (a proxy for, and not a forecast of, the equity risk premium). Under Review (UR) Stocks may be flagged as UR by the analyst, indicating that the stock's price target and/or rating are subject to possible change in the near term, usually in response to an event that may affect the investment case or valuation. Equity Price Targets have an investment horizon of 12 months.

EXCEPTIONS AND SPECIAL CASES:UK and European Investment Fund ratings and definitions are: Buy: Positive on factors such as structure, management, performance record, discount; Neutral: Neutral on factors such as structure, management, performance record, discount; Sell: Negative on factors such as structure, management, performance record, discount. Core Banding Exceptions (CBE): Exceptions to the standard +/-6% bands may be granted by the Investment Review Consultation (IRC). Factors considered by the IRC include the stock's volatility and the credit spread of the respective company's debt. As a result, stocks deemed to be very high or low risk may be subject to higher or lower bands as they relate to the rating. When such exceptions apply, they will be identified in the Company Disclosures table in the relevant research piece.

Research analysts contributing to this report who are employed by any non-US affiliate of UBS LLC are not registered/qualified as research analysts with FINRA. Such analysts may not be associated persons of UBS LLC and therefore are not subject to the FINRA restrictions on communications with a subject company, public appearances, and trading securities held by a research analyst account. The name of each affiliate and analyst employed by that affiliate contributing to this report, if any, follows.

UBS AG Hong Kong Branch: Charles Zhou, Dennis Bai, Jessica Chan.

Company Disclosures 

<table><tr><td>Company Name</td><td>Reuters</td><td>12-month rating</td><td>Price</td><td>Price date</td></tr><tr><td>China Life Insurance $^{16,7,18a,6a,6b}$ </td><td>2628.HK</td><td>Buy</td><td>HK$29.76</td><td>18 May 2026</td></tr><tr><td>Ping An Insurance (Group) $^{13,4,16,28,7,18a,6a,18b}$ </td><td>2318.HK</td><td>Buy</td><td>HK$61.85</td><td>18 May 2026</td></tr></table>

Source: UBS Global Research; LSEG Eikon. All prices as of local market close. Ratings in this table are the most current published ratings prior to this report. They may be more recent than the stock pricing date.   
4. Within the past 12 months, UBS has received compensation for investment banking services from this company/entity or one of its affiliates.   
6a. This company/entity is, or within the past 12 months has been, a client of UBS LLC, and non-investment banking securities-related services are being, or have been, provided.   
6b. This company/entity is, or within the past 12 months has been, a client of UBS LLC, and non-securities services are being, or have been, provided.   
7. Within the past 12 months, UBS has received compensation for products and services other than investment banking services from this company/entity.   
13. UBS beneficially owned 1% or more of a class of this company's common equity securities as of last month's end (or the prior month's end if this report is dated less than 10 days after the most recent month's end).   
16. UBS Hong Kong Limited is a market maker in the Hong Kong-listed securities of this company.   
18a. Market capitalisation is calculated by multiplying the current share price by the sum of A and H shares.   
18b. This company/entity is, or within the past 12 months has been, a client of UBS LLC and/or its affiliates, and investment banking services are being, or have been, provided.   
28. UBS holds a long or short position of 0.5% or more of the listed shares of this company.

Unless otherwise indicated, please refer to the Valuation and Risk sections within the body of this report. For a complete set of disclosure statements associated with the companies discussed in this report, including information on valuation and risk, please contact UBS LLC, 11 Madison Avenue, New York, NY 10010, USA, Attention: Investment Research.

China Life Insurance (HK\$)   
![](images/91f2e7fcfd0cf10e569f880ae32e4becffd03fa3c50792bf222ade18d0bf417a.jpg)

<details>
<summary>line</summary>

| Date       | Price Target (HK$) | Stock Price (HK$) |
|------------|--------------------|-------------------|
| 01-Feb-23  | 20                 | 15                |
| 01-Apr-23  | 20                 | 15                |
| 01-Jun-23  | 20                 | 15                |
| 01-Aug-23  | 20                 | 15                |
| 01-Oct-23  | 20                 | 15                |
| 01-Dec-23  | 15                 | 10                |
| 01-Feb-24  | 15                 | 10                |
| 01-Apr-24  | 15                 | 10                |
| 01-Jun-24  | 15                 | 10                |
| 01-Aug-24  | 15                 | 10                |
| 01-Oct-24  | 20                 | 20                |
| 01-Dec-24  | 20                 | 15                |
| 01-Feb-25  | 20                 | 15                |
| 01-Apr-25  | 20                 | 15                |
| 01-Jun-25  | 20                 | 15                |
| 01-Aug-25  | 25                 | 20                |
| 01-Oct-25  | 30                 | 25                |
| 01-Dec-25  | 30                 | 30                |
| 01-Feb-26  | 40                 | 35                |
| 01-Apr-26  | 40                 | 30                |
</details>

Source: UBS Global Research; LSEG Eikon as of 18-May-2026. All prices as of local market close. Ratings as of date shown. 

<table><tr><td>Date</td><td>Stock Price (HK$)</td><td>Price Target (HK$)</td><td>Rating</td></tr><tr><td>2023-02-17</td><td>13.52</td><td>19.20</td><td>Buy</td></tr><tr><td>2023-03-29</td><td>13.16</td><td>18.70</td><td>Buy</td></tr><tr><td>2023-05-03</td><td>14.64</td><td>20.10</td><td>Buy</td></tr><tr><td>2023-10-31</td><td>10.60</td><td>16.00</td><td>Buy</td></tr><tr><td>2024-03-28</td><td>9.39</td><td>14.50</td><td>Buy</td></tr><tr><td>2024-10-18</td><td>16.66</td><td>19.00</td><td>Buy</td></tr><tr><td>2025-07-17</td><td>18.70</td><td>-</td><td>No Rating</td></tr><tr><td>2025-08-28</td><td>23.92</td><td>27.40</td><td>Buy</td></tr><tr><td>2025-10-20</td><td>23.52</td><td>29.00</td><td>Buy</td></tr><tr><td>2026-01-29</td><td>35.52</td><td>42.00</td><td>Buy</td></tr><tr><td>2026-03-26</td><td>25.04</td><td>40.00</td><td>Buy</td></tr></table>

Ping An Insurance (Group) (HK\$)   
![](images/627b43155f547e12843ba44da3dbbd0f21f33c6e0aa6a880f30d4deadf56bae3.jpg)

<details>
<summary>line</summary>

| Date       | Price Target (HK$) | Stock Price (HK$) |
|------------|--------------------|-------------------|
| 01-Feb-23  | 85                 | 54                |
| 01-Apr-23  | 85                 | 54                |
| 01-Jun-23  | 85                 | 54                |
| 01-Aug-23  | 85                 | 54                |
| 01-Oct-23  | 70                 | 36                |
| 01-Dec-23  | 70                 | 36                |
| 01-Feb-24

[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/5e61a3936b67dfc050c0a63e676932a62397b89246ca13237d9eb66d45169c71.jpg)
"""
