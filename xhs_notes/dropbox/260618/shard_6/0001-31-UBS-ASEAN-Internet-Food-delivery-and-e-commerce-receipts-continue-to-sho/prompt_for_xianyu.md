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
# ASEAN Internet

# Food delivery and e-commerce receipts continue to show healthy growth in May'26

## What did we learn from the May'26 ASEAN Food Delivery and E-commerce Receipts data?

Leveraging UBS Evidence Lab Food Delivery (> Access Dataset) and e-commerce receipts, we conclude that: 1) Grab's food delivery volume growth remained healthy at 21% YoY in May'26, though moderating from 26-28% in Mar/Apr'26, partly due to weakness in Indonesia; 2) Similarly, Shopee's e-commerce GMV growth also posted healthy +21% YoY GMV growth, moderating from 22/33% in Mar/Apr'26, due to seasonality; 3) Competitive intensity for both ASEAN food delivery and e-commerce sectors ticked up in May'26, with discounts trending up MoM. We attribute part of the slowdown to changing timing for Lebaran, but also see weak macro as a factor that needs to be closely monitored.

## Growth momentum remains healthy in May'26

- Food delivery: Grab's ASEAN "GMV weighted average" order volumes grew 21% YoY in May'26, healthy albeit moderating from 26-28% in Mar-Apr'26. This was partly due to continued weakness in Indonesia (-2.6% YoY orders) amid a weak macro backdrop. AOV was flat MoM (-0.3%) and slightly down (-1.1%) YoY, as Grab continues to push affordability focused products to drive growth. In comparing peers, Grab gained 69/136bps market share vs foodpanda in Philippines/Malaysia, although it lost some (17bps) share in Singapore.  
- E-commerce: Shopee's ASEAN e-commerce GMV grew 20.6% YoY in May'26 - healthy but, similar to food delivery, moderating from 23/33% in Mar/Apr'26 as we move past Lebaran seasonality. Volumes grew at a healthy pace of 28% YoY, although AOV was down 5.6% YoY.

## Competitive intensity broadly inched up in May'26

- Food delivery: On a MoM basis, competitive intensity inched up slightly in May'26, with higher discounting and lower delivery fees. Grab's discounts as a % AOV increased 5-140bps MoM across ASEAN with the exception of Vietnam (-38bps) and Philippines (-390bps). foodpanda took the opposite approach of Grab by lowering discounts in Malaysia (-22bps) and Singapore (-200bps) while increasing in Philippines (+70bps). Delivery fees as a % AOV were down 5-105bps MoM across ASEAN for both Grab and foodpanda, except Vietnam (+8bps for Grab) and Malaysia (+23bps for foodpanda).  
- E-commerce: Competitive intensity was up with both Shopee and seller funded promotions trending higher MoM in May'26. Shopee funded discounts were flat in Singapore but up 60-125bps MoM in Malaysia, Vietnam and Thailand. That said, it was down 30/73bps in Indonesia/Philippines. Meanwhile, seller funded discounts were up 10-95bps MoM across all ASEAN markets.

## Sector view: Maintain Buy on both Grab (PT US\$5.9) and Sea (PT US\$125)

Overall, receipts data continue to indicate robust growth and a generally healthy competitive environment, supporting our thesis that: 1) Grab's affordability initiatives to expand TAM continue to drive structural growth, reinforcing its position as the leading pan-ASEAN food delivery platform; 2) Shopee continues to outgrow the e-commerce market as its moat around logistics, scale and customer engagement via ShopeeVIP starts to differentiate it vs peers. Maintain Buy on Grab (PT US\$5.9) and Sea (PT US \$125).

## Equities

Asia Emerging

Internet Services

Navin Killa

Analyst

navin.killa@ubs.com

+852-2971 7594

Calvin Chur

Associate Analyst

calvin.chur@ubs.com

+65-6495 3992

## GRAB ASEAN

Figure 1: Grab ASEAN avg daily orders MoM %  
![](images/4f1083364af41f6cdfb1e705a860f569671965d6e29c50bc922f9858372c5fd7.jpg)

<details>
<summary>line chart</summary>

| Month    | Grab ASEAN avg daily orders MoM % (GMV weighted) |
| -------- | ----------------------------------------------- |
| Jan-21   | 2%                                              |
| Feb-21   | 10%                                             |
| Mar-21   | 5%                                              |
| Apr-21   | 18%                                             |
| May-21   | 10%                                             |
| Jun-21   | 0%                                              |
| Jul-21   | -5%                                             |
| Aug-21   | 25%                                             |
| Sep-21   | 0%                                              |
| Oct-21   | 7%                                              |
| Nov-21   | 4%                                              |
| Dec-21   | 3%                                              |
| Jan-22   | 0%                                              |
| Feb-22   | 4%                                              |
| Mar-22   | 5%                                              |
| Apr-22   | 4%                                              |
| May-22   | 3%                                              |
| Jun-22   | 0%                                              |
| Jul-22   | 4%                                              |
| Aug-22   | 5%                                              |
| Sep-22   | 3%                                              |
| Oct-22   | 0%                                              |
| Nov-22   | 4%                                              |
| Dec-22   | 5%                                              |
| Jan-23   | 3%                                              |
| Feb-23   | 0%                                              |
| Mar-23   | 4%                                              |
| Apr-23   | 10%                                             |
| May-23   | 3%                                              |
| Jun-23   | 0%                                              |
| Jul-23   | 4%                                              |
| Aug-23   | 5%                                              |
| Sep-23   | 3%                                              |
| Oct-23   | 0%                                              |
| Nov-23   | 4%                                              |
| Dec-23   | 5%                                              |
| Jan-24   | 3%                                              |
| Feb-24   | 0%                                              |
| Mar-24   | 4%                                              |
| Apr-24   | 5%                                              |
| May-24   | 3%                                              |
| Jun-24   | 0%                                              |
| Jul-24   | 4%                                              |
| Aug-24   | 5%                                              |
| Sep-24   | 3%                                              |
| Oct-24   | 0%                                              |
| Nov-24   | 4%                                              |
| Dec-24   | 5%                                              |
| Jan-25   | 3%                                              |
| Feb-25   | 0%                                              |
| Mar-25   | 4%                                              |
| Apr-25   | 5%                                              |
| May-25   | 3%                                              |
| Jun-25   | 0%                                              |
| Jul-25   | 4%                                              |
| Aug-25   | 5%                                              |
| Sep-25   | 3%                                              |
| Oct-25   | 0%                                              |
| Nov-25   | 4%                                              |
| Dec-25   | 5%                                              |
| Jan-26   | 3%                                              |
| Feb-26   | 0%                                              |
| Mar-26   | 4%                                              |
| Apr-26   | 5%                                              |
| May-26   | 3%                                              |
</details>

Source: UBS Evidence Lab

Figure 2: Grab ASEAN total orders YoY %  
![](images/14929816c294fdbe2b050748fa4633b26a5ceaee327d6c28c67f06a57c9dd1dc.jpg)

<details>
<summary>line chart</summary>

| Month    | Grab ASEAN total orders YoY % (GMV weighted) |
| -------- | ------------------------------------------- |
| Jan-21   | ~85%                                        |
| Mar-21   | ~75%                                        |
| May-21   | ~90%                                        |
| Jul-21   | ~120%                                       |
| Sep-21   | ~95%                                        |
| Nov-21   | ~105%                                       |
| Jan-22   | ~115%                                       |
| Mar-22   | ~100%                                       |
| May-22   | ~60%                                        |
| Jul-22   | ~45%                                        |
| Sep-22   | ~75%                                        |
| Nov-22   | ~20%                                        |
| Jan-23   | ~5%                                         |
| Mar-23   | ~10%                                        |
| May-23   | ~20%                                        |
| Jul-23   | ~15%                                        |
| Sep-23   | ~25%                                        |
| Nov-23   | ~30%                                        |
| Jan-24   | ~35%                                        |
| Mar-24   | ~30%                                        |
| May-24   | ~35%                                        |
| Jul-24   | ~30%                                        |
| Sep-24   | ~35%                                        |
| Nov-24   | ~30%                                        |
| Jan-25   | ~25%                                        |
| Mar-25   | ~30%                                        |
| May-25   | ~35%                                        |
| Jul-25   | ~40%                                        |
| Sep-25   | ~35%                                        |
| Nov-25   | ~30%                                        |
| Jan-26   | ~20%                                        |
| Mar-26   | ~25%                                        |
| May-26   | ~20%                                        |
</details>

Source: UBS Evidence Lab

Figure 3: Grab's MoM daily avg order volumes across markets  
![](images/428945cc793803973cfc75944ff8f61b58d1ebe9089f9cbe8d66098458ba65ab.jpg)

<details>
<summary>bar chart</summary>

Grab ASEAN avg daily order May-26 vs Apr-26 (MoM)
| Company | Value (%) |
| :--- | :--- |
| ID | 0.4 |
| MY | 2.5 |
| PH | 6.3 |
| SG | 0.9 |
| TH | 1.5 |
| VN | 9.8 |
| ASEAN | 2.8 |
</details>

Source: UBS Evidence Lab

Figure 4: Grab's YoY total orders across markets  
![](images/6aca29783e081ba4e2526b35584e1372f27023890574c6291f64045f85335a0f.jpg)

<details>
<summary>bar chart</summary>

Grab ASEAN total order May-26 vs May-25 (YoY)
| Country | Grab ASEAN total order (%) |
| :--- | :--- |
| ID | -2.6 |
| MY | 17.1 |
| PH | 29.0 |
| SG | 28.4 |
| TH | 32.2 |
| VN | 42.2 |
| ASEAN | 21.1 |
</details>

Source: UBS Evidence Lab

Figure 5: Grab's MoM AOV across markets  
![](images/2ca2a8b1b75fbf2bcb6458b6b69647381346dbcec1196b4ad14e2f7fab07b85a.jpg)

<details>
<summary>bar chart</summary>

Grab ASEAN AOV May-26 vs Apr-26 (MoM)
| Country | Value (%) |
| :--- | :--- |
| ID | -1.7 |
| MY | 3.4 |
| PH | -0.3 |
| SG | 2.9 |
| TH | -4.2 |
| VN | -0.8 |
| ASEAN | -0.3 |
</details>

Source: UBS Evidence Lab

Figure 6: Grab's YoY AOV across markets  
![](images/bc33e72441a0b810f72fd98300bf5c53791fdced01e5cd7e0ae69c08a7ea0bd4.jpg)

<details>
<summary>bar chart</summary>

Grab ASEAN AOV May-26 vs May-25 (YoY)
| Entity | Value (%) |
|---|---|
| ID | 1.7 |
| MY | 6.6 |
| PH | -8.9 |
| SG | 1.3 |
| TH | -5.6 |
| VN | -3.8 |
| ASEAN | -1.1 |
</details>

Source: UBS Evidence Lab

## SHOPEE ASEAN

Figure 7: Shopee's ASEAN avg daily GMV MoM %  
![](images/77f097a174e6c31567d40787d3db34b315dc5003bba12be6e5837821a97de88d.jpg)

<details>
<summary>line chart</summary>

| Month    | Shopee ASEAN avg daily GMV MoM % |
| -------- | ---------------------------------- |
| Oct-24   | 5%                                 |
| Nov-24   | 7%                                 |
| Dec-24   | 12%                                |
| Jan-25   | -5%                                |
| Feb-25   | 3%                                 |
| Mar-25   | 7%                                 |
| Apr-25   | -10%                               |
| May-25   | 10%                                |
| Jun-25   | 2%                                 |
| Jul-25   | 5%                                 |
| Aug-25   | 0%                                 |
| Sep-25   | 3%                                 |
| Oct-25   | 5%                                 |
| Nov-25   | 5%                                 |
| Dec-25   | 5%                                 |
| Jan-26   | -3%                                |
| Feb-26   | 1%                                 |
| Mar-26   | 3%                                 |
| Apr-26   | -5%                                |
| May-26   | 0%                                 |
</details>

Source: UBS Evidence Lab

Figure 8: Shopee's ASEAN GMV YoY %  
![](images/40ba0cfa624067b89969312d231b28a2ca730ee21840823fec9ce9716ca39d07.jpg)

<details>
<summary>line chart</summary>

| Month    | Shopee ASEAN GMV YoY % |
| -------- | ---------------------- |
| Oct-24   | 32%                    |
| Nov-24   | 26%                    |
| Dec-24   | 38%                    |
| Jan-25   | 42%                    |
| Feb-25   | 40%                    |
| Mar-25   | 38%                    |
| Apr-25   | 31%                    |
| May-25   | 36%                    |
| Jun-25   | 38%                    |
| Jul-25   | 37%                    |
| Aug-25   | 32%                    |
| Sep-25   | 38%                    |
| Oct-25   | 39%                    |
| Nov-25   | 37%                    |
| Dec-25   | 29%                    |
| Jan-26   | 31%                    |
| Feb-26   | 29%                    |
| Mar-26   | 24%                    |
| Apr-26   | 33%                    |
| May-26   | 21%                    |
</details>

Source: UBS Evidence Lab

Figure 9: Shopee's ASEAN avg daily orders MoM %  
![](images/be15cb73d8439b3d1c246f42b1f77a5042959eba4e4d78e616186bd71693db11.jpg)

<details>
<summary>line chart</summary>

| Month    | Shopee ASEAN Orders MoM % |
| -------- | ------------------------- |
| Oct-24   | 5%                        |
| Nov-24   | 0%                        |
| Dec-24   | 12%                       |
| Jan-25   | -5%                       |
| Feb-25   | -7%                       |
| Mar-25   | 25%                       |
| Apr-25   | -15%                      |
| May-25   | 13%                       |
| Jun-25   | 0%                        |
| Jul-25   | 9%                        |
| Aug-25   | -1%                       |
| Sep-25   | 0%                        |
| Oct-25   | 8%                        |
| Nov-25   | 0%                        |
| Dec-25   | 7%                        |
| Jan-26   | -10%                      |
| Feb-26   | -10%                      |
| Mar-26   | 15%                       |
| Apr-26   | -7%                       |
| May-26   | 6%                        |
</details>

Source: UBS Evidence Lab

Figure 10: Shopee's ASEAN total orders YoY %  
![](images/4e05b79a8c2bca0c842f206e90b7914f46aad25f18522ef6d381769480f3f61e.jpg)

<details>
<summary>line chart</summary>

| Month    | Shopee ASEAN Orders YoY % |
| -------- | ------------------------- |
| Oct-24   | 31%                       |
| Nov-24   | 32%                       |
| Dec-24   | 43%                       |
| Jan-25   | 38%                       |
| Feb-25   | 35%                       |
| Mar-25   | 31%                       |
| Apr-25   | 30%                       |
| May-25   | 37%                       |
| Jun-25   | 39%                       |
| Jul-2

[中间内容因长度限制已省略]

egislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/d8476cf39621eab9659d9b8cd95ea28ec260aaa4b7b2e7883c56ebd59c0bd26a.jpg)
"""
