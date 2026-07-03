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
# China RatingDog PMI: Stabilization, Not Reflation

\- June RatingDog manufacturing PMI eased marginally to 51.7.

\- New orders remained resilient, but output and future output slowed.

\- Export orders declined again, confidence softened, and employment gains look selective.

\- Price indices point to margin relief, not broad reflation.

\- We expect managed stabilization in 2H. Lower energy prices, a global IP/AI cycle and possible fiscal catch-up are supportive, but trade uncertainty, weak consumer demand and limited pricing power still constrain recovery.

Consistent with NBS PMIs. RatingDog's June manufacturing PMI points to resilient manufacturing momentum, but not a broad demand-led upturn. The headline index came in below expectations, easing marginally to 51.7 (JPM: 52.1; consensus: 52.0) from 51.8, but stayed above 50 for a seventh consecutive month and delivered the strongest quarterly average since 4Q 2020. New orders expanded for a thirteenth month, matching the longest expansion sequence since 2018, while output increased for a seventh month and remained above its long-run trend. The April-May soft patch has stabilized, supported by genuine order flow rather than inventory adjustment.

Export orders declined again to 49.4, albeit marginally, suggesting that export resilience is becoming more contested as front-loading fades and tariff uncertainty persists into 2H. Employment rose to expansion at 50.5, the fastest pace since August 2023, while backlogs increased, pointing to better capacity utilization. But this looks like selective hiring to meet existing orders rather than the start of a broad employment cycle. NBS details reinforce this caution, with weak employment and inventories pointing to continued corporate caution on demand durability, restocking and capex.

Price indicators point to margin stabilization, not broad reflation. RatingDog input prices slowed to 52.4 from 55.8 in May, while output prices (52.2) increased for a sixth month. The combination is constructive for margins as energy and upstream-cost pressures ease, but it does not yet indicate strong downstream pricing power. Consistent with the latest NBS price signals, the worst deflation concerns may have eased, but reflation remains narrow, cost-sensitive and dependent on whether stronger orders translate into income, services demand and firmer domestic pricing power. In the near term, RatingDog PMIs point to stabilizing PPI rather than renewed reflation. But CPI pass-through should remain limited given subdued CPI and core CPI, weak wage growth and still-soft services demand.

## Supply resilience but weak transmission

RatingDog PMIs indicates supply-led resilience in a two-speed economy. Manufacturers tied to domestic orders, equipment upgrading, high-end manufacturing and selected export supply chains continue to outperform the wider economy. Two external drivers have become more supportive. The re-opening of

See page 4 for analyst certification and important disclosures.

Emerging Markets Asia, Economic and Policy Research

Feng Zhu  
(852) 2800 1745  
feng.zhu@JPM.com

Tingting Ge (852) 2800-0143 tingting.ge@JPM.com

Tongfang Yuan (852) 2800-0085 tongfang.yuan@JPM.com

jiayi.c.li@JPM.com

JPM Chase Bank, N.A., Hong Kong Branch

the Strait of Hormuz and lower energy prices have reduced input-cost and freight pressures, helping explain the easing in input-cost inflation. At the same time, the global IP/AI cycle continues to support electronics, capital goods, power equipment and advanced manufacturing. These forces reinforce China's manufacturing rebalancing, but they do not by themselves generate a broad recovery in household-facing demand.

The binding constraint is transmission. Better hiring and rising backlogs likely reflect firms meeting current orders rather than a generalized shift in labor demand or investment appetite. Export orders have slipped for two months, and trade frictions with the US, Europe and other major partners could keep external demand uneven through tariff uncertainty, rules-of-origin scrutiny, anti-subsidy actions and local-content pressure. Manufacturing resilience may cushion growth and keep activity near target, but without stronger wages, household confidence and private-sector returns, it is unlikely to become a self-sustaining recovery. We therefore expect managed stabilization, not a recovery broad enough to reflate.

China: RatingDog PMI breakdown  
![](images/856a2bad719dcb43f0474eef28ee63eb0f26523f0f1bea2dc92665dc43523a5d.jpg)  
Source: S&P Global, JPM

China: RatingDog PMI  
Index, sa

<table><tr><td></td><td>2025</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td></tr><tr><td>Overall</td><td>50.2</td><td>52.1</td><td>50.8</td><td>52.2</td><td>51.8</td><td>51.7</td></tr><tr><td>Output</td><td>50.7</td><td>53.6</td><td>50.8</td><td>53.8</td><td>53.4</td><td>52.8</td></tr><tr><td>New orders</td><td>50.7</td><td>53.5</td><td>51.1</td><td>53.4</td><td>52.5</td><td>52.7</td></tr><tr><td>Export orders</td><td>49.5</td><td>54.0</td><td>50.4</td><td>51.1</td><td>49.6</td><td>49.4</td></tr><tr><td>Future output</td><td>54.9</td><td>56.4</td><td>54.4</td><td>55.7</td><td>55.0</td><td>54.2</td></tr><tr><td>Input prices</td><td>50.3</td><td>53.7</td><td>57.0</td><td>57.5</td><td>55.8</td><td>52.4</td></tr><tr><td>Output prices</td><td>49.1</td><td>51.0</td><td>52.2</td><td>53.6</td><td>52.0</td><td>52.2</td></tr><tr><td>Employment</td><td>49.1</td><td>50.1</td><td>50.3</td><td>49.9</td><td>49.8</td><td>50.5</td></tr><tr><td>Backlogs of Work</td><td>50.5</td><td>50.7</td><td>51.4</td><td>50.9</td><td>51.0</td><td>51.0</td></tr><tr><td>Finished goods inventory</td><td>49.8</td><td>50.0</td><td>49.4</td><td>50.1</td><td>50.6</td><td>50.2</td></tr><tr><td>Order to inventory ratio</td><td>1.0</td><td>1.07</td><td>1.03</td><td>1.07</td><td>1.04</td><td>-</td></tr></table>

Source: S&P Global, JPM  
Note: green: >50 & improving; light green: >50 but declining; yellow: <50 but improving; red: <50 & declining.

China: Manufacturing PMIs  
![](images/97dbdc688edc7ce8e68bf0968e2cce7e4dc5b877242f37d2cc715f74c891bb85.jpg)

China: IP and manufacturing PMI output  
![](images/64185dcf4cba12e1e7926411dcf439b5a6f9e4f118d772ac77fd0b5a433106db.jpg)

China: manufacturing PMI export orders and merchandise exports  
![](images/cdf99588296b236423553daef9d5e660512350f1f57f0ee41011de369a20bdd3.jpg)  
Source: S&P Global, NBS, JPM

China: PPI and manufacturing PMI input prices  
![](images/effa48b4c0f32f4cdd95c3531f9ec5de3f64e3d73705599c4525f5127f8b4a34.jpg)

China: Manufacturing future output PMIs  
![](images/26e025bd589e9bba64b5fff4f3fcd8804d99ef8acc6a83d1175d52bf73084804.jpg)  
Source: NBS, S&P Global, JPM

China: Manufacturing PMI - employment  
![](images/bf4eb0b446da68d172fbf97575b882856a93eab839169b54bcfaaf928f467657.jpg)

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

Argentina: JPM Chase Bank N.A Sucursal Buenos Aires is regulated by Banco Central de la República Argentina (“BCRA”- Central Bank of Argentina) and Comisión Nacional de Valores (“CNV”- Argentinian Securities Commission - ALYC y AN Integral N°51).

Australia: JPM Securities Australia Limited ("JPMSAL") (ABN 61 003 245 234/AFS Licence No: 238066) is regulated by the Australian Securities and Investments Commission and is a Market Participant of ASX Limited, a Clearing and Settlement Participant of ASX Clear Pty Limited and a Clearing Participant of ASX Clear (Futures) Pty Limited. This material is issued and distributed in Australia by or on behalf of JPMSAL only to "wholesale clients" (as defined in section 761G of the Corporations Act 2001). A list of all financial products covered can be found by visiting https://www.jpmm.com/research/disclosures. JPM seeks to cover companies of relevance to the domestic and international investor base across all Global Industry Classification Standard (GICS) sectors, as well as across a range of market capitalisation sizes. If applicable, in the course of conducting public side due diligence on the subject company(ies), the Research Analyst team may at times perform such diligence through corporate engagements such as site visits, discussions with company representatives, management presentations, etc. Research issued by JPMSAL has been prepared in accordance with JPM Australia's Research Independence Policy which can be found at the following link: JPM Australia - Research Independence Policy.

Brazil: Banco JPM S.A. is regulated by the Comissao de Valores Mobiliarios (CVM) and by the Central Bank of Brazil. Ombudsman

JPM: 0800-7700847 / 0800-7700810 (For Hearing Impaired) / ouvidoria.jp.morgan@jpmchase.com.

Canada: JPM Securities Canada Inc. is a registered investment dealer, regulated by the Canadian Investment Regulatory Organization and the Ontario Securities Commission and is the participating member on Canadian exchanges. This material is distributed in Canada by or on behalf of JPM Securities Canada Inc.

Chile: Inversiones JPM Limitada is an unregulated entity incorporated in Chile.

China: JPM Securities (China) Company Limited has been approved by CSRC to conduct the securities investment consultancy business.

Colombia: Banco JPM Colombia S.A. is supervised by the Superintendencia Financiera de Colombia (SFC). Any reference in this material to products or services offered abroad by entities other than the Bank in Colombia is included exclusively for descriptive purposes. Such references do not constitute, and should not be construed as, promotional activity or the provision of financial products or services within Colombian territory, as defined under applicable Colombian regulation.

Dubai International Financial Centre (DIFC): JPM Chase Bank, N.A., Dubai Branch is regulated by the Dubai Financial Services Authority (DFSA) and its registered address is Dubai International Financial Centre - The Gate, West Wing, Level 3 and 9 PO Box 506551, Dubai, UAE. This material has been distributed by JPM Chase Bank, N.A., Dubai Branch to persons regarded as professional clients or market counterparties as defined under the DFSA rules.

European Economic Area (EEA): Unless specified to the contrary, research is distributed in the EEA by JPM SE (“JPM SE”), which is authorised as a credit institution by the Federal Financial Supervisory Authority (Bundesanstalt für Finanzdienstleistungsaufsicht, BaFin) and jointly supervised by the BaFin, the German Central Bank (Deutsche Bundesbank) and the European Central Bank (ECB). JPM SE is a company headquartered in Frankfurt with registered address at TaunusTurm, Taunustor 1, Frankfurt am Main, 60310, Germany. The material has been distributed in the EEA to persons regarded as professional investors (or equivalent) pursuant to Art. 4 para. 1 no. 10 and Annex II of MiFID II and its respective implementation in their home jurisdictions (“EEA professional investors”). This material must not be acted on or relied on by persons who are not EEA professional investors. Any investment or investment activity to which this material relates is only available to EEA relevant persons and will be engaged in only with EEA relevant persons.

Hong Kong: JPM Securities (Asia Pacific) Limited (CE number AAJ321) is regulated by the Hon

[中间内容因长度限制已省略]

of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
