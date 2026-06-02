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
# China Metals Activity Tracker

Copper consumption slows, aluminum picks up. Mysteel analysis of China's new rules for steel capacity replacement

We present our high-frequency inventory trends for base metals, steel and iron ore in China for the week ended 29 May'26. Our data plots China weekly metals inventory trends, a proxy for consumption. Copper recorded a fifth consecutive week of weak destocking (-3kt); although this marks a slowdown vs exceptionally strong consumption across March-April, slower destocking is consistent with normal seasonality. Aluminum shows greater momentum and has moved into a destocking phase (-16kt), albeit running slightly slower vs normal seasonality. Despite slower copper consumption, China's total copper inventories remain low vs historic seasonality at just \~200kt. Conversely, total aluminium inventories are significantly above historic seasonality and very high at 1.4Mt.

Most noteworthy from Mysteel's weekly data, is a $\sim 19\%$ increase in weekly global iron ore shipments (+6Mt), and $\sim 19\%$ increase YoY, with Australia $+20\%$ WoW and Brazil $+30\%$ WoW. Mysteel report flat iron ore volumes at China ports (171Mt).

Weak metals drawdowns suggest slowing China metals consumption, after an exceptionally strong reopening post China New Year. JPM China Economists noted last week that China's April fiscal expenditure saw a decline in fixed asset investments (-18.6% YoY in infrastructure), but weaker growth data may imply additional fiscal support in H2'26 (link). China PMI for May declined to 50.0 (JPMe 50.1) from 50.3, with exports dropping to 48.6 (link). China's Steel PMI declined to 47.9 from 49.2 in April.

Mysteel provide an interpretation of the Ministry of Industry and Information Technology's recent new measures governing capacity additions for China's steel industry. The new rules break from previous regionally differentiated standards by raising the national replacement ratio for pig iron and crude steel capacity uniformly to no less than 1.5:1. This means that for every tonne of new capacity built, 1.5 tonnes of old capacity must be eliminated. In order to encourage substantive M&A, the rules specify a favorable replacement ratio of 1.25:1 for M&A. Green and high-end projects such as hydrogen-based metallurgy and EAFs are allowed to replace capacity on 1:1 basis. Stainless steel induction furnaces are brought under supervision to prevent disguised capacity expansion. The new rules establish a two-year transition period during which cross-enterprise and cross-group transfers of capacity quotas remain permitted in order to preserve market stability.

Mysteel estimate that the nationally uniform 1.5:1 reduction replacement, combined with the elimination of zombie capacity, means that after 2027 there will be virtually no new capacity additions. That the industry will shift to net reductions in crude steel capacity. The supply-demand balance will tighten, providing stronger floor support for steel prices and improving the stability of industry profitability, thereby easing the problem of low-price involution.

![](images/94fda53e83371e636fb6e4c11ec42015fbf97816aa1e2d78a72b4de422ca6e60.jpg)

JPM Data Insights

# European Metals, Mining & Steel

# Dominic O'Kane AC

(44-20) 7742-6729

dominic.j.okane@JPM.com

JPM Securities plc

# Patrick Jones

(44-20) 7742-5964

patrick.jones@JPM.com

JPM Securities plc

# Asia Pacific Basic Materials

# Lyndon Fagan

(61-2) 9003-8648

lyndon.fagan@JPM.com

JPM Securities Australia Limited

# North America Metals, Mining & Clean Tech

# Bill Peterson

(1-415) 315-6766

bill.peterson@jpmchase.com

JPM Securities LLC

# Global Commodities Research

# Gregory C. Shearer

(44-20) 7134-8161

gregory.c.shearer@JPM.com

JPM Securities plc

We provide our latest EMEA Metals & Mining valuations and commodity price scenario analysis (here).

Table 1: China iron ore shipment & steel production data - week ended 29 $^{th}$ May 

<table><tr><td></td><td></td><td>29/05/2026</td><td>22/05/2026</td><td>WoW %</td><td>29/05/2025</td><td>YoY %</td></tr><tr><td>Iron ore arrivals in China of 47 ports</td><td>Mt</td><td>26.05</td><td>28.30</td><td>-8.0%</td><td>23.44</td><td>11.1%</td></tr><tr><td>Australia iron ore shipments</td><td>Mt</td><td>21.46</td><td>17.90</td><td>19.9%</td><td>19.71</td><td>8.9%</td></tr><tr><td>Brazil iron ore shipments</td><td>Mt</td><td>9.16</td><td>7.04</td><td>30.1%</td><td>7.58</td><td>20.8%</td></tr><tr><td>Global iron ore shipments</td><td>Mt</td><td>38.02</td><td>32.06</td><td>18.6%</td><td>31.89</td><td>19.2%</td></tr><tr><td>Tubarão–Qingdao freight rate</td><td>$/t</td><td>37.4</td><td>36.1</td><td>3.6%</td><td>19.9</td><td>87.9%</td></tr><tr><td>Hedland–Qingdao freight rate</td><td>$/t</td><td>16.2</td><td>15.5</td><td>4.5%</td><td>8.6</td><td>88.4%</td></tr><tr><td>Weekly China steel production</td><td>Mt</td><td>8.64</td><td>8.62</td><td>0.2%</td><td>8.81</td><td>-1.9%</td></tr><tr><td>Weekly China steel apparent consumption</td><td>Mt</td><td>8.76</td><td>8.81</td><td>-0.6%</td><td>9.14</td><td>-4.2%</td></tr><tr><td>Weekly rebar apparent consumption</td><td>Mt</td><td>2.32</td><td>2.42</td><td>-4.1%</td><td>2.49</td><td>-6.8%</td></tr><tr><td>Weekly HRC apparent consumption</td><td>Mt</td><td>2.94</td><td>2.98</td><td>-1.3%</td><td>3.27</td><td>-10.1%</td></tr><tr><td>Total China steel inventory</td><td>Mt</td><td>15.44</td><td>15.57</td><td>-0.8%</td><td>13.66</td><td>13.0%</td></tr><tr><td>BF Capacity Utilisation of 247 steel mills</td><td>%</td><td>90.4%</td><td>90.3%</td><td>0.1%</td><td>90.7%</td><td>-0.3%</td></tr><tr><td>Iron ore portside inventory at 47 ports</td><td>Mt</td><td>171.16</td><td>171.15</td><td>0.0%</td><td>144.70</td><td>18.3%</td></tr></table>

Source: MySteel, JPM estimates.

Figure 1: Weekly change in China visible copper inventory (SHFE + Bonded). Rate of de-stocking has slowed in the last few weeks; inventories -3kt for week ended 29 May'26   
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of copper increase / (decrease)   
![](images/132f985ba58ba1c89d28f019c1255ed5ef4c04853a3ed8c9222dad5615cd62f8.jpg)

<details>
<summary>bar</summary>

| X  | 2026 | 5-yr avg |
|----|------|----------|
| -3 | 10   | 5        |
| -1 | 15   | 10       |
| 2  | 120  | 100      |
| 4  | 30   | 40       |
| 6  | -60  | -5       |
| 8  | -40  | -10      |
| 10 | -45  | -5       |
| 12 | -10  | -5       |
| 14 | 5    | -5       |
| 16 | -5   | -5       |
| 18 | -10  | -15      |
| 20 | -5   | -5       |
| 22 | -5   | -5       |
| 24 | -5   | -5       |
| 26 | -5   | -10      |
| 28 | -5   | -10      |
| 30 | -5   | -15      |
| 32 | -5   | -10      |
| 34 | -5   | 5        |
| 36 | -5   | -10      |
| 38 | -5   | 10       |
| 40 | -5   | -10      |
| 42 | -5   | -5       |
| 44 | -5   | -5       |
| 46 | -5   | 0        |
</details>

\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.   
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

Figure 2: Iron ore bulk shipping costs continue to rise, with latest reported Australia, Brazil & South African rates +50% vs end of February US\$/t   
![](images/41cbd3dd43b13e79c2013ae639d8c5b4e0593f6d5a4be9573837eba0f3a0deb2.jpg)

<details>
<summary>line</summary>

| Month   | West Australia to Qingdao | Tubarao to Qingdao | Saldanha to Beilun |
|---------|----------------------------|---------------------|---------------------|
| Jan-25  | 7                          | 18                  | 13                  |
| Feb-25  | 6                          | 17                  | 12                  |
| Mar-25  | 9                          | 24                  | 16                  |
| Apr-25  | 8                          | 20                  | 18                  |
| May-25  | 7                          | 19                  | 15                  |
| Jun-25  | 8                          | 27                  | 19                  |
| Jul-25  | 6                          | 19                  | 13                  |
| Aug-25  | 10                         | 24                  | 18                  |
| Sep-25  | 10                         | 24                  | 18                  |
| Oct-25  | 10                         | 25                  | 19                  |
| Nov-25  | 10                         | 24                  | 18                  |
| Dec-25  | 12                         | 25                  | 20                  |
| Jan-26  | 8                          | 23                  | 17                  |
| Feb-26  | 9                          | 26                  | 18                  |
| Mar-26  | 10                         | 24                  | 17                  |
| Apr-26  | 13                         | 30                  | 21                  |
| May-26  | 15                         | 37                  | 27                  |
</details>

Source: JPM estimates, Bloomberg Finance L.P.

Figure 3: Australian FOB Iron Ore price now flat vs mid-Feb'26 level   
![](images/96ef88cb0dbfe68ffca1be67550c36620bbf73881a694fd866fc56bd6236086c.jpg)

<details>
<summary>line</summary>

| Date   | CFR - 62% Iron Ore Price | FOB - 62% Iron Ore - Australia |
|--------|--------------------------|-------------------------------|
| Jan-25 | ~92                      | ~85                           |
| Feb-25 | ~98                      | ~90                           |
| Mar-25 | ~97                      | ~82                           |
| Apr-25 | ~93                      | ~81                           |
| May-25 | ~89                      | ~80                           |
| Jun-25 | ~90                      | ~79                           |
| Jul-25 | ~91                      | ~84                           |
| Aug-25 | ~98                      | ~87                           |
| Sep-25 | ~100                     | ~88                           |
| Oct-25 | ~101                     | ~89                           |
| Nov-25 | ~98                      | ~86                           |
| Dec-25 | ~100                     | ~87                           |
| Jan-26 | ~107                     | ~98                           |
| Feb-26 | ~104                     | ~90                           |
| Mar-26 | ~95                      | ~85                           |
| Apr-26 | ~106                     | ~93                           |
| May-26 | ~110                     | ~95                           |
| Jun-26 | ~107                     | ~90                           |
</details>

Source: JPM estimates, Bloomberg Finance L.P.

# China metals inventory channel check – week ended 29 May 2026

JPM is tracking China's metal inventories for potential insights regarding end-consumer demand activity. These high-frequency datapoints provide signals to gauge China metals consumption trends. Rapid pivots in inventory de-stocking volumes (or re-stocking) can potentially provide signals that downstream consumption is improving (or weakening).

The pace of copper consumption in China has continued to slow. Latest data suggests only a small 2.7kt de-stocking in the past week but this is in line vs seasonal average level. Copper inventories in China remain relatively tight (\~220kt) although we note that following three weeks of weaker drawdowns, inventory level has risen back above the level same time last year which was driven by pulling of copper imports into the US on fear of copper tariffs. China, on the other hand, has begun to ramp up aluminium drawdown which de-stocked another 16kt last week. Zinc inventory was broadly flat in the past week, and continues to sit at the top end vs past five years' range.

Figure 4: Weekly change in China visible copper inventory (SHFE + Bonded). Rate of de-stocking has slowed in the last few weeks; inventories declined 2.7kt in week ended 29 May'26   
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of copper increase / (decrease)   
![](images/2f0edcdf48d23482809411b5ea8673ca81f111d745b6541cf7f8d1986f819288.jpg)

<details>
<summary>bar</summary>

| X  | 2026 | 5-yr avg |
|----|------|----------|
| -3 | 10   | 5        |
| -1 | 15   | 10       |
| 2  | 120  | 100      |
| 4  | 30   | 40       |
| 6  | -60  | -5       |
| 8  | -40  | -10      |
| 10 | -45  | -5       |
| 12 | -5   | -5       |
| 14 | 5    | -5       |
| 16 | -5   | -5       |
| 18 | -5   | -10      |
| 20 | -5   | -5       |
| 22 | -5   | -5       |
| 24 | -5   | -5       |
| 26 | -5   | -10      |
| 28 | -5   | -10      |
| 30 | -5   | -20      |
| 32 | -5   | -10      |
| 34 | -5   | 5        |
| 36 | -5   | -10      |
| 38 | -5   | 10       |
| 40 | -5   | -10      |
| 42 | -5   | -5       |
| 44 | -5   | -5       |
| 46 | -5   | 5        |
</details>

\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.   
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

Figure 5: Total China visible copper inventory (SHFE + Bonded) week ended 29 May'26. Copper inventory (218kt) remains at bottom end of seasonal range but \~60kt higher vs 2025   
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of copper   
![](images/751589cf58ef56ea4f8cb92a876419288ab5baba45fb906e376077f0f87ee942.jpg)

<details>
<summary>line</summary>

| x  | 5-yr range (min) | 5-yr range (max) | 5-yr avg | 2025 | 2026 |
|----|------------------|------------------|----------|------|------|
| -4 | ~100             | ~480             | ~200     | ~100 | ~300 |
| -2 | ~100             | ~500             | ~220     | ~110 | ~310 |
| 0  | ~100             | ~550             | ~250     | ~120 | ~330 |
| 2  | ~150             | ~600             | ~300     | ~180 | ~450 |
| 4  | ~200             | ~650             | ~350     | ~250 | ~500 |
| 6  | ~250             | ~680             | ~380     | ~300 | ~480 |
| 8  | ~300             | ~690             | ~400     | ~320 | ~450 |
| 10 | ~350             | ~700             | ~420     | ~330 | ~350 |
| 12 | ~400             | ~710             | ~430     | ~320 | ~250 |
| 14 | ~450             | ~720             | ~440     | ~280 | ~220 |
| 16 | ~500             | ~730             | ~450     | ~180 | —    |
| 18 | ~550             | ~740             | ~460     | ~170 | —    |
| 20 | ~600             | ~750             | ~470     | ~160 | —    |
| 22 | ~650             | ~760             | ~480     | ~150 | —    |
| 24 | ~700             | ~770             | ~490     | ~140 | —    |
| 26 | ~750             | ~780             | ~500     | ~130 | —    |
| 28 | ~800             | ~790             | ~510     | ~120 | —    |
| 30 | ~850             | ~800             | ~520     | ~110 | —    |
| 32 | ~900             | ~810             | ~530     | ~100 | —    |
| 34 | ~950             | ~820             | ~540     | ~90  | —    |
| 36 | ~1000            | ~830             | ~550     | ~85  | —    |
| 38 | ~1100            | ~840             | ~560     | ~85  | —    |
| 40 | ~1200            | ~850             | ~570     | ~85  | —    |
| 42 | ~1300            | ~860             | ~580     | ~85  | —    |
| 44 | ~1400            | ~870             | ~590     | ~85  | —    |
| 46 | ~1500            | ~880             | ~600     | ~85  | —    |
</details>

Source: SHFE, CRU, SMM, JPM Commodities

Figure 6: Aluminum inventories movements in 2026 – weekly change in China visible aluminium inventory (SHFE + Bonded). Aluminum de-stocking continues at -16kt last week   
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of aluminium increase / (decrease)   
![](

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1)

includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 31 May 2026 09:47 PM BST

Disseminated 01 Jun 2026 12:15 AM BST
"""
