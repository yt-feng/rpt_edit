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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Hong Kong Property | Asia Pacific

# Expect Call with C&W; Robust Data but Uncertain Sentiment

## Key Takeaways

We hosted an expert call with Miss Rosanna Tang, Head of Research at Cushman & Wakefield, on Hong Kong Property. Key takeaways include:  
(+) Residential: 5M26 sales +44% YoY – the 15th straight month of 5k+ units. 2026 ASP to rise 7-10% (YTD +6% by R&V).  
(=) Uncertainty on residential volume/price from new outbound investment rules, stock market volatility and interest rate uncertainty, but no impact yet.  
(+) Grade A office is improving, with Central and West Kowloon leading the recovery, helped by banking and finance demand and peaked-out supply.  
MS view: Still constructive despite recent underperformance and concerns (rates and regulation). Valuation at a 50% discount to NAV remains attractive.

(+) Completed residential inventory fell to 20K in 1Q26, down 30% from the 28K peak in 1Q25. Student accommodation is a new opportunity, with a student-to-bed ratio of 3.4:1 across HK's eight major universities. Beds equal roughly half the number of non-local students.  
(+) C&W expects office rents to rise in Greater Central (+6-8%) and Prime Central (+6-8%). Net absorption stayed positive at 217K in 1Q26. Office supply remains limited at 2.6m sf over 2026-29.  
(+) HK Retail sales grew 11.3% YoY in 4M, helped by visitation (+15% YoY) and a stronger RMB. High-street rents are rising, with zero vacancy in Central/CWB.

Our view: We prefer stocks with visible launches, improving margin and growing total shareholders' return: CKA (OW), Hongkong Land (OW) and Swire Properties (OW).

Exhibit 1: Official R&V Home Price Rose 5.7% YTD  
![](images/28fd93b8a93fed03940f9ea8fa2fe83d011d487c8384e017c7c881711217fb23.jpg)

<details>
<summary>line chart</summary>

| Date   | Private domestic price index | YoY change |
|--------|------------------------------|----------|
| Jan-15 | 290                          | 350      |
| Jan-16 | 310                          | 300      |
| Jan-17 | 330                          | 250      |
| Jan-18 | 350                          | 200      |
| Jan-19 | 390                          | 150      |
| Jan-20 | 370                          | 100      |
| Jan-21 | 380                          | 50       |
| Jan-22 | 390                          | 0        |
| Jan-23 | 350                          | -50      |
| Jan-24 | 310                          | -100     |
| Jan-25 | 290                          | -150     |
| Jan-26 | 310                          | -200     |
</details>

Source: RVD, MS

Exhibit 2: Office - 1Q26 New Lettings  
![](images/16ccb07d33256eeb1370fb180b8f9242f932a1cd6b30f30ac1eda45041826c58.jpg)

<details>
<summary>pie chart</summary>

| Category | Percentage (%) |
| :--- | :--- |
| Banking & finance | 61 |
| Insurance | 13 |
| Consumer products / manufacturing | 9 |
| TMT | 6 |
| Business center... | 3 |
| Professional services & real estate | 3 |
| Others | 4 |
</details>

Source: Cushman & Wakefield, MS Note: Data up to mid-March, 2026.

Miss Rosanna Tang is not member of MS's Research Department. Unless otherwise indicated, his view is their own and may differ from the views of the MS Department and from the views of others within MS.

MS ASIA LIMITED+

Praveen K Choudhary

Equity Analyst

Praveen.Choudhary@morganstanley.com

+852 2848-5068

Anson Lee, CFA

Research Associate

Anson.Lee@morganstanley.com

+852 2239-7435

![](images/de2fe62e67866beb6e5024318c377bc084ec5dfba6baa2cc46b443b4b6faa9d8.jpg)

<details>
<summary>text_image</summary>

Asia Summer School 2026
</details>

## HONG KONG PROPERTY

Asia Pacific

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Valuation Methodology and Risks

## CK Asset Holdings Ltd (1113.HK)

Base-case value, derived from a sum-of-the-parts valuation. We apply a 30% target discount to NAV, 1.5SD above historical average, given better-than-expected home price recovery and defensive gearing level.

## Risks to Upside

■ Announcement of a new buyback plan  
■ Successful launch of its residential projects in Hong Kong  
■ Successful acquisition of sizable recurring income business such as infrastructure

## Risks to Downside

■ Deeper conglomerate discount if more geographically diverse assets are added  
■ Pure-play property investors exiting  
■ Higher cost pressure in its pub and hotel businesses  
■ Higher-for-longer interest rate environment

## Swire Properties (1972.HK)

Base case scenario value, from sum-of-the-parts analysis.

HK - Office and retail: Gross cap rates of 4.75% and 5.75%, respectively.

China - Office and retail: Gross cap rates of 7.0% and 8.0%, respectively. Rents remain stable.

HK development properties: DCF, WACC of 8%.

30% NAV discount: 1SD above average since 2011.

## Risks to Upside

■ Faster-than-expected ramp up of new investment properties to grow recurring income base  
■ More capital recycling to unlock asset value  
■ Strong recovery in office and retail segments in Hong Kong

## Risks to Downside

■ Slow recovery in HK office and retail  
■ Slowdown in China retail recovery  
■ Difficulty in off-loading non-core assets

## Hongkong Land (HKLD.SI)

Base case scenario value, from sum-of-the-parts analysis.

HK office and HK retail: Gross cap rates of 4.75% and 5.75%, respectively.

China DP: 1x EV/Asset, reflecting current book value.

20% NAV discount: 1SD above long-term average since 2011.

## Risks to Upside

■ Faster-than-expected capital recycling  
■ Value-accretive acquisitions  
■ Turnaround in Hong Kong retail and office

## Risks to Downside

■ Core business EBIT to remain challenged  
■ A lot of upside already in the price  
■ Difficulty sourcing third-party capital  
■ Difficulty recycling capital  
■ Worse-than-expected supply/demand mismatch in Hong Kong office market

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Praveen K Choudhary.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from CK Asset Holdings Ltd, Hang Lung Properties Ltd., Henderson Land, Hongkong Land, Hysan Development Company Ltd., Link REIT, New World Development, Sun Hung Kai Properties, Swire Properties, Wharf Holdings, Wharf REIC.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Henderson Land, New World Development, Sun Hung Kai Properties, Wharf Holdings, Wharf REIC.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: CK Asset Holdings Ltd, Hang Lung Properties Ltd., Henderson Land, Hongkong Land, Hysan Development Company Ltd., Link REIT, New World Development, Sun Hung Kai Properties, Swire Properties, Wharf Holdings, Wharf REIC.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: CK Asset Holdings Ltd, Henderson Land, New World Development, Sun Hung Kai Properties, Wharf Holdings, Wharf REIC. The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

(as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment ServicesClients (MISC)</td></tr><tr><td>Stock RatingCategory</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of RatingCategory</td><td>Count</td><td>% of Total OtherMISC</td></tr><tr><td>Overweight/Buy</td><td>1542</td><td>42%</td><td>465</td><td>51%</td><td>30%</td><td>707</td><td>43%</td></tr><tr><td>Equal-weight/Hold</td><td>1571</td><td>43%</td><td>369</td><td>40%</td><td>23%</td><td>723</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>3</td><td>0%</td><td>0</td><td>0%</td><td>0%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>551</td><td>15%</td><td>86</td><td>9%</td><td>16%</td><td>201</td><td>12%</td></tr><tr><td>Total</td><td>3,667</td><td></td><td>920</td><td></td><td></td><td>1632</td><td></td></tr></table>

Data include common stock and ADRs currently assigned ratings. Investment Banking Clients are companies from whom MS received investment banking compensation in the last 12 months. Due to rounding off of decimals, the percentages provided in the "% of total" column may not add up to exactly 100 percent.

## Analyst Stock Ratings

Overweight (O). The stock's total return is expected to exceed the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Equal-weight (E). The stock's total return is expected to be in line with the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Not-Rated (NR). Currently the analyst does not have adequate conviction about the stock's total return relative to the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Underweight (U). The stock's total return is expected to be below the average total return of the analyst's industry (or industry team's) coverage universe, on a risk-adjusted basis, over the next 12-18 months.

Unless otherwise specified, the time frame for price targets included in MS is 12 to 18 months.

## Analyst Industry Views

Attractive (A): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be attractive vs. the relevant broad market benchmark, as indicated below.

In-Line (I): The analyst expects the performance of his or her industry coverage universe over the next 12-18 months to be in line with the relevant broad market benchmark, as indicated below. Cautious (C): The analyst views the performance of his or her industry coverage universe over the next 12-18 months with caution vs. the relevant broad market benchmark, as indicated below. Benchmarks for each region are as follows: North America - S&P 500; Latin America - relevant MSCI country index or MSCI Latin America Index; Europe - MSCI Europe; Japan - TOPIX; Asia - relevant MSCI country index or MSCI sub-regional index or MSCI AC Asia Pacific ex Japan Index.

Stock Price, Price Target and Rating History (See Rating Definitions)

CK Asset Holdings Ltd (1113.HK) - As of 06/11/26 GMT in HKD
Industry : Hong Kong Property  
![](images/4cec0477bf7c571a4265a8ccb95940ef6d40dd45775d002c9c7db5cdea1a45d8.jpg)

<details>
<summary>line chart</summary>

| Date       | Value |
| ---------- | ----- |
| 06/01 2023 | 59    |
|            | 58    |
|            | 51    |
|            | 52    

[中间内容因长度限制已省略]

s and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of CK Asset Holdings Ltd, Henderson Land, Link REIT, Sun Hung Kai Properties listed on the

Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Hong Kong Property

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/11/2026)</td></tr><tr><td colspan="3">Praveen K Choudhary</td></tr><tr><td>CK Asset Holdings Ltd (1113.HK)</td><td>O (01/06/2026)</td><td>HK$45.54</td></tr><tr><td>Hang Lung Properties Ltd. (0101.HK)</td><td>O (09/05/2025)</td><td>HK$7.61</td></tr><tr><td>Henderson Land (0012.HK)</td><td>O (05/04/2026)</td><td>HK$26.68</td></tr><tr><td>Hongkong Land (HKLD.SI)</td><td>O (05/19/2025)</td><td>US$7.19</td></tr><tr><td>Hysan Development Company Ltd. (0014.HK)</td><td>E (01/06/2026)</td><td>HK$16.93</td></tr><tr><td>Kerry Properties (0683.HK)</td><td>E (05/30/2023)</td><td>HK$19.88</td></tr><tr><td>Link REIT (0823.HK)</td><td>O (05/04/2026)</td><td>HK$36.44</td></tr><tr><td>New World Development (0017.HK)</td><td>U (12/13/2023)</td><td>HK$7.46</td></tr><tr><td>Sino Land (0083.HK)</td><td>E (06/19/2025)</td><td>HK$11.12</td></tr><tr><td>Sun Hung Kai Properties (0016.HK)</td><td>O (12/07/2022)</td><td>HK$115.20</td></tr><tr><td>Swire Properties (1972.HK)</td><td>O (01/06/2026)</td><td>HK$21.42</td></tr><tr><td>Wharf Holdings (0004.HK)</td><td>U (10/11/2023)</td><td>HK$19.66</td></tr><tr><td>Wharf REIC (1997.HK)</td><td>U (12/13/2024)</td><td>HK$22.08</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
