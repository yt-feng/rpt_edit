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
China

# AI and green-tech keep exports strong

Exports accelerated further in May, exceeding expectations amid a global manufacturing upswing. AI-related and green-tech goods remained key drivers, supported by the AI investment boom and energy shock-driven demand for renewables. Imports were lifted by higher commodity and electronics prices.

• May: 19.4% y/y for exports, and 27.4% y/y for imports (both in USD terms)  
- Bloomberg consensus (BARC): 15% y/y (14%) for exports, and 26% y/y (25%) for imports  
- April: $14.1\%$ y/y for exports, and $25.3\%$ y/y for imports (both in USD terms)

China's export growth accelerated further, rising 19.4% y/y in May following a 14.1% increase in April, exceeding both the market and our expectations (Bloomberg: 15%, BARC: 14%). Breakdown data suggest stronger shipments to the US and across the region (ASEAN, Korea, Japan and Taiwan), while shipments to the EU and UK softened. The robust performance came against the backdrop of 1) a continued uptick in global manufacturing activity, evidenced by the global manufacturing PMI holding at a four-year high of 52.6 in May despite the prolonged energy shock, and 2) broad-based strength across major manufacturing exporters, ranging from low-to-mid product exports from Vietnam (May: 18% y/y), to high-end oriented product exports from Korea (May: 53.2%), to the full-supply-chain exports from China (May: 19.4%).

Demand for high-tech products, particularly AI-related and green-tech goods, remained a key driver, helping to alleviate concerns over the impact of the Middle East energy shock on external demand. The ongoing global AI capex cycle continues to underpin demand for China's AI-related exports, given the country is a key supplier of AI manufactured components. High-tech exports accounted for 29.8% of total export value in May, growing 51% y/y (April: 39%), with notable acceleration in semiconductors (+111%) and automatic data processing equipment and parts (+66%). At the same time, the energy shock is supporting demand for renewable products, while persistent geopolitical tensions could further accelerate the global green transition, an area where China remains well positioned as a leading low-cost, high-quality supplier. Year-to-date data show sustained double-digit growth in EVs, lithium batteries, wind turbines, and solar cells.

## Details of May export data

\- By destination: Trade flows between the US and China are showing signs of continued normalization, with shipments to the US surging $35.4\%$ y/y (April: $11.3\%$ ) partly helped by a low base a year earlier following the Liberation Day tariffs. On a sequential basis, exports to

## Ying Zhang

+852 2903 2652

ying.zhang3@BARC.com

BARC Bank, Hong Kong

## Yingke Zhou

+852 2903 2653

yingke.zhou@BARC.com

BARC Bank, Hong Kong

## Jian Chang

+852 2903 2654

jian.chang@BARC.com

BARC Bank, Hong Kong

the US rose by 6.2% m/m-better than the 2022–24 average of around 5.6% (excluding tariff-distorted dynamics in 2025)-pointing to recovery in shipment momentum. It contributed 3.2pp to headline export growth, well above the 1.2pp recorded in April. Meanwhile, regional exports to ASEAN (May: 24.3%, April: 15.2%) and to Japan, Korea and Taiwan (May: 27.5%, April: 16.8%) strengthened further. In contrast, export growth to the EU (May: 7.6%, April: 13.4%) and the UK (May: 1.7%, April: 9.6%) weakened. Moreover, shipments to Africa continued to expand at double-digit pace (May: 18.6%, April: 17.3%), while exports to LatAm softened.

\- By product: Most major export categories accelerated in May. Semiconductor exports value more than doubled from a year earlier, up 110.9% y/y following an already strong 99.6% increase in the previous month. Auto exports remained resilient, rising 39% y/y, although softening from the 44% increase in April. Exports of mechanical and electrical products grew 27.4% y/y, up from 20.3% previously, while home appliance exports continued to expand. Exports of furniture, general equipment and machinery also reversed to pick up in May.

FIGURE 1. China May exports accelerated...  
![](images/a05aaa87a57396264600e606778f084f758d3a9b6dc0d8fb1e8282c9da32634f.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date    | Trade balance (USD bn, RHS) | Exports (% y/y) | Imports (% y/y) |
|---------|-----------------------------|-----------------|-----------------|
| Nov-23  | 12                          | 0               | 0               |
| May-24  | 18                          | 60              | 30              |
| Nov-24  | 18                          | 120             | -30             |
| May-25  | 24                          | 60              | 30              |
| Nov-25  | 24                          | 120             | 90              |
| May-26  | 24                          | 120             | 150             |
</details>

Source: Wind, BARC

FIGURE 2. ... with faster regional trade (Asean, Japan, Korea and Taiwan) and shipments to the US  
![](images/133ddd7dfcb72121ac31ce30bcb4601c5fd3d13905c3f7c8e7121b7d3c1c501e.jpg)

<details>
<summary>line chart</summary>

| Date   | Exports value: headline | US  | EU  | UK  | ASEAN | Africa |
|--------|--------------------------|-----|-----|-----|-------|--------|
| Nov-23 | ~5                       | ~5  | ~-10| ~-5 | ~-5   | ~-5    |
| May-24 | ~10                      | ~5  | ~10 | ~-10| ~20   | ~-25   |
| Nov-24 | ~10                      | ~10 | ~10 | ~-5 | ~10   | ~20    |
| May-25 | ~5                       | ~-30| ~10 | ~10 | ~20   | ~40    |
| Nov-25 | ~10                      | ~-30| ~10 | ~-5 | ~30   | ~50    |
| May-26 | ~20                      | ~35 | ~10 | ~-5 | ~25   | ~20    |
</details>

Source: Wind, BARC

FIGURE 3. Strong exports were led by AI-related and green-tech products  
![](images/1dfd1d653ff5391857c6bdd327d75cef35fcdc3ca52dc71530c8c558bdab2a94.jpg)

<details>
<summary>bar chart</summary>

| Category | 2025 export value growth (%) | 2026YTD growth (%) |
| :--- | :---: | :---: |
| Semiconductor | 27.0 | 90.0 |
| Drones | 94.0 | 77.0 |
| Autos | 21.0 | 50.4 |
| Wind turbines | 48.0 | 47.7 |
| Lithium-ion batteries | 25.0 | 47.6 |
| Solar cells | -5.0 | 35.4 |
| Transformers | 35.0 | 31.3 |
| Ships | 27.0 | 26.5 |
| Overall exports | 5.0 | 19.4 |
</details>

Source: Wind, BARC

FIGURE 4. High frequency shipping data showed still strong exports in early June  
![](images/4c79f80b5f401881704d8d4934157bfb038c3f8d3fb6919235550220456da73b.jpg)

<details>
<summary>line chart</summary>

| Week | 2024 | 2025 | 2026 |
|------|------|------|------|
| 1    | 5.9  | 6.1  | 6.5  |
| 5    | 5.3  | 5.3  | 7.4  |
| 9    | 4.4  | 5.6  | 5.6  |
| 13   | 5.9  | 6.0  | 6.8  |
| 17   | 6.2  | 6.5  | 6.8  |
| 21   | 6.0  | 6.5  | 6.9  |
| 25   | 6.3  | 6.7  | -    |
| 29   | 6.4  | 6.5  | -    |
| 33   | 6.2  | 6.8  | -    |
| 37   | 6.5  | 6.7  | -    |
| 41   | 6.4  | 6.5  | -    |
| 45   | 6.3  | 6.8  | -    |
| 49   | 6.2  | 6.7  | -    |
| 53   | 5.6  | 6.0  | -    |
</details>

Source: Wind, BARC

## May headline imports posted a strong growth due to price effects

Imports have continued to exceed expectations this year. Against the backdrop of surging energy and semiconductor related prices, China's import value posted a solid growth of 27.4% y/y in May, following a 25.3% increase in April, supported by robust imports of mechanical and electrical products (May: 38.2%, April: 33.5%) and commodities (May: 16.4%, April: 13.3%). In contrast, imports of agricultural products softened, while auto imports remained weak, falling 25% y/y after a 34% decline previously.

On a volume basis, imports of energy-related products showed mixed developments. Crude oil imports fell at a faster pace of 29% y/y, following a 20% decline in April. Imports of coal continued to decline, but the pace moderated to -7.7% versus -12.5% previously. In contrast, natural gas imports stabilized after two consecutive months of double-digit declines (May: 0%; April: -12.9%). Market reports suggest a pickup in LNG purchases since mid-April $^{1}$ , driven by expectations of stronger summer power demand, with momentum extending into June. Major buyers have stepped up purchases, increasing imports from Canada, Malaysia, and Russia to offset reduced LNG shipments from Qatar.

Imports of industrial materials showed mixed developments: iron ore import volume growth reversed to fall, while steel imports declined for a second month, though at a slower pace. In contrast, copper imports accelerated, up 4.4% versus 2.7% previously.

Import value of agricultural products rose by 4% following a 20% increase previously. China has agreed to expand agriculture trade with the US following the mid-May Trump–Xi summit, with the US readout noting purchases of at least USD17bn of US agricultural products annually in 2026–2028, on top of earlier soybean commitments. Soybean imports moderated, falling 10% (April: +49.3%) in value terms and 15% (April: +39.5%) in volume in May. That said, the import level of 11.79 million metric tons was still the second highest on record for the month, supported by strong Brazil supplies and faster customs clearance $^{2}$ .

FIGURE 5. Imports of mechanical and electrical products accelerated...  
![](images/510359e0df8212db73a3a9f80547dabe2ada268b0d53eb6390ad4b62f8ca07fe.jpg)

<details>
<summary>line chart</summary>

| Date   | Imports value: headline | Commodities (iron ore, crude oil and copper) | Mechanical & electrical products | Agricultural products | Autos |
|--------|--------------------------|-----------------------------------------------|-----------------------------------|------------------------|-------|
| May-23 | -5                       | -10                                           | -15                               | -5                     | -30   |
| Feb-24 | 5                        | 10                                            | 10                                | 5                      | 20    |
| Nov-24 | 0                        | -10                                           | 0                                 | -10                    | -50   |
| Aug-25 | 5                        | -10                                           | 10                                | 5                      | -50   |
| May-26 | 30                       | 15                                            | 40                                | 20                     | -40   |
</details>

Source: Wind, BARC

FIGURE 6. ...with semiconductor import surging on a value basis  
![](images/79e4104a4c23920168cf6b1a21542f64baa921f360696574b97e4a60af392179.jpg)

<details>
<summary>line chart</summary>

| Date   | Semiconductor imports volume | Semiconductor imports value |
|--------|------------------------------|-----------------------------|
| Nov-18 | -10                          | -5                          |
| May-20 | 60                           | 30                          |
| Nov-21 | 20                           | 25                          |
| May-23 | -15                          | -40                         |
| Nov-24 | 15                           | 10                          |
| May-26 | 10                           | 70                          |
</details>

Source: Wind, BARC

FIGURE 7. Imports of steel and iron ore stayed soft  
![](images/d1bc230701bb026f2bae609caa63101240561f7b8abbf87600b2b8f35aa14e3b.jpg)

<details>
<summary>line chart</summary>

| Date   | Iron ore | Copper | Steel |
|--------|----------|--------|-------|
| May-23 | ~5       | ~-5    | ~-25  |
| Feb-24 | ~10      | ~25    | ~-10  |
| Nov-24 | ~5       | ~20    | ~-15  |
| Aug-25 | ~10      | ~-15   | ~-20  |
| May-26 | ~5       | ~5     | ~-10  |
</details>

Source: Wind, BARC

FIGURE 8. Imports of crude oil weakened further  
![](images/40b2d0bc6c927575c711b294f8bb1b6b8e89c38b47a4eb2d7d98e74a1be69727.jpg)

<details>
<summary>line chart</summary>

| Date   | Coal | Crude oil | Natural gas |
|--------|------|-----------|-------------|
| May-23 | 70   | 45        | 15          |
| Feb-24 | 50   | 5         | 20          |
| Nov-24 | 25   | 10        | 15          |
| Aug-25 | -20  | 10        | 0           |
| May-26 | -10  | -30       | -10         |
</details>

Source: Wind, BARC

## Analyst(s) Certification(s):

We, Yingke Zhou, Jian Chang and Ying Zhang, hereby certify (1) that the views expressed in this research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

## Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC").

All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

## Availability of Disclosures:

For current important disclosures regarding any issuers which are the subject of this research report please refer to https://publicresearch.barlays.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that BARC may have a conflict of interest that could affect the objectivity of this report. BARC Capital Inc. and/or one of its affiliates regularly trades, generally deals as principal and generally provides liquidity (as market maker or otherwise) in the debt securities that are the subject of this research report (and related derivatives thereof). BARC trading desks may have either a long and / or short position in such securities, other financial instruments and / or derivatives, which may pose a conflict with the interests of investing customers. Where permitted and subject to appropriate information barrier restrictions, BARC fixed income research analysts regularly interact with its trading desk personnel regarding current market conditions and prices. BARC fixed income research analysts receive compensation based on various factors including, but not limited to, the quality of their work, the overall performance of the firm (including the profitability of the Investment Banking Department), the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst. To the extent that any historical pricing information was obtained from BARC trading desks, the firm makes no representation that it is accurate or complete. All levels, prices and spreads are historical and do not necessarily represent current market levels, prices or spreads, some or all of which may have changed since the publication of this document. BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis, quantitative analysis, and trade ideas. Recommendations and trade ideas contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https://publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

## Disclosure(s) regarding

[中间内容因长度限制已省略]

 and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
