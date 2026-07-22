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
# The five C's for a broadening

Global Equity Strategy

\- We remain constructive on global equities but expect a broadening in performance driven by the five C's

Corporate earnings, Central banks, Capex, Consumer and Capital flows

\- Middle East tensions and higher energy prices are downside risks, but for now offset by improving fundamentals elsewhere

We remain bullish on global equity markets, but are increasingly positioning for a rotation in performance. Early signs of that shift are already emerging. Our global long-versus-short momentum factor has fallen 15% over the past 3 weeks, but we believe the reversal likely has further to run. The rally in momentum stocks year-to-date has been one of the strongest on record. Historical precedent suggests that, after a 20% rise in the momentum factor, the subsequent reversal typically persists for around six months. The current episode is particularly unusual: after initially rising 20%, momentum subsequently squeezed another 25% higher. In our view, that leaves the factor increasingly vulnerable to a sharper and more sustained reversal.

Other signs of a potential rotation are also becoming more evident. Concentration across global equity indices – particularly in the US and EM – remains close to record highs. Yet, for all the focus on AI and technology outperformance, the rest of the market has, broadly speaking, also performed well. Equal-weighted indices in the US, EM, and Europe are up 12%, 5%, and 10%, respectively, year-to-date. Renewed tensions in the Middle East and a large spike in energy prices are downside risks, but for now we believe the improving fundamental backdrop elsewhere should more than offset this.

We believe a further rally and sustained broadening in global equity-market performance can be supported by the five Cs:

Corporate earnings: US earnings growth looks strong and broadening beyond tech/energy with revision improving. EM and Europe EPS are also accelerating.

Central banks: Markets are pricing 37bps of hike by mid-2027; further hawkish repricing may be limited, which should support cyclicals.

Capex: Broadening depends on steady AI capex: cuts look unlikely as monetisation emerges, but big hyperscaler upgrades are limited, moderating semiconductor outperformance after strong gains.

Consumer: Despite a slowdown in real-time spending data, outlook remains constructive amid strong labor data, World Cup boost and wealth effects. Cons. discretionary valuations are cheap, and earnings expectations look too pessimistic.

Capital flows: Despite record US IPO and secondary issuance, equity demand looks strong: buybacks remain large, retail ETF inflows are accelerating, global inflows are rising, Europe funds are rotating into cyclicals, and EM ex-tech is seeing inflows.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Equity Strategy Global

Alastair Pinder, CFA
Head EM and Global Equity Strategist
HSBC Securities (USA) Inc.
alastair.pinder@us.hsbc.com
+1 212 525 5972

## Pankaj Agarwala\*, CFA

Pankaj Agarwala, SFA
EM and Global Equity Strategist
HSBC Securities and Capital Markets (India) Private Limited
pankajagarwala@hsbc.co.in
+91 0 80 30013716

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

## No country for bears

The $24^{\text{th}}$ edition of the EM Sentiment Survey Click to view

Issuer of report: HSBC Securities (USA) Inc.

View HSBC Global Investment Research at: https://www.research.hsbc.com

## The five C's for a broadening

We believe a further rally and sustained broadening in global equity-market performance can be supported by the five Cs:

Corporate earnings: Earnings season is upon us, and we think the setup once again looks favorable for the US. Consensus expects the S&P 500 to deliver earnings growth of nearly 23% y-o-y, but the bulk of this – 85% – is expected to come from tech and energy, where earnings are forecast to grow 62% and 124% y-o-y, respectively $^{1}$ . Yet, for all the focus on tech and its outsized contribution to overall US earnings growth, we think the market is underestimating the potential breadth of the expansion. The consensus expects the median US stock to see EPS growth slow from 15% y-o-y in Q1 to 9% y-o-y in Q2. Areas such as consumer discretionary and industrials are expected by consensus to experience a sharp deceleration, but we believe consensus is underestimating the resilience of corporate earnings despite the spike in energy costs amid the Middle East conflict. Corporate guidance trends also point to a broadening in earnings momentum. The ratio of companies raising guidance relative to those lowering it has reached the top-seventh percentile, as management teams become more positive. The US earnings revisions ratio has risen to 73%, its highest level since 2021 and in the top-fifth percentile since 2000 – indicative of early-cycle market dynamics. Nor is the potential broadening confined to the US. In emerging markets, consensus expects EPS growth to accelerate to 35% in Q2, predominantly driven by semiconductors. However, even excluding Taiwan and Korea, EM earnings are expected to grow close to 10.5% y-o-y, their fastest pace since Q2-22. Meanwhile, European earnings could grow 15% y-o-y in Q2, their strongest rate since 2022.

Central banks: Market pricing for the Fed has shifted dramatically in recent months. As recently as March, the options market was pricing a 70% probability that the Fed would leave rates unchanged by the April 2027 meeting and a 25% probability of 25bp of rate cuts. Fast-forward to today, and the market is assigning roughly a 35% probability to both a 25bp and a 50bp rate hike. In our view, this creates a relatively high bar for further hawkish repricing. It was a surprise that, at the June FOMC meeting – the first under new Fed Chair Kevin Warsh – the committee actively discussed the potential need for rate hikes later this year. However, HSBC economists expect the FOMC to keep the federal funds target range unchanged throughout 2026 and 2027 $^{2}$ . Core inflation has accelerated, but there is a notable divergence between core PCE, at 3.4% y-o-y, and Warsh's preferred Dallas Fed trimmed-mean PCE measure, which stands much closer to the Fed's 2% target at 2.4% y-o-y. The recent soft inflation data with headline CPI fell 0.4% m/m (consensus -0.1%) should also push back against the hawkish narrative $^{3}$ . We think a shift toward pricing fewer Fed rate hikes, alongside a “no landing” scenario, would support a stronger rotation into cyclical sectors and small caps. Indeed, the sweet spot for equity markets historically has been a gradual unwinding of rate expectations: during episodes in which the 12m Fed futures have fallen 0-25bps over a 3m period, equities have rallied over 4% on average.

Capex: The sweet spot for a broadening trade is neither cuts to AI capex nor another round of material increases in spending expectations. In our view, concerns about capex cuts are overdone, at least for now, as early signs of monetization are clearly emerging. Anthropic is currently operating at a revenue run rate of USD47bn. Despite concerns about falling token costs, the more important data point may come from Ramp AI, which shows that monthly AI spending per employee continues to rise from a low base. Median spending is just USD10.66, up 2.5x y-o-y, versus the top-10th percentile which is currently spending USD516 per employee per month. At the same time, material upgrades to hyperscaler capex estimates from current levels appear unlikely. The powerful earnings upgrades across semiconductors and memory have been driven directly by rising US hyperscaler capex. Consensus estimates for 2026 and 2027 have been raised by USD200bn and USD300bn, respectively, year-to-date, with around 70% of that capex directed toward GPUs and servers. This has effectively redirected free cash flow from US hyperscalers – where FCF is expected to fall from USD220bn in Q1-25 to -USD2bn by Q4-26e – to NVIDIA and Micron, where FCF is expected to rise from USD74bn to USD280bn during the same period. However, the scope for capex upgrades of a similar magnitude over the next 12-18 months is limited, in our view, which should moderate the speed of semiconductor outperformance.

Consumer: The consumer is another important source of support for a broadening trade, particularly in the US. Overall, we believe US consumer data remain healthy. Although real-time spending data from Bloomberg Second Measure has slowed in recent weeks – largely because of lower spending on gasoline – we are beginning to see signs of stabilization. Several other factors remain supportive: (1) Employment data remain resilient, with initial jobless claims at multi-year lows; (2) Consumer confidence, as measured by Morning Consult, is recovering sharply, particularly among higher-income households; (3) The FIFA World Cup should provide an additional, albeit temporary, boost as OpenTable data already show y-o-y growth in US seated diners at multi-year highs; and (4) Higher equity markets and the AI boom are generating a pronounced wealth effect, with more than 50% of US household wealth held in equities. Overall, we believe the market remains too cautious on the consumer discretionary sector. Excluding Amazon and Tesla, the sector trades at a 12-month forward PE of just 16.6x, placing it in the bottom-tenth percentile since 2015. Meanwhile, the median consumer stock is expected to see earnings growth slow from 15.5% y-o-y in Q1 to 4.5% in Q2, which we believe is overly pessimistic.

Capital flows: Sustained equity demand is also essential to support a rotation and broadening in market performance. There has been considerable debate over whether the record volume of US IPOs expected this year – driven by the mega-cap technology listings of OpenAI, Anthropic, and SpaceX – could mark a market peak or create excess supply. We estimate that total US IPO issuance, including the mega-caps, could exceed USD270bn this year, alongside an additional USD470bn of secondary issuance. This would make 2026 the heaviest year of issuance on record for the US equity market. Even so, we see sufficient demand to absorb the supply. First, buybacks remain substantial. Announced buybacks already total USD850bn this year, almost USD100bn more than at the same point in 2025. Our estimates suggest that net US buybacks – buybacks less primary and secondary issuance – could still reach USD700bn in 2026, broadly in line with 2025. Retail demand for equities also appears relentless. US ETFs have attracted around USD550bn year-to-date, equivalent to a monthly pace of nearly USD85bn, compared with roughly USD62bn in 2025. Outside the US, there are further signs that equity demand is broadening. Amid an easing in global energy prices, weekly global equity fund inflows have risen to their highest level since March 2021. In Europe, funds are increasing their exposure to cyclicals relative to defensives from low levels – a shift consistent with broader risk-on positioning among buy-side investors and an improving sell-side outlook for cyclical sectors. Meanwhile, although foreign outflows from EM equities have reached a record USD90bn so far this year, they have been entirely driven by EM's tech trident: TSMC, Samsung Electronics, and SK Hynix. Excluding those three stocks, EM equities have attracted close to USD20bn of foreign inflows year-to-date $^{4}$ .

## Our preferences from a broadening story

Globally, our preferred areas that should benefit from a broadening include: in the US we like the consumer discretionary sector, as well as the banks which have had a strong start to the earnings season supported by good loan growth, generally favorable NII dynamics, robust IB fees and sales & trading, continued efficiency progress, and benign credit. In Europe, we believe that some of the beaten up cyclical areas could also recover – this includes airlines and hotels (which should be buoyed by lower energy prices and recovering tourism), luxury names (strong US consumer, stabilization in mainland China and sharp acceleration in spending in pockets of Asia like Korea), and also the defense sector. We continue to like the banks that have seen renewed price momentum in recent weeks and where the forward dividend yield is the highest across all sectors $^{5}$ . A higher rate backdrop and/or steeper curves could continue to support the sector. Within EM, we anchor our views on three conviction themes $^{6}$ : (1) cyclical recovery plays that are resilient to higher food price pressures: South Africa, Chile, and parts of CEE; (2) AI spillovers and innovation winners: Korea consumer names, which should benefit from higher compensation from the semi names, and also mainland China’s tech hardware stack, which benefits from faster technology self-reliance and provides diversification from the reliance on US hyperscaler capex; and (3) Deep-value plays: such as Brazil and Türkiye, which have underperformed by more than fundamentals warrant and/or where valuations look excessively cheap.

HSBC global equity strategy regional and sector allocation  
Global regional allocation

<table><tr><td>HSBC view</td><td>Region</td><td>Benchmark weight</td></tr><tr><td>Overweight</td><td>US</td><td>62%</td></tr><tr><td>Overweight</td><td>Emerging Markets</td><td>10%</td></tr><tr><td>Neutral</td><td>Europe (ex UK)</td><td>11%</td></tr><tr><td>Neutral</td><td>Developed Asia ex JP</td><td>5%</td></tr><tr><td>Neutral</td><td>UK</td><td>3%</td></tr><tr><td>Neutral</td><td>Canada</td><td>3%</td></tr><tr><td>Underweight</td><td>Japan</td><td>6%</td></tr></table>

Global sector allocation

<table><tr><td>HSBC view</td><td>Sector</td><td>Benchmark weight</td></tr><tr><td>Overweight</td><td>Technology</td><td>34%</td></tr><tr><td>Overweight</td><td>Financials</td><td>16%</td></tr><tr><td>Overweight</td><td>Basic Materials</td><td>3%</td></tr><tr><td>Neutral</td><td>Industrials</td><td>12%</td></tr><tr><td>Neutral</td><td>Consumer Discretionary</td><td>11%</td></tr><tr><td>Neutral</td><td>Healthcare</td><td>8%</td></tr><tr><td>Neutral</td><td>Energy</td><td>4%</td></tr><tr><td>Neutral</td><td>Real Estate</td><td>2%</td></tr><tr><td>Underweight</td><td>Consumer Staples</td><td>4%</td></tr><tr><td>Underweight</td><td>Telecoms</td><td>3%</td></tr><tr><td>Underweight</td><td>Utilities</td><td>3%</td></tr></table>

1. Global momentum factor has had an extraordinary run...  
![](images/6663e246d705b2bf1413cd28a5f773f73213f7919e9d6eac0d7378134ff4d45c.jpg)  
Source: FTSE Russell, FactSet, HSBC

2. ... but momentum stocks appear to have overrun and could continue to struggle the next few months  
![](images/fd4102da38bebf7dd92e88e361e2429a0ed3aea958a8ace3c92a746c69f16dbf.jpg)  
Source: FTSE Russell, FactSet, HSBC

3. Equal-weighted performance has been admirable despite underperforming broader benchmarks  
![](images/07333a53a4d05dc1120dc7dd09f189662443edb815b9bf41d12d183d15206d68.jpg)  
Source: FTSE Russell, FactSet, HSBC

4. A rotation could support a move into mid-caps  
![](images/9c4254eece2f043edd2216ab38ee8cf8c1289652eaf65e249099c93b98d05850.jpg)  
Source: FTSE Russell, FactSet, HSBC

5. Concentration in benchmark equities is at record highs in indices for US and EM  
![](images/d88a0a1ff50b2887a5e1d0f71d54439703dfe6f016e1f12417a37d1ff81a0d15.jpg)  
Source: FTSE Russell, FactSet, HSBC

6. S&P 500 stock correlations has fallen to record lows indicating a high level of alpha opportunities  
![](images/50007d82fbbcf6489a374fa9381f8aefffa40b478397b25125a803fafcc4424e.jpg)  
Source: Bloomberg, HSBC

7. LLM token e

[中间内容因长度限制已省略]

ed investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB.

© Copyright 2026, HSBC Securities (USA) Inc., ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Securities (USA) Inc.

# Global Equity Strategy Research Team

## Global

Head EM and Global Equity Strategist
Alastair Pinder, CFA +1 212 525 5972
alastair.pinder@us.hsbc.com

Allison Buck +1 212 525 4119
allison.buck@us.hsbc.com

Dmitriy Leskin +1 212 525 4110
dmitriy.leskin@us.hsbc.com

Pankaj Agarwala, CFA +91 80 4550 3716
pankajagarwala@hsbc.co.in

## Europe

Sustainability Research; European Equity Strategist  
Amit Shrivastava +971 4 509 3349  
amit1.shrivastava@hsbc.com

## Asia

Head of Equity Strategy, Asia Pacific
Herald van der Linde, CFA +852 2996 6575
heraldvanderlinde@hsbc.com.hk

Raymond Liu +852 2996 6743 raymond.w.m.liu@hsbc.com.hk

Prerna Garg +852 9831 6901
prerna.garg@hsbc.com.hk

Adam Qi +852 2288 9311
adam.x.l.qi@hsbc.com.hk

Jer Shyuen Chong +852 2899 8682
jer.shyuen.chong@hsbc.com.hk

Danelle Teo +65 6658 5497 danelle.t.y.teo@hsbc.com.sg

## Americas

Head of Equity Strategy, Americas
Nicole Inui +55 11 98984 6169
nicole.inui@hsbc.com
"""
