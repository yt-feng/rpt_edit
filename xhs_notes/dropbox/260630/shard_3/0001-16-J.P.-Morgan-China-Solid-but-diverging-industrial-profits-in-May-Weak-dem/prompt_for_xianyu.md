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
# China: Solid but diverging industrial profits in May

## Weak demand caps a broader profit recovery

• Year-to-date industrial profit growth remained strong at 18.8% oya.

\- Two-speed growth continues: tech and upstream raw materials drove the gains; consumer-related sectors lagged.

\- Tech/equipment manufacturing profits could continue to outperform on the “AI+”/industrial upgrade push.

• Receding energy risks could provide cost relief.

Headline industrial profits growth edged up to 18.8% oya ytd (vs 18.2% in Jan-April), while the pace of expansion slightly moderated to 21.1% oya in May (from 24.7% in April). In Jan-May, sales revenue rose 5.5% oya, while costs rose more slowly at 4.7%, supporting net profit margin. That said, accounts receivable climbed 7.7% oya and finished goods inventories rose 8.8%, pointing to cash conversion pressure and slower turnover. Profit gains remained broad-based across ownership types, led by shareholding firms (+24.1% oya ytd), followed by SOEs (+19.6%), private (+10.7%) and foreign firms (+4.2%).

The profit gains continued to be led by the policy tailwinds and raw materials sectors. Electronics manufacturing profits rose 103.9% in Jan-May, on the global AI upcycle and strong demand for memory chips, despite overall equipment manufacturing profits expanding at a slower pace (+14.1% oya ytd). In Jan-May, high-tech manufacturing profits rose 44.7% oya, driven by fast improvements in the semiconductor supply chain (e.g. electronic special materials +665.4%, optoelectronic devices +53.8%, etc.).

Rising demand from AI and new energy products has also benefited upstream materials, keeping non-ferrous metal prices at high levels (e.g. copper, aluminum) and driving its profits up by 117.1% oya. Along the oil production chain, the petro-processing industry swung from last year's loss to profit, and profits in the chemical industry rose by 71.6% oya ytd, driven by elevated global energy prices through May.

In contrast, downstream and consumer-related industries underperformed, reflecting weak pricing power and limited pass-through amid still-soft demand. While producer-goods PPI has improved, consumer-goods PPI remained in deflation in May (-0.8% oya), posing margin squeeze risks. Profit declines deepened in furniture in Jan-May (-58.4% vs -54.4% in Jan-Apr) and autos (-19.8% vs -16.8% in Jan-Apr), and remained negative in apparel (-11.4%) and cultural/sports/entertainment goods (-7.4%).

Emerging Markets Asia, Economic and Policy Research

Looking ahead, we expect the two-speed profit growth to persist as industrial restructuring and upgrading deepen. High-tech/equipment manufacturing profits may continue to outperform, supported by the government's multi-year "AI+" and industrial upgrading agenda and the global IP and AI cycle. However, a more binding constraint on broader profit recovery remains soft domestic demand and a likely lengthy rebalancing process, which could keep profit recovery in consumer

See page 4 for analyst certification and important disclosures.

Jiayi Li  
(852) 2800-5229  
jiayi.c.li@JPM.com

Feng Zhu  
(852) 2800 1745  
feng.zhu@JPM.com

Tingting Ge (852) 2800-0143 tingting.ge@JPM.com

Tongfang Yuan  
(852) 2800-0085  
tongfang.yuan@JPM.com  
JPM Chase Bank, N.A., Hong Kong Branch

industries lagging. While we expect below-par fiscal execution in 2Q to leave room for stronger fiscal support later in the year, a more balanced industrial profits gain likely requires a larger fiscal push. With Brent now expected to average \$80/bbl in 2H26, input cost and supply chain pressures could ease for energy-intensive industries and margin-thin downstream sectors, modestly narrowing the existing profit divergence.

Industrial enterprise profit growth

<table><tr><td></td><td>2025</td><td>Jan-Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Profit growth (%oya, ytd)</td><td>0.6</td><td>15.2</td><td>15.5</td><td>18.2</td><td>18.8</td></tr><tr><td>Profit growth (%oya)</td><td></td><td>15.2</td><td>15.8</td><td>24.7</td><td>21.1</td></tr><tr><td>Sales revenue (%oya, ytd)</td><td>1.1</td><td>5.3</td><td>5.0</td><td>5.2</td><td>5.5</td></tr><tr><td>Cost of sales (%oya, ytd)</td><td>1.3</td><td>5.0</td><td>4.5</td><td>4.5</td><td>4.7</td></tr><tr><td>Profit margin (%)</td><td>5.31</td><td>4.92</td><td>5.11</td><td>5.43</td><td>5.56</td></tr></table>

Source: NBS, JPM

![](images/328a5fcf4c108d35c8c10cd31db4f183b5ef363af2e13ce90df32d0bc74bbca7.jpg)  
Source: NBS, JPM

Industrial enterprise finished goods inventory to sales ratio Ratio, 3mma, sa  
![](images/dbed21d481714966171e41f7ba76fae6630711f8e182c7a1e0fb96f98770df11.jpg)  
Source: NBS, JPM

China PPI and industrial profits %oya, ytd, both scales  
![](images/2d75ebbe36950dc81130e7337b21a9511cc3d278389d365d84aa804a145c08b8.jpg)  
Source: NBS, JPM

China industrial enterprises' profits and sales revenue %oya, ytd, both scales  
![](images/84041d9e0aa8086bb49d37d7a53e8b56baff402ef5ba06330f9538fb819ea163.jpg)  
Source: NBS, JPM

Industrial enterprise profit growth by type  
![](images/6769c9a04e0a0f15f9e7e8218ff70c1b3d321345135de2da5f36c8b44d7d3a24.jpg)  
Source: NBS, JPM

China: Industrial enterprise inventory and PPI inflation %oya, both scales PPI inflation  
![](images/0273133a118516644d392434bcfe420490f69c41fdf00f43ef4c39a229e13700.jpg)  
Source: NBS, JPM

Industrial enterprise financial data

<table><tr><td></td><td>Jan-Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Product inventory (%oya)</td><td>6.6</td><td>5.2</td><td>6.7</td><td>8.8</td></tr><tr><td>Product inventory turnover (days)</td><td>22.7</td><td>21.5</td><td>21.4</td><td>21.6</td></tr><tr><td>Accounts receivable (%oya)</td><td>7.1</td><td>6.7</td><td>7.2</td><td>7.7</td></tr><tr><td>Payback period of receivables (days)</td><td>76.4</td><td>72.6</td><td>72.2</td><td>72.6</td></tr><tr><td>Liability to asset ratio (%)</td><td>57.6</td><td>57.8</td><td>58.0</td><td>58.2</td></tr><tr><td>SOE liability to asset ratio (%)</td><td>57.3</td><td>57.4</td><td>57.6</td><td>57.6</td></tr></table>

Source: NBS, JPM

Industrial enterprise profit growth by sector

<table><tr><td></td><td>% share (2025)</td><td>2025</td><td>Jan-Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Mining</td><td>11.3</td><td>-26.2</td><td>9.9</td><td>16.2</td><td>26.0</td><td>33.5</td></tr><tr><td>Manufacturing</td><td>76.9</td><td>5.0</td><td>18.9</td><td>19.1</td><td>20.4</td><td>20.0</td></tr><tr><td>Chemical Material &amp; Product</td><td>5.1</td><td>-7.3</td><td>35.9</td><td>54.5</td><td>73.4</td><td>71.6</td></tr><tr><td>Pharmaceutical</td><td>4.7</td><td>-1.7</td><td>16.2</td><td>-42.6</td><td>-50.7</td><td>-48.9</td></tr><tr><td>Automobile</td><td>6.2</td><td>0.6</td><td>-30.2</td><td>-17.7</td><td>-16.8</td><td>-19.8</td></tr><tr><td>Electrical Machinery &amp; Equipment</td><td>8.6</td><td>4.9</td><td>6.2</td><td>0.0</td><td>-11.4</td><td>-13.7</td></tr><tr><td>General Equipment</td><td>4.9</td><td>4.2</td><td>3.6</td><td>-1.9</td><td>-0.6</td><td>-0.2</td></tr><tr><td>Special Equipment</td><td>4.1</td><td>5.7</td><td>4.3</td><td>-8.2</td><td>-7.2</td><td>-5.5</td></tr><tr><td>Computer, Communication &amp; Other Electronic Equipment</td><td>10.1</td><td>19.5</td><td>203.5</td><td>124.5</td><td>107.7</td><td>103.9</td></tr></table>

Source: NBS, JPM

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

Australia: JPM Securities Australia Limited ("JPMSAL") (ABN 61 003 245 234/AFS Licence No: 238066) is regulated by the Australian Securities and Investments Commission and is a Market Participant of ASX Limited, a Clearing and Settlement Participant of ASX Clear Pty Limited and a Clearing Participant of ASX Clear (Futures) Pty Limited. This material is issued and distributed in Australia by or on behalf of JPMSAL only to "wholesale clients" (as defined in section 761G of the Corporations Act 2001). A list of all financial products covered can be found by visiting https://www.jpmm.com/research/disclosures. JPM seeks to cover companies of relevance to the domestic and international investor base across all Global Industry Classification Standard (GICS) sectors, as well as across a range of market capitalisation sizes. If applicable, in the course of conducting public side due diligence on the subject company(ies), the Research Analyst team may at times perform such diligence through corporate engagements such as site visits, discussions with company representatives, management presentations, etc. Research issued by JPMSAL has been prepared in accordance with JPM Australia's Research Independence Policy which can be found at the following link: JPM Australia - Research Independence Policy.

Brazil: Banco JPM S.A. is regulated by the Comissao de Valores Mobiliarios (CVM) and by the Central Bank of Brazil. Ombudsman

JPM: 0800-7700847 / 0800-7700810 (For Hearing Impaired) / ouvidoria.jp.morgan@jpmchase.com.

Canada: JPM Securities Canada Inc. is a registered investment dealer, regulated by the Canadian Investment Regulatory Organization and the Ontario Securities Commission and is the participating member on Canadian exchanges. This material is distributed in Canada by or on behalf of JPM Securities Canada Inc.

Chile: Inversiones JPM Limitada is an unregulated entity incorporated in Chile.

China: JPM Securities (China) Company Limited has been approved by CSRC to conduct the securities investment consultancy business.

Colombia: Banco JPM Colombia S.A. is supervised by the Superintendencia Financiera de Colombia (SFC). Any reference in this material to products or services offered abroad by entities other than the Bank in Colombia is included exclusively for descriptive purposes. Such references do not constitute, and should not be construed as, promotional activity or the provision of financial products or services within Colombian territory, as defined under applicable Colombian regulation.

Dubai International Financial Centre (DIFC): JPM Chase Bank, N.A., Dubai Branch is regulated by the Dubai Financial Services Authority (DFSA) and its registered address is Dubai International Financial Centre - The Gate, West Wing, Level 3 and 9 PO Box 506551, Dubai, UAE. This material has been distributed by JPM Chase Bank, N.A., Dubai Branch to persons regarded as professional clients or market counterparties as defined under the DFSA rules.

European Economic Area (EEA): Unless specified to the contrary, research is distributed in the EEA by JPM SE (“JPM SE”), which is authorised as a credit institution by the Federal Financial Supervisory Authority (Bundesanstalt für Finanzdienstleistungsaufsicht, BaFin) and jointly supervised by the BaFin, the German Central Bank (Deutsche Bundesbank) and the European Central Bank (ECB). JPM SE is a company headquartered in Frankfurt with registered address at TaunusTurm, Taunustor 1, Frankfurt am Main, 60310, Germany. The material has been distributed in the EEA to persons regarded as professional investors (or equivalent) pursuant 

[中间内容因长度限制已省略]

of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
