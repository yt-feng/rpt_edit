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
# China alt-data trackers chartpack (Series 57)

Exports still the bright spot, oil supply recovery limited

April domestic activity weakness tilted 2Q growth risks to the downside. Incoming May data have been mixed, with trade beating expectations but credit demand remaining soft. May–June data will be key to recalibrating 2Q growth momentum. While we await May domestic hard-activity indicators, we update our alt-data trackers (vs. our last update) and our key takeaways are below.

- Exports: Port tracking shows departing container (+8.9%) and bulk (+10.8) shipping deadweight tonnage both increased m/m nsa mtd in June. Annual growth held up further. In aggregate, departing shipments deadweight tonnage (excluding tankers) rose 17.9% oya mtd in June (vs. 7.7% in May), suggesting volume growth is picking-up alongside recent price gains. Oil tanker arrivals remained subdued mtd in June, at a similar level to May.  
- CCFI to USEC, USWC rose 6.5%, 9.1%, respectively, compared to two weeks ago; CCFI to the Persian Gulf/Red Sea route increased by another 8.6%.  
China's domestic and int'l flight cancelation rate remained elevated.  
Production: Processed crude oil production contraction may have deepened in May, with further decline in June (vs -5.8% oya in April) as petroleum asphalt plants' operating rates declined further. Auto IP growth may have improved modestly in May, with a slowdown in June (vs -2.6% oya in Apr). Steel IP contraction may have deepened in May but may narrow in June (vs -1.7% oya in Apr). Coke oven plants ticked down mtd in June.  
- Fiscal: Government bond issuance moderated to 616bn yuan in June mtd (vs. 1140bn yuan in May). CGB issuance slipped to 164bn yuan while special LGB issuance picked up only modestly to 212bn yuan. Absent a month-end jump, fiscal delivery will remain less front-loaded by June. If domestic demand weakness persists, we expect an acceleration in government bond issuance and fund deployment in 3Q.  
- Monetary: PBOC net injected 410bn yuan of liquidity via pledged OMO in June mtd, while it withdrew 300bn yuan via outright OMO. A cut could become more likely in 2H if growth headwinds intensify and outweigh inflation risks.  
- Auto sales remained a drag on retail sales. Passenger car retail sales fell 22% oya in May, partially on lower per-car trade-in subsidies and purchase tax exemptions, and higher fuel costs. NEV sales fell a narrower 7.5%. In the first week of June, passenger car sales fell 23% oya and NEV sales fell 14%.  
- Housing: Home sales in both new and secondary home markets outperformed the same period last year in June mtd, with some momentum easing lately. Uncertainty remains over whether this marks a housing market bottoming-out.  
- Inflation: Gasoline, diesel and LPG prices continued to moderate in the first ten days of June, while LNG prices ticked up mildly. Coal prices rose further to the highest level in nearly 20 months, also on summer seasonal demand. Some petrochemical products moderated from recent peaks, while sulfuric acid stayed elevated. Agricultural food prices fell $0.1\%$ oya in June mtd, narrowing the drag on headline CPI. Pork wholesale prices contraction remained elevated, as overcapacity in the industry prolongs.

## Emerging Markets Asia, Economic and Policy Research

## Tingting Ge

(852) 2800-0143

tingting.ge@JPM.com

## Jiayi Li

(852) 2800-5229

jiayi.c.li@JPM.com

## Tongfang Yuan

(852) 2800-0085

tongfang.yuan@JPM.com

## Feng Zhu

(852) 2800 1745

feng.zhu@JPM.com

JPM Chase Bank, N.A., Hong Kong Branch

## 1. Mapping: High-frequency trackers --> official activity

Regarding the mapping efforts from high-frequency data to monthly official activity tracking:

- Operating rates for petroleum asphalt plants suggest processed crude oil production contraction may have deepened in May, with further decline in June (vs -5.8% oya in April).  
- Operating rates for tire plants suggest auto IP growth may have improved modestly in May, followed by slowdown in June (vs -2.6% oya in Apr).  
- Operating rates for steel rebar suggest that steel IP contraction may have deepened in May but may narrow in June (vs -1.7% oya in Apr).  
- Housing transactions for 30 major cities gained $4.0\%$ oya mtd in June (vs $-1.4\%$ in May).  
- Port tracking shows that departing container and bulk shipping deadweight tonnage both increased m/m nsa, mtd in June. Over-year-ago growth mtd also improved. In aggregate, departing shipments deadweight tonnage (excluding tankers) rose 17.9% oya mtd in June (vs. 7.7% in May).

Figure 1.1: Industrial production - Processed crude oil  
![](images/7f52b58a20c6351bb25e541d88e7847e889235f0c1c49feb8d54fe7ad44392ac.jpg)

<details>
<summary>line chart</summary>

| Year | Weekly tracking (operating rate) 1/ | Monthly from the NBS (RHS) |
|------|-------------------------------------|----------------------------|
| 17   | ~-10                                | ~5                         |
| 18   | ~-30                                | ~10                        |
| 19   | ~-40                                | ~5                         |
| 20   | ~-20                                | ~15                        |
| 21   | ~50                                 | ~20                        |
| 22   | ~-50                                | ~-10                       |
| 23   | ~-30                                | ~15                        |
| 24   | ~-20                                | ~5                         |
| 25   | ~-10                                | ~0                         |
| 26   | ~-50                                | ~-10                       |
</details>

Source: CEIC, Wind, JPM; 1/ Latest for June 2026.

Figure 1.2: Industrial production - Auto  
![](images/024c6a9096c49b7723afe97ff5d508197864f7987c78412552b0d0b757dd1636.jpg)

<details>
<summary>line chart</summary>

| Year | Monthly from NBS | Weekly tracking (full-steel tire) 1/ |
|------|------------------|--------------------------------------|
| 17   | ~10              | ~40                                  |
| 18   | ~0               | ~0                                   |
| 19   | ~-10             | ~-10                                 |
| 20   | ~-50             | ~-50                                 |
| 21   | ~75              | ~50                                  |
| 22   | ~-30             | ~-30                                 |
| 23   | ~60              | ~25                                  |
| 24   | ~-10             | ~-10                                 |
| 25   | ~10              | ~0                                   |
| 26   | ~-10             | ~-10                                 |
</details>

Source: CEIC, Wind, JPM; 1/ Latest for June 2026.

Figure 1.3: Industrial production - Steel  
![](images/d2b5320c11b53045ec1bbbb074ddbab753488f173c073c9abdc387508d5f8c83.jpg)

<details>
<summary>line chart</summary>

| Year | Weekly tracking (operating rate) 1/ (%) | Monthly from the NBS (RHS) (%) |
|------|------------------------------------------|---------------------------------|
| 17   | -20                                      | 0                               |
| 18   | 15                                       | 5                               |
| 19   | 5                                        | 10                              |
| 20   | -10                                      | 5                               |
| 21   | 20                                       | 25                              |
| 22   | -30                                      | -10                             |
| 23   | -10                                      | 10                              |
| 24   | 5                                        | 5                               |
| 25   | -20                                      | 0                               |
| 26   | -5                                       | -5                              |
</details>

Source: CEIC, Wind, JPM; 1/ Latest for June 2026.

Figure 1.4: China exports  
![](images/fdaee79ee11b476bb7c3eacedfa16ec977927751ed057cbd21c9407e2069b035.jpg)

<details>
<summary>line chart</summary>

| Year | Export volume from China Customs (%) | Deadweight daily tracking of departing ships (lhs) 1/ (%) |
|------|----------------------------------------|----------------------------------------------------------|
| 2020 | -15                                    | 15                                                       |
| 2021 | 50                                     | 18                                                       |
| 2022 | -5                                     | -15                                                      |
| 2023 | -10                                    | 10                                                       |
| 2024 | 20                                     | 5                                                        |
| 2025 | 15                                     | -5                                                       |
| 2026 | 45                                     | 10                                                       |
</details>

Source: Elane Shipping, China Customs, JPM; 1/ Latest for June 2026, excl. tankers

## 2. Trade

China's outbound container costs rose further across major routes. By destination, CCFI to USEC, USWC rose $6.5\%$ , $9.1\%$ , respectively, compared to two weeks ago; CCFI to the Persian Gulf/Red Sea route increased by another $8.6\%$ . Baltic Dry Index ticked down after several weeks of increases since April. US-bound shipping edged up $0.4\%$ oya or rose $7.1\%$ m/m nsa mtd in June (vs $27.8\%$ oya or $2.9\%$ m/m nsa in May).

\- Container ships usually carry consumer goods, as well as some machinery equipment and electronics. Departing container ships' deadweight tonnage rose 5.0% oya or 8.9% m/m nsa mtd in June. Arriving container ships' deadweight tonnage fell 1.3% oya or up 5.7% m/m nsa.

- Bulk carriers transport unpackaged bulk cargo for grain, coal, iron ore, steel, etc., in their cargo holds. Departing bulk ships' deadweight tonnage rose 21.7% oya mtd (or 10.8%m/m nsa), while arriving bulk ships' deadweight tonnage rose 24.3% oya or 8.8%m/m nsa.  
- Oil tanker arrivals remained subdued mtd in June, at a similar level to May.

China's domestic and international flight cancelation rates remained elevated mtd in June at above $25\%$ and $20\%$ , respectively, partly due to still high jet fuel costs and airfares. Flight execution edged lower in June.

China's soybean imports increased in May, following seasonal trend. Purchases from the US have been rising. The Ministry of Commerce confirmed the agreement with the US to purchase 200 Boeing aircraft, as well as engines and spare parts. The White House statement said China would purchase at least US\$17bn US agricultural products annually from 2026 to 2028.

![](images/80a4027e9172eb3183ea01a55c15bd71774a091040abe364a66017963dcf1b97.jpg)

<details>
<summary>line chart</summary>

| Date   | Mediterranean | USEC  | USWC  | Europe | Red Sea | South America |
|--------|--------------|-------|-------|--------|---------|---------------|
| Jan 24 | 3,000        | 1,000 | 800   | 2,500  | 1,500   | 700           |
| May 24 | 3,500        | 1,200 | 900   | 3,000  | 2,000   | 800           |
| Sep 24 | 3,800        | 1,500 | 1,000 | 3,500  | 2,500   | 900           |
| Jan 25 | 3,200        | 1,300 | 950   | 3,200  | 2,200   | 850           |
| May 25 | 2,800        | 1,100 | 850   | 2,800  | 2,000   | 750           |
| Sep 25 | 2,500        | 1,000 | 800   | 2,500  | 1,800   | 700           |
| Jan 26 | 2,200        | 950   | 750   | 2,200  | 1,600   | 650           |
| May 26 | 2,800        | 1,100 | 850   | 2,800  | 2,500   | 750           |
</details>

Source: Wind, JPM

Figure 2.3: Deadweight tonnage of departing ships - Container  
![](images/d92d4cbb1994ade8e5cafe9de2e35eebedd9120a97a09b5f6c54b024fc491972.jpg)

<details>
<summary>line chart</summary>

| Month | 19-24 range | 19-24 avg. | 2025 | 2026 |
|-------|-------------|------------|------|------|
| Jan   | ~0.8        | ~0.7       | ~0.9 | ~1.2 |
| Feb   | ~0.7        | ~0.6       | ~0.8 | ~1.0 |
| Mar   | ~0.6        | ~0.6       | ~0.7 | ~0.8 |
| Apr   | ~0.7        | ~0.7       | ~0.9 | ~1.0 |
| May   | ~0.8        | ~0.7       | ~1.0 | ~1.1 |
| Jun   | ~0.8        | ~0.7       | ~1.0 | ~1.1 |
| Jul   | ~0.8        | ~0.7       | ~1.0 | ~1.0 |
| Aug   | ~0.7        | ~0.6       | ~0.9 | ~0.9 |
| Sep   | ~0.7        | ~0.6       | ~1.0 | ~1.0 |
| Oct   | ~0.7        | ~0.6       | ~1.0 | ~1.0 |
| Nov   | ~0.7        | ~0.6       | ~1.1 | ~1.1 |
| Dec   | ~0.7        | ~0.6       | ~1.0 | ~1.0 |
</details>

Source: Elane Shipping Statistics, JPM.

Figure 2.5: Deadweight tonnage of departing ships - Bulk  
![](images/c4a4b1c762de24ad023c3c08abc9a6d58173b0bafdde8287f6200dee705f7989.jpg)

<details>
<summary>line chart</summary>

| Month | 19-24 range | 19-24 ave. | 2025 | 2026 |
|-------|-------------|------------|------|------|
| Jan   | ~8.5        | ~9.5       | ~8.5 | ~8.5 |
| Feb   | ~8.5        | ~9.0       | ~7.0 | ~10.5 |
| Mar   | ~8.5        | ~8.5       | ~8.0 | ~9.5 |
| Apr   | ~8.5        | ~8.5       | ~9.0 | ~11.0 |
| May   | ~8.5        | ~8.5       | ~9.5 | ~10.5 |
| Jun   | ~8.5        | ~8.5       | ~9.5 | ~12.0 |
| Jul   | ~8.5        | ~8.5       | ~9.5 | ~11.5 |
| Aug   | ~8.5        | ~8.5       | ~9.5 | ~10.5 |
| Sep   | ~8.5        | ~8.5       | ~9.5 | ~10.0 |
| Oct   | ~8.5        | ~8.5       | ~9.5 | ~10.0 |
| Nov   | ~8.5        | ~8.5       | ~9.5 | ~10.0 |
| Dec   | ~8.5        | ~8.5       | ~9.5 | ~10.0 |
</details>

Source: Elane Shipping Statistics, JPM.

Figure 2.2: BEISL freight index  
![](images/2b424ff0f294ab90d38ea2b0eecd11a82c3c8ee8a53b2855ab09abf267b287ba.jpg)

<details>
<summary>line chart</summary>

| Year | Baltic Exchange Dry Index | Global Container Freight Index (RHS) |
|------|---------------------------|---------------------------------------|
| 20   | ~500                      | ~1000                                 |
| 21   | ~1500                     | ~3000                                 |
| 22   | ~5500                     | ~10000                                |
| 23   | ~1000                     | ~2000                                 |
| 24   | ~3500                     | ~4000                                 |
| 25   | ~1500                     | ~3000                                 |
| 26   | ~3000                     | ~2000                                 |
</details>

Source: Baltic Exchange Information Services Limited, JPM

Figure 2.4: Deadweight tonnage of arrived ships - Container  
![](images/c6948b851c712071c919c82882dea828a68dc2a899b1b3f389e26307101ebcd1.jpg)

<details>
<summary>line chart</summary>

| Month | 19-24 range | 19-24 ave. | 2025 | 2026 |
|-------|-------------|------------|------|------|
| Jan   | ~0.8        | ~0.75      | ~0.9 | ~0.95 |
| Feb   | ~0.7        | ~0.7       | ~0.8 | ~0.95 |
| Mar   | ~0.6        | ~0.65      | ~0.7 | ~0.8 |
| Apr   | ~0.7        | ~0.75      | ~0.85| ~0.9 |
| May   | ~0.75       | ~0.75      | ~0.9 | ~0.95|
| Jun   | ~0.8        | ~0.75      | ~0.95| ~1.0 |
| Jul   | ~0.8        | ~0.75      | ~1.0 | ~1.0 |
| Aug   | ~0.75       | ~0.75      | ~0.95| ~0.95|
| Sep   | ~0.7        | ~0.75      | ~0.9 | ~0.95|
| Oct   | ~0.7        | ~0.75      | ~1.05| ~1.05|
| Nov   | ~0.7        | ~0.75      | ~1.05| ~1.05|
| Dec   | ~0.7        | ~0.75      | ~0.95| ~0.95|
</details>

Source: Elane Shipping Statistics, JPM.

Figure 2.6: Deadweight tonnage of arrived ships - Bulk  
![](images/255c5e021cd3eac15ad1e31880dbae53f5b7eaea5210fcaacdb18ad58176936b.jpg)

<details>
<summary>line chart</summary>

| Month | 19-24 range | 19-24 ave. | 2025 | 2026 |
|------

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 16 Jun 2026 01:55 AM HKT

Disseminated 16 Jun 2026 01:55 AM HKT
"""
