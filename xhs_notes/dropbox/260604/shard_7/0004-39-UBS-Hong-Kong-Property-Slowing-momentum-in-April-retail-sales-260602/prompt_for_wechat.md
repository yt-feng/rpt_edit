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

# Hong Kong Property

# Slowing momentum in April retail sales

# April retail sales up 9% YoY, in-line with UBSe

The Hong Kong government released April retail sales figures today. Overall retail sales rose 9% YoY, compared with +13% YoY in March and +12% in 2M26, in line with our expectation of high-single-digit growth. Similar to March, key growth drivers remained: i) strong gold price performance; ii) continued robust demand for new iPhones; and iii) delayed delivery of electric vehicles following the expiration of the first registration tax exemption at end-March. However, all three key categories have seen a moderation in growth. Excluding consumer electronics (+22% YoY in April) and motor vehicles and parts (+46% YoY in April), April retail sales growth would have slowed to 6% YoY, compared with +8% YoY in March and +9% in 2M26, implying a marginal deceleration in underlying demand.

# Excluding price effects, luxury sales volume up 6.5% YoY

By segment, luxury goods growth slowed to 20% YoY in April, compared with +28% YoY in March. However, after adjusting for price effects, luxury sales volume remained broadly stable at 6.5% YoY versus +6.4% YoY in March, indicating stabilisation in volume growth. On the staples side, food beverage sales were flat YoY in April, compared with +1% YoY growth in March, while supermarkets returned to 3% YoY growth after remaining broadly flat in March. Online retail sales growth moderated slightly to 31% YoY in April, compared with +35% YoY in March. As headline retail sales slowed, online penetration remained stable at 10% MoM.

# May retail sales growth likely at mid to high single digit

Looking ahead to May 2026, we expect retail sales growth to come in at mid- to high-single digits, supported by several factors. First, both mainland and overseas visitor arrivals recorded growth of 12% and 3% YoY, respectively, in April, compared with +10% and +8% in March. The slowdown in overseas visitors could be linked to recent increases in airfares following the Middle East conflict. Second, weaker gold prices sequentially may continue to weigh on luxury spending growth. Outbound travel to the mainland remained largely stable at +10% YoY in April, compared with +9% in March, while overseas outbound travel narrowed to a 1% decline, versus a 12% decline in March. This should provide some support to local consumption.

# Stock views:

We believe the slowing momentum in luxury goods in April 2026 has negative read-across for discretionary-focused retail landlords such as WREIC and Hysan. Meanwhile, the slight pickup in supermarket sales could act as a positive catalyst for Link REIT.

# Equities

Hong Kong

Real Estate

Mark Leung

Analyst

mark.leung@ubs.com

+852-2971 8636

John Lam, CFA

Analyst

john-za.lam@ubs.com

+852-2971 6358

Ben Ho

Associate Analyst

ben.ho@ubs.com

+852-3712 2819

Vera Gong, CFA

Analyst

vera.gong@ubs.com

+852-2971 8950

Figure 1: Hong Kong's retail sales rose by 9% YoY in Apr, in-line with our forecast of high single digit increase   
![](images/fe78c62e3cd274015160f2cd6ae3f9bd10ba129ba253fcbe86aa8c67afd12b97.jpg)

<details>
<summary>bar_line</summary>

HK retail sales value (HK$m)
| Date | HK retail sales value (HK$m) | YoY growth (%) |
|---|---|---|
| Oct-18 | 40,000 | 5.0 |
| Apr-19 | 48,000 | 3.0 |
| Oct-19 | 35,000 | -10.0 |
| Apr-20 | 25,000 | -45.0 |
| Oct-20 | 30,000 | 15.0 |
| Apr-21 | 40,000 | 30.0 |
| Oct-21 | 35,000 | 10.0 |
| Apr-22 | 30,000 | -15.0 |
| Oct-22 | 35,000 | 5.0 |
| Apr-23 | 45,000 | 40.0 |
| Oct-23 | 35,000 | 15.0 |
| Apr-24 | 30,000 | -15.0 |
| Oct-24 | 35,000 | -10.0 |
| Apr-25 | 35,000 | 5.0 |
| Oct-25 | 35,000 | 15.0 |
| Apr-26 | 35,000 | 25.0 |
</details>

Source: CEIC

Figure 2: The April retail sales recovery rate reached 79% (vs 2018)   
![](images/4ba0a417d9339a293aeea838c0b8bc480ed06e26b6bac4ebe16616b02fbd1f18.jpg)

<details>
<summary>bar_line</summary>

HK retail sales vs mainland visitation recovery rate vs 2018
| Month | HK retail sales recovery rate (%) | Mainland visitors recovery rate (%) | Other visitors recovery rate (%) |
|---|---|---|---|
| Jan-23 | 75 | 10 | 20 |
| Feb-23 | 80 | 40 | 35 |
| Mar-23 | 85 | 55 | 45 |
| Apr-23 | 85 | 60 | 50 |
| May-23 | 85 | 65 | 55 |
| Jun-23 | 85 | 70 | 60 |
| Jul-23 | 85 | 75 | 65 |
| Aug-23 | 85 | 70 | 60 |
| Sep-23 | 85 | 60 | 65 |
| Oct-23 | 85 | 55 | 70 |
| Nov-23 | 85 | 60 | 75 |
| Dec-23 | 85 | 65 | 80 |
| Jan-24 | 85 | 70 | 85 |
| Feb-24 | 85 | 75 | 90 |
| Mar-24 | 85 | 70 | 85 |
| Apr-24 | 85 | 65 | 80 |
| May-24 | 85 | 70 | 75 |
| Jun-24 | 85 | 75 | 80 |
| Jul-24 | 85 | 70 | 75 |
| Aug-24 | 85 | 65 | 70 |
| Sep-24 | 85 | 60 | 65 |
| Oct-24 | 85 | 55 | 60 |
| Nov-24 | 85 | 60 | 65 |
| Dec-24 | 85 | 65 | 70 |
| Jan-25 | 85 | 70 | 75 |
| Feb-25 | 85 | 75 | 80 |
| Mar-25 | 85 | 70 | 85 |
| Apr-25 | 85 | 65 | 90 |
| May-25 | 85 | 70 | 85 |
| Jun-25 | 85 | 75 | 80 |
| Jul-25 | 85 | 70 | 75 |
| Aug-25 | 85 | 65 | 70 |
| Sep-25 | 85 | 60 | 65 |
| Oct-25 | 85 | 65 | 70 |
| Nov-25 | 85 | 70 | 75 |
| Dec-25 | 85 | 75 | 80 |
| Jan-26 | 85 | 80 | 85 |
| Feb-26 | 85 | 85 | 90 |
| Mar-26 | 85 | 90 | 95 |
| Apr-26 | 85 | 95 | 90 |
| May-26 | 85 | 90 | 85 |
Source: UK Invitational Department, Group & Service Department UBC
</details>

Source: CEIC

Figure 3: Electrical goods, luxury goods and EV sales continued to drive the retail sales growth in Apr   
![](images/badd0b0dd59a31d3ae58a71d6b96602f2b19622ac40f917f8d7b5fc7d7a1b14b.jpg)

<details>
<summary>bar</summary>

| Category | Apr-26 (%) | Mar-26 (%) | 2M26 (%) |
| :--- | :--- | :--- | :--- |
| Clothing, Footwear and Allied Products (CF) | 5 | 6 | 7 |
| Supermarkets | 3 | 0 | 3 |
| Department Stores | -7 | 1 | 6 |
| Consumer Durable Goods (CD) | 26 | 41 | 30 |
| HK retail sales value | 9 | 13 | 12 |
| Food, Alcoholic Drinks and Tobacco (FA) | 0 | 1 | 3 |
| Jewellery, Watches, Clocks & Valuable Gift | 20 | 28 | 28 |
| Medicines, Cosmetics | 2 | 3 | 8 |
</details>

Source: CEIC

Figure 4: Online penetration remained at 10% in Apr 2026   
![](images/87df289ba3f81526e325e35b8a7a00a49cc33c9b5af9437eda1a7722ea862063.jpg)

<details>
<summary>bar_line</summary>

HK online retail sales growth vs online penetration
| Date | HK online retail sales growth (LHS) (%) | Trailing 12m e-commerce penetration - RHS (%) |
|---|---|---|
| Jul-21 | 30 | 8.5 |
| Oct-21 | 34 | 8.7 |
| Jan-22 | 50 | 9.0 |
| Apr-22 | 35 | 9.1 |
| Jul-22 | 20 | 9.2 |
| Oct-22 | 35 | 9.6 |
| Jan-23 | 12 | 9.8 |
| Apr-23 | -15 | 8.8 |
| Jul-23 | -5 | 8.5 |
| Oct-23 | 22 | 8.7 |
| Jan-24 | -30 | 7.8 |
| Apr-24 | 10 | 8.0 |
| Jul-24 | -5 | 8.3 |
| Oct-24 | -15 | 8.5 |
| Jan-25 | -5 | 8.6 |
| Apr-25 | -5 | 8.7 |
| Jul-25 | 10 | 8.8 |
| Oct-25 | 30 | 9.1 |
| Jan-26 | 35 | 9.4 |
| Apr-26 | 33 | 9.7 |
</details>

Source: CEIC

Figure 5: Monthly HK residents' northbound departures have recently stabilized at +10% in May   
![](images/1b463034e3ea229bb6d4311655f02b52633db91fc8f5dca195d343629ff64709.jpg)

<details>
<summary>bar</summary>

| Date    | Value (Millions) |
|---------|------------------|
| Sep-10  | 5.8              |
| Mar-11  | 5.7              |
| Sep-11  | 5.8              |
| Mar-12  | 5.9              |
| Sep-12  | 5.8              |
| Mar-13  | 5.7              |
| Sep-13  | 5.6              |
| Mar-14  | 5.5              |
| Sep-14  | 5.6              |
| Mar-15  | 5.7              |
| Sep-15  | 5.8              |
| Mar-16  | 5.9              |
| Sep-16  | 6.0              |
| Mar-17  | 6.1              |
| Sep-17  | 6.2              |
| Mar-18  | 6.3              |
| Sep-18  | 6.4              |
| Mar-19  | 6.5              |
| Sep-19  | 6.6              |
| Mar-20  | 6.7              |
| Sep-20  | 6.8              |
| Mar-21  | 6.9              |
| Sep-21  | 7.0              |
| Mar-22  | 7.1              |
| Sep-22  | 7.2              |
| Mar-23  | 7.3              |
| Sep-23  | 7.4              |
| Mar-24  | 7.5              |
| Sep-24  | 7.6              |
| Mar-25  | 7.7              |
| Sep-25  | 7.8              |
| Mar-26  | 7.9              |
</details>

Source: CEIC

Figure 6: Overseas departure volumes by HK residents was slightly down 1% in May   
![](images/1768e53bb745cfa3a2cc545254f6938eac9727918e1f204938d93d7b04954532.jpg)

<details>
<summary>bar</summary>

| Date     | Value (Millions) |
|----------|------------------|
| Sep-01   | 0.4              |
| Mar-02   | 0.4              |
| Sep-03   | 0.4              |
| Mar-04   | 0.4              |
| Sep-05   | 0.4              |
| Mar-06   | 0.4              |
| Sep-06   | 0.4              |
| Mar-07   | 0.4              |
| Sep-07   | 0.4              |
| Mar-08   | 0.4              |
| Sep-08   | 0.4              |
| Mar-09   | 0.4              |
| Sep-09   | 0.4              |
| Mar-10   | 0.4              |
| Sep-10   | 0.4              |
| Mar-11   | 0.4              |
| Sep-11   | 0.4              |
| Mar-12   | 0.4              |
| Sep-12   | 0.4              |
| Mar-13   | 0.4              |
| Sep-13   | 0.4              |
| Mar-14   | 0.4              |
| Sep-14   | 0.4              |
| Mar-15   | 0.4              |
| Sep-15   | 0.4              |
| Mar-16   | 0.4              |
| Sep-16   | 0.4              |
| Mar-17   | 0.4              |
| Sep-17   | 0.4              |
| Mar-18   | 0.4              |
| Sep-18   | 0.4              |
| Mar-19   | 0.4              |
| Sep-19   | 0.4              |
| Mar-20   | 0.4              |
| Sep-20   | 0.4              |
| Mar-21   | 0.4              |
| Sep-21   | 0.4              |
| Mar-22   | 0.4              |
| Sep-22   | 0.4              |
| Mar-23   | 0.4              |
| Sep-23   | 0.4              |
| Mar-24   | 0.4              |
| Sep-24   | 0.4              |
| Mar-25   | 0.4              |
| Sep-25   | 0.4              |
| Mar-26   | 0.4              |
</details>

Source: CEIC

# Valuation Method and Risk Statement

We believe the key risks related to the Hong Kong property sector include: 1) weakening macroeconomic conditions; 2) a gradual increase in new housing supply; 3) higher-than-expected US Fed rate hikes.

Hysan: Our NAV-based valuation for Hysan is derived from a methodology of yield capitalisation on its investment property portfolio. Hysan has high exposure to Hong Kong office/retail properties. Therefore, our estimates depend on the performance of the Hong Kong commercial leasing market. We believe government policies, mortgage rate hikes, new supply, and global economic outlook are the main risks to the Hong Kong property market. We believe key downside risks to the Hong Kong office market include the level of social unrest, business confidence, and Chinese corporate office demand. For retail, we believe the uncertain political environment, a lack of central government policy support, and narrowing price differentials between Hong Kong and China are the key downside risks.

Link REIT: We derive our price target from a dividend discount model. Link REIT's ability to raise rent depends heavily on tenants' profitability, which relies on domestic macroeconomic conditions, especially factors that affect consumer spending in Hong Kong. Upside risk on further lower US 10-yr treasury yield and weakening HKD against USD. Downside risk on US 10-yr treasury yield further increases, outbound consumption leakage further picks up due to remained strong HKD, significantly delayed launch schedule for REIT connect.

Wharf REIC: We derive our price target from a dividend discount model. The performance of Wharf REIC's two flagship shopping centres in Hong Kong (Harbour City and Times Square) depends on the inflow of mainland Chinese shoppers and local economic conditions. Key downside risks include a slower-than-expected tourist spending recovery, fast growing onshore duty-free sales and the potential downgrade of Times Square. Upside risks include a stronger-than-expected recovery in tourist spending in Hong Kong and Macau due to the ongoing closure of international borders to Chinese tourists, which would result in Hong Kong and Macau becoming the only outbound travel destinations for Chinese tourists.

# Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 02 June 2026 02:33 PM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

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

UBS AG Hong Kong Branch: Ben Ho, John Lam, CFA, Mark Leung, Vera Gong, CFA.

Company Disc

[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/f7c23a9f411f54fa2c28fa2656856125f1dc72493a950fad154989ae365f17ff.jpg)
"""
