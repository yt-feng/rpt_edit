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
# JPM

# Hardware & Networking

## Channel Talk: Takeaways from a Discussion with a Large U.S. VAR on Enterprise Spending and OEM Trends

We recently connected with a large U.S. VAR to collect feedback on broader demand and customer spending trends in recent months, as well as vendor-specific insights relevant to our coverage. Key takeaways from the recent discussion include:

\- Demand is tracking above plan, with a strong backlog into 2H26 and 2027. Revenue was described as tracking well above typical double-digit annual growth targets, with broad strength across networking, data centers, cybersecurity, and AI. Growth is coming from both units and pricing, with the 12-month backlog through 2H26 and into 2027 being described as unprecedented. The VAR noted that it has seen some order acceleration, with customers placing larger orders to secure supply, but emphasized that this reflects genuine demand and that it does not see conditions for demand to “fall off a cliff”.

\- Memory costs are driving OEM pricing sharply higher. The VAR indicated that the rapid increase in memory prices as a portion of component costs has left storage and compute the most exposed. Some OEMs now only honor pricing for one-to-two weeks, down from 60-90 days earlier, and in some cases are reserving the right to reprice at ship date. Meanwhile, lead times for storage, compute, and AI clusters have moved beyond six months, while networking is less impacted given lower memory usage. The VAR expects the supply constraints to persist through 2H26 and 2027.

\- Servers and storage are broadly strong, with Dell the standout in AI. On servers, the VAR characterized Dell as a standout among the major OEMs, given its aggressiveness in AI factories, but noted HPE is seeing adoption and that Cisco's Nvidia partnership is also drawing interest, while SuperMicro and Lenovo are increasingly relevant to clients. In storage, AI-oriented vendors (Vast, Weka, etc.) are gaining traction while Dell, Everpure, and NetApp remain strong, noting that by July the traditional storage vendors have already eclipsed all of last year's performance.

\- Networking also strong across the board. In traditional data center networking, Arista and Cisco were described as trading share, while in AI, Nvidia was noted as very strong and white-box was characterized as gaining share at hyperscalers. At the enterprise edge (e.g., branch, campus, etc.), Cisco is seeing strong uptake on the back of a reinvigorated product suite and as clients tackle large estates, with HPE / Juniper the primary alternative. The VAR views HPE / Juniper's data center portfolio as technically viable, although it has not seen a meaningful inflection in revenue to-date.

\- On-prem repatriation is an accelerating area of private data-center investment. The VAR pointed to two drivers of on-prem repatriation: 1) Frustration with large cloud bills on workloads that were migrated to the cloud without being redesigned; and 2) Reluctance to place proprietary or sensitive data in the cloud. Moreover, cost analysis now increasingly favors on-prem for large token consumption workloads, helping to drive demand as the VAR noted that private data center spending in 2026 has already passed the prior-year level

See page 3 for analyst certification and important disclosures.

IT Hardware/ Telecom & Networking Equipment

Joseph Cardoso AC
(1-212) 622-9036
joseph.cardoso@jpmchase.com

Manmohanpreet Singh (1-212) 622-4527 manmohanpreet.singh@jpmchase.com

Marc Vitenzon (1-212) 622-3342 marc.vitenzon@jpmchase.com

Akanksh Chauhan
(1-212) 622-0045
akanksh.chauhan@JPM.com

Software - Large Cap / Mid & Small Cap

Samik Chatterjee, CFA AC
(1-212) 622-0798
samik.x.chatterjee@JPM.com

Arti Vula, CFA
(1-415) 315-5919
arti.vula@jpmchase.com

Jaiden R Patel
(1-212) 270-6953
jaiden.patel@jpmchase.com

Brian Hyska (1-212) 622-2883 brian.hyska@jpmchase.com

Mashu Nishi (1-212) 622-0078  
mashu.nishi@JPM.com  
JPM Securities LLC

by July.

\- F5 is on track to at least match prior year and is well positioned for agentic AI. The VAR indicated that F5 is on its way to “at least” matching its record growth level from 2025. The strong performance was attributed to F5’s shift from load-balancing toward securing API-driven applications, a trend that is expected to accelerate as MCP enables agent-to-agent traffic, with F5 well positioned to secure those connections.

\- Mythos-class model risk is driving incremental security and infrastructure spend rather than cannibalizing budgets. The VAR indicated that the emerging Mythos-class of frontier models, including, but not confined to only, Anthropic, have become an undeniable source of focus for his clients. The ability of the Mythos-class models to chain vulnerabilities and execute attacks are described as “serious” and beyond human capabilities. As a result, customers are appropriating budget for AI, security, and infrastructure refreshes, and the VAR expects the trend to continue into 2027 and 2028. While difficult to be certain, the VAR believes the budget for the aforementioned is generally coming in as new budget dollars rather than cannibalizing other line items. Observability tools were also called out as a category for investment, in addition to categories outlined above, in response to the Mythos-class frontier model development.

\- Token budgets are evolving as governance is shifting from wide-open to credit-limit model. The VAR conveys that token consumption has become a daily workstream with clients and has reached materially greater urgency over the last one to two quarters. A direct analogy is drawn to the early cloud spend cycle, easy to start, painful to control, and notes his firm has stood up a dedicated “FinOps for AI” practice focused on visibility into spend and whether that spend is productive, which is more difficult to determine. The VAR describes “tokenmaxxing” as an ongoing behavior pattern, where employees measured on AI adoption via token consumption game the metric regardless of productivity. Whereas most clients a year ago were flexible and generous on token consumption, now nearly all are instituting limits with exception-based approvals for confirmed heavy users, framed like a credit limit, a dynamic we view as a governor on near-term consumption-revenue but also positive for durability of spend.

\- Copilot is still the default turn-on, but competitive suites are materializing in the enterprise. The VAR views Microsoft's M365 Copilot as effectively a “default” for clients given the installed 365 base, describing daily use both internally and across clients for enterprise data access, email, calendaring, and workflow automation, and expects Microsoft to continue folding capability into the annual licensing schema. Although at the same time, customers are a taking a serious look at alternates, like Claude Cowork (which was described in positive terms), as well as Gemini Enterprise, there are no signs of the alternates driving customers to substitute usage of Microsoft Copilot yet.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Cardoso, Joseph : Amphenol (APH), Arista (ANET), Axon (AXON), CDW (CDW), Calix (CALX), Celestica (CLS), Ceva (CEVA), Ciena (CIEN), Cisco (CSCO), Coherent Corp (COHR), Corning (GLW), Credo (CRDO), Dell Technologies (DELL), Everpure (P), F5 Inc (FFIV), Fabrinet (FN), Flex Ltd (FLEX), Garmin Ltd. (GRMN), HP Inc (HPQ), Hewlett Packard Enterprise (HPE), Ingram Micro (INGM), Insight Enterprises (NSIT), Jabil Inc (JBL), Keysight Technologies (KEYS), Logitech International (LOGI), Lumentum (LITE), Mobileye (MBLY), Motorola Solutions Inc (MSI), NetApp, Inc. (NTAP), Nutanix (NTNX), Qualcomm (QCOM), Seagate (STX), Super Micro (SMCI), TD SYNNEX (SNX), Teradyne (TER), Vistance Networks (VISN), Western Digital (WDC), Wolfspeed Inc (WOLF), Xerox Holdings Corp (XRX) Chatterjee, Samik : Adobe Inc (ADBE), Akamai Technologies, Inc. (AKAM), Apple (AAPL), Cloudflare (NET), CoreWeave (CRWV), Datadog (DDOG), Dynatrace (DT), Figma (FIG), HubSpot (HUBS), Intuit (INTU), Microsoft (MSFT), Oracle (ORCL), Salesforce Inc (CRM), ServiceNow (NOW), Snowflake (SNOW), Twilio (TWLO), Workday (WDAY), Zoom Communications (ZM)

## JPM Equity Research Ratings Distribution, as of July 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>53%</td><td>36%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>80%</td><td>73%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>95%</td><td>92%</td><td>87%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is redistributed, e-mailed or made available to third-party aggregators. For all research material available on a particular stock, please contact your sales representative.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or construed as encouraging, facilitating, promoting or otherwise approving investment or d

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 20 Jul 2026 02:05 AM EDT

Disseminated 20 Jul 2026 06:00 AM EDT
"""
