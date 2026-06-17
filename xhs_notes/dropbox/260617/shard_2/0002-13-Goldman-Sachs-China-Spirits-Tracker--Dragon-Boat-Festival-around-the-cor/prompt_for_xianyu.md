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
# China Spirits Tracker: Dragon Boat Festival around the corner: Weak outlook despite a low base; Muted wholesale price trend

Indicative Dragon Boat Festival demand - weaker distributor expectations: We see a relatively weak outlook for this year's Dragon Boat Festival sell-through (based on some early distributor feedback which indicate expectations of 10\~20% retail growth for Moutai/Wuliangye, moving down vs. prior expectations for 20\~30%), despite the low base in 2025 due to policy impacts (which saw a DD% decline for premium spirits, and high DD% decline for upper mid end). In terms of distributor stocking pace/demand for the Dragon Boat Festival, our channel checks show relatively muted pre-season channel actions by brands, indicating still cautious distributor sentiment/outlook for retail demand in the upcoming festival. We note that the Dragon Boat Festival typically has a small seasonal impact on China's spirits consumption, while Mid Autumn Festival/National Holiday tends to be more important for observing an inflection point.

Feitian wholesale price has been largely stable (at c.Rmb1,635\~Rmb1,670 per bottle) with low channel inventory (<1 month in East China per channel checks). Wholesale prices for non-standard SKUs remained soft (esp. Zodiac and 1-L Moutai) probably due to increasing volume on i-Moutai (Moutai's AGM highlighted c.7.13mn transactions in 5M26 vs. 3.98mn in 1Q26, and MAU reached 9.56mn in 5M26).

Common Wuliangye and Guojiao 1573 wholesale prices were still soft at Rmb840 each per Daily Spirits Prices (while Common Wuliangye's wholesale price declined to Rmb760/bottle per Bairong Wholesale Market, which has been impacted by the 618 event subsidy pressure, despite a suspension in shipments).

Feitian Moutai wholesale price largely stable despite a slight fall in original case, Common Wuliangye and Guojiao 1573 stayed largely flattish. In the past 2 weeks, original case Feitian Moutai's wholesale price/bottle decreased by Rmb5 from Rmb1,675 to Rmb1,670, and unpacked Feitian Moutai's wholesale price stayed flattish at Rmb1,635. For non-standard Moutai SKUs, the wholesale price of Zodiac/Moutai 1L decreased by Rmb60/30 per bottle, Jingpin Moutai/Moutai 15 years stayed flattish. Common Wuliangye's wholesale price/bottle stayed flattish/decreased by Rmb10 at Rmb840/to Rmb760 per "Daily Spirits Prices"/Bairong Wholesale Market, respectively. Guojiao 1573's wholesale price/bottle stayed flattish at Rmb840.

The authors would like to thank Lily Qi for her contribution to this report.

Leaf Liu

+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

Christina Liu

+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

Valerie Zhou

+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

Weekly Momentum of China Spirits Sector  
![](images/8286e34ec593caefe38ad1fd6a200d524a9bc239a7348fa0d93faa8aa382081a.jpg)

<details>
<summary>gauge chart</summary>

| Segment Color | Value |
|---|---|
| Red | 100 |
| Yellow | 80 |
| Green | 90 |
| Black | 50 |
</details>

Weekly wholesale price indicator

![](images/de8a2b5552f29ee42b831f52e1990bc13e9afe48e04cd0bfe4140f7ba1dfdc1a.jpg)

<details>
<summary>gauge chart</summary>

| Category | Value |
|---|---|
| Red | 100 |
| Yellow | 80 |
| Green | 90 |
| Black | 50 |
</details>

Channel policy indicator

## Methodology: Red/Yellow/Green represents negative/neutral/positive for each indicator.

- Wholesale price of Moutai Original Case and Package Opened: both up/1 up & 1 down/both down represent positive/neutral/negative, respectively.  
• Channel policies that benefits spirits manufacturers are considered positive (e.g. price hikes, sales targets) and vice versa.

Source: GS Global Investment Research

Source: GS Global Investment Research

i-Moutai APP tracker: Our Quest Mobile database indicated monthly active users (MAU) on the i-Moutai app reached 10.2mn/10.1mn in May/Apr, up by 4.4%/0.4% yoy, normalized vs. 18mn MAU in 1Q26 on average and is still above the level before Feitian Moutai's launch (MAU at 5\~7mn in 4Q25). DAU/MAU penetration ratio was at 11%/11% in May/Apr.

Exhibit 1: I-Moutai active users surged from Jan 1st 2026 when Feitian was officially launched on i-Moutai  
![](images/24396f8d7c8e8c288189656e6778a7bfe6dd5ef14123a90454d14e0e489be96c.jpg)

<details>
<summary>line chart</summary>

| Date       | DAU/MAU % | Active user (k) | Avg. daily active users (k) |
| ---------- | --------- | --------------- | --------------------------- |
| 2022-05    | ~21,000   | ~13,500         | ~5,000                      |
| 2022-07    | ~23,000   | ~14,000         | ~5,500                      |
| 2022-09    | ~22,500   | ~13,800         | ~5,200                      |
| 2022-11    | ~23,500   | ~14,500         | ~5,800                      |
| 2023-01    | ~24,500   | ~16,500         | ~6,500                      |
| 2023-03    | ~25,000   | ~17,000         | ~7,000                      |
| 2023-05    | ~24,500   | ~16,800         | ~6,800                      |
| 2023-07    | ~24,000   | ~16,500         | ~6,500                      |
| 2023-09    | ~23,500   | ~17,500         | ~6,800                      |
| 2023-11    | ~24,500   | ~18,500         | ~7,500                      |
| 2024-01    | ~27,500   | ~28,500         | ~11,500                     |
| 2024-03    | ~26,500   | ~25,500         | ~11,800                     |
| 2024-05    | ~25,500   | ~23,500         | ~11,500                     |
| 2024-07    | ~24,500   | ~19,500         | ~9,500                      |
| 2024-09    | ~23,500   | ~17,500         | ~7,500                      |
| 2024-11    | ~19,500   | ~14,500         | ~5,500                      |
| 2025-01    | ~18,500   | ~16,500         | ~6,500                      |
| 2025-03    | ~19,500   | ~14,500         | ~6,800                      |
| 2025-05    | ~17,500   | ~13,500         | ~6,500                      |
| 2025-07    | ~14,500   | ~11,500         | ~4,500                      |
| 2025-09    | ~13,500   | ~9,500          | ~3,500                      |
| 2025-11    | ~11,500   | ~7,500          | ~3,800                      |
| 2026-01    | ~8,500    | ~6,500          | ~4,800                      |
| 2026-03    | ~7,500    | ~4,800          | ~3,888                      |
| 2026-05    | ~6,500    | ~3,888          | ~3,888                      |
</details>

Source: Quest Mobile

## Key news this week:

Wuliangye announced management change (Jun 9): Wuliangye announced that Mr. Deng Min was proposed to serve as the chairman of Wuliangye Group. Wuliangye will hold its AGM on Jun 26, 2026.  
75.2k cases of counterfeit liquor products were investigated by the State Council Food Safety Office (Jun 12): The State Council Food Safety Office announced that 52 cases were filed for investigation due to the production and sale of liquor falsely labeled as “specially supplied” for government related institutions. 5 companies and 36 sales platforms were shut down.  
Laojiao collaborated with Longmen Grottoes for its new product launch (Jun

12): Laojiao launched its new product “Wushang Longmenfu” collaborating with the national Longmen Grottoes (UNESCO World Heritage Site), with a trial price of Rmb159/bottle for 500ml.

## Wholesale price summary of high-end liquors

## From Jun 2 to Jun 14, 2026:

Original case Feitian Moutai's wholesale price/bottle decreased by Rmb5 from Rmb1,675 to Rmb1,670, and unpacked Feitian Moutai's wholesale price stayed flattish at Rmb1,635.  
Common Wuliangye's wholesale price/bottle stayed flattish/decreased by Rmb10 at Rmb840/to Rmb760 per “Daily Spirits Prices”/Bairong Wholesale Market, respectively.  
Guojiao 1573's wholesale price/bottle stayed flattish at Rmb840.

## From Jan 1 to Jun 14, 2026:

Original case Feitian Moutai's wholesale price/bottle increased by Rmb165 from Rmb1,505 to Rmb1,670. Unpacked Feitian Moutai's wholesale price/bottle increased by Rmb145 from Rmb1,490 to Rmb1,635.  
Common Wuliangye's wholesale price/bottle decreased by Rmb10 to Rmb840 per "Daily Spirits Prices," and decreased by Rmb50 to Rmb760 per Bairong Wholesale Market.  
Guojiao 1573's wholesale price/bottle stayed flattish at Rmb840.

Exhibit 2: 53% Feitian Moutai product prices  
![](images/4183459f82739c92e42a707222ac2a09308fb9a0caf3a10d7b9a4d2f434ce46c.jpg)

<details>
<summary>line chart</summary>

| Date       | 53% v/v Feitian Moutai wholesale price (original case) | 53% v/v Feitian Moutai wholesale price-Real (package opened) |
|------------|--------------------------------------------------------|---------------------------------------------------------------|
| Mar Week 2 | 1670                                                   | 1635                                                          |
</details>

Most recent data points as of Jun 14, 2026.  
Source: Daily Spirits Prices, Data compiled by GS Global Investment Research

Exhibit 3: 52% Common Wuliangye product prices  
![](images/153539419d723f458561ebf7c5b43786d280a1659c50bca376cb81b85fddb601.jpg)

<details>
<summary>line chart</summary>

| Date | 52% v/v Common Wuliangye ex-factory price | 52% v/v Common Wuliangye wholesale price (source 1) | 52% v/v Common Wuliangye wholesale price (source 2) | 52% v/v Common Wuliangye wholesale price (source 3) |
| --- | --- | --- | --- | --- |
| Apr-22 | 980 | 980 | 980 | 980 |
| Jun-22 | 970 | 970 | 970 | 970 |
| Aug-22 | 960 | 960 | 960 | 960 |
| Nov-22 | 950 | 950 | 950 | 950 |
| Jan-23 | 940 | 940 | 940 | 940 |
| Mar-23 | 930 | 930 | 930 | 930 |
| May-23 | 920 | 920 | 920 | 920 |
| Jul-23 | 910 | 910 | 910 | 910 |
| Sep-23 | 900 | 900 | 900 | 900 |
| Nov-23 | 890 | 890 | 890 | 890 |
| Jan-24 | 880 | 880 | 880 | 880 |
| Mar-24 | 870 | 870 | 870 | 870 |
| May-24 | 860 | 860 | 860 | 860 |
| Jul-24 | 850 | 850 | 850 | 850 |
| Sep-24 | 840 | 840 | 840 | 840 |
| Nov-24 | 830 | 830 | 830 | 830 |
| Jan-25 | 820 | 820 | 820 | 820 |
| Mar-25 | 810 | 810 | 810 | 810 |
| May-25 | 800 | 800 | 800 | 800 |
| Jul-25 | 790 | 790 | 790 | 790 |
| Sep-25 | 780 | 780 | 780 | 780 |
| Nov-25 | 770 | 770 | 770 | 770 |
| Jan-26 | 760 | 760 | 760 | 760 |
| Mar-26 | 750 | 750 | 750 | 750 |
| Apr Week 1 | 740 | 740 | 740 | 740 |
| Apr Week 3 | 730 | 730 | 730 | 730 |
| May-26 | 720 | 720 | 720 | 720 |
| Jun-26 | 710 | 710 | 710 | 710 |
| Weekly | 900 | - | - | - |
| End | - | - | - | - |
| Final | - | - | - | - |
| Final | - | - | - | - |
| Final | - | - | - | - |
| Final | - | - | - | - |
| Final | - | - | - | - |
| Final | - | - | - | - |
</details>

Most recent data points as of Jun 14, 2026. Source 1 = Spirits Price References; Source 2 = Daily Spirits Prices; Source 3 = Bairong Wholesale Market  
Source: Spirits Price References, Daily Spirits Prices, Bairong Wholesale Market, Data compiled by GS Global Investment Research

Exhibit 4: Guojiao 1573 product prices  
![](images/cb92e4a4901183895b4410137aefdf74d18b2bd6da190f59c4af3b74acd02553.jpg)

<details>
<summary>line chart</summary>

| Date | Ex-factory price of Guojiao 1573 (Post rebate) | Ex-factory price of Guojiao 1573 (Nominal) | Wholesale price of Guojiao 1573 |
| --- | --- | --- | --- |
| Apr-22 | 900 | 960 | 920 |
| Jun-22 | 900 | 960 | 910 |
| Aug-22 | 900 | 960 | 900 |
| Nov-22 | 900 | 960 | 890 |
| Jan-23 | 900 | 960 | 880 |
| Mar-23 | 900 | 960 | 870 |
| May-23 | 900 | 960 | 860 |
| Jul-23 | 900 | 960 | 850 |
| Sep-23 | 900 | 960 | 840 |
| Nov-23 | 900 | 960 | 840 |
| Jan-24 | 900 | 960 | 840 |
| Mar-24 | 900 | 960 | 840 |
| May-24 | 900 | 960 | 840 |
| Jul-24 | 900 | 960 | 840 |
| Sep-24 | 900 | 960 | 840 |
| Nov-24 | 900 | 960 | 840 |
| Jan-25 | 900 | 960 | 840 |
| Mar-25 | 900 | 960 | 840 |
| May-25 | 900 | 960 | 840 |
| Jul-25 | 900 | 960 | 840 |
| Sep-25 | 900 | 960 | 840 |
| Nov-25 | 900 | 960 | 840 |
| Jan-26 | 900 | 960 | 840 |
| Mar-Week 1 | 900 | 960 | 840 |
| Mar-Week 4 | 900 | 960 | 840 |
| Apr-Week 1 | 900 | 960 | 840 |
| Apr-Week 3 | 900 | 960 | 840 |
| May-Week 1 | 900 | 960 | 840 |
| May-Week 3 | 900 | 960 | 840 |
| May-Week 5 | 900 | 960 | 840 |
| May-Week 2 | 900 | 960 | 840 |
| Jun-Week | 900 | 960 | 840 |
| End | 900 | 960 | 840 |
| Weekly | - | - | - |
| End | - | - | - |
| Weekly | - | - | - |
| End | - | - | - |
| Weekly | - | - | - |
| End | - | - | - |
| Weekly | - | - | - |
| End | - | - | - |
| Weekly | - | - | - |
| End | - | 980 | - |
| End | - | - | - |
| End | - | - | - |
| End | - | - | - |
| End | - | - | - |
| End | - | - | - |
| End | - | - | - |
| End | - | - | - |
| End | - | - | - |
| End | End | - | - |
| End | End | - | - |
| End | End | - | - |
| End | End | - | - |
| End | End | - | - |
| End | End | - | - |
| End | End | - | - |
| End | End | - | - |
| Mid | Ex-factory price of Guojiao 1573 (Post rebate) | Ex-factory price of Guojiao 1573 (Nominal) | Wholesale price of Guojiao 1573 |
| Mid | Ex-factory price of Guojiao 1573 (Post rebate) | Ex-factory price of Guojiao 1573 (Nominal) | Wholesale price of Guojiao 1573 |
| Mid | Ex-factory price of Guojiao 1573 (Post rebate) | Ex-factory price of Guojiao 1573 (Nominal) | Wholesale Price of Guojiao (1573) |
| Mid | Ex-factory price of Guojiao 1573 (Post rebate) | Ex-factory price of Guojiao 1573 (Nominal) | Wholesale Price of Guojiao (1573) |
| Mid | Ex-factory price of Guojiao 1573 (Post rebate) | Ex-factory price of Guojiao 1573 (Nominal) | Non-Guojiao Price of Guojiao (1573) |
| Mid | Ex-factory price of Guojiao 1573 (Post rebate) | Ex-factory price of Guojiao 1573 (Nominal) | Non-Guojiao Price of Guojiao (1573) |
| Mid | Ex-factory price of Guojiao 1573 (Post rebate) | Ex-factory Price of Guojiao (Nominal) | Non-Guojiao Price of Guojiao (1573) |
| Mid | Ex-factory price of Guojiao 1573 (Post rebate) | Ex-factory Price of Guojiao (Nominal) | Non-Guojiao Price of Guojiao (1573) |
</details>

Most recent data points as of Jun 14, 2026.  
Source: Daily Spirits Prices, Data compiled by GS Global Investment Research

Moutai non-standard SKUs: In the past 2 weeks, the wholesale price of Zodiac/Moutai 1L decreased by Rmb60/30 per bottle, Jingpin Moutai/Moutai 15 years stayed flattish.

Exhibit 5: Wholesale prices of Moutai's 4 non-standard SKUs  
![](images/442c9481ed5f5f1c836aa340e96b8be3ff505dab50b70689ae953702293fc616.jpg)

<details>
<summary>line chart</summary>

| Month       | Wholesale price | Ex-factory price |
| ----------- | --------------- | ---------------- |
| Apr Week    | 1920            | 1804             |
</details>

![](images/3902e272c1819fdbd1bf391d68d378cc92d0c8040e7ef63e1dc7b19b0c62d858.jpg)

<details>
<summary>line chart</summary>

| Date       | Wholesale price | Ex-factory price | Implied 500ml price |
| ---------- | --------------- | ---------------- | ------------------- |
| Mar-26     | 3320            | 2963             | 1660                |
</details>

![](images/144241d64ac5fcfaada6dbce61f87656c7aa1e5c16d088b43bcedefaafba3fc9.jpg)

<details>
<summary>line chart</summary>

| Date       | Ex-factory price | Wholesale price |
| ---------- | ---------------- | ---------------- |
| Mar-24     | 2,241            | 2,350            |
</details>

![](images/0928be52ade7a1996f4de46c6eb1771ff9e00ee3d2a4a79493c9422f04e29220.jpg)

<details>
<summary>line chart</summary>

| Date       | Wholesale price | Ex-factory price |
| ---------- | --------------- | ---------------- |
| Jun-Week 2 | 4280            | 4,065            |
</details>

Latest data as of Jun 14, 2026.  
Source: Data compiled by GS Global Investment Research, Daily Spirits Prices

## Monthly Wholesale Prices Tracker - 40+ SKUs

Exhibit 6: Wholesale price summary

<table><tr><td rowspan="2"></td><td colspan="9">Moutai</td></tr><tr><td>Feitian Original Case</td><td>Feitian Unpacked</td><td>Hanjiang</td><td>Moutai 1935</td><td>Moutai Prince</td><td>Zodiac</td><td>Caiyou Zhenpin</td><td>Jingpin Moutai</td><td>Moutai - 15yr</t

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
