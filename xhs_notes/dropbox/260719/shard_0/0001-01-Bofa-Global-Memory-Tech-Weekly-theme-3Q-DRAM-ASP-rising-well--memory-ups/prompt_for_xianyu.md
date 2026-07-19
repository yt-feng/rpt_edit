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
Global Memory Tech

# Weekly theme: 3Q DRAM ASP rising well, memory upside with TSMC/ASML guidance

Industry Overview

## What we learned from our 3Q contract price check

Investors have increasingly asked about memory chipmakers' likely 3Q earnings miss, given limited ASP hike vs consensus. This prompted us to check newly negotiated 3Q DRAM contract prices more closely. What we learned: (1) stronger server DRAM pricing, up 20-30% QoQ, led by high-speed LPDDR5 vs consensus of 20% or less; (2) upbeat spot demand, led by commodity DDR5 and even legacy DDR4, with July prices up again MoM; (3) a near-term rise in orders for higher-priced HBM4 vs cheaper HBM3e; (4) LTA-based DRAM sales well below 50% of total, with non-LTA portion at 60-70%, and a solid QoQ price rise (e.g., 5-10%), often settled even under LTAs; and (5) some OEMs' rush orders confirming more than 20% QoQ price rise, not only for commodity DRAM but also for NAND. Overall, our global forecast for 3Q DRAM ASP, up 21% QoQ, is consistent with what we learned from channel check. This is more optimistic than TrendForce's current assumptions of a 13-18% QoQ rise in 3Q conventional DRAM, or only 8-13% including HBM. Of course, TrendForce's 2Q DRAM ASP assumptions, up 58-63% QoQ for conventional DRAM only or 53-58% on an overall blended basis, including HBM, seem to be 10ppt higher than Korea-specific average but in line with ex-Korea global assumption.

## Spot prices also rise, led by DRAM

DRAM spot prices have risen for eight consecutive weeks, though being at a abnormally high level. This is completely different vs 2-3 months ago sentiment (e.g., no further upside at US\$35-40 for 16Gb DDR5; already higher than HBM price). Many OEMs, which had previously purchased DRAM at only around US\$5 per unit, resisted the DRAM spot-price rally and consequently reduced PC/tablet/smartphone production volume. But, they are now buying more memory chips to prepare for higher sales in Sept. and the 4Q peak season. Since spot trading volume is very small, at a low-single-digit% of global supply, some OEMs are purchasing conventional DRAM on more of a rush-order basis. Current spot prices for both DDR5 and DDR4 point to a roughly 20% QoQ rise. NAND spot prices also recovered well this week, led by 1Tb, up 4% WoW. This is also a positive signal to expect 10%+ NAND ASP rise in 3Q. But, similar to Korea’s 2Q DRAM ASP miss vs global trend, Japan NAND ASP should not have been upbeat vs Street expectation; still, it is too early to expect a 3Q miss, given solid July data, with monthly spot/contract prices rising.

## Positive implications of TSMC's strong results/capex

TSMC's (Taiwan Semi Manufacturing Co.) strong 2Q results, with sales of US\$40bn (+34% YoY), and OPM of 60%; bullish guidance, including a 2nm node ramp-up and low-40% annual revenue growth; and record-high capex of US\$60-64bn for 2026, plus a separate additional US\$100bn investment in US fabs, have positive implications for memory, as TSMC's customers need more advanced HBM, SOCAMM, and eSSD. ASML's 2Q results/guidance were also favorable for memory due to muted China exports (local chipmakers' lower spending); more Taiwan/logic-centric sales growth (vs memory/Korea); and management's optimistic view on new AI chip and high NA EUV (memory order upside for new logic).

## 16 July 2026

Equity
Global
Technology

Simon Woo, CFA >>
Research Analyst
BofA (Seoul)
+82 2 3707 0554
simon.woo@bofa.com

Dai Shen >>
Research Analyst
BofA (Hong Kong)
dai.shen@bofa.com

Vivek Arya
Research Analyst
BofAS
vivek.arya@bofa.com

Mikio Hirakawa >>
Research Analyst
BofAS Japan
mikio.hirakawa@bofa.com

Matt Shin >>
Research Analyst
BofA (Seoul)
matt.shin2@bofa.com

## Exhibit 1: DDR5/DDR4 well rebounded

this week; even 1Tb NAND recovery seen
Spot-market prices among DRAM and NAND

<table><tr><td>US$</td><td>Current</td><td>WoW</td><td>QoQ</td><td>YoY</td></tr><tr><td colspan="5">DRAM spot</td></tr><tr><td>16Gb DDR5</td><td>49.2</td><td>3%</td><td>28%</td><td>712%</td></tr><tr><td>16Gb DDR4</td><td>80.1</td><td>3%</td><td>16%</td><td>829%</td></tr><tr><td>8Gb DDR4</td><td>39.9</td><td>6%</td><td>21%</td><td>685%</td></tr><tr><td>4Gb DDR4</td><td>12.9</td><td>4%</td><td>81%</td><td>426%</td></tr><tr><td colspan="5">NAND spot</td></tr><tr><td>1Tb wafer</td><td>25.1</td><td>4%</td><td>-3%</td><td>397%</td></tr><tr><td>512Gb wafer</td><td>19.2</td><td>-1%</td><td>-9%</td><td>617%</td></tr><tr><td>256Gb wafer</td><td>10.2</td><td>0%</td><td>-3%</td><td>578%</td></tr></table>

Source: DRAMeXchange

BofA GLOBAL RESEARCH

## AI: Artificial intelligence

ASP: Average selling price

DDR4/5: $4^{th}/5^{th}$ gen double-data rate DRAM

DRAM: Dynamic random-access memory

EUV: Extreme ultraviolet lithography

eSSD: Enterprise solid-state drive

Gb/Tb: Gigabit/Terabit

GM/OPM: Gross/OP margin

HBM: High bandwidth memory

HBM3e/4: 5 $^{th}$ /6 $^{th}$ gen of HBM

LPDDR5: Low-power DDR5

LTA: Long-term agreement

NAND: Not-AND memory

OEM: Original equipment manufacturer

SOCAMM: Small-outline compression

## TrendForce memory ASP forecast vs BofA estimates

Exhibit 2: TrendForce expects conventional DRAM price to moderate through 2H26, decelerating from \~93-98% QoQ growth in 1Q to \~58-63% in 2Q to \~13-18% in 3Q and just \~3-8% by 4Q
TrendForce DRAM ASP forecast updated as of 30 $^{th}$ June 2026

![](images/e8f2f19155520cf0d64c8e5cb9616dff3d4030462570e96454593f05feb975fd.jpg)  
\*Blended ASP refers to entire DRAM (conventional + HBM)
Source: TrendForce, BofA Global Research estimates

BofA GLOBAL RESEARCH

Exhibit 3: TrendForce forecasts NAND ASP to normalize to \~+10-15% QoQ in 3Q26 and \~+0-5% QoQ in 4Q26 after reaching peak levels of \~85-90% QoQ and \~55-60% QoQ in 1Q/2Q26
TrendForce NAND ASP forecast updated as of 30 $^{th}$ June 2026  
![](images/c0df477ace5870c365be40613a2552cc42eb37c8be85c0c25e7771291f8c31f2.jpg)  
Source: TrendForce  
BofA GLOBAL RESEARCH  
Exhibit 4: Following the exceptional +70-90% QoQ increase in 1Q26, we expect global DRAM and Samsung ASP growth to moderate to +45-50% in 2Q and \~+20% QoQ in 3Q26 and high-single-digit QoQ in 4Q26 BofA Global DRAM ASP and Samsung DRAM ASP estimates

![](images/2c3fb409566dbba25c30d813da777b60378b798602e551ef3e1d7f0c89d92f27.jpg)  
Source: Companies, BofA Global Research estimates  
BofA GLOBAL RESEARCH  
Exhibit 5: Following the +75-88% QoQ spike in 1Q26, we expect global NAND and Samsung ASP growth to moderate to \~+65% QoQ in 2Q26, easing further to \~+15% QoQ in 3Q26 and near-flat levels by 4Q26
BofA Global NAND ASP and Samsung NAND ASP estimates

![](images/c6fbd155be6416640c8f51558a8a16bd98025905dada50ddc9f08e10e4dec6ac.jpg)  
Source: Companies, BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 6: Both DRAM and NAND prices are at record highs, with DDR5 DRAM reaching approximately \$45 compared with NAND at \~\$25 16Gb DDR5 vs 512Gb wafer contract price trend  
![](images/6a0258735895f5283573c1129ac88aaa544e1325042a27ae329a9714ca2731a2.jpg)  
Source: TrendForce  
BofA GLOBAL RESEARCH

Exhibit 7: NAND and DRAM price expected to rise 3-10% MoM in Jul-26
16Gb DDR5 vs 512Gb wafer contract price trend – MoM change  
![](images/f9f606cf743c3c4b62905655e3040b31564e07f11a977c3d29ed95ad57081d46.jpg)  
Source: TrendForce  
BofA GLOBAL RESEARCH

BofA vs TrendForce NAND ASP assumptions (QoQ change)

Exhibit 8: TrendForce has revised up its 3Q26 DRAM ASP forecast to 13–18% QoQ vs previous estimate of 3–8% QoQ
TrendForce DRAM ASP forecast (QoQ change) – Jun-26 update vs Mar-26

![](images/4abc7cbe87e7bccca1978d424e62b7f510636ea63996f0d80e9a5cc670fdb3d6.jpg)  
TrendForce's latest update as of $30^{\text{th}}$ June-2026  
Source: TrendForce  
BofA GLOBAL RESEARCH  
Exhibit 9: TrendForce has revised down its 2Q26 NAND ASP forecast to 55–60% QoQ (from 70–75%), while raising its 4Q26 outlook to 10–15% QoQ from the earlier 8–13% range  
TrendForce NAND ASP forecast (QoQ change) – Jun-26 update vs Mar-26

![](images/5ee8a3e8c333f3e07b356604a5af5d89c100ca560883b1c9408fb19bce4e0ba5.jpg)  
TrendForce's latest update as of $30^{\text{th}}$ June-2026  
Source: TrendForce  
BofA GLOBAL RESEARCH  
Exhibit 10: Our estimates are largely in line for 3Q26 and 4Q26 and more conservative for 2Q26 relative to TrendForce, with DRAM ASPs projected to increase 53% / 21% / 7% QoQ across 2Q–4Q26 (BofA) BofA vs TrendForce DRAM ASP assumptions (QoQ change)

![](images/3fca6c666389fbf0aa3941f0548e06fabfd25200801d0f0811a772c67e5976e3.jpg)  
TrendForce's latest update as of $30^{\text{th}}$ June-2026 vs BofA update as of $10^{\text{th}}$ July 2026  
Source: TrendForce, BofA Global Research estimates  
Exhibit 11: Similarly, our NAND assumptions are either conservative or broadly aligned with TrendForce, with ASPs expected to grow 65% / 15% / 1% QoQ across 2Q–4Q26

![](images/3955a2a4dadb9a0665f15d1c6df4cd75f24127a874e68134b93db6a48bb82ba0.jpg)  
TrendForce's latest update as of $30^{\text{th}}$ June-2026 vs BofA update as of $10^{\text{th}}$ July 2026  
Source: TrendForce, BofA Global Research estimates

## TSMC's strong 2Q results and higher capex guidance

Exhibit 12: 2Q26 sales (NT\$1,270bn; +36% YoY) came in at the high-end of its guidance; 3Q sales guidance (NT\$1,446bn) also indicates solid YoY growth (up 46%)

TSMC – Revenue and growth trend

![](images/f5f123eb5841a533e86d2ecd7671cb341d82b3a3b6597f8655cf57fbe4f59f7b.jpg)  
Source: Company, BofA Global Research estimates  
BofA GLOBAL RESEARCH  
Exhibit 13: Margins further improved in 2Q (GM 68%, OPM 60%); high-margin profile well-expected to continue  
TSMC – Gross margin and OP margin trend

![](images/4a21abc2bdc56e04a75498ce6d72baa2d1c8ec548cf854e6edc9ffc9a3a8b103.jpg)  
Source: Company, BofA Global Research estimates  
BofA GLOBAL RESEARCH  
Exhibit 14: TSMC revised up its 2026 annual capex guidance from US\$60-64bn vs US\$56bn previously  
Capex comparison between TSMC and Samsung memory/foundry

![](images/1c7a64483503f6371caed71e353b3a470882142f8b8b665cc6d82f1b0253087f.jpg)  
Source: Companies, BofA Global Research estimates

Exhibit 15: Significant drop in capex-to-sales ratio seen for both TSMC and Samsung due to AI-driven exceptionally robust topline growth
Capex-to-sales comparison – TSMC and Samsung \*memory-only  
![](images/ef855eb41e2f7ddbc1e2e4a0875a754fd67d47742fc51273f11cc1930d5082f5.jpg)  
Source: Companies, BofA Global Research estimates

## ASML's upbeat 2Q results and 2H guidance

Exhibit 16: Upbeat 2Q26 sales (€9.3bn; up 21% YoY) led by stronger-than-expected IBM (installed base management) sales; management's sales guidance indicates robust growth in 2H (3Q: €11.5bn, up 53% YoY / 4Q: €14.4bn, up 48% YoY)

ASML – Total sales and growth trend

![](images/8ed0e5e887a1878c04e0e1d3e079e55691cb29f842fb7e073f6cc4d0ba4a23ee.jpg)  
Source: Company, BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 17: Strong margins well-observed in 2Q26 (GM $54\%$ , OPM $37\%$ ) and management's guidance indicates robust margins in 2H (GM $55\%+$ , OPM $40\%+$ )  
![](images/119ba1ef18813d86ca23eba3af868091805cce967e7967bad7a07114a0fabc9e.jpg)  
Source: Company, BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 18: Memory sales closely catching up to logic during the last three years on the back of DRAM super-cycle
ASML – Net system sales by application – memory vs logic (IDM+foundry)  
![](images/9058054f0bf60a674f30fe13ee21a1bbd9e721b5351c01dfaa84401da3e43f42.jpg)

Exhibit 19: Korea accounted for 43% of ASML's net system sales in 2Q26, followed by Taiwan (30%), China (14%), and US (9%) ASML – Net system sales by region  
![](images/5a762d8236ed2fd4da237bcbe5022e3c690404c417d35794e58a44428be0e260.jpg)

Source: Company

## Korea exports and Taiwan sales

Exhibit 20: MoM growth rate decelerated, but still record-high in July (US\$11.2bn; +1.3% MoM)
Korea semis exports – First 10 days of month US\$bn  
![](images/3d82ddd8e7f747cfeec0cb03653e56f460517ad316c6343dcb58e21a01241f53.jpg)  
Source: MoTIR  
BofA GLOBAL RESEARCH

Exhibit 21: YoY rebound still robust at +193% in July; already six consecutive months of triple-digit growth
Korea semis exports – YoY change in first 10 days of month  
![](images/8db82aa8ed6f7722b457c7e9d9b457b9bebfea0a75c8be26d750145969cf1cf3.jpg)  
Source: MoTIR  
BofA GLOBAL RESEARCH

Exhibit 22: Robust MoM growth led by logic/foundry/ODM names including Vanguard (+41%), MediaTek (+22%), Quanta (+24%)  
Taiwan tech companies' MoM monthly sales (Jun-2026)  
![](images/77cb6eec42c86f51773c7c0d5b3ab7d85fa24ee9b0e6eda3bc9a426020abc3f3.jpg)  
Source: Companies  
BofA GLOBAL RESEARCH

Exhibit 23: Exceptionally strong YoY rebound led by memory names such as Nanya, Phison, Transcend; TSMC also solid at +68%
Taiwan tech companies' YoY monthly sales (Jun-2026)  
![](images/9751c19844e89becbbdd249d90feb23427d37fa087da599af2221896f8b244ee.jpg)

\*Nanya Tech up 621%, Transcend up 382%, Phison up 301%
Source: Companies

China IC imports and smartphone shipments
Exhibit 24: IC imports hit record high at US\$59.6bn in Jun, +72% YoY
China monthly integrated circuit (IC) imports and YoY  
![](images/a71d7d265143c712c7cb624479001389674bff8e39e7ddbf5ad809a580593d98.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 25: China IC imports reached 53.7bn units in Jun, +7% YoY
China monthly integrated circuit (IC) imports volume and YoY  
![](images/2f268e25af9b62e7f8e88265c334e8130057507d94355d72344e2a1817cded65.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 26: Memory imports reached record high at US\$30.8bn in May, accounting for 54% of total imports
China IC imports by chip type  
![](images/ea8024518f7bcbd15632c20892220883c9a9b9a598b6baf269fd4dee526f53e3.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 27: Memory monthly imports grew 249% YoY growth during May  
Monthly memory chip imports to China and YoY  
![](images/823121b694c74e5df190414141e8f1479e0198a0f4f3822c587b220ce50de7c5.jpg)  
Source: China General Customs

Exhibit 28: China smartphone shipments were 26.8mn units in May; well recovered but sustainable growth not yet confirmed
China smartphone – monthly shipment  
![](images/c956fc4a196f9aec83b9055570fa86f01e37402c5c2b5dc6901ca2e39a974551.jpg)  
Source: MIIT/CAICT, BofA Global Research  
BofA GLOBAL RESEARCH

## Exhibit 29: May smartphone shipment +19% YoY despite DRAM shortage

China smartphone – monthly shipment YoY  
![](images/861f270c4edf766d38b298f09f92bac5a2ff930f8862852d2554796166cf3f81.jpg)  
Source: MIIT/CAICT, BofA Global Research  
BofA GLOBAL RESEARCH  
China smartphone – foreign brands' shipment

Exhibit 30: Implied smartphone shipment by foreign brands 3.7mn units in May

![](images/08ddecbcb204a3319218178ca7ce5957d4e8d29315f7f34a8bb8a02ad202a856.jpg)  
Source: MIIT/CAICT, BofA Global Research  
BofA GLOBAL RESEARCH

Exhibit 31: Foreign brands shipment dropped 19% YoY in May
China smartphone – foreign brands' shipment YoY  
![](images/e479532c01c5baaafebfe3834c54682af946261e2eba3c8196424270db653dbb.jpg)  
Source: MIIT/CAICT, BofA Global Research  
BofA GLOBAL RESEARCH  
China smartphone shipments YoY growth

Exhibit 32: China's smartphone shipments down $4.3\%$ in 2Q26, with $19 - 24\%$ YoY growth for Apple and Huawei while $10 - 22\%$ decline for other major brands

![](images/5a102f930fe219ba3fa46aaa3fac19f3376aa1130651c67591bdf7e701e6cbf6.jpg)  
BofA GLOBAL RESEARCH

Exhibit 33: Huawei saw clear market share gain (23% in 2Q26 vs 18% in 2Q25, followed by Apple
China smartphone market share  
![](images/c7ef0aea9a5993c830447e3b9a7f99aee2d466f8182f5dae795c0526d13f4e93.jpg)  
BofA GLOBAL RESEARCH

## Memory price forecast and spot price short term trend

Exhibit 34: Well rebounded in June-July following April-May corrections; summary rally also possible given t

[中间内容因长度限制已省略]

ect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
