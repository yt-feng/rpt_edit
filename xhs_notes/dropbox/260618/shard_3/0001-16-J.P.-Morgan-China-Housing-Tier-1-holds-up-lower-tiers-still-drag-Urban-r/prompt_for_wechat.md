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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Housing: Tier-1 holds up, lower tiers still drag

Urban renewal agenda ramps

- JPM's housing activity index ticked up in May but remained subdued; home prices continued to fall, dragged by weakness in lower-tier cities.  
- $15^{th}$ FYP urban renewal is more systematic/execution-focused, with stronger targets for "good housing", more fiscal support and land-flexibility tools.  
- Recovery remains narrow and K-shaped: tier-1 secondary markets outperformed, but lower-tier cities remained weak.  
- Elevated inventories, weak household credit, and falling real estate FAI point to a prolonged quantity adjustment.

JPM's housing activity index ticked up in May but remained subdued. The mild uptick reflected a smaller contraction in floor space starts (-22.9% oya in May vs -28.2% in Apr) and completions (-20.2% oya in May vs -22.5% in Apr), while a steeper decline in real estate FAI (-24.3% oya in May vs -20.1% in Apr) and new home sales (-8.6% oya in May vs -6.5% in Apr) capped the gain.

The NBS 70-city new-home price decline stabilized at $0.20\% \mathrm{m / m}$ nsa in May (vs $-0.19\%$ in Apr). Weakness continued to be concentrated in lower-tier cities, while tier-1 cities posted a sequential gain of $+0.2\%$ m/m nsa. The secondary home price fall widened modestly to $0.26\% \mathrm{m / m}$ nsa (vs $-0.23\%$ in Apr): tier-1 price gains held at $+0.4\%$ , but lower-tier cities remained under pressure. New-home prices are now down $13.7\%$ from the 2021 peak; secondary prices are down $22.6\%$ . Centraline's sales manager confidence index inched up in early June, while the secondary home asking price index edged down.

The State Council published the Urban Renewal 15 $^{th}$ FYP in early June. Compared to the 14 $^{th}$ FYP, the latest plan moves from pilot-style and incremental renovation towards a more systematic model built around three major project categories: livelihood, development, and safety. It places stronger emphasis on improving housing quality, building “good houses”, upgrading old residential communities, and addressing safety risks, such as dilapidated housing and urban villages. Targets are also more ambitious, with the planned renovation volume for urban dilapidated housing doubling and urban village renovation remaining at a high level. The 15 $^{th}$ FYP also gives much greater weight to funding, land policy, and real estate transformation. It details stronger fiscal support through budgetary investment, affordable housing subsidies, special LGBs, ultra-long special CGBs, tax incentives, and potential use of REITs and social capital. Land policy is also more flexible, with support for idle land reuse, mixed-use redevelopment, temporary use, land-use conversion, and lower transaction frictions for stock-asset revitalization. Overall, the 15th FYP is more integrated, market-oriented, and execution-focused, positioning urban renewal as a key tool for improving livelihoods, stabilizing (instead of reviving) the property market, and supporting high-quality urban growth.

Home sales recovery remains narrow, with gradual momentum fading. Early stabilization signs in tier-1 cities have been supported by lower secondary-market inventory, stronger transaction volumes, better conversion rates, selective price increases, and possible wealth effects from IPO activity and firmer equity markets. However, these signals do not yet indicate a broad or durable recovery. The

## Emerging Markets Asia, Economic and Policy Research

## Tingting Ge

(852) 2800-0143

tingting.ge@JPM.com

## Feng Zhu

(852) 2800 1745

feng.zhu@JPM.com

## Jiayi Li

(852) 2800-5229

jiayi.c.li@JPM.com

## Tongfang Yuan

(852) 2800-0085

tongfang.yuan@JPM.com

JPM Chase Bank, N.A., Hong Kong Branch

improvement remains uneven and K-shaped: tier-1 cities and upgrade/luxury products are outperforming, while lower-tier cities remain broadly weak.

China's housing market remains in a time-inconsistency trap. Policymakers aim to improve affordability and reduce reliance on property, but have slowed price clearing to protect household wealth and local governments, forcing the adjustment mainly through quantities, with falling starts, sales, land purchases, and real estate FAI. Recent tier-1 secondary-market improvement is encouraging, but broader conditions remain challenging, with elevated inventories, weak household credit demand, and continued declines in real estate investment. As a result, the baseline should not yet be reassessed: current trends look more like narrow, K-shaped stabilization within a prolonged quantity adjustment, not the start of a durable nationwide recovery. With the secondary market increasingly taking share from primary sales, headline transaction stabilization may coexist with continued softness in new-home sales, construction, and developer investment.

Housing policy and housing market activity  
![](images/b9c01ec3470e37fb8615666961692a6640174a8b8bd48577ea8e3da31a10bb73.jpg)

<details>
<summary>line chart</summary>

| Year | Housing policy index | Housing market activity index |
|------|----------------------|-------------------------------|
| 03   | -30                  | 100                           |
| 04   | -20                  | 80                            |
| 05   | -10                  | 60                            |
| 06   | 0                    | 40                            |
| 07   | 10                   | 20                            |
| 08   | 20                   | 10                            |
| 09   | 30                   | 5                             |
| 10   | 40                   | 0                             |
| 11   | 50                   | -5                            |
| 12   | 60                   | -10                           |
| 13   | 70                   | -15                           |
| 14   | 80                   | -20                           |
| 15   | 90                   | -25                           |
| 16   | 100                  | -30                           |
| 17   | 90                   | -35                           |
| 18   | 80                   | -40                           |
| 19   | 70                   | -45                           |
| 20   | 60                   | -50                           |
| 21   | 50                   | -55                           |
| 22   | 40                   | -60                           |
| 23   | 30                   | -65                           |
| 24   | 20                   | -70                           |
| 25   | 10                   | -75                           |
| 26   | 0                    | -80                           |
</details>

Source: NBS; JPM; Note: Preliminary estimates for Apr '26 housing market activity index with tentative assumptions for land sales growth.

China housing inventory months  
![](images/70546f780630c88e0e8490f0018cb45adc511e6295dbeb4c922022d73c7c6de7.jpg)

<details>
<summary>line chart</summary>

| Year | Under construction | Finished |
|------|---------------------|----------|
| 13   | 40                  | 3        |
| 14   | 45                  | 3        |
| 15   | 55                  | 4        |
| 16   | 55                  | 4        |
| 17   | 50                  | 3        |
| 18   | 45                  | 3        |
| 19   | 40                  | 3        |
| 20   | 35                  | 3        |
| 21   | 35                  | 3        |
| 22   | 40                  | 4        |
| 23   | 50                  | 5        |
| 24   | 60                  | 6        |
| 25   | 70                  | 7        |
| 26   | 75                  | 7        |
</details>

Source: NBS, JPM

China housing activity indicators  
![](images/45d68efdf6f8a21710eeca23cee4cd0bebf19be2fb15040eec789db08edcc969.jpg)

<details>
<summary>line chart</summary>

| Year | New home sold | Secondary home price |
|------|---------------|----------------------|
| 11   | 100           | 100                  |
| 12   | 105           | 105                  |
| 13   | 100           | 100                  |
| 14   | 110           | 105                  |
| 15   | 105           | 95                   |
| 16   | 115           | 85                   |
| 17   | 130           | 95                   |
| 18   | 140           | 105                  |
| 19   | 150           | 115                  |
| 20   | 160           | 125                  |
| 21   | 180           | 130                  |
| 22   | 170           | 125                  |
| 23   | 140           | 110                  |
| 24   | 120           | 90                   |
| 25   | 100           | 70                   |
| 26   | 80            | 50                   |
</details>

Source: NBS, JPM

China 70-city housing prices  
![](images/aad6a3ed179cc972d5e23a451aaf651232376c0d5f91be0e126fcc2e083fc4dd.jpg)

<details>
<summary>line chart</summary>

2010 Dec=100
| Year | New home | Secondary home |
|---|---|---|
| 11 | 100 | 100 |
| 12 | 100 | 99 |
| 13 | 100 | 99 |
| 14 | 112 | 102 |
| 15 | 108 | 99 |
| 16 | 110 | 102 |
| 17 | 120 | 108 |
| 18 | 128 | 115 |
| 19 | 138 | 123 |
| 20 | 148 | 128 |
| 21 | 158 | 132 |
| 22 | 155 | 133 |
| 23 | 153 | 128 |
| 24 | 148 | 122 |
| 25 | 142 | 113 |
| 26 | 136 | 103 |
</details>

Source: NBS, JPM

Housing transactions by sqm in 30 major cities  
![](images/a768ca12921c22281263a7f47c27f8269660d5623c41f4978de464adc82acf85.jpg)

<details>
<summary>line chart</summary>

| Month | 19-24 range | 19-24 ave. | 2025 | 2026 |
|-------|-------------|------------|------|------|
| Jan   | ~600        | ~650       | ~300 | ~350 |
| Feb   | ~400        | ~450       | ~200 | ~250 |
| Mar   | ~300        | ~350       | ~150 | ~100 |
| Apr   | ~450        | ~500       | ~250 | ~300 |
| May   | ~500        | ~550       | ~300 | ~350 |
| Jun   | ~600        | ~650       | ~350 | ~400 |
| Jul   | ~700        | ~750       | ~400 | ~450 |
| Aug   | ~600        | ~650       | ~350 | ~400 |
| Sep   | ~500        | ~550       | ~300 | ~350 |
| Oct   | ~400        | ~450       | ~250 | ~300 |
| Nov   | ~500        | ~550       | ~300 | ~350 |
| Dec   | ~600        | ~650       | ~350 | ~400 |
</details>

Source: Wind, JPM

Major cities' secondary housing transactions  
![](images/0dfcd6d0e427e545b1558a131a0d89e5870f5e981d08904624df2a3b62d0e3ab.jpg)

<details>
<summary>line chart</summary>

| Month | 19-23 range | 2024 | 2025 | 2026 |
|-------|-------------|------|------|------|
| Jan   | ~150        | ~180 | ~250 | ~230 |
| Feb   | ~180        | ~170 | ~260 | ~240 |
| Mar   | ~160        | ~150 | ~270 | ~310 |
| Apr   | ~190        | ~200 | ~280 | ~300 |
| May   | ~170        | ~250 | ~260 | ~330 |
| Jun   | ~180        | ~240 | ~250 | ~280 |
| Jul   | ~190        | ~230 | ~240 | ~260 |
| Aug   | ~180        | ~220 | ~230 | ~240 |
| Sep   | ~170        | ~210 | ~220 | ~230 |
| Oct   | ~160        | ~150 | ~160 | ~170 |
| Nov   | ~180        | ~310 | ~240 | ~330 |
| Dec   | ~190        | ~330 | ~250 | ~340 |
</details>

Source: Wind, JPM

Table: Central finance support for urban renewal

<table><tr><td rowspan="2">Year</td><td rowspan="2">No. of cities</td><td rowspan="2">Eligible city</td><td rowspan="2">Priority city</td><td colspan="3">Subsidy by city location (bn yuan)</td><td rowspan="2">Focus area</td></tr><tr><td>East</td><td>Midland</td><td>West</td></tr><tr><td>2024</td><td>15</td><td>Any prefecture-level</td><td>Mega-cities and large cities along the Yangtze River Economic Belt</td><td></td><td></td><td></td><td rowspan="2">Upgrade and rehabilitate urban underground utility networks. Develop model zones for full wastewater pipeline coverage. Address gaps in municipal infrastructure (&quot;short-board&quot; strengthening). Renew and retrofit aging districts. Underground network renewal + cost-efficient utility tunnel development. &quot;Plant-network integration&quot; wastewater treatment + model zones for full sewer network coverage. Municipal infrastructure upgrading and retrofitting. Renew existing areas with integrated culture-tourism-consumption activation.</td></tr><tr><td>2025</td><td>&lt;=20</td><td>Large prefecture-level or beyond</td><td>Mega-cities and large cities along the Yangtze River Economic Belt</td><td>0.8</td><td>1</td><td>1.2</td></tr><tr><td>2026</td><td>&lt;=15</td><td>Any prefecture-level</td><td>No priority</td><td></td><td></td><td></td><td>Improve the quality of urban infrastructure. Develop &quot;complete communities&quot; and retrofit neighborhood supporting facilities. Renew aging areas (blocks) and promote adaptive reuse. Use existing land and idle properties to fill public-service gaps and expand consumption infrastructure.</td></tr></table>

Source: MOF, JPM

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or construed as encouraging, facilitating, promoting or otherwise approving investment or dealing in such Sanctioned Securities. Clients should be aware of their own legal and compliance obligations when making investment decisions.

Any digital or crypto assets discussed in this research report are subject to a rapidly changing regulatory landscape. For relevant regulatory advisories on crypto assets, including bitcoin and ether, please see https://www.JPM.com/disclosures/cryptoasset-disclosure.

The author(s) of this research report may not be licensed to carry on regulated activities in your jurisdiction and, if not licensed, do not hold themselves out as being able to do so.

Exchange-Traded Funds (ETFs): JPM Securities LLC (“JPMS”) acts as authorized participant for substantially all U.S.-listed ETFs. To the extent that any ETFs are mentioned in this report, JPMS may earn commissions and transaction-based compensation in connection with the distribution of those ETF shares and may earn fees for performing other trade-related services, such as securities lending to short sellers of the ETF shares. JPMS may also perform services for the ETFs themselves, including acting as a broker or dealer to the ETFs. In addition, affiliates of JPMS may perform services for the ETFs, including trust, custodial, administration, lending, index calculation and/or maintenance and other services.

Changes to Interbank Offered Rates (IBORs) and other benchmark rates: Certain interest rate benchmarks are, or may in the future become, subject to ongoing international, national and other regulatory guidance, reform and proposals for reform. For more information, please consult: https://www.JPM.com/global/disclosures/interbank\_offered\_rates

Private Bank Clients: Where you are receiving research as a client of the private banking businesses offered by JPM Chase & Co. and its subsidiaries (“JPM Private Bank”), research is provided to you by JPM Private Bank and not by any other division of JPM, including, but not limited to, the JPM Corporate and Investment Bank and its Global Research division.

Legal entity responsible for the production and distribution of research: The legal entity identified below the name of the Reg AC Research Analyst who authored this material is the legal entity responsible for the production of this research. Where multiple Reg AC Research Analysts authored this material with different legal entities identified below their names, these legal entities are jointly responsible for the production of this research. Where more than one legal entity is listed under an analyst's name, the first legal entity is responsible for the production unless stated otherwise. Research Analysts from various JPM affiliates may have contributed to the production of this material but may not be licensed to carry out regulated activities in your jurisdiction (and do not hold themselves out as being able to do so). Unless otherwise stated below in the legal entity disclosures, this material has been distributed by the legal entity responsible for production, or where more than one legal entity is listed under the analyst's name, the first legal entity will be responsible for distribution. If you have any queries, please contact the relevant Research Analyst in your jurisdiction or the entity in your jurisdiction that has distributed this research material.

## Legal Entities Disclosures and Country-/Region-Specific Disclosures:

Argentina: JPM Chase Bank N.A Sucursal Buenos Aires is regulated by Banco Central de la República Argentina ("BCRA"- Central Bank of Argentina) and Comisión Nacional de Valores ("CNV"- Argentinian Securities Commission - ALYC y AN Integral N°51).

Australia: JPM Securities Australia Limited (“JPMSAL”) (ABN 61 003 245 234/AFS Licence No: 238066) is regulated by the Australian Securities and Investments Commission and is a Market Participant of ASX Limited, a Clearing and Settlement Participant of ASX Clear Pty Limited and a Clearing Participant of ASX Clear (Futures) Pty Limited. This material is issued and distributed in Australia by or on behalf of JPMSAL only to "wholesale clients" (as defined in section 761G of the Corporations Act 2001). A list of all financial products covered can be found by visiting https://www.jpmm.com/research/disclosures. JPM seeks to cover companies of relevance to the domestic and international investor base across all Global Industry Classification Standard (GICS) sectors, as well as across a range of market capitalisation sizes. If applicable, in the course of conducting public side due diligence on the subject company(ies), the Research Analyst te

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market

conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 16 Jun 2026 03:00 PM HKT

Disseminated 16 Jun 2026 03:00 PM HKT
"""
