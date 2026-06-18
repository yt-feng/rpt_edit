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
## China Steel - Channel checker

10-day China steel output +4% vs previous (+2% YoY). Bulk iron ore freight rates drop significantly

10-day China steel output 1,018Mt annualised, +4% vs previous: latest China daily crude steel output (10 days to 10 Jun) is tracking at a run rate of 1,018Mt annualised. This is +4% vs the previous 10 days (to 31 May) and +2% YoY. Trailing 30-day steel production is -1% vs previous 30-day period and +1% YoY. Since May, China reported steel output has tracked at the bottom end of the 5-year range.

A notable datapoint this week is a significant decline in bulk shipping costs; rates from Australia, Brazil and South Africa to China all saw declines week-on-week. Australia to China bulk freight rates are now quoted at \$10.9/t, -22% WoW (-\$3/t) and both Brazil and South Africa to China bulk shipping rates are -3% WoW. This implies an Australian FOB iron ore price at \$90/t, which is +4% vs end of Feb (+\$3.5/t) when the US-Iran conflict began. However, we also note that Brazil and South Africa iron ore bulk shipping freight rates remain >50% above pre-conflict levels, which competitively favours Australian iron ore miners.

Among EMEA Metals & Mining iron ore exposed equities, we are Neutral on Rio Tinto and BHP's London listing. Our colleague Lyndon Fagan is OW BHP's Primary Australia listing and is OW Rio Tinto Ltd. With greater exposure to iron ore bulk shipping rates in Brazil and South Africa, we see Anglo American and Kumba Iron Ore as more susceptible to margin pressure and we are Underweight on both names.

## European Metals, Mining & Steel

## Dominic O'Kane AC

(44-20) 7742-6729

dominic.j.okane@JPM.com

JPM Securities plc

## Patrick Jones

(44-20) 7742-5964

patrick.jones@JPM.com

JPM Securities plc

## Varun Bhattad

(91-22) 6157-5027

varun.bhattad@jpmchase.com

JPM India Private Limited

## Rosie Jia

(44-20) 3493-7448

rosie.jia@JPM.com

JPM Securities plc

Link to our latest EMEA Mining & Steel equity valuations and commodity price sensitivities is found here.

Figure 1: Total China steel output 1,018Mt annualised run rate: daily CISA steel output for 10-days ended 10 Jun: +4% vs previous (+2% YoY), in line with seasonal trend  
![](images/591acc20426ab020e25fb0284adc8a07522d3e2e5d7f29edb1f235ea20510856.jpg)

<details>
<summary>line chart</summary>

| Month | 2025 | 2026 |
|-------|------|------|
| Jan   | 970  | 910  |
| Feb   | 980  | 880  |
| Mar   | 1000 | 910  |
| Apr   | 1020 | 980  |
| May   | 1030 | 1040 |
| Jun   | 1010 | 1020 |
| Jul   | 1000 | -    |
| Aug   | 980  | -    |
| Sep   | 950  | -    |
| Oct   | 920  | -    |
| Nov   | 850  | -    |
| Dec   | 750  | -    |
</details>

Source: JPM estimates, CISA, Bloomberg Finance L.P.

See page 5 for analyst certification and important disclosures, including non-US analyst disclosures.

![](images/d4fc2ac62dfa2296dc93e3cfccefb7057e19147fa7c43567a94686ad03b2e39d.jpg)  
JPM Data Insights

Figure 2: FOB iron ore price from Australia to China at \~\$90/t, +\$4/t vs end of Feb & -\$1/t YTD  
LHS: Iron ore price \$/mt; RHS: Shipping cost \$/mt  
![](images/d2c0532ea827de857cca39c926c8355dba922cc25050cd4c568cc85060fd2f4c.jpg)

<details>
<summary>line chart</summary>

| Month   | CFR - 62% Iron Ore Price | FOB - 62% Iron Ore - Australia |
|---------|--------------------------|-------------------------------|
| Jan-25  | ~91                      | ~84                           |
| Feb-25  | ~97                      | ~90                           |
| Mar-25  | ~98                      | ~81                           |
| Apr-25  | ~90                      | ~83                           |
| May-25  | ~88                      | ~80                           |
| Jun-25  | ~89                      | ~79                           |
| Jul-25  | ~90                      | ~84                           |
| Aug-25  | ~97                      | ~87                           |
| Sep-25  | ~98                      | ~88                           |
| Oct-25  | ~100                     | ~89                           |
| Nov-25  | ~98                      | ~85                           |
| Dec-25  | ~100                     | ~87                           |
| Jan-26  | ~106                     | ~97                           |
| Feb-26  | ~104                     | ~90                           |
| Mar-26  | ~94                      | ~85                           |
| Apr-26  | ~104                     | ~93                           |
| May-26  | ~108                     | ~94                           |
| Jun-26  | ~101                     | ~90                           |
</details>

FOB 62% Iron Ore price calculated as CFR 62% Iron Ore price less West Australia to Qingdao bulk shipping costs.  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 3: Iron ore bulk shipping costs from Australia, Brazil and South Africa to China all recorded a decline in the past week with Australian bulk shipping rates -22% WoW to \$10.9/t  
LHS: Iron ore price \$/mt; RHS: Shipping cost \$/mt  
![](images/c3931815cb5393e5cffe48fadd82a82c7e7b6d7f18eda756fac56f83eeb1d5cd.jpg)

<details>
<summary>line chart</summary>

| Month    | West Australia to Qingdao | Tubarao to Qingdao | Saldanha to Beilun |
| -------- | -------------------------- | ------------------ | ------------------ |
| Jan-25   | ~7                         | ~18                | ~12                |
| Feb-25   | ~6                         | ~17                | ~11                |
| Mar-25   | ~9                         | ~20                | ~13                |
| Apr-25   | ~10                        | ~24                | ~18                |
| May-25   | ~8                         | ~19                | ~14                |
| Jun-25   | ~10                        | ~27                | ~19                |
| Jul-25   | ~6                         | ~19                | ~13                |
| Aug-25   | ~9                         | ~24                | ~18                |
| Sep-25   | ~10                        | ~25                | ~19                |
| Oct-25   | ~9                         | ~24                | ~18                |
| Nov-25   | ~10                        | ~24                | ~18                |
| Dec-25   | ~11                        | ~24                | ~20                |
| Jan-26   | ~8                         | ~23                | ~17                |
| Feb-26   | ~9                         | ~19                | ~14                |
| Mar-26   | ~10                        | ~24                | ~17                |
| Apr-26   | ~13                        | ~30                | ~21                |
| May-26   | ~15                        | ~34                | ~24                |
| Jun-26   | ~17                        | ~37                | ~28                |
</details>

FOB 62% Iron Ore price calculated as CFR 62% Iron Ore price less West Australia to Qingdao bulk shipping costs.  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 4: China steel mill margins extend losses in the past few weeks on higher coking coal prices  
![](images/2d5e916ec1ee4d012bc0ea21245c2dfe702d196ce9a5d9bc0683a088bd91160a.jpg)

<details>
<summary>line chart</summary>

| Date    | China HRC Margin | China Rebar Margin |
|---------|------------------|--------------------|
| Jun-19  | ~250             | ~400               |
| Dec-19  | ~500             | ~750               |
| Jun-20  | ~300             | ~500               |
| Dec-20  | ~600             | ~200               |
| Jun-21  | ~1,300           | ~700               |
| Dec-21  | ~700             | ~1,000              |
| Jun-22  | ~100             | ~-400              |
| Dec-22  | ~150             | ~-250              |
| Jun-23  | ~50              | ~-300              |
| Dec-23  | ~-250            | ~-500              |
| Jun-24  | ~-500            | ~-300              |
| Dec-24  | ~-100            | ~-250              |
| Jun-25  | ~150             | ~-100              |
| Dec-25  | ~-150            | ~-400              |
</details>

Source: Bloomberg Finance L.P, JPM estimates.

Figure 5: Total China Steel exports (seasonality): May'26 export run-rate of 122Mtpa at top end of historical average  
![](images/d5843f43aa8430bda3480db4a731eb979581b684a5770eca365e553bbda4addb.jpg)

<details>
<summary>line chart</summary>

| Month | Avg (6yr) | 2026 YTD |
|-------|-----------|----------|
| Jan   | 75        | 90       |
| Feb   | 70        | 95       |
| Mar   | 95        | 100      |
| Apr   | 98        | 110      |
| May   | 95        | 120      |
| Jun   | 90        | 115      |
| Jul   | 85        | 110      |
| Aug   | 82        | 105      |
| Sep   | 85        | 110      |
| Oct   | 83        | 115      |
| Nov   | 84        | 110      |
| Dec   | 85        | 115      |
</details>

Source: JPM estimates, Bloomberg Finance L.P.

Figure 6: 5M'2026 China steel exports at 45Mt, tracking at \~ 10% of total output  
![](images/a9d706072f5bd0aa0fc3acce21660755728186e63f20d098e41da524dcd3ba4c.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | Total exports (Mt) | YTD run-rate (%) |
| :--- | :--- | :--- |
| 2017 | 76 | 10 |
| 2018 | 70 | 8 |
| 2019 | 64 | 7 |
| 2020 | 54 | 5 |
| 2021 | 67 | 7 |
| 2022 | 67 | 7 |
| 2023 | 91 | 9 |
| 2024 | 111 | 12 |
| 2025 | 119 | 12 |
| 2026 | 45 | 11 |
</details>

Source: JPM estimates, Bloomberg Finance L.P.

Figure 7: Official NBS China steel output (annualised) – we estimate 2026 China steel production at \~1,000Mt  
![](images/1021b332420fea5066a45278d0cefc43e39eefb15857b79b2f6ae6ce351a48d3.jpg)

<details>
<summary>bar chart</summary>

| Year | Production (Mt) |
| :--- | :--- |
| 2016 | 808 |
| 2017 | 832 |
| 2018 | 928 |
| 2019 | 996 |
| 2020 | 1,065 |
| 2021 | 1,033 |
| 2022 | 1,013 |
| 2023 | 1,019 |
| 2024 | 1,005 |
| 2025 | 961 |
| 2026 | 414 |
JPMe (dashed box) 586
</details>

Source: JPM estimates, NBS, Bloomberg Finance L.P.

Figure 8: China steel inventory week ending 12 June, flat WoW and +7% YoY; total steel inventory tracking in line with seasonal level  
![](images/20c0eeada5d864f87cfdb44e0042b08b87e54a1fd327dfc2297dc9553826b644.jpg)

<details>
<summary>area chart</summary>

| Month | 2025 | 2026 |
|-------|------|------|
| Jan   | 20.5 | 26.0 |
| Feb   | 22.0 | 27.5 |
| Mar   | 31.0 | 31.5 |
| Apr   | 28.5 | 31.0 |
| May   | 27.0 | 30.0 |
| Jun   | 26.5 | 29.5 |
| Jul   | 26.5 | -    |
| Aug   | 27.0 | -    |
| Sep   | 28.0 | -    |
| Oct   | 28.5 | -    |
| Nov   | 28.0 | -    |
| Dec   | 26.0 | -    |
</details>

Source: JPM estimates, Bloomberg Finance L.P.

Figure 9: Iron Ore inventory held at ports in China at \~160Mt, tracking at historical high but 7Mt down since peak inventory in March  
![](images/5af95b148b2c442027e104c5754b78741b58ee3eb5e941aab2821bcf78ba1db8.jpg)

<details>
<summary>line chart</summary>

| Month | 5 year range | 2025 | 2026 |
|-------|--------------|------|------|
| Jan   | ~145         | ~145 | ~150 |
| Feb   | ~148         | ~147 | ~158 |
| Mar   | ~150         | ~140 | ~168 |
| Apr   | ~148         | ~138 | ~167 |
| May   | ~145         | ~135 | ~165 |
| Jun   | ~148         | ~132 | ~160 |
| Jul   | ~149         | ~130 | -    |
| Aug   | ~148         | ~130 | -    |
| Sep   | ~149         | ~132 | -    |
| Oct   | ~148         | ~132 | -    |
| Nov   | ~149         | ~135 | -    |
| Dec   | ~150         | ~148 | -    |
</details>

Source: JPM estimates, Bloomberg Finance L.P.

Companies Discussed in This Report (all prices in this report as of market close on 15 June 2026, unless otherwise indicated) Anglo American(AAL.L/4,088p/UW), Anglo American (AGLJ.J)(AGLJ.J/88,300c/UW), BHP(BHP.AX/A\$65.19[16 June 2026]/OW), BHP Group Ltd (BHG SJ)(BHGJ.J/74,350c/N), BHP Group Ltd (BHP LN)(BHPB.L/3,431p/N), Kumba Iron Ore Limited(KIOJ.J/30,766c/UW), Rio Tinto Limited(RIO.AX/A\$188.72[16 June 2026]/OW), Rio Tinto plc(RIO.L/7,924p/N)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifyin

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 16 Jun 2026 08:36 AM BST

Disseminated 16 Jun 2026 08:36 AM BST
"""
