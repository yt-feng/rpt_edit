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
# China PCB Equipment

## 2Q26 Preliminary: Strong or Strong Beat for Both Han's Laser and Han's CNC

## CITI'S TAKE

Both Han's Laser (HL) and Han's CNC (HC) released strong 1H26 preliminary results. HL: 1H26 preliminary results imply 2Q26 net profit of Rmb896mn-996mn, up 176%-207% YoY and beating Visible Alpha consensus of Rmb818mn by 10%-22%. HC: 1H26 preliminary results suggest that 2Q26 earnings could reach Rmb577mn-677mn, up 294%-362% YoY and showing an accelerating earnings growth trend despite now consensus forecast available. The strong results of HC were primarily due to higher revenue exposure to AI products, including CCD back drill and laser drilling equipment for mSAP SLP/high-end HDI. On top of that, HL also benefits from strong demand for: 1) IT (Apple) equipment due to new product launches, 2) battery equipment driven by leading battery makers' expansions, 3) pan-semi equipment because of repeated AMOLED orders and recovery packaging, and 4) general laser equipment. Our pecking order remains HL (002008.SZ) > HC-H (3200.HK) > HC-A (301200.SZ).

HC – 1H26 revenue grew at least by 100% YoY to Rmb4.8bn, similar to the trend of Ta Liang (3167.TW). As we pointed out in our previous note, HL benefits from the spill-over effect on not only mechanical drilling equipment for AI PCB (HLC or HDI for switch tray and computer tray) but also ultrafast laser drilling equipment for 800G/1.6T optical transceivers.

HL – IT revenue grew strongly by 180% YoY to Rmb2.3bn in 1H26, which we believe was due to HL's more laser welding and cutting equipment order wins from Apple (AAPL.O) supply chain; battery revenue increased by 45% YoY to Rmb1.3bn in 1H26 driven by leading battery makers' expansions in China and overseas; pan-semi revenue also grew by 40% YoY due to repeated AMOLED orders and strong packaging equipment demand; and general laser equipment revenue could reach Rmb3.7bn driven by strong demand for low power welding, auto, and UV/ultrafast laser sources. Looking ahead, we believe that IT equipment business could remain as the strongest positive catalyst driven by new iPhone launches (e.g., foldable iPhone) and 3D printing/additive manufacturing adoption.

<table><tr><td rowspan="3">Company</td><td rowspan="3">Ticker</td><td rowspan="3">Ccy</td><td rowspan="3">Price</td><td rowspan="3">Mkt Cap (M)</td><td rowspan="3">Date &amp; Time</td><td colspan="2">Rating</td><td rowspan="3">Short-Term View</td><td colspan="2">Target Price</td><td rowspan="3">ESPR (%)</td><td rowspan="3">Div Yld (%)</td><td rowspan="3">ETR (%)</td><td rowspan="3">Last Rpt Yr</td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td></tr><tr><td rowspan="2">Old</td><td rowspan="2">New</td><td rowspan="2">Old</td><td rowspan="2">New</td><td colspan="2">EPS</td><td colspan="2">EPS</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td></tr><tr><td>Han&#x27;s CNC Technology</td><td>301200.SZ</td><td>Rmb</td><td>328.000</td><td>160,395</td><td>09 Jul 15:00</td><td>2</td><td>nc</td><td>-</td><td>377.000</td><td>nc</td><td>14.9</td><td>0.3</td><td>15.3</td><td>Dec-25</td><td>3.558</td><td>nc</td><td>5.576</td><td>nc</td></tr><tr><td>Han&#x27;s CNC Technology</td><td>3200.HK</td><td>HK$</td><td>145.00</td><td>185,838</td><td>09 Jul 16:10</td><td>1</td><td>nc</td><td>-</td><td>325.00</td><td>nc</td><td>124.1</td><td>0.9</td><td>125.0</td><td>Dec-25</td><td>3.558</td><td>nc</td><td>5.576</td><td>nc</td></tr><tr><td>Han&#x27;s Laser Technology</td><td>002008.SZ</td><td>Rmb</td><td>130.900</td><td>134,775</td><td>09 Jul 15:00</td><td>1</td><td>nc</td><td>-</td><td>177.000</td><td>nc</td><td>35.2</td><td>0.3</td><td>35.5</td><td>Dec-25</td><td>2.156</td><td>nc</td><td>3.219</td><td>nc</td></tr><tr><td colspan="6">1 = Buy, 2 = Neutral, 3 = Sell, H = High Risk</td><td colspan="13">ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change</td></tr><tr><td colspan="6">Source: Citi</td><td colspan="13">^Catalyst Watch</td></tr></table>

Jamie Wang $^{AC}$ +852-2501-2772
jamie.ck.wang@citi.com

Eric Lau
+852-2501-2726
eric.h.lau@citi.com

Figure 1. HL: 1H26/2Q26 preliminary results snapshot

<table><tr><td rowspan="2">(Rmb mn)</td><td rowspan="2">1H25</td><td colspan="3">1H26P</td><td rowspan="2">2Q25</td><td rowspan="2">1Q26</td><td colspan="3">2Q26P</td></tr><tr><td>Lower bound</td><td>Mid point</td><td>Upper bound</td><td>Lower bound</td><td>Mid point</td><td>Upper bound</td></tr><tr><td>Net profit</td><td>488</td><td>1,250</td><td>1,300</td><td>1,350</td><td>325</td><td>354</td><td>896</td><td>946</td><td>996</td></tr><tr><td>Recurring profit</td><td>261</td><td>1,350</td><td>1,400</td><td>1,450</td><td>189</td><td>408</td><td>942</td><td>992</td><td>1,042</td></tr><tr><td>YoY</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net profit</td><td>-60%</td><td>156%</td><td>166%</td><td>177%</td><td>38%</td><td>117%</td><td>176%</td><td>191%</td><td>207%</td></tr><tr><td>Recurring profit</td><td>18%</td><td>417%</td><td>436%</td><td>455%</td><td>-16%</td><td>468%</td><td>398%</td><td>424%</td><td>451%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Company Reports

Figure 2. HC: 1H26/2Q26 preliminary results snapshot

<table><tr><td rowspan="2">Rmb mn</td><td></td><td colspan="3">1H26P</td><td></td><td></td><td colspan="3">2Q26P</td></tr><tr><td>1H25</td><td>Lower bound</td><td>Mid point</td><td>Upper bound</td><td>2Q25</td><td>1Q26</td><td>Lower bound</td><td>Mid point</td><td>Upper bound</td></tr><tr><td>Net profit</td><td>263</td><td>900</td><td>950</td><td>1,000</td><td>147</td><td>323</td><td>577</td><td>627</td><td>677</td></tr><tr><td>Recurring profit</td><td>250</td><td>900</td><td>950</td><td>1,000</td><td>142</td><td>323</td><td>577</td><td>627</td><td>677</td></tr><tr><td>YoY</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net profit</td><td>84%</td><td>242%</td><td>261%</td><td>280%</td><td>84%</td><td>177%</td><td>294%</td><td>328%</td><td>362%</td></tr><tr><td>Recurring profit</td><td>101%</td><td>260%</td><td>280%</td><td>300%</td><td>111%</td><td>198%</td><td>308%</td><td>343%</td><td>378%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Company Reports

Figure 3. HL: Revenue by segment and YoY growth, 1H26  
![](images/045a99fbc503e6f1b54bc94357c85dd6d494743c04596555bd573556c16e049b.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Company Reports

Figure 4. P/E comparison: Han's Laser vs. Han's CNC-A  
![](images/6fd81de3d19b3cdfbb1d2f64e45b601d85bfa7060fe9909f8730d21119ac02ab.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Company Reports and Citi Estimates

## Bull/Bear: Han's CNC Technology (301200.SZ)

![](images/62c01aa8f7e0e32a90fdc28631c9619c4edcc4a41f5088f82fa075341debc3be.jpg)  
Spread 53pp
Current Price and expected returns (upside/downside) as of 09 Jul 2026

![](images/03ace27afe0a0215718a1dca0ae68ff33caf47d1e91bdf327c8dfb221baae39b.jpg)

## BULL Assumptions

\- Rerate to \~83x 2027E P/E driven by stronger-than-expected demand

![](images/d0fabc1ec51e236f0c3d5c10aa8a3f9d408eb85a722f7186194100ce89db7d87.jpg)

## BASE Assumptions

\- Base case TP is at \~68x 2027E P/E

![](images/c524f415f00ba60c67daef45c8e0ebf3e720716be1adba508bd25356e11ecb13.jpg)

## BEAR Assumptions

\- Derate to \~52x 2027E P/E due to weaker-than-expected demand

## Bull/Bear: Han's CNC Technology (3200.HK)

![](images/bcf6f78dbaee11c0f38a1a46371e6f649e63472e99e13542e34ff8560da33080.jpg)  
Spread 159pp
Current Price and expected returns (upside/downside) as of 09 Jul 2026

![](images/b7ac275aae3ee3bd4badf530cd0cf8efe6d8c9cca268a9b716b593f9eb0694a9.jpg)

## BULL Assumptions

\- Rerate to \~62x 2027E P/E due to stronger AI PCB equipment demand

![](images/ac51a9960507e315a48b59645f64f571716303f3f125d34eb9e87b642c58b541.jpg)

## BASE Assumptions

\- Base case TP is at \~51x 2027E P/E

![](images/7a5ced5d1777e50899c48a1808508b0f5cc75401f55849a1ddd5e0e34262a1a2.jpg)

## BEAR Assumptions

\- Derate to \~26x 2027E P/E due to weaker AI PCB equipment demand

## Bull/Bear: Han's Laser Technology (002008.SZ)

![](images/7dfa9ff22c8059be029e119a065980aa381b1e883e4e3bc825ba84199c008f85.jpg)  
Spread 61pp
Current Price and expected returns (upside/downside) as of 09 Jul 2026

![](images/d08e1a9dd75fad34a33a9c2e7a3a7f776e791b00362399b05bea684d9878a68a.jpg)

## BULL Assumptions

\- Rerate to 65x PE on stronger IT and PCB equipment demand

![](images/c6afc2497919fa6f2107f806d588a6e2e60bc81a1f2b29615ea54d57dca743cd.jpg)

## BASE Assumptions

• 55x 2027E P/E, similar to the previous peak during 2018

![](images/b815b68ba2f5dc5f570e3498f99f48ecd89042a1ebed7c1c42aaafd23d93ea58.jpg)

## BEAR Assumptions

\- Derate to 40x PE on slower IT and PCB equipment demand

## Han's CNC Technology

## Company description

Founded in 2002, Han's CNC (HC) is a leading PCB equipment supplier in China specializing in PCB drilling, exposure, testing, formation, as well as attachment equipment. According to China Insights Consultancy (CIC), Han's CNC ranks as the world's largest specialized PCB production equipment manufacturer with $6.6\%$ of global market share in terms of 2024 revenue. Its market share even reached $10 - 11\%$ in 2024, also being the biggest specialized PCB equipment in China. With accumulated experience and technology edge on high-speed control, electronic engineering, software algorithm, advanced optical system, laser technology, image algorithm, and electronic testing, Han's CNC successfully penetrates into leading domestic and international PCB makers.

## Investment strategy

We rate Han's CNC-A (HC-A) at Neutral primarily due to its rich valuation, although we still expect HC to deliver strong earnings growth led by strong demand for both mechanical and ultrafast laser drilling equipment.

## Valuation

Our target price of Rmb377 is based on \~68x 2027E P/E, slightly above its average over the past three years to reflect its brighter demand outlook. We believe that our target multiple is not aggressive given a \~81% earnings CAGR for 2026-27E.

## Risks

Han's CNC stock is rated High Risk based on our quantitative model, but we think that its share price risk is mitigated given its high earnings visibility due to strong equipment demand from AI PCB makers. Potential downside risks include: 1) weaker-than-expected AI PCB equipment demand; 2) worse-than-expected GPM due to rising component costs; and 3) intensifying price competition due to the industry's equipment supply increase. Potential upside risks include: 1) stronger-than-expected AI PCB equipment demand; 2) better-than-expected GPM due to favorable product mix change; and 3) strong AI equipment demand leads to supply shortage for general PCB equipment. Any of these risk factors could cause the shares to deviate from our target price.

## Han's CNC Technology

## Company description

Founded in 2002, Han's CNC (HC) is a leading PCB equipment supplier in China specializing in PCB drilling, exposure, testing, formation, as well as attachment equipment. According to China Insights Consultancy (CIC), Han's CNC ranks as the world's largest specialized PCB production equipment manufacturer with $6.6\%$ of global market share in terms of 2024 revenue. Its market share even reached $10 - 11\%$ in 2024, also being the biggest specialized PCB equipment in China. With accumulated experience and technology edge on high-speed control, electronic engineering, software algorithm, advanced optical system, laser technology, image algorithm, and electronic testing, Han's CNC successfully penetrates into leading domestic and international PCB makers.

## Investment strategy

We rate Han's CNC-H (HC-H) at Buy as we think that it offers investors a better risk/reward than HC-A (301200.SZ) for participating in the company's strong earnings growth in 2026E-27E, driven by strong PCB equipment demand from Chinese AI PCB makers.

## Valuation

Our target price of HK\$325 is based on \~51x 2027E P/E, set at 25% discount to its A-share's valuation. We believe that our target multiple is not aggressive given a \~81% earnings CAGR for 2026E-27E.

## Risks

Potential downside risks that could impede the shares from reaching our target price include: 1) weaker-than-expected AI PCB equipment demand, 2) worse-than-expected GPM due to rising component costs, and 3) intensifying price competition due to the industry's equipment supply increase.

## Han's Laser Technology

## Company description

Han's Laser is a China-based company primarily engaged in the research, development, manufacture, and sale of laser processing equipment. The company's main products are laser marking equipment, laser welding equipment, laser cutting equipment, printed circuit boards (PCBs) equipment, photovoltaic devices, as well as light emitting diode (LED) packing equipment, among others. The company distributes its products principally in domestic and overseas markets.

## Investment strategy

We rate Han's Laser shares Buy as we see strong PCB drilling and testing equipment demand from PCB makers for AI server/datacenter such as Victory Giant Technology (VGT; 300476.SZ) and strong order growth from Apple supply chain driven by iPhone 18 – potentially Apple's first foldable phone. We believe that the IT and PCB equipment "super" cycle could drive \~65% core profit CAGR in 2026-27E and lead to a share price rerating, similar to what we saw in 2017 – an Apple order-led strong upcycle.

## Valuation

Our 12-month target price for Han's Laser of Rmb177.0 is based on 55x 2027E P/E, set at the previous peak P/E in 2018 to reflect its "super cycle" led by stronger demand for PCB and IT (Apple) equipment.

## Risks

Key fundamental downside risks that could prevent the shares from reaching our target price include: 1) fewer-than-expected Apple orders; 2) fiercer competition, which could pressure margins; 3) any weakening of auto sales, which would hurt high-power laser equipment demand; 4) failure of any of the new investment projects; and 5) newly emerging technologies substituting laser equipment.

![](images/59012f66c2cab9b3d2c13d096bd24dfc5f09e046bb4b7955f961c1837fd75334.jpg)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations o

[中间内容因长度限制已省略]

ipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing

such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
