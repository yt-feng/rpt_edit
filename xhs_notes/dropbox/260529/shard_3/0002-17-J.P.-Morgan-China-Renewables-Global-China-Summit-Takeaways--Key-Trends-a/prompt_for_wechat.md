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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Renewables

# Global China Summit Takeaways: Key Trends and 4 key picks

We returned from the Energy Evolution Tour and Global China Summit last week and observed a pick-up in investor interest in China renewables, driven by heightened energy-security concerns from the Middle East conflict and developed-market data-center power infrastructure constraints. Sungrow and Deye share prices are up 14%/20%, respectively, since May 15 $^{th}$ (vs. SHCOMP -1%). Within ESS, Sungrow cited early AIDC-related ESS orders, while it also benefits from global ESS installations, though it cautioned on near-term cost pressure. Meanwhile, we also heard consistent evidence of surging DG ESS demand in emerging markets (notably Southeast Asia), a positive read-across to Deye. Goldwind-H may also benefit from rising WTG shipment to the EM. Within offshore wind, policy visibility improved with the State Council’s offshore wind installation target in 2030, supporting the offshore supply chain, especially submarine cables, which have high market concentration and entry barriers; we remain constructive on Orient Cables. Within solar, progress on the anti-involution initiative remains slow, while in renewable power operators, power market liberalization hurts the tariff outlook of wind/solar farms, so we prefer nuclear/hydro exposure.

Improving investor interest: Underpinned by refreshed concerns on energy security from the Middle East conflict and DC (data center) constraints on power related infrastructure in DM, we are seeing a pick-up in investor interest in select pockets within China Renewables vs. previous years. On individual names, similar to our recent marketing feedback, Sungrow has seen the most investor interest, followed by Orient Cables.

Emerging AIDC ESS use case for Sungrow: Sungrow shared that it has gained AIDC-related ESS orders recently, from data-center power developers. Management framed AIDCs as a new opportunity set, where aging grid infrastructure and reliability requirements create a natural role for ESS, including configurations to enable “grid-friendly” data centers, support rapid-start of AIDCs, and potentially grid interconnection priority, pending the DOE’s upcoming decision. For more details on AIDC ESS, refer to our report (link). In addition to this, Sungrow also benefits from the global ESS installation growth. On the cautious side, mgmt shared that utility-scale ESS projects have a long contract-to-sales lead time, hinting that cost pressure for 2Q should endure.

Off-shore wind: the key driver for China's renewable push into 15-FYP. For the very first time, the State Council released the 2030 off-shore wind capacity target of 100GW in March 2026. In our tally (since 2020), the country has on average exceeded the national-wide renewable capacity target by $\sim 90\%$ . Such a top-down policy push significantly improves Orient Cables' growth visibility. Among the off-shore wind components, we see submarine cable as having a high entry barrier. We affirm our OW on Orient Cables.

# APAC Utilities & Renewables | Sustainable Investing

Alan Hon AC

(852) 2800-8573

alan.hon@JPM.com

Daqi Jiao

(852) 2800-8595

daqi.jiao@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Figure 1: China's offshore wind grid connection from 2022 to 2027E   
![](images/c31af3105ec83673138a868d0a5792f84e958f0a9f8eac735e5694b1d22a0a64.jpg)

<details>
<summary>bar</summary>

| Year | Power Consumption (GW) |
| :--- | :--- |
| 2022 | 5.3 |
| 2023 | 6.1 |
| 2024 | 4.1 |
| 2025 | 6.6 |
| 2026E | 10.0 |
| 2027E | 13.1 |
</details>

Source: CEC, NEA, JPM estimates.

Figure 2: Comparison of government targets and actual development 

<table><tr><td>Items</td><td>Official government targets</td><td>Actual development</td></tr><tr><td>Wind &amp; solar installed capacity</td><td>1,200GW by 2030</td><td>1,800GW by 2025</td></tr><tr><td>12-FYP wind/solar installed capacity (2010-15)</td><td>Solar 21GW by 2015 Wind 100GW by 2015</td><td>Solar 42GW by 2015 Wind 131GW by 2015</td></tr><tr><td>13-FYP wind/solar installed capacity (2015-20)</td><td>Solar 110GW by 2020 Wind 210GW by 2020</td><td>Solar 253GW by 2020 Wind 282GW by 2020</td></tr><tr><td>2025 ESS installed capacity</td><td>30GW by 2025</td><td>143GW by 2025</td></tr></table>

Source: State Council, NEA.

Surge in DG ESS orders in EM: We met with several ESS companies during the Summit and adjacent tour (Sungrow, CSI Solar and Ginlong). This confirms a trend for surging DG (distributed generation) ESS shipment growth in EM (particularly SEA) following the energy supply disruption after the Middle East conflict. Relative to utility-scale ESS, DG ESS has a shorter order-to-delivery cycle, resulting in cost pass-through happening in some orders already. These are two positives for Deye, which we initiated on recently (link). By the same token, we see potential for Goldwind-H to benefit should utility-scale renewable deployment pick up in EM. Goldwind-H is experiencing margin expansion as it takes market share in EM from western OEMs.

Figure 3: CAGR from 2025 to 2027 of the distributed ESS market   
![](images/34508bcc4842b449c8272f8377db24cd61960a3a0f1b088eb7d8250db529c945.jpg)

<details>
<summary>bar</summary>

| Region | BNEF (2H25 forecast) (%) | BNEF (1H26 forecast) (%) |
|---|---|---|
| Australia | 30.0 | 10.0 |
| South Africa | 25.0 | 15.0 |
| Europe | 10.0 | 20.0 |
| India | 75.0 | 70.0 |
| Latin America | 90.0 | 85.0 |
| Middle East and North Africa | 140.0 | 135.0 |
| Southeast Asia | 125.0 | 205.0 |
</details>

Source: BloombergNEF.

Figure 4: Rising ex-China WTG revenue mix (higher GPM)   
![](images/d7327119cff4ad03675b1670e1fb98959ba953a473392efb14e2a157a8b8d1b3.jpg)

<details>
<summary>bar</summary>

| Year | Value (%) |
|---|---|
| 2024 | 18 |
| 2025 | 23 |
| 2026E | 30 |
</details>

Source: Goldwind, JPM estimates.

Anti-involution is taking time for policy roll-out. While the central government has set the direction on industry consolidation, there is still no clear executable strategy. In this part of the value chain, we remain selective and cherry pick the cost leader with differentiated technology (GCL Tech) and value (Daqo, trading on -ve enterprise value) as our OW for investors with patience.

Figure 5: Polysilicon production cash costs by major players in 2025   
![](images/4ddd205a22ed1a8d4ecc3b1ddc4a51a437b199305732eb967e0e2a40e732cac5.jpg)

<details>
<summary>bar</summary>

| Company | Polysilicon production cash costs (Rmb/kg) |
|---|---|
| GCL Tech | 23.9 |
| Tongwei | 32.5 |
| Daqo | 36.2 |
| East Hope | 37.6 |
| Xinte | 41.2 |
| Asia Silicon | 43.4 |
</details>

Source: BloombergNEF (2Q Global PV Outlook), JPM estimates for our covered companies (GCL Tech, Tongwei, Daqo). Note: We assume that USD/CNY is 7.2 and SG&A expense is Rmb2/kg. Polysilicon spot price includes 13% VAT.

Figure 6: Net cash of listed polysilicon producers as of 2025   
![](images/5fd6f44142e909180aa1417fb98d43f830a9ba2c04a0934ff21de3f593371b65.jpg)

<details>
<summary>bar</summary>

| Company | Net cash balance (Rmb mn) |
| :--- | :--- |
| Daqo | 15000 |
| GCL Tech | -2000 |
| Xinte | -3000 |
| Tongwei | -65000 |
</details>

Source: Company reports. Note: Cash and equivalents includes cash, restricted cash, short-term investments and fixed-term deposits within one year. Net cash is cash - bank loans and bonds.

Other observations: Power market liberalization hurts wind/solar farms, nuclear/hydro are our preferred exposure. We have observed an asymmetric power price policy among different types of alternative fuels. We have seen a few provinces (Guangdong, Liaoning and Guangxi) rolling out policies to stabilize nuclear power prices. On the other hand, wind/solar power price liberalization (introducing spot px as a portion of power transaction) pressures wind/solar power prices. While “compute-power coordination” development is a positive development supporting green power prices, the volume is not very meaningful. For reference, data centers use $\sim<2\%$ of China’s electricity demand. On the side, hydropower tariff remains stable due to its cost advantage. We have OW ratings on CGN Power (nuclear) and Yangtze Power (hydro) while having Neutral ratings on wind farms Longyuan and Datang Renewable.

Companies Discussed in This Report (all prices in this report as of market close on 27 May 2026, unless otherwise indicated) CGN Power (1816)(1816.HK/HK\$3.08/OW), Datang Renewable (1798)(1798.HK/HK\$1.64/N), Deye - A(605117.SS/Rmb122.40/OW), Goldwind - H(2208.HK/HK\$13.92/OW), Longyuan (0916)(0916.HK/HK\$6.45/N), Orient Cables - A(603606.SS/Rmb44.81/OW), Sungrow - A(300274.SZ/Rmb184.09/OW), Yangtze Power - A(600900.SS/Rmb27.24/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

# Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

# Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Hon, Alan : Arctech - A (688408.SS), CGN Power (1816) (1816.HK), Daqo (DQ), Datang Renewable (1798) (1798.HK), Deye - A (605117.SS), Envicool - A (002837.SZ), Flat Glass (6865.HK), GCL Tech (3800.HK), Goldwind - A (002202.SZ), Goldwind - H (2208.HK), Hangzhou First - A (603806.SS), Huaneng Hydropower - A (600025.SS), LONGi Green - A (601012.SS), Longyuan (0916) (0916.HK), Maxwell - A (300751.SZ), Mingyang - A (601615.SS), Orient Cables - A (603606.SS), SDIC Power - A (600886.SS), Shenzhen SC - A (300724.SZ), Sichuan Chuantou - A (600674.SS), Sungrow - A (300274.SZ), Tongwei - A (600438.SS), Xinyi Solar (0968) (0968.HK), Yangtze Power - A (600900.SS)

JPM Equity Research Ratings Distribution, as of April 04, 2026 

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

# History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation:The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US Analysts: Unless otherwise noted, the non-US analysts listed on the front of this report are employees of non-US affiliates of JPM Securities LLC, may not be registered as research analysts under FINRA rules, may not be associated persons of JPM Securities LLC, and may not be subject to FINRA Rule 2241 or 2242 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

# Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is redistributed, e-mailed or made available to third-party aggregators. For all research material available on a particular stock, please contact your sales representative.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or construed as encouraging, facilitating, promoting or otherwise approving investment or dealing in such Sanctioned Securities. Clients should be aware of their own legal and compliance obligations when making investment decisions.

Any digital or crypto assets discussed in this research report are subject to a rapidly changing regulatory landscape. For relevant regulatory advisories on crypto assets, including bitcoin and ether, please see https://www.JPM.com/disclosures/cryptoasset-disclosure.

The author(s) of this research report may not be licensed to carry on regulated activities in your jurisdiction and, if not licensed, do not hold themselves out as being able to do so.

Exchange-Traded Funds (ETFs): JPM Secu

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 27 May 2026 08:09 PM HKT

Disseminated 27 May 2026 08:09 PM HKT
"""
