你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

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

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

## Han's CNC Technology (301200.SZ)

![](images/b73380133b40771fbc88f10f2dd3966c716833b19ffd78877a8c5b83e33c64db.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>07-Sep-25 23:58:26</td><td>*1H</td><td>*108.00</td><td>85.55</td></tr><tr><td>2</td><td>16-Oct-25 04:50:23</td><td>1H</td><td>*124.00</td><td>91.80</td></tr><tr><td>3</td><td>20-Oct-25 12:42:56</td><td>1H</td><td>*140.00</td><td>96.06</td></tr></table>

\*Indicates Change

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>4 09-Feb-26 03:30:27</td><td>*2</td><td>*160.00</td><td>149.62</td></tr><tr><td>5 10-Apr-26 12:18:38</td><td>2</td><td>*186.00</td><td>181.82</td></tr><tr><td>6 10-Jun-26 04:05:18</td><td>2</td><td>*290.00</td><td>270.81</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Han's CNC Technology (3200.HK)

Ratings and Target Price History
Fundamental Research

![](images/7c47ef817065fb2fbf01ff8e3eeac2f4e7deb24b203780feefe143c312a8d57d.jpg)  
\*Indicates Change

<table><tr><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>109-Feb-26 03:30:27</td><td>*1</td><td>*142.00</td><td>120.80</td></tr><tr><td>10-Apr-26 12:18:38</td><td>1</td><td>*160.00</td><td>119.80</td></tr></table>

Rating/target price changes above reflect Eastern Time

Han's Laser Technology (002008.SZ)

Ratings and Target Price History
Fundamental Research

Han's CNC Technology (301200.SZ)
Short-Term View/Catalyst Watch Research  
![](images/52cf8b7b0604feb5c47070605ef9dff6c8d2c215ec77d78f3a07e61d8dbe7a03.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>22-Aug-23 02:00:19</td><td>1</td><td>*28.00</td><td>22.53</td></tr><tr><td>2</td><td>23-Oct-23 15:54:01</td><td>1</td><td>*25.00</td><td>21.11</td></tr><tr><td>3</td><td>18-Apr-24 13:03:24</td><td>1</td><td>*23.00</td><td>18.95</td></tr><tr><td>4</td><td>16-Aug-24 03:59:06</td><td>1</td><td>*24.00</td><td>20.12</td></tr><tr><td>5</td><td>26-Jan-25 11:17:15</td><td>1</td><td>*31.00</td><td>25.75</td></tr></table>

\*Indicates Change

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>6</td><td>25-Apr-25 13:05:16</td><td>1</td><td>*28.00</td><td>23.44</td></tr><tr><td>7</td><td>28-Aug-25 00:11:15</td><td>1</td><td>*45.00</td><td>37.19</td></tr><tr><td>8</td><td>30-Sep-25 09:43:36</td><td>1</td><td>*54.00</td><td>40.71</td></tr><tr><td>9</td><td>02-Mar-26 09:47:27</td><td>1</td><td>*89.00</td><td>74.62</td></tr><tr><td>10</td><td>10-Apr-26 12:18:38</td><td>1</td><td>*99.00</td

[中间内容因长度限制已省略]

r investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing

such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
