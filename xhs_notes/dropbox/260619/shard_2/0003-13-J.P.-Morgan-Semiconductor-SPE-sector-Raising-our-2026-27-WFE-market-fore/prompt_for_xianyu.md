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
# Semiconductor/SPE sector

# Raising our 2026–27 WFE market forecasts

We raise our wafer fab equipment (WFE) market growth forecasts for CY2026 from 21% to 28% YoY and for CY2027 from 18% to 29%. We newly estimate a 16% YoY increase in CY2028. Driven by rising and broadening AI-related demand, cloud services providers (CSPs) are further accelerating their investments. We expect total investment by the top four US CSPs to increase 80% YoY in 2026 and 50% in 2027 (see a report by Samik Chatterjee et al.). Although demand is strong, chipmakers' shortage of cleanrooms had been a concern to some extent for CY2026, but the outlook is improving owing to such factors as creative use of factory space. From 2027 onward, we expect demand to increase as cleanroom expansions get underway in earnest.

\- Raising our 2026–27 WFE market forecasts: The global WFE market remained strong in CY2025, growing 11% YoY, although China, which accounts for 35-40% of the total WFE market, saw a slight YoY decline, reflecting a pullback from the previous year. Our bottom-up forecasts for WFE market growth are now 28% YoY (previously 21%) for CY2026 and 29% (previously 18%) for CY2027, and we introduce our CY2028 forecast of 16% growth (see Figure 21 for details). DRAM and TSMC are the main reasons for the upward revisions. We also raise our forecasts for logic chip and NAND flash memory equipment, albeit to a lesser degree, and view the business environment as generally favorable. As AI workloads shift from training to inference, the demand structure is broadening beyond accelerators, and the weighting of memory chip investment in particular is on an uptrend. We expect the memory chip weighting of CSP investment to rise from the previous single-digit-to-15% range to about 50% in 2026 (see a global memory chip report by Jay Kwon et al. for details), and we think companies with a high weighting of sales to TSMC and equipment makers with a high memory chip weighting will likely continue to be favored.

\- Semiconductor shipments: Global semiconductor shipments increased 106% YoY in April 2026, marking the 32nd consecutive month of growth since September 2023, and the strongest increase since at least 1994. While volume also grew in the double-digit %, the increase was largely driven by memory chip prices (with both NAND flash memory and DRAM prices seeing triple-digit growth). Even excluding memory chips, the growth was high at 33% YoY. We think AI accelerators (GPUs and ASICs) and HBM continued to drive this strong demand (see a WSTS report by Gokul Hariharan et al. for details).

## Japan Equity Research

## Technology - Semiconductor/Technical Materials

## Mio Shikanai AC

(81-3) 6736 1313

mio.shikanai@JPM.com

JPM Securities Japan Co., Ltd.

## Harlan Sur

(1-415) 315-6700

harlan.sur@JPM.com

JPM Securities LLC

## Junya Ayada

(81-3) 6736 8631

junya.ayada@JPM.com

JPM Securities Japan Co., Ltd.

## Gokul Hariharan

(852) 2800-8564

gokul.hariharan@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Jay Kwon

(82-2) 758-5725

jay.h.kwon@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

## Sandeep Deshpande

(44-20) 7134-5276

sandeep.s.deshpande@JPM.com

JPM Securities plc

## Billy Feng

(86-21) 6106 6359

billy.feng@JPM.com

SAC Registration Number: S1730520030005

JPM Securities (China) Company Limited

## Mayur Ramdhani

(1-212) 622-1664

mayur.ramdhani@JPM.com

JPM Securities LLC

## Jimmy Huang

(886-2) 2725-9865

jimmy.huang@JPM.com

JPM Securities (Taiwan) Limited

## Contributing Authors

<table><tr><td>Technology - Semiconductor / Technical MaterialsMio ShikanaiACmio.shikanai@JPM.com(81-3) 6736-1313</td><td>Semiconductors &amp; Semiconductor Capital Equipment/ IT HardwareHarlan Surharlan.sur@JPM.com(1-415) 315-6700</td><td>Technology - Consumer Electronics / Industrial Electronics / PrecisionJunya Ayadajunya.ayada@JPM.com(81-3) 6736-8631</td></tr><tr><td>Technology and TelecomsGokul Hariharangokul.hariharan@JPM.com(852) 2800 -8564</td><td>Technology - SemiconductorsJay Kwonjay.h.kwon@JPM.com(82-2) 758-5725</td><td>European Tech Hardware &amp; PaymentsSandeep Deshpandesandeep.s.deshpande@JPM.com(44-20) 7134-5276</td></tr><tr><td>TechnologyBilly Fengbilly.feng@JPM.com(86-21) 6106-6359</td><td>Semiconductors &amp; Semiconductor Capital Equipment/ IT HardwareMayur Ramdhanimayur.ramdhani@JPM.com(1-212) 622-1664</td><td>TechnologyJimmy Huangjimmy.huang@JPM.com(886-2) 2725-9865</td></tr><tr><td>Technology - HardwareAlbert Hungalbert.hung@jpmchase.com(886-2) 2725-9875</td><td>Technology - SemiconductorsSangsik Leesangsik.lee@JPM.com(82-2) 758 5146</td><td>Technology - SemiconductorsNeelay Y Kamathneelay.kamath@jpmchase.com(91-22) 6157-3764</td></tr><tr><td>Technology and TelecomsSubham Singhaniasubham.singhania@JPM.com(91-22) 6157-3801</td><td>TechnologyRi Xuri.xu@jpmchase.com(86-21) 6106 6318</td><td></td></tr></table>

Top picks of JPM tech team analysts within SPE

<table><tr><td>Billy Feng</td><td>AMEC-A (688012 CH), NAURA-A (002371 CH)</td></tr><tr><td>Gokul Hariharan</td><td>ASMPT Ltd (522 HK)</td></tr><tr><td>Harlan Sur</td><td>KLA Corporation (KLAC US)</td></tr><tr><td>Jimmy Huang</td><td>Hon. Precision (7769 TT), Grand Process Tech (3131 TT)</td></tr><tr><td>Mio Shikanai</td><td>Tokyo Electron (8035 JT), Advantest (6857 JT)</td></tr><tr><td>Sandeep Deshpande</td><td>ASML (ASML NA)</td></tr></table>

Our global tech team's main assumptions for end demand are for (1) iPhone sales volume to increase $1.3\%$ YoY in CY2026 and decrease $0.4\%$ in CY2027, (2) notebook PC shipment volume to decrease $8.4\%$ YoY in CY2026 and increase $1.5\%$ in CY2027, (3) server shipments to increase $14.6\%$ YoY in CY2026 and rise $8.3\%$ in CY2027, and (4) smartphone shipment volume to decline $11.3\%$ YoY in CY2026 and decrease $2.6\%$ in CY2027 (see Figure 35for details). Based on aggregate capex by major semiconductor makers, we forecast the WFE market will grow $28\%$ YoY in CY2026, $29\%$ YoY in CY2027 and $16\%$ YoY in CY2028 (see Figure 21for details).

Figure 1: Shipment value of semiconductors and SPE (YoY)  
![](images/f121c24a6a1770044e1d2d3eed73dd98107b178ad430c6a87c9d7f27257f633a.jpg)

<details>
<summary>line chart</summary>

| Date   | Semiconductor Shipment (lhs) | SPE Shipment (rhs) |
|--------|-----------------------------|--------------------|
| Jan-98 | -                           | 20%                |
| Jan-99 | -                           | -25%               |
| Jan-00 | -                           | 75%                |
| Jan-01 | -                           | 50%                |
| Jan-02 | -                           | -30%               |
| Jan-03 | -                           | 25%                |
| Jan-04 | -                           | 60%                |
| Jan-05 | -                           | -10%               |
| Jan-06 | -                           | 25%                |
| Jan-07 | -                           | 10%                |
| Jan-08 | -                           | -10%               |
| Jan-09 | -                           | -30%               |
| Jan-10 | -                           | 125%               |
| Jan-11 | -                           | 75%                |
| Jan-12 | -                           | -10%               |
| Jan-13 | -                           | -25%               |
| Jan-14 | -                           | 25%                |
| Jan-15 | -                           | 10%                |
| Jan-16 | -                           | 5%                 |
| Jan-17 | -                           | 50%                |
| Jan-18 | -                           | 25%                |
| Jan-19 | -                           | 10%                |
| Jan-20 | -                           | 25%                |
| Jan-21 | -                           | 30%                |
| Jan-22 | -                           | 25%                |
| Jan-23 | -                           | 10%                |
| Jan-24 | -                           | 25%                |
| Jan-25 | -                           | 30%                |
| Jan-26 | -                           | 100%               |
</details>

Source: WSTS, SEMI, SEAJ, JPM.

Figure 2: SPE shipment trend by region  
![](images/5380898acf69e95edf3af3e09326e7e096dc49a01b897faaf9005134810a3782.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | China ($bn) | Europe ($bn) | Japan ($bn) | N. America ($bn) | Korea ($bn) | Taiwan ($bn) |
| --- | --- | --- | --- | --- | --- | --- |
| 2004 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2005 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2006 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2007 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2008 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2009 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2010 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2011 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2012 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2013 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2014 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2015 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2016 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2017 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2018 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2019 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2020 | 10 | 15 | 10 | 5 | 5 | 5 |
| 2021 | 30 | 30 | 30 | 30 | 30 | 30 |
| 2022 | 30 | 30 | 30 | 30 | 30 | 30 |
| 2023 | 30 | 30 | 30 | 30 | 30 | 30 |
</details>

Source: SEMI, JPM estimates.

Figure 3: Global SPE shipment trend excluding China  
![](images/66a667ec1186945904ffe22490075898e091f7d2a92e34677b89ef3e6207d8e9.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | WFE ex. China (Ihs) ($bn) | YoY% (rhs) (%) |
| :--- | :--- | :--- |
| 2018 | 50 | 80 |
| 2019 | 40 | -10 |
| 2020 | 50 | 10 |
| 2021 | 70 | 50 |
| 2022 | 80 | 15 |
| 2023 | 70 | -10 |
| 2024 | 75 | 5 |
| 2025 | 90 | 15 |
| 2026E | 120 | 35 |
| 2027E | 155 | 30 |
| 2028E | 180 | 15 |
</details>

Source: Gartner®, JPM estimates.

\- CoWoS/advanced packaging: We expect TSMC's CoWoS production capacity to expand to 115,000 wafers per month at end-2026, 175,000 at end-2027, and 220,000 at end-2028 (previous estimates: 115,000, 145,000, N/A). The accelerated ramp-up of the company's own production capacity and the utilization of OSATs and VIS (for interposer manufacturing) will also likely be an upside factor. CoPoS progress is slower than we expected, and we think TSMC will absorb demand for the time being by extending the life of CoWoS and using larger reticles (up to 14x in 2028). In addition, the pace of CoWoS production capacity expansion will also likely accelerate (TSMC said it plans to expand its CoWoS production capacity at a CAGR of 80%+ in 2022–28). We slightly raise our outlook for Nvidia's CoWoS demand, owing to the strength of the Blackwell GB300, Spectrum X, and Vera CPUs, but are somewhat conservative on Rubin given HBM4 uncertainties. We expect production to ramp up in 3Q 2026 and reach full-scale mass levels in 4Q 2026. We significantly raise our 2027 estimate of AMD's CoWoS demand to reflect the ramp-up of the MI450 and Venice (we assume Venice will be transferred to OSATs by 2027). Google's TPUs are also on an uptrend, and we expect increased CoWoS allocations for both Broadcom and MediaTek. The direction of the TPU v9 architecture is likely to be finalized by year-end between two options: EMIB and CoWoS-L + 3D SoIC. Demand for AWS Trainium (Trn3) remains strong even under supply constraints, and we see upside potential heading into 2027. On the technology front, 3D SoIC adoption will likely expand in 2H 2027 onward. We estimate SoIC capacity of 40,000 wafers per month at end-2027 and 65,000 at end-2028. In addition, CPUs, LPUs, and networks (CPO/NPO) could become new drivers of CoWoS demand; WMCM capacity is likely to expand to 75,000 wafers per month at end-2027 and 90,000 at end-2028; and companies other than Apple could consider similar solutions in 2028 (reference: May 17 report by Gokul Hariharan et al.)

\- Capex at TSMC: We expect capex to increase 37% in 2026 to \$56 billion, 16% in 2027 to \$65 billion, and 11% in 2028 to \$72 billion (previous estimates: \$54 billion, \$56 billion, N/A). We think the supply shortage in the area of advanced nodes (N5 and below) will last until 2027 or early 2028 and expect TSMC to accelerate its production capacity expansion. We expect the company's production capacity of N5 and below to grow at a 25% CAGR in 2025–28, with the majority ramping up in 2027–28. For N3, TSMC plans to ramp up three new fabs (Tainan Fab 18 P9, Arizona Phase 2, and JASM's second fab) from 1H 2027 through 2028. For N2, it has a strong pipeline, including iPhone processors, AMD's Venice and MI450, Google's TPUs, and Nvidia's Feynman. We expect capacity expansion centered on Kaohsiung P1-5 and AZ Phase 2 (we estimate \~60,000 wafers per month at end-2026 and \~150,000 at end-2027) (reference: April 17 report by Gokul Hariharan et al.).

\- Foundry trends: TSMC reported strong 1Q 2026 revenue of \~\$36 billion (+6% QoQ), with N3/N5 production at over 100% capacity and blended ASP rising 11% YoY. Management raised its 2026 USD revenue growth guidance to over 30% from close to 30% previously. Along with the earnings results announcement in July, management could raise its guidance because of strong demand for networks/CPUs in addition to AI accelerators. We expect the shortage in the area of advanced nodes (N5 and below) to last until 2027 or early 2028 and N3/N2 capacity expansions to accelerate (e.g., for N3 to 213,000 wafers per month at end-2027 and to 237,000 at end-2028 and for N2 to \~150,000 wafers per month at end-2028). On pricing, TSMC raised prices by 6-10% for advanced-node chips in 1Q 2026. We think

discussions on additional price hikes for 2027 (likely to be 5-10% for N3 and below) could begin in 2Q 2026 (reference: June 10 report by Gokul Hariharan et al.)

\- Memory chip capex: We expect memory chip industry capex to accelerate over the next three years, driven by a strong improvement in memory chip prices and the likelihood that supply shortages will continue for several years. We estimate total capex over the next three years of \$450 billion, up from our previous estimate of \$300 billion in the end-2025 model. Of the total, we assume DRAM capex of \$364 billion, with EUV procurement and infrastructure development likely the main bottlenecks. We expect WSPM to increase to 2.8 million at end-2028 (+880,000 from end-2025). For NAND flash memory, we assume WSPM of 1.44 million (+165,000) at end-2028 and cumulative capex of \$86 billion over three years. The focus of spending is likely to be on technology transitions, and contributions from greenfield investments will probably come in 2H 2028 onward (reference: May 29 report by Jay Kwon et al.)

\- Cloud capex: We raise our capex growth forecasts for the top four US CSPs (Google, Amazon, Microsoft, and Meta) from 63% to 80% in 2026 and from over 40% to 50% in 2027, driven by accelerating investments to expand AI-related data centers and power capacity in North America. In value terms, we expect the largest step-up ever, exceeding +\$250 billion YoY in 2026 and +\$285 billion YoY in 2027, despite a slowdown in growth. Backing this up, planned power capacity in North America exceeded 175 GW at end-1Q 2026 (and we think it is likely to rise to over 205 GW by year-end). We expect installed capacity to increase from 48 GW in 2025 to 65 GW (previously 62 GW) in 2026 and to 85 GW (previously 78 GW) in 2027. We estimate total capex will exceed \$575 billion in 2026 and \$860 billion in 2027, assuming this will be financed by operating cash flows. Until 2023, the top four US CSPs used 25-30% of their operating cash flows to finance capex. We expect this ratio to rise to 82% in 2026 and to 94% in 2027 (reference: May 26 report by Samik Chatterjee et al.)

\- Summary of TMT conference (US semiconductors/SPE): The biggest 

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 17 Jun 2026 05:08 PM JST

Disseminated 17 Jun 2026 05:10 PM JST
"""
