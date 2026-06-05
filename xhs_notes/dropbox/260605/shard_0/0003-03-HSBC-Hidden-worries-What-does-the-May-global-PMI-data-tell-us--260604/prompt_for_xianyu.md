你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# Hidden worries

# What does the May global PMI data tell us?

- The global composite PMI remained unchanged in May, with both manufacturing and service sector expansion...   
- ...but longer delivery times and frontloading continue to inflate the headline manufacturing index...   
- ...as businesses expect increased price pressures and supply chain problems to persist for now

The global composite PMI in May recorded another month of expansion, at 51.8 – the same as in April. Both manufacturing and services stayed in expansionary territory. Still, the underlying picture isn't especially encouraging.

The global manufacturing PMI came in at 52.6 in May, unchanged from April. The headline is still propped up by longer suppliers' delivery times and frontloading. Firms expect Middle East tensions to disrupt supply chains, pushing prices higher. In the US, both the S&P and ISM manufacturing PMIs showed solid gains in production and rising new orders, largely tied to inventory buildups to hedge against potential shipment delays and cost spikes in coming months. The eurozone, by contrast, is already showing signs of slowing as cost pressures weigh on demand.

The services sector tells a similar story. Higher costs appear to be dampening demand, particularly in the eurozone and the UK. In the US, new orders rose, but firms reduced employment on both measures. Mainland China and India saw activity accelerate on stronger new orders, though price pressures are still a concern.

We don't think the current PMI strength is likely to last, given the challenges of higher inflation. If cost pressures worsen further, demand destruction could follow. In this environment, it's worth leaning more on components like employment, output, and new orders rather than the headline indices.

1. Snapshot of manufacturing and services PMIs 

<table><tr><td rowspan="2"></td><td colspan="3">Manufacturing PMIs</td><td colspan="3">Services PMIs</td></tr><tr><td>Mar 26</td><td>Apr 26</td><td>May 26</td><td>Mar 26</td><td>Apr 26</td><td>May 26</td></tr><tr><td>World</td><td>51.3</td><td>52.6</td><td>52.6</td><td>50.8</td><td>51.2</td><td>51.3</td></tr><tr><td>US</td><td>52.3</td><td>54.5</td><td>55.1</td><td>49.8</td><td>51.0</td><td>50.7</td></tr><tr><td>US ISM</td><td>52.7</td><td>52.7</td><td>54.0</td><td>54.0</td><td>53.6</td><td>54.5</td></tr><tr><td>Mainland China*</td><td>50.8</td><td>52.2</td><td>51.8</td><td>52.1</td><td>52.6</td><td>54.4</td></tr><tr><td>Mainland China NBS</td><td>50.4</td><td>50.3</td><td>50.0</td><td>50.1</td><td>49.4</td><td>50.1</td></tr><tr><td>Eurozone</td><td>51.6</td><td>52.2</td><td>51.6</td><td>50.2</td><td>47.6</td><td>47.7</td></tr><tr><td>Japan</td><td>51.6</td><td>55.1</td><td>54.5</td><td>53.4</td><td>51.0</td><td>50.0</td></tr><tr><td>UK</td><td>51.0</td><td>53.7</td><td>53.9</td><td>50.5</td><td>52.7</td><td>49.3</td></tr><tr><td>India</td><td>53.9</td><td>54.7</td><td>55.0</td><td>57.5</td><td>58.8</td><td>59.8</td></tr><tr><td>Brazil</td><td>49.0</td><td>52.6</td><td>49.1</td><td>50.1</td><td>52.3</td><td>50.4</td></tr><tr><td rowspan="2">Heatmap Key</td><td colspan="3">Below 50 and rising</td><td colspan="3">Above 50 and rising</td></tr><tr><td colspan="3">Below 50 and falling</td><td colspan="3">Above 50 and falling</td></tr></table>

Source: S&P Global, HSBC. \*Refers to RatingDog Mainland China PMI. Due to a later-than-usual release date, May readings for Greece, Indonesia, Ireland, Malaysia, Pakistan, Romania, and Thailand were not available to include in the global calculations.

# Economics Global

# Maitreyi Das

Global Economist

HSBC Securities and Capital Markets (India) Private Limited

maitreyi.das@hsbc.co.in

+91 80 6737 3155

# Bethan Ellis

Global Economist

HSBC Bank plc

bethan.ellis@hsbc.com

+44 20 7991 6714

# Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Issuer of report: HSBC Securities and Capital Markets (India) Private Limited

View HSBC Global Investment Research at:

https://www.research.hsbc.com

# Three key takeaways from this month's data

# 1. Intensifying supply shocks and price pressures are a global theme now

The May PMI releases point to another month of “distorted” growth – headline resilience masking longer delivery times. Quantities of purchases accelerated for a second consecutive month, consistent with firms frontloading inputs amid heightened supply risks linked to the Middle East conflict.

Input costs intensified further in May, with global manufacturing input costs rising at the fastest pace since June 2022. The US recorded the sharpest increase in nearly four years, with respondents pointing to higher costs for petroleum products, steel, and freight. France, Germany, Japan, the UK, and the Philippines also saw faster input price inflation. Yet pass through remains incomplete in many economies, implying renewed margin squeeze rather than a clean shift higher in final-goods pricing. Consequently, orders are being placed to get ahead of increases in output prices. Beyond the Middle East conflict, US tariffs could be another factor in this frontloading. There has been some evidence of US importers bringing forward orders to get ahead of expected increases in tariffs later this year, particularly from Asia.

In the US, both the S&P Global and ISM surveys noted comments pointing to accelerated stockpiling, helping to lift new orders and production to multiyear highs. Japan, India, Korea, and Vietnam also recorded sharp increases in purchasing volumes, reflecting concerns over both supply bottlenecks and rising prices.

# 2. Regional divergence: US strength vs a fragile eurozone

The US manufacturing upswing looks increasingly entrenched, with production rising to its highest level since April 2022. By contrast, the eurozone is losing momentum. The region's two largest economies – Germany and France – both slowed, with respondents noting that Middle East-related disruptions are weighing on demand via higher costs, and new orders remain muted.

The eurozone headline PMI remained above 50, but the composition warrants caution. Part of the support comes from longer delivery times, which can mechanically lift the index (the logic is that, in a normal situation, longer delivery times indicate higher demand). Removing delivery times from the index would place eurozone manufacturing in contraction. A similar distortion can be seen in the world index, but to a lesser extent.

Elsewhere, in Asia, manufacturing activity improved in economies including India, Korea, and Japan, while they expanded at a slower pace in mainland China. However, the positive impulse appears more risk- than demand-led: a meaningful share of the pickup is consistent with precautionary buying ahead of potential supply chain disruption.

# 3. Services PMI: Higher costs have started to impact demand

The global services sector continued to expand in May, with the global services PMI at 51.3. New orders expanded, with panellists citing clients frontloading purchases. But employment declined, signalling subdued underlying demand and higher cost pressures. Ultimately, higher price pressures in many economies will weigh on service activity.

The sector is also showing a familiar split. Asia and the US are holding up better than the eurozone and the UK. Stronger new orders – especially in India and mainland China – have driven a faster pace of activity. In the US, the ISM services accelerated, while the S&P index ticked down but stayed in expansionary territory, both supported by new orders. However, employment fell sharply, reflecting some pessimism in the data. In Europe, meanwhile, higher cost pressures have started to curb demand. In the UK, respondents pointed to subdued consumer spending in travel, tourism, and leisure.

A swift de-escalation in the Middle East would ease supply chain constraints and take some heat out of prices, which would help demand. Nonetheless, the conflict has already run for more than three months, and even if the Strait of Hormuz were to reopen, normalisation in PMIs would take time.

See over the page for all the key PMI charts from the latest releases.

# Manufacturing PMIs

2. The global manufacturing PMI came in at 52.6 in May, unchanged from April...   
![](images/7e2da4805c6545fbe4c795061606381abff604db6ecb3128937e6046411a11d4.jpg)

<details>
<summary>line</summary>

| Year | New Orders | Employment | New Export Orders | Headline |
|------|------------|------------|-------------------|----------|
| 2022 | 51         | 50         | 50                | 54       |
| 2023 | 48         | 50         | 47                | 49       |
| 2024 | 51         | 50         | 50                | 51       |
| 2025 | 50         | 50         | 49                | 51       |
| 2026 | 53         | 50         | 50                | 53       |
</details>

Source: S&P Global, Macrobond. Note: due to a later-than-usual release date, May readings for Greece, Indonesia, Ireland, Malaysia, Pakistan, Romania, and Thailand were not available to include in the global calculations.

4. Manufacturing activity in the US expanded on both measures...   
![](images/fb757cb2f87a5f9fa1ce089e2b53daa8ddd85359580f494554b9d56415fb0998.jpg)

<details>
<summary>line</summary>

| Year | ISM Manufacturing | S&P Manufacturing |
|------|-------------------|-------------------|
| 2022 | 57.5              | 59.0              |
| 2023 | 47.5              | 47.0              |
| 2024 | 50.0              | 52.5              |
| 2025 | 48.0              | 53.0              |
| 2026 | 54.0              | 55.0              |
</details>

Source: S&P Global, Macrobond.

6. Some of the strength in new orders could reflect frontloading...   
![](images/898f648fbd5296746872431fb83ffc44e5c866b4de19c73492a337c0a3a17f00.jpg)

<details>
<summary>line</summary>

| Year | Value (pts) |
|------|-------------|
| 2022 | -13         |
| 2023 | -14         |
| 2024 | -9          |
| 2025 | -7          |
| 2026 | -7          |
</details>

Source: S&P Global, Macrobond. Note: The vertical line reflects the Liberation Day tariff disruption

3. ...although partly due to stockpiling and longer delivery times   
![](images/a3c365c9ba2c0d8abd8d43785b194bd96a5e6b6494225a9d6b9bf7ca81644674.jpg)

<details>
<summary>line</summary>

| Year | Suppliers' Delivery Times Index | Stocks of Purchases Index | Quantity of Purchases Index |
|------|----------------------------------|---------------------------|-----------------------------|
| 2022 | 38.0                             | 51.0                      | 53.0                        |
| 2023 | 49.0                             | 50.0                      | 47.0                        |
| 2024 | 49.5                             | 50.5                      | 49.0                        |
| 2025 | 49.0                             | 50.0                      | 51.0                        |
| 2026 | 45.0                             | 51.0                      | 53.0                        |
</details>

Source: S&P Global, Macrobond. Note: due to a later-than-usual release date, May readings for Greece, Indonesia, Ireland, Malaysia, Pakistan, Romania, and Thailand were not available to include in the global calculations.

5. ...but price pressure remains elevated   
![](images/4217adac767ac1f63be5af70ca60b18ecfefa4dbf268cfbea46984b8c152a215.jpg)

<details>
<summary>line</summary>

| Year | ISM prices | S&P input prices | S&P output prices |
|------|------------|------------------|-------------------|
| 2022 | 85         | 80               | 75                |
| 2023 | 40         | 55               | 50                |
| 2024 | 60         | 65               | 60                |
| 2025 | 70         | 75               | 65                |
| 2026 | 85         | 80               | 70                |
</details>

Source: S&P Global, Macrobond

7. ...as stocks of purchases increased, indicating inventory buildup   
![](images/e022e9c0e17b85199aeb036e59c001a6c4786de631c4359ca471bbd325e15053.jpg)

<details>
<summary>line</summary>

| Year | India | UK  | US  | Mainland China |
|------|-------|-----|-----|----------------|
| 2022 | 57.5  | 55.0| 57.5| 50.0           |
| 2023 | 62.5  | 45.0| 47.5| 50.0           |
| 2024 | 60.0  | 47.5| 50.0| 50.0           |
| 2025 | 62.5  | 45.0| 57.5| 50.0           |
| 2026 | 57.5  | 52.5| 50.0| 50.0           |
</details>

Source: Rating Dog, S&P, Macrobond

8. Manufacturing activity slowed in France and Germany   
![](images/749dd1d4e9073c0d0fcecbcf61218b43c1eae6435f20e2f2e01552f9db02f4ad.jpg)

<details>
<summary>line</summary>

| Year | France | Germany |
|------|--------|---------|
| 2022 | 55.0   | 55.0    |
| 2023 | 48.0   | 40.0    |
| 2024 | 45.0   | 45.0    |
| 2025 | 50.0   | 50.0    |
| 2026 | 52.5   | 52.5    |
</details>

Source: S&P Global, Macrobond.

9. PMIs in the Middle East recovered to some extent in May   
![](images/b27607be34e3b909771e2d936a3919a00b59ef783378b87e3d47c6dd6c07044e.jpg)

<details>
<summary>line</summary>

| Year | Egypt | Kuwait | United Arab Emirates | Saudi Arabia | Qatar |
|------|-------|--------|----------------------|--------------|-------|
| 2022 | 46    | 54     | 58                   | 58           | 66    |
| 2023 | 49    | 56     | 58                   | 58           | 54    |
| 2024 | 50    | 54     | 58                   | 58           | 54    |
| 2025 | 50    | 54     | 58                   | 58           | 54    |
| 2026 | 46    | 54     | 58                   | 58           | 38    |
</details>

Source: S&P Global, Macrobond. Note: Whole economy PMI

10. Employment data suggest a cautious outlook for the manufacturing sector   
![](images/d64f92e9fae2aad12ec1f01e26651341367eaaa3ff5b88635a36a441e7c13932.jpg)

<details>
<summary>bar</summary>

| Country/Region       | 1m ago | Latest |
|----------------------|--------|--------|
| South Korea          |        | 53.5   |
| Japan                |        | 53.0   |
| India                |        | 53.0   |
| UK                   |        | 51.5   |
| US                   |        | 51.0   |
| Brazil               |        | 53.5   |
| Canada               |        | 51.0   |
| Italy                |        | 52.0   |
| Australia            |        | 49.0   |
| Thailand             |        | 50.0   |
| Switzerland          |        | 49.0   |
| Malaysia             |        | 51.5   |
| Taiwan               |        | 50.0   |
| Mainland China       |        | 50.0   |
| Vietnam              |        | 49.5   |
| Spain                |        | 49.0   |
| Indonesia            |        | 49.5   |
| Philippines          |        | 49.0   |
| France               |        | 48.5   |
| Türkiye              |        | 48.0   |
| Euro Area            |        | 47.5   |
| Poland               |        | 46.0   |
| Russia               |        | 46.5   |
| Mexico               |        | 47.0   |
| Germany              |        | 44.5   |
</details>

Source: S&P Global, Macrobond

11. Longer supplier delivery times boost the headline data due to methodological quirks   
![](images/7fc42745598b988331bde7085925beee5a892103aa6ec3fa73d8e8cf9c420e6f.jpg)

<details>
<summary>bar</summary>

| Country/Region       | Headline excluding delivery times component | Change |
|----------------------|---------------------------------------------|--------|
| South Korea          | 3.0                                         | 4.0    |
| US                   | 3.5                                         | 4.0    |
| Mexico               | 2.8                                         | 3.0    |
| Poland               | 2.0                                         | 2.5    |
| Italy                

[中间内容因长度限制已省略]

, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Securities and Capital Markets (India) Private Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Securities and Capital Markets (India) Private Limited.

# Global Economics Research Team

# Global

Global Chief Economist

Janet Henry +44 20 7991 6711

janet.henry@hsbcib.com

Global Economist

James Pomeroy +44 20 7991 6714

james.pomeroy@hsbc.com

Global Economist

Bethan Ellis +44 20 7991 6714

bethan.ellis@hsbc.com

Trade Economist

Shanella Rajanayagam +44 20 3268 4118

shanella.l.rajanayagam@hsbc.com

# Europe

Chief European Economist

Simon Wells +44 20 7991 6718

simon.wells@hsbcib.com

Senior Economist

Chris Hare +44 20 7991 2995

chris.hare@hsbc.com

# United Kingdom

Senior Economist, UK

Elizabeth Martins +44 20 7991 2170

liz.martins@hsbc.com

UK Economist

Emma Wilks + 44 20 3268 5948

emma.wilks@hsbc.com

# Germany

Stefan Schilbe +49 211 910 3137

stefan.schilbe@hsbc.de

Anja Sabine Heimann +44 738 724 7457

anja.sabine.heimann@hsbc.com

# France

Chantana Sam +33 1 4070 7795

chantana.sam@hsbc.fr

# North America

# US

Ryan Wang +1 212 525 3181

ryan.wang@us.hsbc.com

# Asia Pacific

Co-Head of Global Research, Asia-Pacific

and Co-Head of Asian Economics Research

Frederic Neumann +852 2822 4556

fredericneumann@hsbc.com.hk

Chief Economist, Australia, New Zealand and

Global Commodities

Paul Bloxham +612 9255 2635

paulbloxham@hsbc.com.au

Chief Economist, India and Indonesia

Pranjul Bhandari +65 6658 4976

pranjul.bhandari@hsbc.com.sg

Jamie Culling +612 9006 5042

jamie.culling@hsbc.com.au

Jing Liu +852 3941 0063

jing.econ.liu@hsbc.com.hk

Ines Lam +852 2288 7131

ines.y.k.lam@hsbc.com.hk

Yun Liu + 852 2822 4297

yun.liu@hsbc.com.hk

Aayushi Chaudhary +91 22 2268 5543

aayushi.b.chaudhary@hsbc.co.in

Maitreyi Das +91 80 6737 3155

maitreyi.das@hsbc.co.in

Erin Xin +852 2996 6975

erin.y.xin@hsbc.com.hk

Aris Dacanay +852 3945 1247

aris.dacanay@hsbc.com.hk

Jin Choi +852 2996 6597

jin.h.j.choi@hsbc.com.hk

Akiko Kitamura +852 2996 6676

akiko.kitamura@hsbc.com.hk

Justin Feng +852 2288 7108

justin.feng@hsbc.com.hk

Taylor Wang +852 2288 8650

taylor.t.l.wang@hsbc.com.hk

Priya Mehrishi +91 97 3916 9567

priya.mehrishi@hsbc.co.in

# CEEMEA

Chief Economist, CEEMEA

Simon Williams +971 50 9143382

simon.williams@hsbc.com

Senior Economist, Central & Eastern

Europe

Agata Urbanska-Giner +44 20 7992 2774

agata.urbanska@hsbcib.com

Senior Economist, CEEMEA

Melis Metiner +44 20 3359 2636

melismetiner@hsbcib.com

Senior Economist, South Africa

Hugo Pienaar +44 20 7718 9563

hugo.pienaar@hsbc.com

# Latin America

Chief Economist, Mexico

Jose Carlos Sanchez +52 55 5721 5623

jose.c.sanchez@hsbc.com.mx

Allison Buck +1 212 525 4119

allison.buck@us.hsbc.com

Head of Brazil Economics Research

Daniel Lavarda +55 11 2802 2640

daniel.lavarda@hsbc.com
"""
