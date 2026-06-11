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
# China Solar

## Takeaways from SNEC 2026

# Equities

# Energy Equipment &

# Services

## China

- Space-based solar products still a niche segment, residential ESS drew the most attention; solar supply chain was quiet  
- Solar equipment exports are still restricted as most companies wait rather than seek an SE Asia workaround  
- SST products for AIDC are emerging as the next key battleground

Key takeaways: We attended SNEC in Shanghai on 3–4 June, meeting with investors and engaging with leading solar companies across space solar, residential energy storage systems (ESS), inverters and related segments. Below are our key takeaways:

$\diamond$ Space solar: Still niche at SNEC, but positioned as 'flagship' by exhibitors. Solar-cell technology is shifting beyond GaAs towards silicon and tandem. Lightweight covers, such as space colourless polymide film (SCPI), are a key differentiator. Commercial orders more likely around 2027 after multi-round validation.

Solar equipment: Near-term outlook is driven more by policy clarity or enforcement than end-demand. Most companies downplayed US export exposure and rejected exporting via Southeast Asia as a workaround. They claimed to adhere strictly to domestic guidance in China.

Residential solar + ESS: One of the highest-traffic segments. Hardware is commoditising, shifting differentiation to channels and software/service. AI-enabled energy management is becoming baseline, and all-in-one integrated systems are proliferating to simplify installation and user experience.

AIDC & compute/power integration: ‘Green power for AIDC’ was a major theme, with ecosystem focus on DC coupling and system-level integration. Solid-state transformers (SST) are emerging as a key battleground, but deployment is expected to be gradual, pending proof of lifecycle economics and efficiency.

Solar supply chain: Noticeably quieter versus storage/AIDC. Pricing remains under pressure and segmented. Cost pass-through is uneven (tax rebate changes partly passed, silver inflation harder), reinforcing ‘optimise/retrofit’ over new builds. Cost-down levers include reduced-silver/copper metallisation.

Energy storage: Remains the highest-attention growth narrative of some companies. C&I storage is gaining share with improving pipeline stability, while utility-scale is more crowded and price-competitive, pushing some to overseas/niche structures. Margin protection hinges on pricing discipline and the ability to pass through volatile battery input costs.

## Daniel Yang\*

Analyst, Asia Energy Transition

The Hongkong and Shanghai Banking Corporation Limited
daniel.h.yang@hsbc.com.hk

+852 299 66976

## Evan Li\*

Head, Asia Energy Transition Research

The Hongkong and Shanghai Banking Corporation Limited
evan.m.h.li@hsbc.com.hk

+852 2996 6619

## Corey Chan\* (Reg. No. S1700518100001)

Head, A-share Industrials & Renewables Research

HSBC Qianhai Securities Limited

corey.chan@hsbcqh.com.cn

+86 21 5066 2001

## Lucille Tang\*

Associate

Guangzhou

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

## Takeaways from SNEC 2026

We participated in SNEC in Shanghai on 3-4 June to visit some of the leading solar companies. Below is a summary of the discussions with company management, experts and investors we met during the tour.

## Space solar

Space-based solar product demonstration: The number of exhibitors explicitly focused on space solar was relatively limited, but those that did show space-related products tended to place them at the centre of the booth narrative (a ‘flagship storyline’ rather than as a side topic).  
- Technology direction: Industry discussion is moving beyond GaAs-only dependence towards silicon-based flexible solutions and tandem concepts (e.g., silicon + perovskite), with >30% efficiency targets cited versus c20% for current silicon space cells.  
Lightweight materials as a differentiator: A recurring theme was replacing traditional glass cover layers (often cited around c110 $\mu$ m) with ultra-thin polymer/film-based covers (<c25 $\mu$ m), such as SCPI, to reduce mass while improving flexibility and durability. Moreover, SCPI can bend 360° and withstand c10,000 bends without damage while the ultra-thin glass (UTG) cracks after c20 bends.  
Commercialisation timeline: Industry expectations implied multi-year validation cycles (ground + in-orbit testing). A typical validation cycles of 3–6 months per round with multiple in-orbit trial opportunities (e.g., 20+ launch windows) were referenced to accelerate iteration. Meaningful order conversion is more likely around 2027.  
Conservative around SpaceX's 100GW per year of solar capacity goal: Following our earlier report on space solar (Space-based Solar, 1 June 2026), we found that messaging from the SNEC tour implied conservative attitudes from both companies and investors regarding SpaceX and Tesla's 100GW per year of solar manufacturing capacity goal in three years in the US.

## Solar equipment

US export sensitivity: Many equipment companies downplayed or denied direct exports to the US, with a ‘wait-and-see’ stance tied to evolving policy interpretation and enforcement.  
Southeast Asia not an alternative route: Companies denied the alternative export route from Southeast Asia to circumvent the domestic restrictions.  
Policy uncertainty is the key variable: Conversations suggested that the near-term swing factor is regulatory clarity and enforcement, not end-demand. Companies emphasised strict adherence to domestic guidance while awaiting official announcements.  
Demand shifting by region: Export opportunities were described as rebalancing away from parts of Southeast Asia (affected by trade measures) towards Middle East / North Africa / Türkiye and other markets.  
Retrofit cycle is the anchor: With cumulative TOPCon capacity cited at 800GW+, the equipment cycle is increasingly upgrade-led rather than greenfield-led. Typical retrofit packages for upgrading old TOPCon to new TOPCon were cited at cRMB30m per GW, lifting module efficiency from 620W to 650W+.  
- Capex reference points: New TOPCon line equipment investment was cited at cRMB120-140m per GW. BC line equipment was cited as <RMB200m per GW, with equipment value share in high-power BC lines often described as c40-50% of total line value.

## Residential solar + energy storage system (ESS)

Exhibition heat: Residential storage was one of the busiest segments at the show, with consistently high booth traffic.  
Low perceived entry barriers: The segment looked easy to enter from a product standpoint as hardware differentiation is narrowing, accelerating competition and pushing differentiation towards channels, certification, delivery, and software service.  
AI as a standard feature: Many vendors positioned AI-enabled energy management (tariff arbitrage, smart scheduling, predictive control, VPP participation) as a baseline capability rather than a premium add-on.  
All-in-one products proliferating: Integrated ‘all-in-one’ systems were widely launched or previewed, signaling a shift towards simplified installation and packaged user experience.

## AIDC & compute/power integration

A show highlight: ‘Green power for AIDC’ was heavily promoted via renderings, demo boards, and reference architectures, indicating strong ecosystem attention.  
Solid-state transformer (SST) momentum: SST solutions for data-centre power are emerging as a focal point. Multiple players are developing SST-based power solutions for AIDC, and competitive intensity appears real and rising.  
- Architecture focus: Discussions frequently centred on DC coupling and system-level integration, aligning with data-centre power distribution trends.  
Longer adoption cycle: Despite strong interest, deployment is expected to be slower, driven by the need to prove lifecycle economics, efficiency, PUE impact, reliability, and standardisation.

## Solar supply chain

Relatively quiet: Compared with storage and AIDC themes, the traditional solar supply-chain narrative felt noticeably cooler at the exhibition.  
Pricing remains pressured and segmented: Mainstream utility-scale pricing was discussed around RMB0.69-0.75/W, while distributed/overseas mixes could clear at RMB0.85-1.00/W. Very low-priced orders were described as more concentrated earlier in the year.  
Cost pass-through is imperfect: Export tax rebate changes were partially passed through in new contracts, while silver cost inflation was harder to fully transfer, keeping margin management tight.  
‘Optimise and retrofit’ over ‘build new’: The focus is on process optimisation and cost-down, including reduced-silver/copper-based metallisation. Cost-down impact was cited at RMB0.03-0.05/W under silver prices around RMB18k-19k/kg.  
Copper-based metallisation is a key cost-down lever, but ramp takes time: Industry commentary highlighted copper paste / reduced-silver approaches as a major next step. Initial deployment targets were discussed at the single-digit GW level, implying a gradual scale-up rather than an overnight switch.  
Ongoing shakeout: Industry commentary continued to point to low utilisation rates (often cited at ≤50%), implying a prolonged capacity-clearing process.

## Energy storage

Attention remains elevated: Storage drew more traffic and mindshare than modules, reinforcing its role as the current “growth and storytelling” engine.

C&I storage gaining share: Commercial & industrial storage was repeatedly framed as a fast-growing segment, with improving shipment stability and project pipelines.  
Utility-scale is competitive: Large-scale storage was described as more crowded and price-competitive, pushing some participants to prioritise overseas or niche project structures.  
Pricing discipline and cost pass-through: With battery input costs fluctuating, the ability to adjust pricing while protecting margins was highlighted as a key operational differentiator.

# Disclosure appendix

## Analyst Certification

The following analyst(s), economist(s), or strategist(s) who is(are) primarily responsible for this report, including any analyst(s) whose name(s) appear(s) as author of an individual section or sections of the report and any analyst(s) named as the covering analyst(s) of a subsidiary company in a sum-of-the-parts valuation certifies(y) that the opinion(s) on the subject security(ies) or issuer(s), any views or forecasts expressed in the section(s) of which such individual(s) is(are) named as author(s), and any other views or forecasts expressed herein, including any views expressed on the back page of the research report, accurately reflect their personal view(s) and that no part of their compensation was, is or will be directly or indirectly related to the specific recommendation(s) or views contained in this research report: Daniel Yang, Evan Li and Corey Chan

## Important disclosures

## Equities: Stock ratings and basis for financial analysis

HSBC and its affiliates, including the issuer of this report ("HSBC") believes an investor's decision to buy or sell a stock should depend on individual circumstances such as the investor's existing holdings, risk tolerance and other considerations and that investors utilise various disciplines and investment horizons when making investment decisions. Ratings should not be used or relied on in isolation as investment advice. Different securities firms use a variety of ratings terms as well as different rating systems to describe their recommendations and therefore investors should carefully read the definitions of the ratings used in each research report. Further, investors should carefully read the entire research report and not infer its contents from the rating because research reports contain more complete information concerning the analysts' views and the basis for the rating.

## From 23rd March 2015 HSBC has assigned ratings on the following basis:

The target price is based on the analyst's assessment of the stock's actual current value, although we expect it to take six to 12 months for the market price to reflect this. When the target price is more than $20\%$ above the current share price, the stock will be classified as a Buy; when it is between $5\%$ and $20\%$ above the current share price, the stock may be classified as a Buy or a Hold; when it is between $5\%$ below and $5\%$ above the current share price, the stock will be classified as a Hold; when it is between $5\%$ and $20\%$ below the current share price, the stock may be classified as a Hold or a Reduce; and when it is more than $20\%$ below the current share price, the stock will be classified as a Reduce.

Our ratings are re-calibrated against these bands at the time of any 'material change' (initiation or resumption of coverage, change in target price or estimates).

Upside/Downside is the percentage difference between the target price and the share price.

## Prior to this date, HSBC's rating structure was applied on the following basis:

For each stock we set a required rate of return calculated from the cost of equity for that stock's domestic or, as appropriate, regional market established by our strategy team. The target price for a stock represented the value the analyst expected the stock to reach over our performance horizon. The performance horizon was 12 months. For a stock to be classified as Overweight, the potential return, which equals the percentage difference between the current share price and the target price, including the forecast dividend yield when indicated, had to exceed the required return by at least 5 percentage points over the succeeding 12 months (or 10 percentage points for a stock classified as Volatile\*). For a stock to be classified as Underweight, the stock was expected to underperform its required return by at least 5 percentage points over the succeeding 12 months (or 10 percentage points for a stock classified as Volatile\*). Stocks between these bands were classified as Neutral.

\*A stock was classified as volatile if its historical volatility had exceeded 40%, if the stock had been listed for less than 12 months (unless it was in an industry or sector where volatility is low) or if the analyst expected significant volatility. However, stocks which we did not consider volatile may in fact also have behaved in such a way. Historical volatility was defined as the past month's average of the daily 365-day moving average volatilities. In order to avoid misleadingly frequent changes in rating, however, volatility had to move 2.5 percentage points past the 40% benchmark in either direction for a stock's status to change.

## Rating distribution for long-term investment opportunities

As of 31 March 2026, the distribution of all independent ratings published by HSBC is as follows:

<table><tr><td>Buy</td><td>59%</td><td>(12% of these provided with Investment Banking Services in the past 12 months)</td></tr><tr><td>Hold</td><td>36%</td><td>(12% of these provided with Investment Banking Services in the past 12 months)</td></tr><tr><td>Sell</td><td>6%</td><td>(6% of these provided with Investment Banking Services in the past 12 months)</td></tr></table>

For the purposes of the distribution above the following mapping structure is used during the transition from the previous to current rating models: under our previous model, Overweight = Buy, Neutral = Hold and Underweight = Sell; under our current model Buy = Buy, Hold = Hold and Reduce = Sell. For rating definitions under both models, please see “Stock ratings and basis for financial analysis” above.

For the distribution of non-independent ratings published by HSBC, please see the disclosure page available at http://www.hsbcnet.com/gbm/financial-regulation/investment-

[中间内容因长度限制已省略]

on and the Financial Supervisory Service of Korea. In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.

[1280815]
"""
