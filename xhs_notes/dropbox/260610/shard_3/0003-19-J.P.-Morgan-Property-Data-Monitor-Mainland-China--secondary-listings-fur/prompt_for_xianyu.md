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
# Property Data Monitor

Mainland China: secondary listings further dropped in May; HK: home prices have risen 9.6% YTD

## Mainland China

- Secondary listings in tier-1 cities fell 0.7% M/M in May (Figure 7). The implied inventory months (based on 12-month rolling sales volume) marginally fell from 18.8 months in April to 18.6 months. Beijing saw the largest M/M decline of 2%, with inventory months falling to 16.6 (Apr: 17.1), followed by Shanghai (-1%) (inventory months: 11.9 in May vs. 12.4 in April).  
- 60-city primary sales registrations rose $18\%$ Y/Y (last week: $+10\%$ ) (more).  
- 12-city secondary sales registrations rose 38% Y/Y (last week: +14% (Figure 5), Shanghai (+57%) and Shenzhen (+55%) saw the strongest Y/Y growth among tier-1 cities. YTD, 12-city secondary sales have risen 6% Y/Y (Shanghai: +14%).  
- Leading indicator #1) The Centaline tier-1 cities' secondary asking price index stayed flat at 17.7 (Figure 1).  
- Leading indicator #2) The Centaline manager confidence index stayed flat W/W at 54 (Figure 2).  
- Southbound holdings rose 0.54% W/W (Table 5): CRL +1.4%; C&D & Country Garden +1.3%; COLI +1.1%.  
- Share price moves (Figure 15): The sector fell 6% last week, mildly underperforming the HSI (-5%). The outperformers were CG Services and Longfor (both +0%). The underperformer was Shimao (-18%).  
- JPM top picks: COLI (more in A laggard poised to outperform), CR Land, Jinmao and CR Mixc.

## Hong Kong SAR

- Primary projects continue to price at a premium: Three primary projects released price lists last week: (1) Headland Residences (by Swire Prop/CMB; in Chai Wan) released a new batch (78 units) at HK\$17.3K psf, 1% lower than the last batch in Sep 2025, but 15% higher than secondary. The batch will be launched for sale on 9 June (Tuesday); (2) One Victoria Cove Ph4 (led by Henderson; in Hung Hom) released the $1^{st}$ price list (60 units) at HK \$21.3K psf, 2% lower than the first batch of Ph3 in May, but 18% higher than secondary; (3) Pavilia Rosa (by NWD; in Kowloon Tong) released the $1^{st}$ price list (44 units) at HK\$33.8K psf, 41% higher than secondary, marking the highest primary ASP (by price list) over the past 5 years. The project will launch 28 units for sale on 12 June (Friday).  
- The home price index rose 0.3% W/W (Figure 11). Home prices have risen 9.6% YTD and are just 0.4% away from reaching our 2026 home price forecast of 10-15%.  
- Secondary transactions in the top 35 estates totaled 59 units, -19% W/W or -32% Y/Y (Figure 10), the lowest since CNY (partially due to adverse

## Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC

(852) 2800-8513

karl.chan@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Venus Choi

(852) 2800-8599

venus.choi@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Jocelyn Gao

(852) 2800-8529

jocelyn.gao@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## APAC Credit Research

Alvin Au AC

(852) 2800-8533

alvin.au@JPM.com

JPM Securities (Asia Pacific) Limited

Soo Chong Lim

(852) 2800-7387

soochong.lim@JPM.com

JPM Securities (Asia Pacific) Limited

Shirley Yau

(852) 2800-0566

shirley.yau@JPM.com

JPM Securities (Asia Pacific) Limited

weather).

- The Centa Valuation Index (CVI) (Figure 12) stayed elevated at 86.7 (last week: 89.5). This is a leading indicator that home price growth may continue (a reading of >60 = banks revising up property valuations).  
- The Centa Salesman Index (CSI) (Figure 13) mildly rose from 70.6 last week to 71.1. A reading of $>50 =$ sentiment is positive and property prices are likely to rise.  
- Southbound holdings fell 0.09% W/W (Table 5): Hang Lung Prop +0.1%; CK Asset -0.4%.  
- Share price moves (Figure 16): The sector fell 6% last week, mildly underperforming the HSI (-5%), due to concerns over tighter capital outflow controls in Mainland China (more in our note “Implications of State Council’s Regulations on Outbound Investment”) and a potential rate hike (more in our note “After one overhang, here comes another one”). The outperformer was MTRC (+1%), while Wharf Holdings (-12%) underperformed.  
- JPM top picks: Developers – SHKP & Sino; landlords – Swire Prop & Hang Lung; conglomerates – JM & CKH.

## Credit View (by Alvin Au)

- The JACI China HY Property Index rose 1.3% last week (vs China HY: +0.56%), bringing YTD returns to +6.5%.  
- Seazen: Management noted in our recent meeting that tenant sales have risen by a solid \~8% YTD, and the consumption market in tier 3/4 cities is less competitive and policy-driven than top tier cities. They see Seazen as more competent than Wanda in having a long-term strategy with investment commitment, but see CR Mixc's expansion to low-tier cities as a potential threat. Seazen is developing REITs as a new financing channel, and on DP side it will keep a small team with no land acquisition plans in the near term.  
- Shenzhen Property: Our property expert meeting in SZ last week suggested a polarized housing market in SZ. High-end home sales are robust on the back of positive wealth effect from AI/stock market, but the mid-end segment is weak with some volume recovery on the low-end. Nanshan/Futian are more resilient than other SZ districts, and home buyers are still open to buying Vanke properties as they are co-managed by SOEs. The local gov't is hesitant in purchasing unsold inventories due to fiscal constraints, and the expert does not see material impact from the recent capital control tightening on Mainland Chinese's buying of HK homes.  
JPM top picks: LNGFOR '29s (84 offer, 9.8% ytm) and SHUION '29s (101.5 offer, 9.1% ytm).

## Table Of Contents

Mainland China.... 1

Hong Kong SAR 1

Credit views (by Alvin Au) 2

1. Mainland China – Leading indicators.... 4  
2. Mainland China – Weekly Primary Sales 5  
3. Mainland China – Weekly Secondary Sales.... 7  
4. Hong Kong – Residential Market Update 9  
5. Hong Kong – Tourist Arrivals & Resident Departures..... 12  
6. Share price update 13  
7. Credit recommendations .... 17  
8. Equity valuation summary ...... 18

## 1. Mainland China – Leading indicators

Figure 1: Centraline secondary asking price index vs. NBS secondary home price index M/M in tier-1 cities  
![](images/f6c77bf9f36234ca805ad98c7baa1ec8b73d8f457e9ad58e82aad7a36513e2d3.jpg)

<details>
<summary>line chart</summary>

| Date     | Tier-1 cities' secondary asking price index | Tier-1 cities' secondary home price M/M change |
|----------|---------------------------------------------|--------------------------------------------------|
| May-23   | ~28                                         | ~0.0%                                            |
| Jun-23   | ~25                                         | ~0.0%                                            |
| Jul-23   | ~23                                         | ~0.0%                                            |
| Aug-23   | ~28                                         | ~0.0%                                            |
| Sep-23   | ~30                                         | ~0.0%                                            |
| Oct-23   | ~20                                         | ~0.0%                                            |
| Nov-23   | ~18                                         | ~0.0%                                            |
| Dec-23   | ~19                                         | ~0.0%                                            |
| Jan-24   | ~20                                         | ~0.0%                                            |
| Feb-24   | ~25                                         | ~0.0%                                            |
| Mar-24   | ~28                                         | ~0.0%                                            |
| Apr-24   | ~15                                         | ~0.0%                                            |
| May-24   | ~25                                         | ~0.0%                                            |
| Jun-24   | ~26                                         | ~0.0%                                            |
| Jul-24   | ~25                                         | ~0.0%                                            |
| Aug-24   | ~24                                         | ~0.0%                                            |
| Sep-24   | ~23                                         | ~0.0%                                            |
| Oct-24   | ~37                                         | ~0.0%                                            |
| Nov-24   | ~30                                         | ~0.0%                                            |
| Dec-24   | ~28                                         | ~0.0%                                            |
| Jan-25   | ~27                                         | ~0.0%                                            |
| Feb-25   | ~25                                         | ~0.0%                                            |
| Mar-25   | ~23                                         | ~0.0%                                            |
| Apr-25   | ~21                                         | ~0.0%                                            |
| May-25   | ~20                                         | ~0.0%                                            |
| Jun-25   | ~19                                         | ~0.0%                                            |
| Jul-25   | ~18                                         | ~0.0%                                            |
| Aug-25   | ~17                                         | ~0.0%                                            |
| Sep-25   | ~16                                         | ~0.0%                                            |
| Oct-25   | ~15                                         | ~0.0%                                            |
| Nov-25   | ~14                                         | ~0.0%                                            |
| Dec-25   | ~13                                         | ~0.0%                                            |
| Jan-26   | ~14                                         | ~0.0%                                            |
| Feb-26   | ~16                                         | ~0.4%                                            |
| Mar-26   | ~18                                         | ~0.4%                                            |
| Apr-26   | ~19                                         | ~0.4%                                            |
| May-26   | ~17                                         | ~0.4%                                            |
| Jun-26   | ~16                                         | ~0.4%                                            |
</details>

Source: Centraline, Wind, NBS. Note: The asking price index represents the percentage of projects with home price increases. For example, an index of 20 means that 20% of projects raise prices (while 80% do not).

Figure 2: Centraline secondary manager confidence index in tier-1 cities vs. three-month rolling secondary sales  
![](images/b0d1bbff6b18ce4079836c934957aacc490dc11ab27bd08ef3228e476087307e.jpg)

<details>
<summary>line chart</summary>

| Month    | Sales manager confidence index | Sales 3-month rolling Y/Y |
|----------|----------------------------------|---------------------------|
| Jun-21   | 55                               | 0%                        |
| Aug-21   | 40                               | -20%                      |
| Oct-21   | 38                               | -40%                      |
| Dec-21   | 45                               | -20%                      |
| Feb-22   | 50                               | 0%                        |
| Apr-22   | 55                               | 20%                       |
| Jun-22   | 50                               | 0%                        |
| Aug-22   | 55                               | 20%                       |
| Oct-22   | 50                               | 0%                        |
| Dec-22   | 45                               | -20%                      |
| Feb-23   | 65                               | 40%                       |
| Apr-23   | 60                               | 60%                       |
| Jun-23   | 50                               | 40%                       |
| Aug-23   | 45                               | 20%                       |
| Oct-23   | 50                               | 0%                        |
| Dec-23   | 55                               | 20%                       |
| Feb-24   | 50                               | 40%                       |
| Apr-24   | 45                               | 20%                       |
| Jun-24   | 50                               | 0%                        |
| Aug-24   | 55                               | 20%                       |
| Oct-24   | 60                               | 40%                       |
| Dec-24   | 65                               | 60%                       |
| Feb-25   | 60                               | 40%                       |
| Apr-25   | 55                               | 20%                       |
| Jun-25   | 50                               | 0%                        |
| Aug-25   | 45                               | -20%                      |
| Oct-25   | 50                               | -40%                      |
| Dec-25   | 55                               | -60%                      |
| Feb-26   | 60                               | -40%                      |
| Apr-26   | 65                               | -20%                      |
| Jun-26   | 60                               | 0%                        |
</details>

Source: Centraline, Wind. Note: The index surveys managers across the country for their judgment on the market outlook.

## 2. Mainland China – Weekly primary sales

Figure 3: 60-city weekly primary sales registrations – compared with 2019-24  
![](images/ec94e68bb059aa764ce631943bd7b44ec7096f3166145e3f2c35153aa40c1aa6.jpg)

<details>
<summary>line chart</summary>

| Week | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Week 1 | ~35,000 | ~55,000 | ~85,000 | ~50,000 | ~30,000 | ~25,000 | ~20,000 | ~15,000 |
| Week 3 | ~45,000 | ~65,000 | ~75,000 | ~45,000 | ~35,000 | ~30,000 | ~25,000 | ~20,000 |
| Week 5 | ~35,000 | ~55,000 | ~75,000 | ~45,000 | ~35,000 | ~35,000 | ~30,000 | ~25,000 |
| Week 7 | ~15,000 | ~15,000 | ~15,000 | ~15,000 | ~15,000 | ~15,000 | ~15,000 | ~15,000 |
| Week 9 | ~25,000 | ~35,000 | ~45,000 | ~35,000 | ~35,000 | ~35,000 | ~35,000 | ~35,000 |
| Week 11 | ~45,000 | ~55,000 | ~75,000 | ~45,000 | ~45,000 | ~45,000 | ~45,000 | ~45,000 |
| Week 13 | ~65,000 | ~75,000 | ~85,000 | ~65,000 | ~65,000 | ~65,000 | ~65,000 | ~65,000 |
| Week 15 | ~75,000 | ~85,000 | ~95,000 | ~75,000 | ~75,000 | ~75,000 | ~75,000 | ~75,000 |
| Week 17 | ~75,000 | ~85,000 | ~95,000 | ~75,000 | ~75,000 | ~75,000 | ~75,000 | ~75,000 |
| Week 19 | ~75,000 | ~85,000 | ~95,000 | ~75,000 | ~75,000 | ~75,000 | ~75,000 | ~75,000 |
| Week 21 | ~75,000 | ~85,000 | ~95,000 | ~75,000 | ~75,000 | ~75,000 | ~75,000 | ~75,000 |
| Week 23 | ~75,000 | ~85,000 | ~95,000 | ~75,000 | ~75,000 | ~75,000 | ~75,000 | ~75,000 |
</details>

Source: CREIS.

Figure 4: 60-city weekly primary sales registrations  
![](images/80130feb5cc843b79079edd80f1bd94e36393e54dbcad25877307df2cfbaca12.jpg)

<details>
<summary>line chart</summary>

| Date | Sales volume | Y/Y | vs 2018-21 average |
| --- | --- | --- | --- |
| 04-Aug-24 | ~20,000 | ~50% | ~-30% |
| 18-Aug-24 | ~25,000 | ~30% | ~-35% |
| 01-Sep-24 | ~20,000 | ~40% | ~-40% |
| 15-Sep-24 | ~30,000 | ~50% | ~-45% |


[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and

should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 08 Jun 2026 11:18 PM HKT

Disseminated 08 Jun 2026 11:18 PM HKT
"""
