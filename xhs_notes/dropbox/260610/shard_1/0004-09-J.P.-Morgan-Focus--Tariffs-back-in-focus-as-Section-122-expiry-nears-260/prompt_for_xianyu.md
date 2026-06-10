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
# Focus: Tariffs back in focus as Section 122 expiry nears

While the Middle East conflict dominates headlines, recent developments require a reassessment of the state of tariffs in the US war on trade. After the courts invalidated the IEEPA tariffs earlier this year, and with the upcoming expiration of Section 122 tariffs on July 24, the administration is shifting toward Sections 301 tariffs. The two 301 probes cover (i) forced-labor enforcement across 60 economies (USTR floated 10%–12.5% tariffs; comments due July 6) and (ii) “structural excess capacity” across 16 economies (comments closed April 15; no tariff rates announced yet).

These actions are broader and faster-moving than the 2017–18 China measures, but may face heightened legal risk given the courts' emphasis on statutory text rather than the administration's interpretation of trade laws. USTR has also proposed a 25% base tariff on Brazil (effective \~19% with exemptions). The combination of new tariffs and court scrutiny points to another round of prolonged policy uncertainty, with headline risk broadening from geopolitics to tariffs, supply chains, and legal outcomes.

US tariff rates have fallen in recent months. February's US Supreme Court decision striking down the IEEPA-based duties cut the average tariff on US imports by roughly $2.5\%$ -pts to about $11\%$ (using static 2024 weights). In effect, the US administration is using Section 122 to apply an average tariff of $10\%$ on trade with the rest of the world (below the $\sim 15\%$ IEEPA headline average). Yet observed tariff rates (calculated duties over imports) have run well below $10\%$ this year, at an estimated $6.7\%$ in April. The gap largely reflects broad exemptions, especially for energy, pharmaceuticals, and electronics, as well as USMCA-compliant trade. Even with higher-than- $10\%$ Section 232 tariffs on metals and autos, the shift in US imports toward lower-tariffed products and source countries has kept the observed average meaningfully below headline rates.

US effective tariff rates  
![](images/785a0ca5b756b27e6078270c91dfbb10a0372fd86b93e56120a80902d038b34c.jpg)

<details>
<summary>line chart</summary>

| Date   | Static rate w/ 2024 trade weights and tariff rates estimated from announcements* | Floating rate: calculated duties / goods imports |
|--------|--------------------------------------------------------------------------|-----------------------------------------------|
| Jul 26 | 11.0%                                                                    | 6.7%                                          |
</details>

Source: Yale Budget Lab, US Census Bureau, JPM. \*Yale Budget Lab estimate.

The forced-labor Section 301 tariffs have been announced but not implemented, and are expected to replace the temporary Section 122 regime when it lapses on 24

See page 5 for analyst certification and important disclosures.

## Economic and Policy Research

## Nora Szentivanyi

(44-20) 7134-7544

nora.szentivanyi@JPM.com

## Fabio Tomasoni

fabio.tomasoni@JPM.com

JPM Securities plc

July, alongside the newly-announced Brazil tariffs. As proposed, these changes would keep the US average effective tariff rate close to current levels. The forced-labor Section 301 measures target roughly 60 economies (representing 99% of total US trade) and focuses on whether countries have failed to adopt and enforce prohibitions on imports produced with forced labor that could distort competition and disadvantage US businesses.

The recommended Section 301 remedy is a two-tier tariff: 10% for jurisdictions with bans on forced labor but weak enforcement (e.g., Canada, Ecuador, the EU, UK, Indonesia, Mexico) and for countries with completed “agreements on reciprocal trade” (including USMCA partners); and 12.5% for the remaining investigated jurisdictions. Exemptions are once again broad—covering Section 232 goods and selected foodstuffs, fuels, pharmaceuticals, gold, and semiconductors/electronics—and are even more expansive than under IEEPA and current Section 122 carve-outs, notably adding aircraft and additional machinery.

US tariff rates on select countries  
![](images/4b7f9359b6ba39825ea125a1296ef08a4244e80f042335045064b1eb7db5542c.jpg)

<details>
<summary>bar-line hybrid</summary>

| Country | March '26 avg. tariff rate (latest) (%) | After new* Section 301 tariffs replace Section 122 (%) |
| :--- | :--- | :--- |
| chn | 23.0 | 24.0 |
| bra | 10.5 | 19.0 |
| idn | 14.0 | 14.5 |
| tur | 13.5 | 14.0 |
| ury | 12.0 | 13.0 |
| jpn | 9.5 | 9.5 |
| ind | 8.0 | 9.0 |
| nzl | 7.0 | 8.5 |
| kor | 8.0 | 8.0 |
| vnm | 7.0 | 7.5 |
| nor | 7.0 | 7.5 |
| eu | 7.5 | 7.0 |
| glob | 6.5 | 6.5 |
| arg | 6.0 | 6.0 |
| per | 5.0 | 5.5 |
| tha | 5.0 | 5.5 |
| gbr | 6.5 | 5.5 |
| phl | 4.5 | 5.0 |
| chl | 4.0 | 5.0 |
| ecu | 4.5 | 4.5 |
| aus | 4.0 | 4.0 |
| mys | 3.5 | 3.5 |
| isr | 3.5 | 3.5 |
| hkg | 3.0 | 3.0 |
| mex | 3.0 | 3.0 |
| col | 3.0 | 3.0 |
| can | 2.5 | 3.0 |
| zaf | 2.5 | 3.0 |
| twn | 2.0 | 2.5 |
| sgp | 1.5 | 2.0 |
</details>

Source: JPM, Global Trade Alert, US Census Bureau. \*Forced labor and Brazil-specific announced tariff remedies.

By country, the new Section 301 measures would raise Brazil's effective tariff rate the most. A separate Section 301 action on Brazil—citing “unreasonable” trade practices that “burden or restrict US commerce”—would lift the headline tariff on Brazilian exports to the US to 25%. While many products such as coffee, meat, rare earths, orange juice, aircraft, and equipment would continue to be exempt, the imposition of 50% tariffs on steel imports raises the weighted average tariff to 19%—an 8%-pt increase. Still the impact on Brazil’s economy should be limited given its low direct trade exposure to the US and stronger oil exports. Tariffs on other major economies would be broadly unchanged on net, with small increases for some offset by small declines elsewhere, largely reflecting the two-tier structure.

Economies in the 10% tier, including the European Union and UK see their average ease a little as the broad Section 122 surcharge lapses and the targeted duties cover only part of their trade. Canada and Mexico remain close to 3%, because they hold USMCA exemptions that cover much of their trade. Economies in the 12.5% tier, such as Vietnam and India, edge up by roughly half a point. China—already the most heavily tariffed through its existing Section 301 and the Section 232 duties—edges up but stays near 23%.

US tariff rates as new\* Section 301 replace Section 122

<table><tr><td></td><td>2024 avg.</td><td>March &#x27;26 (latest)</td><td>Section 301 tier</td><td>JPM estimate +Section 301 - Section 122</td><td>%-pt chg from current</td></tr><tr><td colspan="6">%; observed tariff rate</td></tr><tr><td>Global</td><td>2.3</td><td>6.8</td><td></td><td>6.8</td><td>-0.1</td></tr><tr><td colspan="6">DM</td></tr><tr><td>Euro area</td><td>1.2</td><td>7.7</td><td>10.0</td><td>6.9</td><td>-0.8</td></tr><tr><td>Japan</td><td>1.5</td><td>9.9</td><td>12.5</td><td>9.4</td><td>-0.5</td></tr><tr><td>United Kingdom</td><td>1.0</td><td>6.5</td><td>10.0</td><td>5.2</td><td>-1.3</td></tr><tr><td>Norway</td><td>0.6</td><td>6.8</td><td>12.5</td><td>7.2</td><td>0.4</td></tr><tr><td>Sweden</td><td>1.4</td><td>11.6</td><td>10.0</td><td>10.6</td><td>-1.0</td></tr><tr><td>Switzerland</td><td>0.6</td><td>4.9</td><td>12.5</td><td>5.2</td><td>0.4</td></tr><tr><td>Canada</td><td>0.1</td><td>3.2</td><td>10.0</td><td>3.0</td><td>-0.1</td></tr><tr><td>Australia</td><td>0.1</td><td>3.9</td><td>12.5</td><td>4.2</td><td>0.3</td></tr><tr><td>New Zealand</td><td>1.1</td><td>7.3</td><td>12.5</td><td>8.3</td><td>1.0</td></tr><tr><td colspan="6">LatAm</td></tr><tr><td>Argentina</td><td>1.0</td><td>6.3</td><td>10.0</td><td>6.2</td><td>0.0</td></tr><tr><td>Brazil</td><td>1.3</td><td>10.6</td><td>25.0</td><td>18.9</td><td>8.3</td></tr><tr><td>Chile</td><td>0.0</td><td>4.0</td><td>12.5</td><td>4.8</td><td>0.8</td></tr><tr><td>Colombia</td><td>0.1</td><td>2.9</td><td>12.5</td><td>3.1</td><td>0.3</td></tr><tr><td>Mexico</td><td>0.2</td><td>3.4</td><td>10.0</td><td>3.2</td><td>-0.2</td></tr><tr><td>Peru</td><td>0.1</td><td>4.9</td><td>12.5</td><td>5.7</td><td>0.8</td></tr><tr><td>Ecuador</td><td>0.4</td><td>4.7</td><td>10.0</td><td>4.7</td><td>0.0</td></tr><tr><td colspan="6">EM Asia</td></tr><tr><td>China</td><td>10.9</td><td>23.1</td><td>12.5</td><td>23.5</td><td>0.5</td></tr><tr><td>India</td><td>2.4</td><td>8.3</td><td>12.5</td><td>8.9</td><td>0.6</td></tr><tr><td>South Korea</td><td>0.2</td><td>8.2</td><td>12.5</td><td>8.2</td><td>0.0</td></tr><tr><td>Taiwan</td><td>0.9</td><td>2.3</td><td>10.0</td><td>2.2</td><td>-0.1</td></tr><tr><td>Hong Kong</td><td>1.0</td><td>3.0</td><td>12.5</td><td>3.4</td><td>0.4</td></tr><tr><td>Malaysia</td><td>0.6</td><td>4.2</td><td>10.0</td><td>3.7</td><td>-0.5</td></tr><tr><td>Singapore</td><td>0.1</td><td>1.9</td><td>12.5</td><td>2.0</td><td>0.1</td></tr><tr><td>Thailand</td><td>1.6</td><td>5.3</td><td>12.5</td><td>5.3</td><td>0.0</td></tr><tr><td>Philippines</td><td>1.4</td><td>5.1</td><td>12.5</td><td>4.9</td><td>-0.2</td></tr><tr><td>Indonesia</td><td>4.9</td><td>14.6</td><td>10.0</td><td>14.4</td><td>-0.2</td></tr><tr><td>Vietnam</td><td>3.8</td><td>7.0</td><td>12.5</td><td>7.2</td><td>0.2</td></tr><tr><td colspan="6">EMEA EM</td></tr><tr><td>Czechia</td><td>1.2</td><td>8.8</td><td>10.0</td><td>7.8</td><td>-1.0</td></tr><tr><td>Poland</td><td>1.4</td><td>9.2</td><td>10.0</td><td>7.9</td><td>-1.3</td></tr><tr><td>Hungary</td><td>1.3</td><td>5.9</td><td>10.0</td><td>5.5</td><td>-0.4</td></tr><tr><td>Romania</td><td>2.4</td><td>12.4</td><td>10.0</td><td>11.6</td><td>-0.8</td></tr><tr><td>Turkey</td><td>3.3</td><td>13.4</td><td>12.5</td><td>14.0</td><td>0.6</td></tr><tr><td>South Africa</td><td>0.3</td><td>2.8</td><td>12.5</td><td>3.0</td><td>0.2</td></tr><tr><td>Israel</td><td>0.1</td><td>3.4</td><td>12.5</td><td>3.6</td><td>0.2</td></tr></table>

Source: US Census Bureau, Global Trade Alert, JPM. \*Forced-Labor and Brazil-specific Section 301 tariffs

In the 10% tier, Section 122 and Section 301 share the same headline rate, but effective rates can still fall because Section 301 narrows the taxable base with additional exclusions—most importantly for aircraft. Under Section 122, aircraft and jet-engine lines paid the surcharge on their full value. Under the proposed duty, only the estimated non-civil share—about a tenth of value—would be dutiable, implying an effective rate near 1% rather than 10%. This is why France—with US-bound exports concentrated in airframes and jet-engine parts—sees the largest decline among major European suppliers. Additional exclusions, particularly for machinery and foodstuffs, explain most of the remaining gap.

The Section 301 investigation and proposed tariffs look like a straightforward effort to recreate the broad IEEPA/Section 122 tariff regime, rather than the more targeted, country-specific approach Section 301 has historically been used for. Litigation seems likely, and the outcome will be important, but either way the process will raise trade policy uncertainty. The next step is likely to be a Section 301 tariff aimed at countries with “foreign structural excess capacity and production”, namely those where government policies have driven production levels above market demand through subsidies and state-owned enterprises, generating overcapacity that harms U.S. industries. These investigations began in March and are expected to conclude in “weeks” according to US Trade Representative Greer. A key question is whether the associated tariffs will be stacked on top of existing tariffs.

Separately, the administration continues to expand the scope of Section 232 tariffs on metals. Over the past year, Section 232 tariffs have been extended to a broader set of downstream “derivative” products—an approach now being challenged in court. In August 2025, more than 400 HTS codes covering downstream steel and aluminum products were added as Section 232 “derivatives,” alongside a tiered rate structure: 50% on primary metal articles, 25% on substantially metal-intensive derivatives, and a temporary 15% floor on industrial and electrical grid equipment through end-2027. The latest orders i) expand Section 232 derivative coverage to include aluminum lithographic plates and steel racks, and ii) cut certain Section 232 “derivative” tariffs on agricultural, industrial, and home-improvement equipment from 25% to 15% through end-2027. Quantifying the direct impact of these changes is difficult because estimated rates are highly sensitive to the metal share of each finished good, but on net we expect these changes to lower Section 232 tariffs (Global Trade Alert points to 0.7%-pt reduction in the average effective tariff rate).

US tariff rate contribution by statutory authority  
![](images/a085acbe40ed452cfc04979c9f23df590891fde66ce6dcd8fa52f910f1a3a6c5.jpg)

<details>
<summary>stacked bar chart</summary>

| Scenario | HTS baseline | Section 232 | Section 122 | Section 301 (China) | IEEPA | Forced-labor S301 | Brazil S301 |
| -------- | ------------ | ----------- | ----------- | ------------------- | ----- | ----------------- | ----------- |
| Pre-SCOTUS (19 Feb) | ~1.5% | ~4.5% | ~0% | ~1.5% | ~6.5% | ~0% | 0% |
| Current (8 June) | ~1.5% | ~4.5% | ~2.5% | ~1.5% | 0% | 0% | 0% |
| +Forced-labor S301 | ~1.5% | ~4.5% | ~0% | ~1.5% | 0% | ~2.5% | 0% |
| +Brazil S301 | ~1.5% | ~4.5% | ~0% | ~1.5% | 0% | ~2.5% | ~0.5% |
</details>

Source: JPM, Global Trade Alert, US Census Bureau.

Visit the JPM Tariff Monitor for a timely tracking of US tariff rates, collected import duties, changes in US imports by sector and country, and pass-through to US prices.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or construed as encouraging, facilitating, promoting or otherwise approving investment or dealing in such Sanctioned Securities. Clients should be aware of their own legal and compliance obligations when making investment decisions.

Any digital or crypto assets discussed in this research report are subject to a rapidly changing regulatory landscape. For relevant regulatory advisories on crypto assets, including bitcoin and ether, please see https://www.JPM.com/disclosures/cryptoasset-disclosure.

The author(s) of this research report may not be licensed to carry on regulated activities in your jurisdiction and, if not licensed, do not hold themselves out as being able to do so.

Exchange-Traded Funds (ETFs): JPM Securities LLC (“JPMS”) acts as authorized participant for substantially all U.S.-listed ETFs. To the extent that any ETFs are mentioned in this report, JPMS may earn commissions and transaction-based compensation in connection with 

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 09 Jun 2026 11:32 AM BST

Disseminated 09 Jun 2026 11:32 AM BST
"""
