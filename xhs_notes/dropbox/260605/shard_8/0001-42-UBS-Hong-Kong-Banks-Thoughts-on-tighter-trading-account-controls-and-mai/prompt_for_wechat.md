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

# Hong Kong Banks

# Thoughts on tighter trading account controls and mainland outbound investment rules

# Additional procedures for investment account management for mainland Chinese investors

Following the CSRC's crackdown on illegal cross-border securities trading, the HKMA introduced additional measures for authorized institutions in relation to the opening and management of investment accounts held by mainland Chinese investors using mainland China-issued identification documents. In response, Hong Kong banks tightened controls on new trading account openings, requiring these investors to sign declarations covering the source of funds, document authenticity, and prior records, including confirmation that the funds were lawfully sourced outside mainland China. Since Hong Kong banks have diversified business lines, securities investment services for mainland Chinese investors likely account for only a small share of total revenue. Local Hong Kong banks could face greater pressure than international peers, given the meaningful contribution of cross-border clients to their customer base. That said, existing KYC and AML requirements should help limit the overall financial impact. We nevertheless expect new customer growth to moderate in the near term, as mainland Chinese clients have been a key growth driver over the past two to three years. For example, BOCHK reported that its cross-border high-end customer base grew by more than 20% YoY, while wealth management income rose by 40% in 2025. BEA also recorded double-digit growth in its southbound cross-boundary client base, AUM, and revenue in 2025. Although implementation details are still pending, the near-term impact appears manageable.

# Tighter outbound investment rules add further friction to capital flows

Separately, China's State Council announced a new regulation on mainland outbound investments, effective 1 July 2026. We expect the new framework to lead to closer scrutiny of outbound investments and, in turn, to weigh further on banks' corporate banking growth, particularly in business linked to mainland Chinese entities. In 2025, China's trade surplus reached US\$1.2tn, compared with only a US\$155.5bn increase in foreign exchange reserves, which may suggest that a significant share of funds is being held offshore, with Hong Kong likely serving as one of the key destinations. In our view, mainland China-related business contributes a double-digit share of revenue for local Hong Kong banks, as reflected in non-bank China exposure accounting for 40% of the banking system's loan portfolio. Against this backdrop, tighter scrutiny of capital flows could create downside risk for excess deposits, cash management and custodian services, insurance product distribution, and securities and brokerage trading. Overall, the measure adds another layer of uncertainty for the sector in the near term.

# Valuation: Reiterate Neutral on BOCHK and BEA

Tighter regulations are likely to weigh on market sentiment in the near term. For BOCHK, we view valuation as stretched at 1.4x 2026E P/B, with a dividend yield of 4.9%, and we continue to monitor further details of the three-year shareholder framework. For BEA, while the stock appears undemanding at 0.3x 2026E P/B, the key question remains where credit cost will settle in 2026, as this will be an important indicator of its progress toward the 7% ROE target by 2028.

# Equities

Hong Kong

Banks

Helen Li, CFA

Analyst

helen-za.li@ubs.com

+852-2971 6066

May Yan

Analyst

may.yan@ubs.com

+852-2971 7157

Jason Napier, CFA

Analyst

jason.napier@ubs.com

+44-20-7568 5037

Angus Chan

Analyst

angus.chan@ubs.com

+852-2971 7530

Perry Yeung

Analyst

perry.yeung@ubs.com

+852-2971 6349

Sanjena Dadawala

Analyst

sanjena.dadawala@ubs.com

+44-20-7567 0753

# Valuation Method and Risk Statement

Hong Kong banks are large, highly leveraged financial institutions operating across a number of markets, and as such are subject to the risk of changes in the general business and economic conditions within these markets. A change in these conditions could include changes in interest rates, inflation, unemployment, monetary supply, exogenous shocks, foreign exchange rates, and the health of the general economy. The banks also face the risk of regulatory changes and increased competition, which could affect the profitability of the sector. A key risk that financial institutions face is associated with extending credit to other parties. Less favourable business conditions could cause potential losses from loans to increase, thereby putting pressure on the group's capital. The bank sector also faces operational risk from operating such large and complex businesses.

Our price targets are derived using a DDM based valuation approach.

Upside risks BOCHK include: 1) faster-than-expected economic recovery in mainland China and Hong Kong; 2) faster balance sheet expansion at or above current profitability; and 3) stronger-than expected recovery in capital market, driving up fee income. Downside risks to our Neutral rating on BOCHK include: 1) slower-than-expected economic recovery that weighs on both NIM and loan growth; 2) higher asset quality risk from mainland/HK CRE and Southeast Asia exposure, 3) prolonged weakness in capital market performance that weighs on fee income.

Upside risks for BEA include: 1) strong policy loosening in China's property sector; 2) delayed and reduced Fed rate cuts; and 3) further restructuring plans involving disposal of low-return operating segments. Downside risks include: 1) worse-than-expected NPL trends especially in the bank's China property developer loan book; and 2) unsatisfactory dividend payout policies.

# Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 02 June 2026 11:08 PM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

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

UBS AG Hong Kong Branch: Angus Chan, Helen Li, CFA, May Yan, Perry Yeung. UBS AG London Branch: Jason Napier, CFA, Sanjena Dadawala.

Company Disclosures 

<table><tr><td>Company Name</td><td>Reuters</td><td>12-month rating</td><td>Price</td><td>Price date</td></tr><tr><td>Bank of China (Hong Kong) $^{16,28,7,6a,6b}$ </td><td>2388.HK</td><td>Neutral</td><td>HK$48.00</td><td>02 Jun 2026</td></tr><tr><td>Bank of East Asia $^{28,7,6a,6b}$ </td><td>0023.HK</td><td>Neutral</td><td>HK$13.78</td><td>02 Jun 2026</td></tr></table>

Source: UBS Global Research; LSEG Eikon. All prices as of local market close. Ratings in this table are the most current published ratings prior to this report. They may be more recent than the stock pricing date.

6a. This company/entity is, or within the past 12 months has been, a client of UBS LLC, and non-investment banking securities-related services are being, or have been, provided.

6b. This company/entity is, or within the past 12 months has been, a client of UBS LLC, and non-securities services are being, or have been, provided.

7. Within the past 12 months, UBS has received compensation for products and services other than investment banking services from this company/entity.

16. UBS Hong Kong Limited is a market maker in the Hong Kong-listed securities of this company.

28. UBS holds a long or short position of 0.5% or more of the listed shares of this company.

Unless otherwise indicated, please refer to the Valuation and Risk sections within the body of this report. For a complete set of disclosure statements associated with the companies discussed in this report, including information on valuation and risk, please contact UBS LLC, 11 Madison Avenue, New York, NY 10010, USA, Attention: Investment Research.

Bank of East Asia (HK\$)   
![](images/1d4265d3deea4faed3b47b9b1e3944e9ef99775103d7129be031df67116f37c0.jpg)

<details>
<summary>line</summary>

| Date       | Price Target (HK$) | Stock Price (HK$) |
|------------|--------------------|-------------------|
| 01-Apr-23  | 12.0               | 11.5              |
| 01-Jun-23  | 12.0               | 10.8              |
| 01-Aug-23  | 12.0               | 11.2              |
| 01-Oct-23  | 12.0               | 10.5              |
| 01-Dec-23  | 12.0               | 9.8               |
| 01-Feb-24  | 12.0               | 9.5               |
| 01-Apr-24  | 12.0               | 9.7               |
| 01-Jun-24  | 12.0               | 10.0              |
| 01-Aug-24  | 11.5               | 9.8               |
| 01-Oct-24  | 11.5               | 9.5               |
| 01-Dec-24  | 11.5               | 9.7               |
| 01-Feb-25  | 11.5               | 10.5              |
| 01-Apr-25  | 11.5               | 11.0              |
| 01-Jun-25  | 12.0               | 11.5              |
| 01-Aug-25  | 12.5               | 12.0              |
| 01-Oct-25  | 12.5               | 12.5              |
| 01-Dec-25  | 13.0               | 13.0              |
| 01-Feb-26  | 13.5               | 14.0              |
| 01-Apr-26  | 13.5               | 13.5              |
| 01-Jun-26  | 13.5               | 13.0              |
</details>

Source: UBS Global Research; LSEG Eikon as of 02-Jun-2026. All prices as of local market close. Ratings as of date shown. 

<table><tr><td>Date</td><td>Stock Price (HK$)</td><td>Price Target (HK$)</td><td>Rating</td></tr><tr><td>2023-03-02</td><td>11.10</td><td>12.00</td><td>Neutral</td></tr><tr><td>2023-07-04</td><td>10.86</td><td>-</td><td>No Rating</td></tr><tr><td>2023-07-14</td><td>11.42</td><td>12.00</td><td>Neutral</td></tr><tr><td>2023-12-12</td><td>9.41</td><td>12.00</td><td>Buy</td></tr><tr><td>2024-07-12</td><td>10.00</td><td>10.50</td><td>Neutral</td></tr><tr><td>2024-08-22</td><td>9.55</td><td>9.80</td><td>Neutral</td></tr><tr><td>2025-01-06</td><td>9.90</td><td>9.90</td><td>Neutral</td></tr><tr><td>2025-02-20</td><td>10.56</td><td>10.20</td><td>Neutral</td></tr><tr><td>2025-05-23</td><td>11.28</td><td>11.50</td><td>Neutral</td></tr><tr><td>2025-07-03</td><td>12.20</td><td>12.00</td><td>Neutral</td></tr><tr><td>2025-08-21</td><td>13.52</td><td>13.00</td><td>Neutral</td></tr><tr><td>2025-09-25</td><td>11.70</td><td>12.50</td><td>Neutral</td></tr><tr><td>2025-12-22</td><td>13.32</td><td>13.50</td><td>Neutral</td></tr><tr><td>2026-02-13</td><td>14.14</td><td>14.50</td><td>Neutral</td></tr></table>

Bank of China (Hong Kong) (HK\$)   
![](images/a6bcda831e79b48fec5b79c6bf9b1a78452e14ff65bf1dd7deb3ec2398333d37.jpg)

<details>
<summary>line</summary>

| Date       | Price Target (HK$) | Stock Price (HK$) |
|------------|--------------------|-------------------|
| 01-Apr-23  | 37                 | 27                |
| 01-Jun-23  | 37                 | 25                |
| 01-Aug-23  | 29                 | 23                |
| 01-Oct-23  | 29                 | 22                |
| 01-Dec-23  | 21                 | 20                |
| 01-Feb-24  | 20                 | 19                |
| 01-Apr-24  | 21                 | 21                |
| 01-Jun-24  | 23                 | 24                |
| 01-Aug-24  | 24                 | 25                |
| 01-Oct-24  | 25                 | 26                |
| 01-Dec-24  | 26                 | 27                |
| 01-Feb-25  | 27                 | 28                |
| 01-Apr-25  | 30                 | 31                |
| 01-Jun-25  | 35                 | 36                |
| 01-Aug-25  | 37                 | 38                |
| 01-Oct-25  | 38                 | 39                |
| 01-Dec-25  | 39                 | 40                |
| 01-Feb-26  | 40                 | 41                |
| 01-Apr-26  | 43                 | 44                |
| 01-Jun-26  | 44                 | 48                |
</details>

<table><tr><td>Date</td><td>Stock Price (HK$)</td><td>Price Target (HK$)</td><td>Rating</td></tr><tr><td>2023-03-02</td><td>26.90</td><td>36.00</td><td>Buy</td></tr><tr><td>2023-07-24</td><td>22.75</td><td>28.00</td><td>Buy</td></tr><tr><td>2023-12-12</td><td>20.45</td><td>20.00</td><td>Neutral</td></tr><tr><td>2024-04-17</td><td>22.55</td><td>21.80</td><td>Neutral</td></tr><tr><td>2024-07-11</td><td>23.00</td><td>24.00</td><td>Neutral</td></tr><tr><td>2024-10-18</td><td>25.60</td><td>26.50</td><td>Neutral</td></tr><tr><td>2025-01-06</td><td>24.90</td><td>26.00</td><td>Neutral</td></tr><tr><td>2025-04-16</td><td>29.25</td><td>29.00</t

[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/256eb9fd99b85206e7239d85546b4fb27f7e81cca5df0f063de21e0b49a4f4db.jpg)
"""
