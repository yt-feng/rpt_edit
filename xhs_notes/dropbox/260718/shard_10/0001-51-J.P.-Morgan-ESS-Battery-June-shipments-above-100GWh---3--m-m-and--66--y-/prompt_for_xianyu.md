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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

## ESS Battery

## June shipments above 100GWh, +3% m/m and +66% y/y despite a high base; FY26 on track to 1,100Gwh

Global ESS battery shipments exceeded 100GWh in Jun-26, rising 66% y/y and 3% m/m, according to ICCSino. This brought 1H26 shipments to 508GWh, up 98% y/y, on track to meet or beat JPM's FY26 forecast of 1.1TWh (+78% y/y). Shipments accelerated in 2Q26, although y/y growth moderated due to a high base. China domestic demand remained the primary growth engine, accounting for 45% of global demand and growing >140% y/y in 1H26. Among overseas markets, the EU and RoW represented 19% and 26% of global demand, respectively, with both recording growth of >130% y/y; meanwhile, US demand is increasingly being captured by KR/JP suppliers. Looking ahead, July-August production schedules remain constructive, with most ESS battery makers targeting 3-4% m/m growth and July shipments tracking well across both domestic and overseas markets. BYD is the exception, given a partial reallocation of production from ESS to EV batteries, according to ICCSino's latest forecasts. Overall, ESS demand remains intact and continues to show strong momentum YTD. However, ESS value-chain stocks have corrected materially from their recent peaks, largely reversing their earlier YTD gains. We believe the pullback reflects: (1) technical and near-term sentiment headwinds surrounding CATL and the broader ESS and battery sector; and (2) growing investor concerns over the sustainability of the current pace of China domestic ESS installation and shipments growth. Among JPM's Asia ESS value chain coverage, our top picks are CATL (global leader with market share gains in non-US regions), Sungrow (re-rating potential from direct sales to data centers on new use cases), Deye (riding distributed-generation ESS with strong emerging market exposure), LGES and SDI (well positioned for US ESS opportunities). ESS is also increasingly important for BYD, contributing >20% of its total battery shipments in 2026.

## ESS installations: US +11% y/y in 5M26, China sets 2030 ESS target at 300GW

\- China issued a 2030 ESS target of 300GW for the first time: 15th Five-Year-Plan for New Energy System targeted 300GW energy storage by 2030. This is mentioned for the first time in official government plans. The NDRC previously targeted 180GW ESS capacity by 2027, and we expect China to beat this target. A target of 300GW ESS by 2030 seems conservative, but directionally supportive. Importantly, it points to continued development into 2028-30. For details, please refer to our report (link).

\- US BESS installations +11% y/y in 5M26. US BESS installation reached 570MW in May-26, bringing 5M26 to 5.6GW, up 11% y/y, per the EIA. We continue to see strong US BESS demand in 2026, in part due to a tight power market from AIDCs. JPM view: These data-points are a positive read-across to Sungrow and Korean battery makers.

\- Chinese ESS integrators taking 76% global share, with Sungrow & BYD ranked No. 2 & 3. Wood Mackenzie released the Global Energy Storage System Integrator Market Share Report (link), which finds that Chinese storage system integrators held 76% of global share in 2025, with eight of the

## Asia Autos & EV Battery

Rebecca Wen AC
(852) 2800-8505
rebecca.y.wen@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Alan Hon AC

(852) 2800-8573
alan.hon@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Cathy Liu

(852) 2800-8629
cathy.xiao.liu@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Daqi Jiao

(852) 2800-8595
daqi.jiao@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Sonny Lee

(82-2) 758 5716
sonny.lee@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

## Parsley Ong

(65) 6882-8578
parsley.rh.ong@JPM.com
JPM Securities Singapore Private Limited/
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Nick Lai

(65) 6801-3176
nick.yc.lai@JPM.com
JPM Securities Singapore Private Limited/
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Stephen Tsui, CFA
(852) 2800-8592
stephen.tsui@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

top ten headquartered in China; Tesla and Sungrow remain No.1 and No.2, and BYD rises to No.3. As the market expands, the top three's combined share declines and competition broadens. Sungrow was ranked No.2 in North America & Middle East and No.1 in Europe & Latin America. Note that Sungrow's share price has pulled back due to concerns over geopolitical tensions, and we view its current valuation as attractive and maintain OW on Sungrow.

## Global ESS battery shipments: +98% y/y in 1H26

\- Global ESS battery demand remained strong in June although y/y growth moderated to 66% on a high base. The moderation from over 100% y/y growth in previous months to 66% y/y in June primarily reflected a high Jun-25 base, partly associated with shipment pull-forward ahead of anticipated policy changes, including the US IRA and tariffs and China's Doc 136. Sequential shipment growth also moderated to 3–4% m/m in May-June, versus double-digit growth in March-April, mainly due to capacity constraints. June growth was driven mainly by China domestic demand (>180% y/y) and robust China exports to all ex-US regions (>80% y/y). Global ESS battery supply remains China-led (at a 97% share) in 1H26, while demand is balanced at \~55% overseas and \~45% domestic.

\- Chinese ESS battery exports surged 133% y/y to the EU and 136% y/y to RoW in 1H26. 2Q26 sustained the strong trajectory in ESS exports with 25% q/q and 56% y/y growth despite changes in export tax rebate policy (export tax rebate reduced from 9% to 6% from 1 April). US ESS battery sourcing is continuously shifting away from Chinese suppliers towards KR players, with KR/JP shipments surging \~190% y/y, while Chinese player ESS shipments to the US fell \~40% y/y in 1H25. US battery import data also confirms this trend: China-origin lithium battery shipments declined 52% y/y in 5M26, while Korea-origin shipments (largely from SDI) rose \~40% y/y, underscoring the ongoing sourcing shift as OBBBA regulations remain effective.

\- Distributed storage added a second growth engine, while utility-scale remained the volume backbone. Utility-scale shipments reached \~380 GWh in 1H26, up \~90% y/y, accounting for 77% of Chinese players' shipments (down from 81% in FY25). C&I and residential shipments grew faster, rising 150% and 130% y/y in 1H26. We see this as a broadening of the industry's growth drivers: utility-scale remains critical for absolute volume, while C&I and residential storage offer incremental growth and potentially greater differentiation through channels, products and regional exposure.

\- The market's focus has shifted to 2027 demand - should we be worried about demand sustainability? We see limited risk of broad ESS growth deceleration in 2H26, but flag a higher China-specific shipment slowdown risk from 2H27. We highlighted in our 2-June report that the latest NDRC target calls for 180GW of China ESS installed capacity by 2027 (vs. \~75GW in 2024), while JPM's base case already assumes installations to exceed 320GW by 2027. That points to potential overachievement of the official target and, by extension, the risk of a sharp slowdown or decelerated growth in 1H28. We forecast China ESS installation growth to decelerate to 4% in 2028 from 25% in 2027, with a more meaningful slowdown likely in 1H28; because ESS battery shipments typically lead installations by about six months, shipment deceleration risk could begin as early as 2H27. However, we believe any post-2027 softness may be temporary rather than structural, as underlying storage needs tied to rising renewable penetration should keep growth intact into 2030, with China's renewable mix expected to rise from \~24% by end-2025 toward \~35% by 2030 and ESS penetration catching up from \~7% toward \~18% (still consistent with markets like the UK, where storage remains a grid priority even near \~18% penetration). Finally, other demand drivers may cushion any China ESS slowdown, as China ESS is expected to be less than 20% of total battery demand in 2026 and overseas ESS, particularly Europe and emerging markets, likely to be the more important contributor to battery growth.

## Recommendations

The table below summarizes the key relevant stocks under JPM Asia equity coverage and their exposure to the ESS business.

\- Largest PCS supplier – Sungrow (OW): Sungrow is the world’s largest solar inverter producer by volume, gaining market share in recent years due to cost advantage. Sungrow offers superior product quality and stronger brand recognition compared to domestic peers. We expect Sungrow to benefit from robust ESS demand and rising orders from utilities and data centers.

\- Deye (OW) is a distributed generation (DG) energy storage (ESS) producer with first-mover advantage in emerging markets (EM). Near term, energy supply shocks are accelerating DG solar+storage adoption, especially where diesel DG was prevalent. Longer term, policy may shift toward resilience, supporting sustained growth. Deye's appliance legacy supports cost leadership via rising in-house fabrication.

\- China ESS battery: CATL (OW) is the largest ESS battery maker globally and our top pick in China's battery value chain. EVE Energy (N) has the highest ESS exposure among covered battery makers, followed by CALB (OW). We also favor BYD (OW), given strong demand for its EV models in overseas markets and benefits from vertical integration in EV and ESS.

\- Korean battery players see improved opportunities and margins in US ESS. LGES's (OW) ESS order win momentum has been strong, and we estimate that the company has the largest LFP ESS order backlog among Korean battery makers. SDI's (OW) ESS visibility is also improving: US battery import data indicate that China-origin shipments have fallen further since July 2025 (post-OBBBA), while Korea-origin (largely SDI) shipments have risen sequentially, supporting an ongoing sourcing shift as US regulations remain effective.

## Summary of ESS-related stocks under JPM coverage

Table 1: Summary of ESS value chain stocks under JPM coverage

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Cover Analyst</td><td rowspan="2">JPM Rating</td><td rowspan="2">ESS business</td><td colspan="3">ESS revenue exposure</td><td colspan="3">ESS volume exposure</td></tr><tr><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY25A</td><td>FY26E</td><td>FY27E</td></tr><tr><td>CATL</td><td>300750 CH</td><td>Rebecca Wen</td><td>OW</td><td>ESS battery</td><td>15%</td><td>18%</td><td>22%</td><td>18%</td><td>22%</td><td>26%</td></tr><tr><td>CALB</td><td>3931 HK</td><td>Rebecca Wen</td><td>OW</td><td>ESS battery</td><td>32%</td><td>26%</td><td>29%</td><td>41%</td><td>39%</td><td>42%</td></tr><tr><td>EVE Energy*</td><td>300014 CH</td><td>Rebecca Wen</td><td>N</td><td>ESS battery</td><td>40%</td><td>38%</td><td>40%</td><td>59%</td><td>54%</td><td>56%</td></tr><tr><td>Gotion</td><td>002074 CH</td><td>Rebecca Wen</td><td>UW</td><td>ESS battery</td><td>19%</td><td>21%</td><td>24%</td><td>30%</td><td>33%</td><td>37%</td></tr><tr><td>BYD-H</td><td>1211 HK</td><td>Nick Lai</td><td>OW</td><td>ESS battery</td><td>4%</td><td>5%</td><td>n/a</td><td>20%</td><td>27%</td><td>n/a</td></tr><tr><td>LGES</td><td>373220 KS</td><td>Parsley Ong</td><td>OW</td><td>ESS battery</td><td>13%</td><td>33%</td><td>41%</td><td>8%</td><td>23%</td><td>31%</td></tr><tr><td>Samsung SDI</td><td>006400 KS</td><td>Sonny Lee</td><td>OW</td><td>ESS battery</td><td>22%</td><td>30%</td><td>31%</td><td>33%</td><td>44%</td><td>49%</td></tr><tr><td>Sungrow</td><td>300274 CH</td><td>Alan Hon</td><td>OW</td><td>PCS+EMS+integration</td><td>42%</td><td>49%</td><td>53%</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>Deye</td><td>605117 CH</td><td>Alan Hon</td><td>OW</td><td>PCS+battery+packs</td><td>74%</td><td>86%</td><td>89%</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>Nari</td><td>600406 CH</td><td>Stephen Tsui</td><td>OW</td><td>BMS+PCS+EMS+integration</td><td>&lt;10%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr></table>

Source: Company data, JPM estimates. Note: ESS battery may include BMS or system integration. EVE's ESS volume exposure refers to ESS battery volume over total power battery, not including consumer battery. Note: Gotion's FY25 exposure is JPMe. Note: SDI's total revenue includes electronic materials and small battery, while volume excludes electronic materials and small battery.

Table 2: Global ESS shipment forecasts

<table><tr><td>ESS battery shipment</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="9">Global shipment by end demand market</td></tr><tr><td rowspan="2">China market demand</td><td>26</td><td>64</td><td>139</td><td>155</td><td>257</td><td>501</td><td>606</td><td>697</td></tr><tr><td></td><td>145%</td><td>117%</td><td>12%</td><td>65%</td><td>95%</td><td>21%</td><td>15%</td></tr><tr><td rowspan="2">Ex-China market demand</td><td>39</td><td>62</td><td>74</td><td>175</td><td>382</td><td>635</td><td>892</td><td>1,091</td></tr><tr><td></td><td>57%</td><td>20%</td><td>136%</td><td>118%</td><td>66%</td><td>40%</td><td>22%</td></tr><tr><td>Global ESS battery shipment (GWh)</td><td>66</td><td>126</td><td>213</td><td>330</td><td>639</td><td>1,136</td><td>1,498</td><td>1,789</td></tr><tr><td>yoy</td><td></td><td>92%</td><td>70%</td><td>55%</td><td>93%</td><td>78%</td><td>32%</td><td>19%</td></tr></table>

Source: ICCSino, JPM estimates.

Figure 1: US BESS installations (MW)  
![](images/06c707a3350e226c9bb149310e6af7a460c23101876490bcdd5e8903ccc411a1.jpg)  
Source: EIA.

Figure 2: US: China battery imports (\$mn) -52% y/y in 5M26  
![](images/c9aed8d6e0df3c8fd1a3ac50eb2090a17c1c2bac3df0a454caa7c60f4588affc.jpg)  
Source: United States International Trade Commission.

Figure 3: US: Korea battery imports (\$mn) +38% y/y in 5M26  
![](images/5f55bf75dc359e8796f752df9ccb9a85947fa839d696bc64f01166f4a987f1a4.jpg)  
Source: United States International Trade Commission.

## Summary of latest ESS battery production and shipment trends

Table 3: Summary of ESS battery production trends

<table><tr><td></td><td colspan="2">2025</td><td colspan="3">1Q26</td><td colspan="3">2Q26</td><td></td><td colspan="2">1H26</td></tr><tr><td>GWh</td><td>Production</td><td>Y/Y</td><td>Production</td><td>Q/Q</td><td>Y/Y</td><td>Production</td><td>Q/Q</td><td>Y/Y</td><td></td><td>Production</td><td>Y/Y</td></tr><tr><td>Global ESS battery production</td><td>609.1</td><td>76%</td><td>224.7</td><td>11%</td><td>119%</td><td>285.5</td><td>27%</td><td>109%</td><td></td><td>510.2</td><td>113%</td></tr><tr><td>By battery producer country:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>KR/JP battery players</td><td>19.9</td><td>121%</td><td>7.9</td><td>-5%</td><td>192%</td><td>10.1</td><td>27%</td><td>195%</td><td></td><td>18.1</td><td>194%</td></tr><tr><td>CH battery players</td><td>589.2</td><td>75%</td><td>216.8</td><td>11%</td><td>117%</td><td>275.4</td><td>27%</td><td>107%</td><td></td><td>492.2</td><td>111%</td></tr></table>

Source: ICCSino, JPM.

Table 4: Summary of ESS battery shipment trends (

[中间内容因长度限制已省略]

 market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is

brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
