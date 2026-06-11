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
# China: AI-related high-tech boosted May exports

- Exports beat expectations on strong high-tech shipments, with a growing price lift (memory chips/modules, AI datacenter equipment, and new energy).  
- Imports firmed for a sixth month, driven more by AI supply-chain needs and commodity stockpiling than broad domestic-demand recovery.  
- More narrowly product-focused and increasingly price-driven trade strength makes production and net export contribution to growth less clear-cut.  
- The export outlook is supported by resilient global demand and a broadening of capex to non-tech, with a downside skew from renewed US tariff uncertainties (a pivot to Sections 301/232) and a tougher EU stance against China.

Echoing the upside surprise in FX reserves, China's May exports beat expectations by a wide margin, lifted by shipments of high-tech and mechanical and electrical products. The official price-volume split will come in two weeks, but price gains in memory chips and modules, AI datacenter buildout equipment, and new energy products likely remained a meaningful boost. Imports expanded for a sixth straight month, likely driven by AI-related high-tech imports and commodity stockpiling. As price effects become more supportive, we believe that the read-through to domestic production and the net export contribution to growth is less clear-cut, more volatile, and more sensitive to relative price moves and product mix.

Headline exports rose 3.1%m/m sa, after April's 6.7% jump. Annual growth accelerated to 19.4%oya (vs. market consensus: 15%, JPM: 12.1%), though the trend pace slipped to -6.5%3m/3m saar on an unusually high February base. Imports expanded for a sixth straight month, up 2.9%m/m sa, keeping annual growth elevated at 27.5%oya (vs. market consensus: 26%oya, JPM: 22.9%). Trend growth stayed strong at 57.8%3m/3m saar. The trade surplus widened to US \$105.4bn, lifting the ytd surplus to \$453bn (vs. \$470bn same period last year).

In the destination breakdown, exports logged solid gains across EM Asia (7.0%m/m sa, led by 13.2% for Korea), Japan (6%), and the US (4.9%), alongside increases to Africa and Russia, despite a partial pullback in the EU (-1.5%). By product, low-end consumer goods (textiles, garments, toys, etc.) slipped 0.3%m/m sa. High-tech shipments rose for the seventh consecutive month, up 8.0%m/m sa, led by mobile phones (+19.4%), electronic integrated circuits (+15.2%), and ADP (automatic data processing, +11.0%). This likely reflects memory price inflation amid tight supply. Auto exports rose 2.2%m/m sa, keeping annual growth strong at 39.3%.

After undershooting for most of 2025, imports have beaten expectations since December, averaging a 4.3% monthly run rate as of May. By origin, May gains were led by Asia (Korea +10.2%m/m sa, Japan +2.9%), alongside Brazil and the US (+2.1%). By product, the pattern mirrors exports: high-tech imports rose 5.9%m/m sa, helped by price effects, especially in memory products sourced from Korea. Commodity imports were mixed, with volume gains in coal, natural gas,

## Emerging Markets Asia, Economic and Policy Research

## Tingting Ge

(852) 2800-0143

tingting.ge@JPM.com

## Feng Zhu

(852) 2800 1745

feng.zhu@JPM.com

## Jiayi Li

(852) 2800-5229

jiayi.c.li@JPM.com

## Tongfang Yuan

(852) 2800-0085

tongfang.yuan@JPM.com

JPM Chase Bank, N.A., Hong Kong Branch

soybeans, and copper, while crude oil and refined petroleum products continued to slide. The decline in crude imports partly reflects last year's reserve build and a preference to draw inventories. However, as the Middle East conflict drags on, a return toward more “normal” import levels could tighten the regional oil market.

## Trade blows out, growth impact less clear-cut amid tariff risks

Trade strength year-to-date has far exceeded our prior expectations, which has prompted an outlook recalibration. Granular breakdowns suggest the impulse is unusually narrow and increasingly price-driven. Export gains are concentrated in memory ICs and AI-linked storage/modules, alongside EVs, solar, and batteries, together accounting for around 60% of total export gains. Within this, semiconductor export prices have surged, with memory rotating from a volume-led story in 2025 to a price-led one in recent months. “New three” pricing (EV/solar/batteries) has also firmed, alongside solid volume growth. Elsewhere, average export prices turned marginally positive in April and could face further upward pressure from elevated energy costs. Imports, meanwhile, look less like a domestic-demand rebound and more like AI supply-chain pull and commodity stockpiling.

This mix makes the GDP and employment implications less straightforward. Net export contribution is likely smaller and more volatile, and more sensitive to relative price moves (chips, commodities, FX) and composition. Uncertainty is compounded by the risk that the US trade truce is not extended and by the prospect of new Section 301 tariffs.

After courts struck down earlier IEEPA and Section 122 tariffs, the Trump administration is pivoting to Sections 301 and 232, including probes into excess capacity across 16 economies and forced-labor enforcement across 60 economies. The measures are broader and faster-moving than the 2017–18 China tariff cycle and could still disproportionately hit China-linked supply chains. Trump’s China visit delivered modest stabilization, creating new Board of Trade and Board of Investment channels, plus preliminary commitments on critical minerals, Boeing, and agriculture, but little substantive resolution. Up to four presidential summits this year may preserve a fragile floor under US-China relations. But with no joint statement, China calling the deals preliminary, and courts scrutinizing tariff authority, trade risk is likely to remain a prolonged source of uncertainty unless the new boards convert dialogue into finalized agreements before President Xi’s scheduled visit to the US in September.

The risk of an intensified EU–China trade conflict is rising as Europe's political tone hardens and policymakers look for stronger tools to curb surging imports, especially in sectors where China is increasingly dominant (notably EVs and other strategic industries). A further escalation could bring tighter market access via trade-defense actions and industrial policy (e.g., subsidy design and eligibility rules that effectively exclude Chinese firms), raising the probability of slower China-to-EU export growth, greater destination re-routing, and more headline volatility driven by policy rather than underlying demand. Retaliation risk is also material as China has signaled willingness to respond to protective measures, and Europe is also sensitive to supply-chain leverage (e.g., rare-earth-related disruptions). For China's trade outlook, this points to an asymmetric and composition-driven profile. Categories already under scrutiny (autos/EVs, green energy, selected high-tech inputs) face higher downside skew, and the balance of risks is shifting towards policy shocks, tit-for-tat measures, and confidence effects on cross-border investment and supply-chain planning.

One upside for exports going forward is resilient external demand. Global growth has held up despite the energy shock, supported by policy cushioning, a still-solid consumer, and a business sentiment lift as last year's trade-war drag fades. The key shift is that capex strength is broadening beyond AI infrastructure into non-tech spending, AI adoption across industries, manufacturing, and potential inventory rebuilds, helped by strong profits and lean stock positions. For China, a firmer global goods and capex cycle should support export momentum and China-linked supply chains, partly offsetting uneven domestic demand.

Barring a sharp pullback, this year's nominal export growth could land in the high single digits, and potentially above $10\%$ . Meanwhile, imports are also firming, partly on renewed stockpiling and AI supply-chain inputs, raising the likelihood that full-year nominal import growth outpaces exports for the first time since 2021.

Merchandise trade  
US\$ billion and percent change

<table><tr><td></td><td>2025</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td colspan="6">Exports</td></tr><tr><td>$ billion</td><td>3770.5</td><td>299.8</td><td>321.0</td><td>359.4</td><td>376.8</td></tr><tr><td>%oya</td><td>5.4</td><td>39.6</td><td>2.5</td><td>14.1</td><td>19.4</td></tr><tr><td>%m/m, sa</td><td></td><td>21.2</td><td>-18.8</td><td>6.7</td><td>3.1</td></tr><tr><td colspan="6">Imports</td></tr><tr><td>$ billion</td><td>2587.8</td><td>209.3</td><td>270.5</td><td>274.6</td><td>271.3</td></tr><tr><td>%oya</td><td>0.1</td><td>14.0</td><td>28.1</td><td>25.3</td><td>27.5</td></tr><tr><td>%m/m, sa</td><td></td><td>3.3</td><td>4.4</td><td>2.4</td><td>2.9</td></tr><tr><td colspan="6">Trade balance</td></tr><tr><td>$ billion</td><td>1182.8</td><td>90.5</td><td>50.6</td><td>84.8</td><td>105.4</td></tr></table>

Source: Customs Statistics, JPM

Exports volume vs. price (US\$)  
![](images/9e7f350d8e9034161a44ac284159356624c13144d1426d892ca6bbf8be3de038.jpg)

<details>
<summary>line chart</summary>

| Year | Volume | Price |
|------|--------|-------|
| 17   | ~5     | ~-5   |
| 18   | ~15    | ~5    |
| 19   | ~5     | ~0    |
| 20   | ~-10   | ~-10  |
| 21   | ~20    | ~5    |
| 22   | ~15    | ~15   |
| 23   | ~-10   | ~-15  |
| 24   | ~15    | ~-10  |
| 25   | ~10    | ~-5   |
| 26   | ~20    | ~0    |
</details>

Source: China Customs, JPM

Export price breakdown (in US\$ terms)  
![](images/b9d9a4ad4de38300dc4343d48f60cd584c2d820af04d95bc0442469551d09002.jpg)

<details>
<summary>line chart</summary>

| Year | Headline | Memory chips/moduels and new-three | Others |
|------|----------|-------------------------------------|--------|
| 21   | ~8       | ~-5                                 | ~0     |
| 22   | ~15      | ~50                                 | ~10    |
| 23   | ~5       | ~25                                 | ~0     |
| 24   | ~-10     | ~-15                                | ~-5    |
| 25   | ~-5      | ~-10                                | ~-5    |
| 26   | ~10      | ~55                                 | ~-10   |
</details>

Source: China Customs, JPM

Automatic data processing machines & unit  
![](images/14ab448eb8caa6714bb0fa0c4bb4501397b2f44e0088f315a3c1d98e638cc05d.jpg)

<details>
<summary>line chart</summary>

| Year | Exports | Imports |
|------|---------|---------|
| 2016 | ~0      | ~0      |
| 2018 | ~0      | ~0      |
| 2020 | ~300    | ~500    |
| 2022 | ~0      | ~0      |
| 2024 | ~200    | ~150    |
| 2026 | ~400    | ~150    |
</details>

Source: China Customs, JPM

China's high-tech exports  
![](images/60eedb64dbdda3379d35f667af93b720fdf4d06cd455177cf7c7375c11053ac2.jpg)

<details>
<summary>line chart</summary>

| Year | ICT products | Electronic ICs | Others |
|------|--------------|----------------|--------|
| 2015 | ~40          | ~10            | ~7     |
| 2016 | ~38          | ~12            | ~7     |
| 2017 | ~39          | ~10            | ~7     |
| 2018 | ~45          | ~11            | ~7     |
| 2019 | ~43          | ~12            | ~7     |
| 2020 | ~30          | ~13            | ~6     |
| 2021 | ~50          | ~18            | ~8     |
| 2022 | ~60          | ~22            | ~10    |
| 2023 | ~45          | ~18            | ~11    |
| 2024 | ~43          | ~20            | ~11    |
| 2025 | ~45          | ~25            | ~11    |
| 2026 | ~50          | ~45            | ~13    |
</details>

Source: China Customs, JPM

China battery and solar PV exports  
![](images/b36fd00623932722352b4378f1f80a0340b653f18bf22c13571e9392fc1fa6ff.jpg)

<details>
<summary>line chart</summary>

| Year | Batteries | Solar PV* |
|------|-----------|-----------|
| 2016 | -40       | -40       |
| 2017 | 20        | 50        |
| 2018 | 100       | 20        |
| 2019 | 20        | 10        |
| 2020 | -40       | -40       |
| 2021 | 150       | 60        |
| 2022 | 100       | 60        |
| 2023 | 150       | -40       |
| 2024 | 20        | -40       |
| 2025 | 60        | 20        |
| 2026 | 100       | 40        |
</details>

Source: CEIC, JPM. \*Estimates at HS4-digit level

China exports to US and RoW  
![](images/34fd50fcf6966a236dd7c97fef3cc56fe06a2fe6d223f5274e90e306b4273943.jpg)

<details>
<summary>line chart</summary>

| Date   | China exports - all | China exports to RoW | China exports to US |
|--------|---------------------|----------------------|---------------------|
| Jan 24 | ~10                 | ~0                   | ~0                  |
| Jul 24 | ~5                  | ~0                   | ~0                  |
| Jan 25 | ~15                 | ~10                  | ~0                  |
| Jul 25 | ~30                 | ~25                  | ~-10                |
| Jan 26 | ~70                 | ~60                  | ~-5                 |
</details>

Source: China Customs, JPM

China merchandise trade growth  
![](images/5c09dfdbc225c9abbfc486824801788938efcca7054772c5fc1274235351dbde.jpg)

<details>
<summary>line chart</summary>

| Year | Exports | Imports |
|------|---------|---------|
| 15   | -20     | -15     |
| 16   | -30     | -25     |
| 17   | 45      | 35      |
| 18   | 40      | 30      |
| 19   | 10      | 5       |
| 20   | -30     | -20     |
| 21   | 60      | 50      |
| 22   | 30      | 25      |
| 23   | -10     | -5      |
| 24   | 15      | 10      |
| 25   | 5       | 0       |
| 26   | 35      | 25      |
</details>

Source: China Customs, JPM

China trade surplus by partner  
![](images/040a1a2434b20103132946cfff5bf97ffda808cc9602af6b6d1e419e9aa1f1cb.jpg)

<details>
<summary>bar chart</summary>

US$bn, monthly average
| Region | 2024 (US$bn) | 2025 (US$bn) | 2026ytd (US$bn) |
| :--- | :--- | :--- | :--- |
| US | 30 | 23 | 22.5 |
| EU | 20.5 | 24.5 | 28.5 |
| ASEAN | 16 | 23 | 26 |
| India | 8.5 | 9.5 | 11 |
| Africa | 5 | 8.5 | 9.5 |
| LatAm | 3 | 4 | 1.5 |
| Other | -0.5 | 7 | -7.5 |
</details>

Source: NBS, JPM

China's trade with GCC - growth rate  
![](images/042fbfe6ae676136006457e1297c349822811fa65692365d4fa72f036bb91ab2.jpg)

<details>
<summary>line chart</summary>

| Year | Exports to GCC | Imports from GCC |
|------|----------------|------------------|
| 2017 | -15            | -10              |
| 2018 | 5              | 30               |
| 2019 | 10             | 50               |
| 2020 | 15             | 10               |
| 2021 | 5              | -20              |
| 2022 | 30             | 80               |
| 2023 | 25             | 40               |
| 2024 | 10             | -15              |
| 2025 | 15             | -10              |
| 2026 | 10             | -5               |
</details>

Source: China Customs, JPM

China's oil imports  
![](images/a472cef361f100d08a7d921c83eefe5d610f317ffca044ece0e432eaf1c6355f.jpg)

<details>
<summary>line chart</summary>

| Date   | Oil tanker arrival | Actual oil import volume* |
|--------|-------------------|---------------------------|
| 1/2025 | 98                | 85                        |
| 4/2025 | 100               | 102                       |
| 7/2025 | 108               | 100                       |
| 10/2025| 105               | 98                        |
| 1/2026 | 118               | 112                       |
| 4/2026 | 90                | 75                        |
</details>

Source: IMF, Haver, China Customs, JPM. \* Includes both crude and refined oil

China exports to US vs. US imports from China  
![](images/bcc1090a7a4524761e684722eb3af27720606bac67e57f2915220a7b20161186.jpg)

<details>
<summary>line chart</summary>

| Year | China reported exports to US (US$bn) | US reported imports from China (U

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 09 Jun 2026 02:54 PM HKT

Disseminated 09 Jun 2026 02:54 PM HKT
"""
