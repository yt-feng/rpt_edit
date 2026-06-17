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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Citi`。标题格式建议：`# Citi：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
15 Jun 2026 15:42:00 ET | 11 pages

# Global FX Strategy

## Fade EUR rallies if Warsh disappoints hawks

## CITI'S TAKE

The FOMC is unlikely to deliver the hawkish surprise needed to finally break the USD out of its 12-month range. On the contrary, increasing potential for an Iran deal, which we expect new Fed Chair Warsh will lean into, could be an additional factor for looking past any commodity-induced inflation surprises. While we had been more tactically cautious risk assets, the combination of a potential deal, Warsh delivering a neutral message, and a successful major IPO last week could see risk stabilize and rally. In FX, that should see carry trades resume, which we prefer funding with EUR and CAD.

## Daniel Tobon AC

+1-212-816-8340

daniel.tobon@citi.com

## Brian Levine AC

+1-212-816-6896

brian.levine@citi.com

## Osamu Takashima

+81-3-6776-3251

osamu.takashima@citi.com

Despite significant interest for Kevin Warsh's first meeting, we do not expect any big surprises this week. Market expectations already lean towards a hawkish statement and SEP: (1) the statement is likely to drop the easing bias; (2) the core PCE forecast should be revised higher; and (3) the median dot likely shifts to no change for 2026 (we might even see a dot or two move towards a hike, but this is more of a risk than a base case). In our view, these changes should not cause a significant FX reaction, as they are already priced in.

The real uncertainty for markets is what we will hear from Warsh during the press conference. While many questions and answers will focus on Warsh's potential structural changes for the Fed, we think the most immediate focus for FX will be around Warsh's attitude towards current market pricing (+18bps of hikes through year-end, with the first hike fully priced for March 2027). Our base case is Warsh will rely on his view of providing less forward guidance to give ambiguous answers towards current market pricing. A potential US-Iran deal and weaker CPI give the Fed room to look past goods and energy inflation, but with USD longs unwound (Figure 1) and DXY near fair value (Figure 2), there may be limits to any knee-jerk USD selling.

Figure 1. USD longs have been unwound pre-FOMC  
![](images/381943e9b22e7feed998396f06dec1e716432f9bb847d52e3d557b657303e35e.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jun/25 | -3.5  |
| Aug/25 | -1.0  |
| Oct/25 | -4.0  |
| Dec/25 | -9.0  |
| Feb/26 | 1.5   |
| Apr/26 | 7.0   |
| Jun/26 | 0.5   |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Bloomberg

Figure 2. DXY is close to its short-term fair value  
![](images/c651f61d08377479e176c7c4be715a3b7a36186cbc9181c9ae0d0954dc31f9a3.jpg)

<details>
<summary>line chart</summary>

| Date     | Mis val %: DXY vs US-G6 2y yield differential |
| -------- | ----------------------------------------------- |
| Jun/21   | -1.5%                                           |
| Dec/21   | 0.5%                                            |
| Jun/22   | 3.0%                                            |
| Dec/22   | -5.0%                                           |
| Jun/23   | 2.0%                                            |
| Dec/23   | -2.0%                                           |
| Jun/24   | 1.0%                                            |
| Dec/24   | 3.5%                                            |
| Jun/25   | -6.0%                                           |
| Dec/25   | 1.5%                                            |
| Jun/26   | 0.0%                                            |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Bloomberg

Ultimately, our medium-term USD view is based on relative growth differentials, which leaves us looking for EURUSD towards 1.14 (with potential for a downside overshoot). But we may first need clearer signs that global front-end yields have peaked and could ease as conflict concerns fade. In the meantime, we like using any USD weakness around the FOMC meeting to add to EURUSD shorts, especially towards resistance around 1.1660–1.1680 (Figure 3; converging historically pivotal level and multiple moving averages including the 200dma).

Figure 3. Risk/reward to sell EURUSD is attractive around 1.1660–1.1680 resistance  
![](images/b18deb1f6675cd9c96533df7cf94105897a296298af49fb58040cc51366e6a45.jpg)

<details>
<summary>line chart</summary>

| Date       | EUR Currency (Euro Spot) - Last Price | SWAVG (185) on Close (EUR) | SWAVG (206) on Close (EUR) | SWAVG (319) on Close (EUR) |
|------------|--------------------------------------|-----------------------------|-----------------------------|-----------------------------|
| 15-Jun-2026| 1.17                                 | 1.16612                     | 1.16768                     | 1.16848                     |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Bloomberg

Figure 4. DXY range at the base of the uptrend continues  
![](images/a694f92d99ed244b5015ded7bbd1275ebabc226bda2d359c035b4135210a0533.jpg)

<details>
<summary>line chart</summary>

| Date       | Value |
| ---------- | ----- |
| 15-Jun-2026 | 99.575 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Bloomberg

In assessing the risks, though, our view is that the asymmetry skews USD-positive. While not our base case, a Warsh endorsement of market pricing—or at least endorsing the statement/SEP notion that a hike or a cut is equally likely—could lead to a material USD rally with chasing. That is because we would expect any indication that a hike is on the table would lead markets to bring forward such pricing, while likely adding in premium for a second hike. Such a development could finally see the DXY break out of its 12-month consolidation at the base of the long-term channel uptrend (Figure 4). Historically, such breakouts should be chased if confirmed (preferably on a multi-day basis).

Meanwhile, we see a high bar for the market to price out hikes even if these hawkish risks do not materialize, as this likely requires data that first shows inflation breadth is peaking. But one pair that could see a bigger reaction on any knee-jerk USD selling is USDJPY if the MoF uses it as an opportunity to intervene. We have seen the MoF use JPY-positive catalysts to give their intervention more "bang for their buck" (as seen July 11, 2024 when they intervened after a US CPI miss). And given the buildup in speculative JPY short positioning, this is a pair we would monitor tactically in such a scenario.

But for now, the more likely path remains for the USD to remain in its range, with a bias to buy dips on corrections. Combined with an improving risk backdrop (see below), this maintains a positive backdrop for carry which we like funding with EUR and CAD.

Please also see the below for additional context:

US Economics - The Daily Update – Another dovish development

US Economics - FOMC Preview – Hawkish SEP, dovish Warsh

US Rates Weekly - New chair, same Fed inertia

## Tactical bearish risk sentiment fades

We started flagging tactical caution on risk assets on June 2 (the day of the S&P 500 all-time high...so far). As this was a tactical view, we suggested short-dated downside protection (specifically NZD and SEK puts) rather than exiting any risk-positive trades. While we did see a market correction (along with weakness in those currencies), we may have kept the bearish view longer than we should have.

The combination of a greater likelihood for a US-Iran deal, the successful placement of a major tech IPO last week, and what we think will be a relatively banal Fed meeting could support risk assets from here (and big picture we remain constructive on US equities while the AI capex backlog remains robust). And many of the negative tactical indicators we flagged turned positive alongside the stock rally (e.g., discretion vs staples, vol of vol versus vol, etc.). Citi Commodities has also shifted down their oil forecast as they see Strait of Hormuz flows resuming relatively quickly, normalizing by mid-late July. Uncertainty remains, but given investor fatigue with endless headlines in recent months, we would expect any memorandum that elongates the ceasefire will be viewed as a welcome relief. Therefore, absent an actual re-escalation, this summer should shift towards a lower vol regime. Earnings remain a positive catalyst to risk assets and are due to start again in a month.

In G10, AUD outperformance could resume as the best proxy for risk assets; however, a recent patch of soft data, peak hawkishness close to priced for the RBA, and slowing China data could see the fundamental case weaken. And NOK could be sensitive to further corrections in oil, especially if Norges flips to NOK selling next month as we expect. We think the fundamental cases for CAD, SEK, and NZD remain weak, and carry is limited. That leaves G10 as a better source of funders, with CAD and EUR especially attractive given yields and growth outlooks, while USD remains the best carry long in the group, in our view.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

<table><tr><td>Within the past 12 months, Citi Global Markets Inc. or its affiliates has acted as manager or co-manager of an offering of securities of Canada, EUROPEAN UNION, Sweden.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from Australia, Commonwealth of (Government),Canada,EUROPEAN UNION,Japan,New Zealand,Norway,Sweden,United States.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates expects to receive or intends to seek, within the next three months, compensation for investment banking services from Norway.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Australia, Commonwealth of (Government),Canada,EUROPEAN UNION,Japan,New Zealand,Norway,Sweden,United States in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): Australia, Commonwealth of (Government),Canada,EUROPEAN UNION,Japan,New Zealand,Norway,Sweden,United States.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Australia, Commonwealth of (Government),Canada,EUROPEAN UNION,Japan,New Zealand,Norway,Sweden,United States.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Australia, Commonwealth of (Government),Canada,EUROPEAN UNION,Japan,New Zealand,Norway,Sweden,United States.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to Australia, Commonwealth of (Government),Canada,EUROPEAN UNION,Japan,New Zealand,Norway,Sweden,United States. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts&#x27; compensation is determined by Citi management and Citi&#x27;s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the &quot;Firm&quot;). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.</td></tr><tr><td>Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.</td></tr><tr><td>For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product (&quot;the Product&quot;), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013,</td></tr></table>

Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

## RESEARCH ANALYST AFFILIATIONS / NON-US RESEARCH ANALYST DISCLOSURES

The legal entities employing the authors of this report are listed below (and their regulators are listed further herein). Non-US research analysts who have prepared this report (i.e., all research analysts listed below other than those identified as employed by Citi Global Markets Inc.) are not registered/qualified as research analysts with FINRA. Such research analysts may not be associated persons of the member organization (but are employed by an affiliate of the member organization) and therefore may not be subject to the FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Citi Global Markets Inc.

Daniel Tobon; Brian Levine

Citi Global Markets Japan Inc.

Osamu Takashima

## OTHER DISCLOSURES

Any price(s) of instruments mentioned in recommendations are as of the prior day's market close on the primary market for the instrument, unless otherwise stated.

The completion and first dissemination of any recommendations made within this research report are as of the Eastern date-time displayed at the top of the Product. If the Product references views of other analysts then please refer to the price chart or rating history table for the date/time of completion and first dissemination with respect to that view.

European regulations require that where a recommendation differs from any of the author's previous recommendations concerning the same financial instrument or issuer that has been published during the preceding 12-month period that the change(s) and the date of that previous recommendation are indicated. Please refer to the trade history in the published research or contact the research analyst.

Citi has implemented policies for identifying, considering and managing potential conflicts of interest arising as a result of publication or distribution of investment research. A description of these policies can be found at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures.

The proportion of all Citi recommendations that were the equivalent to "Buy", "Hold", "Sell" at the end of each quarter over the prior 12 months (with the % of these that had received investment firm services from Citi in the prior 12 months shown in brackets) is as follows; Q1 2026 Buy $33\% (63\%)$ , Hold $44\% (52\%)$ , Sell $23\% (46\%)$ , RV $0.5\% (89\%)$ : Q4 2025 Buy $33\% (63\%)$ , Hold $44\% (50\%)$ , Sell $23\% (46\%)$ , RV $0.4\% (91\%)$ ; Q3 2025 Buy $33\% (61\%)$ , Hold $44\% (52\%)$ , Sell $23\% (50\%)$ , RV $0.4\% (80\%)$ ; Q2 2025 Buy $33\% (63\%)$ , Hold $44\% (51\%)$ , Sell $23\% (49\%)$ , RV $0.4\% (86\%)$ . For the purposes of disclosing recommendations other th

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
