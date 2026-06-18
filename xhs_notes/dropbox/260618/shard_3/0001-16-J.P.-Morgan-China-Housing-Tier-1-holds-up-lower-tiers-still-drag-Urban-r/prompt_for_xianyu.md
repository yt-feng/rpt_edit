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

Private Bank Clients: Where you are receiving research as a client of the private banking businesses offered by JPM Chase & Co. and its subsidiaries (“JPM Private Bank”), research is provided to you by JPM Private Bank and not by any other di

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 16 Jun 2026 03:00 PM HKT

Disseminated 16 Jun 2026 03:00 PM HKT
"""
