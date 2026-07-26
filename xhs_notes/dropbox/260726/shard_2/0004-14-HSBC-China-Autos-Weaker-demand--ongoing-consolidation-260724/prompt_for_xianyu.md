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
Key changes to ratings and target prices

# China Autos

Weaker demand, ongoing consolidation

◆ Lower 2026 forecasts on weaker-than-expected 1H26 demand

\- Ongoing consolidation and pricing pressure continue to weigh on sector earnings

◆ Revise OEM forecasts and remain selective on stock picks; downgrade Great Wall A/H to Hold/Hold; cut TPs

Demand has softened faster than expected: We lower our 2026 China passenger vehicle and EV demand y-o-y growth forecasts to -13% (from -5%) and -6% (from +10%), respectively, following a weaker-than-expected 1H26. The latest CPCA data continue to point to soft demand, with 1-19 July passenger car retail volume down 16% y-o-y and NEV retail volume down 4% y-o-y. Replacement demand has moderated after the subsidy-driven pull-forward, while consumers have become increasingly selective given frequent product launches and a more competitive market. Although we expect demand to improve sequentially in 2H26, we believe the recovery will be more gradual than previously anticipated.

Industry consolidation still in process, while domestic pricing likely to remain under pressure: Rising EV penetration continues to reshape China's auto market, but industry profitability remains under pressure. Intense competition, persistent pricing pressure and elevated inventories at traditional OEMs continue to weigh on margins, particularly for joint-venture businesses. At the same time, exports remain an important source of growth, helping leading Chinese OEMs partially offset softer domestic demand. We therefore expect industry consolidation and earnings divergence to continue as stronger players further extend their competitive advantages.

Stock selection matters more than sector exposure: While Great Wall's shares have already corrected significantly, we believe earnings visibility has weakened further following softer-than-expected Q2 guidance, lower industry demand expectations and continued uncertainty around the Russia scrappage tax refund. We therefore downgrade Great Wall A/H shares from Buy to Hold, while maintaining Hold on GAC A/H shares and BAIC. We continue to prefer OEMs with stronger export franchises, competitive local brands and healthier product cycles, and do not yet see conditions for a broader sector re-rating. Until industry demand and profitability stabilize, we expect execution differences to drive performance divergence.

# Equities Automobiles

China

## Yuqian Ding\*

Head of China Technology & Autos Research
The Hongkong and Shanghai Banking Corporation Limited
yuqian.ding@hsbc.com.hk
+852 2288 5108

Li Yang\*
Analyst, China Autos
The Hongkong and Shanghai Banking Corporation Limited
li01.yang@hsbc.com.hk
+852 2288 6216

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

![](images/0b1bdf0006aa2c4d68bf4a24558b0804457d68784f597f4cbf979e6f70f2edd9.jpg)

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Company</td><td rowspan="2">Ccy.</td><td rowspan="2">Market Cap (USDm)</td><td rowspan="2">3M ADTV (USDm)</td><td rowspan="2">Close price</td><td colspan="2">Target price</td><td colspan="2">Rating</td><td rowspan="2">Upside/ downside</td><td colspan="3">PB</td><td colspan="3">ROE</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2028e</td></tr><tr><td>601633 CH</td><td>Great Wall A</td><td>CNY</td><td>17,501</td><td>56</td><td>16.09</td><td>31.20</td><td>15.90</td><td>Buy</td><td>Hold</td><td>1%</td><td>1.4</td><td>1.3</td><td>1.2</td><td>11%</td><td>13%</td><td>14%</td></tr><tr><td>2333 HK</td><td>Great Wall H</td><td>HKD</td><td>20,178</td><td>24</td><td>9.09</td><td>21.60</td><td>9.30</td><td>Buy</td><td>Hold</td><td>-2%</td><td>0.7</td><td>0.6</td><td>0.6</td><td>11%</td><td>13%</td><td>14%</td></tr><tr><td>601238 CH</td><td>GAC A</td><td>CNY</td><td>6,351</td><td>23</td><td>5.10</td><td>8.23</td><td>5.08</td><td>Hold</td><td>Hold</td><td>0%</td><td>0.5</td><td>0.5</td><td>0.5</td><td>-6%</td><td>0%</td><td>2%</td></tr><tr><td>2238 HK</td><td>GAC H</td><td>HKD</td><td>6,351</td><td>5</td><td>2.19</td><td>3.62</td><td>2.13</td><td>Hold</td><td>Hold</td><td>3%</td><td>0.2</td><td>0.2</td><td>0.2</td><td>-6%</td><td>0%</td><td>2%</td></tr><tr><td>1958 HK</td><td>BAIC</td><td>HKD</td><td>889</td><td>1</td><td>0.87</td><td>2.20</td><td>0.80</td><td>Hold</td><td>Hold</td><td>9%</td><td>0.1</td><td>0.1</td><td>0.1</td><td>-2%</td><td>-1%</td><td>0%</td></tr></table>

Source: Bloomberg, HSBC estimates. Priced as of close on 21Jul 2026

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Issuer of report: The Hongkong and Shanghai Banking Corporation Limited

# Demand reset, ongoing consolidation

We trim our 2026 China auto demand forecasts on weaker demand

\- Consolidation continues as competition weighs on profitability, despite rising EV penetration

We remain selective on stocks; cut estimates on Great Wall, GAC and BAIC, and downgrade Great Wall A/H to Hold/Hold

## Demand reset; recovery pushed further into 2H26

Trim PC and EV 2026e demand; turning point might come in September

In 1H26, China's passenger-vehicle retail sales totalled 8.72m units, a 20% y-o-y decline, while EV sales reached 4.7m units, down 14% y-o-y. The latest CPCA weekly data suggest demand remianed soft into July, with passenger car retail volume down 16% y-o-y and NEV retail volume down 4% y-o-y during 1-19 July. Beside the broader low level of overall consumer propensity, the reduced replacement-subsidy support likely pulled forward demand into 2025, leaving less momentum in 1H26. On the industry side, while headline price wars have been contained, manufacturers have competed by launching more new models with improved specifications without raising prices. Given the market is increasingly replacement-led, faster product refresh cycles may be reinforcing a “wait-and-see” approach among buyers, extending replacement timelines.

Against this backdrop, we have revised our 2026 China passenger-car demand growth forecast to -13% (from -5%). We maintain a -2% y-o-y forecast for 2027, as we still expect some demand to be pulled forward into late 2026 ahead of the anticipated phase-out of replacement subsidies. We have also lowered our EV penetration assumptions following weaker-than-expected 1H26 EV sales growth; our updated EV penetration forecasts for 2026–28 are 58%, 65%, and 71%, respectively.

In our updated forecasts, we expect a modest sequential recovery in 2H26, with the y-o-y decline narrowing to 7%, driven mainly by a seasonal uplift from September and refreshed product line-ups (180+ new models in 2H26) to reignite consumer interest, alongside a likely pre-buying wave in 4Q26 ahead of the potential expiry of the replacement subsidies policy at end-2026.

Exhibit 1. China passenger car and EV demand forecast changes

<table><tr><td rowspan="2"></td><td colspan="4">New forecasts</td><td colspan="4">Old forecasts</td><td colspan="4">Change</td></tr><tr><td>2026e</td><td>2027e</td><td>2028e</td><td>2030e</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2030e</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2030e</td></tr><tr><td>PV volume (in m units)</td><td>20.6</td><td>20.2</td><td>20.2</td><td>20.2</td><td>22.5</td><td>22.1</td><td>22.1</td><td>22.1</td><td>-8%</td><td>-8%</td><td>-8%</td><td>-8%</td></tr><tr><td>PV volume y-o-y growth (%)</td><td>-13%</td><td>-2%</td><td>0%</td><td>0%</td><td>-5%</td><td>-2%</td><td>0%</td><td>0%</td><td>-8%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>EV volume (in m units)</td><td>12.0</td><td>13.2</td><td>14.3</td><td>16.7</td><td>14.1</td><td>15.5</td><td>17.0</td><td>19.5</td><td>-15%</td><td>-15%</td><td>-16%</td><td>-15%</td></tr><tr><td>EV volume y-o-y growth (%)</td><td>-6%</td><td>10%</td><td>8%</td><td>8%</td><td>10%</td><td>10%</td><td>10%</td><td>6%</td><td>-16%</td><td>0%</td><td>-2%</td><td>2%</td></tr><tr><td>EV penetration (%)</td><td>58%</td><td>65%</td><td>71%</td><td>82%</td><td>62%</td><td>70%</td><td>77%</td><td>88%</td><td>-4%</td><td>-5%</td><td>-6%</td><td>-6%</td></tr></table>

Source: HSBC estimates. PV: passenger vehicle. EV: electric vehicle.

Exhibit 2. We trim 2026e demand growth to -13% y-o-y, -6% for EV  
![](images/725305f1af900f69789f6220b5dd0fb3e2905e8f91e4e83d8391589334967715.jpg)  
Source: CPCA, HSBC estimates

Exhibit 3. EV penetration rate remained at 63% in June 2026  
![](images/ba739e5c14f214e791f490a38db4efe3be191992c4f0c664723a9f2ae87069ea.jpg)  
Source: CPCA, HSBC

Exhibit 4. Overall auto retail sales decreased 20% y-o-y in 1H26  
![](images/3216aa8e14dff734dd6daf684c330d85623e8c3c0c372a7bcc3b59e91e2d0a0f.jpg)  
Source: CPCA, HSBC

## ICE segment under siege: structural contraction accelerates in 2026

Retail sales of ICE vehicles fell 26.3% y-o-y in 1H26, with the decline widening sharply in 2Q (-38.2%) versus 1Q (-14.3%). Demand was comparatively resilient only in the RMB200k–300k price band; by contrast, ICE demand weakened materially in both the mass market and premium segments above RMB300k (down 24–36%). As consumers weighed refuelling and running costs alongside smart cockpit and intelligent driving capabilities, preferences continued to shift towards EVs.

On the supply side, pressure intensified. While inventory indicators for JV brands and traditional luxury brands eased m-o-m in June, they remained well above the 1.5 threshold. Dealers sustained elevated discounts to clear stock, further undermining pricing discipline. OEMs also curtailed new ICE launches –12 of 102 new models in 1H26, and 16 of 184 in 2H26e – slowing product refresh cycles. With ICE product competitiveness lagging EVs, ICE market share continued to be displaced across most price tiers in 1H26.

By brand, high-end Chinese EVs (Zeekr 9X, NIO ES8/ES9, XPeng GX, etc) have continued to pressure incumbent luxury players since 2H25. Despite ongoing discounting, BMW and Mercedes-Benz saw faster declines in 1H26 versus 2025: BMW -20% y-o-y (vs -15% in 2025) and Mercedes-Benz -27% y-o-y (vs -20%). In the mass-market segment, Toyota and Volkswagen returned to contraction in 1H26 amid softer trade-in subsidies versus 2025: Toyota -9% y-o-y and Volkswagen -27% y-o-y.

Looking into 2H26, we expect ICE demand to recover sequentially with the peak season, though the rebound should lag EVs. The long-term trajectory remains unchanged: EVs will continue to take share from ICE vehicles, with EV penetration projected to reach 82% by 2030.

Exhibit 5. ICE cars lost share in most price segments except RMB200k-300k  
![](images/dcfeba4db182209bc46e8e178b7de0b0293e51216e054b8a7c57d85059a3852e.jpg)  
Source: CPCA, HSBC

Exhibit 6. In 1H26, ICE vehicle volumes contracted significantly across nearly all price segments  
![](images/c16efebf73a989a71c54916d071ac95f3dff18fd29a382c3316bcc899407925f.jpg)  
Source: CPCA, HSBC

Exhibit 7. In 1H26, demand for premium EVs proved more resilient  
![](images/4eeaf1034552d582e12029a67283ad80755f3290998183807f294745a15d7697.jpg)  
Source: CPCA, HSBC

Exhibit 8. China overall passenger car market: Top 15 brands took 60% share in 1H26
25%  
![](images/fb56a743c9c57ac0e3360e1141c1ed8e1d434cd6454f40d528f705da148b9d2f.jpg)

Exhibit 9. China EV passenger vehicle discount level at relatively low level...  
![](images/d419069d511202894ec62aa16cc410e441d4c2451209f331db861c68864b1eb7.jpg)  
Source: CPCA, HSBC  
Exhibit 10. ...while ICE still under pricing pressure  
Source: CPCA, HSBC

Exhibit 11. Luxury ICE car discount levels are even higher  
![](images/b12e56163bf147bfb18f5fd4c92e06a15769d7db83a2ae3d56ab096ebae4f1e8.jpg)  
Source: CPCA, HSBC

![](images/789626479869340d6df706f6ecc0e667c0c13f787779e74a887fcf9a15db59aa.jpg)

Exhibit 12. JV brands and conventional luxury brands are at high inventory levels  
![](images/bbfceaaad7bda4a987c6034197f4fdf1afc76c465147796c2fe7e6e994cb816a.jpg)  
Source: CADA, HSBC

## Mapping OEM stocks

Based on our lower industry demand forecasts, we cut our estimates for Great Wall, GAC and BAIC, which are relatively under pressure given weaker EV cycles. We downgrade Great Wall A/H shares to Hold from Buy ratings, and retain our Hold ratings on GAC A/H shares, and BAIC.

Exhibit 13. Key changes to ratings and estimates

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Company</td><td rowspan="2">Ccy.</td><td rowspan="2">Market Cap (USDm)</td><td rowspan="2">3M ADTV (USDm)</td><td rowspan="2">Close price</td><td colspan="2">Target price</td><td colspan="2">Rating</td><td rowspan="2">Upside/ downside</td><td colspan="3">PB</td><td colspan="3">ROE</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2028e</td></tr><tr><td>601633 CH</td><td>Great Wall A</td><td>CNY</td><td>17,501</td><td>56</td><td>16.09</td><td>31.20</td><td>15.90</td><td>Buy</td><td>Hold</td><td>1%</td><td>1.4</td><td>1.3</td><td>1.2</td><td>11%</td><td>13%</td><td>14%</td></tr><tr><td>2333 HK</td><td>Great Wall H</td><td>HKD</td><td>20,178</td><td>24</td><td>9.09</td><td>21.60</td><td>9.30</td><td>Buy</td><td>Hold</td><td>-2%</td><td>0.7</td><td>0.6</td><td>0.6</td><td>11%</td><td>13%</td><td>14%</td></tr><tr><td>601238 CH</td><td>GAC A</td><td>CNY</td><td>6,351</td><td>23</td><td>5.10</td><td>8.23</td><td>5.08</td><td>Hold</td><td>Hold</td><td>0%</td><td>0.5</td><td>0.5</td><td>0.5</td><td>-6%</td><td>0%</td><td>2%</td></tr><tr><td>2238 HK</td><td>GAC H</td><td>HKD</td><td>6,351</td><td>5</td><td>2.19</td><td>3.62</td><td>2.13</td><td>Hold</td><td>Hold</td><td>3%</td><td>0.2</td><td>0.2</td><td>0.2</td><td>-6%</td><td>0%</td><td>2%</td></tr><tr><td>1958 HK</td><td>BAIC</td><td>HKD</td><td>889</td><td>1</td><td>0.87</td><td>2.20</td><td>0.80</td><td>Hold</td><td>Hold</td><td>9%</td><td>0.1</td><td>0.1</td><td>0.1</td><td>-2%</td><td>-1%</td><td>0%</td></tr></table>

Source: Bloomberg, HSBC estimates. Priced as of close at Jul 21, 2026

We base our valuations on prevailing/trough trading PE multiples rather than long term historical averages. While valuations appear depressed, we do not expect a meaningful re-rating over our target price horizon, given muted demand, ongoing pricing pressure and limited product cycle catalysts across conventional OEMs. In the absence of a clear earnings or demand inflection, we believe current market multiples better represent fair value than historical averages. The key debate is not whether these stocks are cheap on an historical range basis, but whether there is a catalyst for the market to pay a higher multiple. We think the answer is not yet.

## Valuation and risks

## Great Wall

## Lower 2026-27e net profit mainly on weaker domestic demand

Great Wall Motor has released its Q2 2026 earnings preview, guiding net profit of RMB1.4–1.6bn, below our prior expectations. The key headwind is a delay in the Russian scrappage tax refund process. Around RMB2bn was refundable for the period Q4 2025 to Q1 2026; while partial receipt had been expected in Q2 2026, the funds are now anticipated before year-end. Additionally, despite Q2 sales rising 17% q-o-q (vs +14% q-o-q for overall passenger vehicle wholesale volumes), supported by export momentum (export sales +24% q-o-q), its 1H26 volumes dropped 12% y-o-y, driven by weak domestic demand.

Great Wall's A- and H-shares are down 27% and 38% YTD, respectively (vs CSI300 +2% and HSI -2%), reflecting weak domestic auto sector beta and ongoing quarterly earnings uncertainty linked to the Russian tax refund. Looking ahead, we expect 2H26 volumes to improve with the seasonal upturn from September an

[中间内容因长度限制已省略]

gapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.

## Stay connected to our topical and timely thought leadership

![](images/387318d68a0876c8c652ed6651e4b326d53c440bb947b927d0b6eb0877c659b5.jpg)

## Download the HSBC Global Investment Research app

From Apple's App Store or Google Play The app features topical and timely curated reports, multimedia, and upcoming events

![](images/78b91b072eb32ba672bf00f905babf38795a056e29c253d8af995fe18abc89dd.jpg)

## Log on to the Global Investment Research website

To access all reports and videos, visit research.hsbc.com

![](images/ce2c0deb5b302f86e68ca748ad40f42206821e89305c60de9de1f44e3ec2ec96.jpg)

## Connect with Global Investment Research on LinkedIn

Search #HSBCResearch for free to view insights that can easily be shared with clients and prospects

![](images/287682a26ba7191f6844f53a2f0472b7007d6216fed53fcfae10abbe035fdaea.jpg)

## Subscribe and listen

Under the Banyan Tree by HSBC Global Investment Research on Apple, Spotify or YouTube The Macro Brief by HSBC Global Investment Research on Apple, Spotify or YouTube

![](images/f93f76dd959cafc2b93509083f705577dcb2343d031817f17cefc52316eedcaf.jpg)

## Newsletters

Subscribe to our monthly collection of free to view reports and interviews in Open Pass or read our bite-sized round up of research covering our nine key themes, Talking Points
"""
