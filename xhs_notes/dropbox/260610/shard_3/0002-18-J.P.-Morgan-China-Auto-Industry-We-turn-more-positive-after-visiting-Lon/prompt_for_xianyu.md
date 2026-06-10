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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Auto Industry

We turn more positive after visiting London and Paris

We turn more optimistic on Chinese OEMs' overseas expansion, particularly in Europe, following our annual European Auto Conference last week (here), where we took the opportunity to visit BYD stores in London and Paris. To reflect our positive stance, we raise our 2026 overseas sales forecasts for BYD/Geely by \~15%/30%. Key strategic highlights below:

- Europe: Mixed-propulsion transition market: Chinese OEMs are shifting from single-powertrain exports to balanced portfolios (BEV+PHEV/HEV) plus brand ladders (e.g., BYD to Denza) and tech stories. Our store checks show robust PHEV demand alongside “value-for-money” BEV wins.  
- Retail execution moat: Channels + after-sales + residual value: BYD emphasizes dense dealership/store coverage and high test-drive conversion (\~50%); Chinese OEMs stress after-sales depth to build trust, residual value and monthly payment competitiveness, aiming to avoid pure price competition. Foreign brands face pressure as Chinese cars bundle high feature content as standard vs. options-heavy incumbents. Chinese OEMs reached an 18% share in Europe's NEV segment in Apr-26, tripled from the same time last year.  
- Charging/ecosystem as differentiator (not just the car): BYD is using flash/ultra-fast charging rollout as part of the value proposition, targeting 3,000 flash-charging posts in Europe by end-2026. We believe execution will be key to boosting conversion and reducing buyer friction, helping defend residuals and compete on total ownership experience, rather than sticker price.  
- Export tailwinds are structural: China's export mix is shifting rapidly toward NEVs (NEVs $>50\%$ of PV exports; PHEV share rising within NEVs), supporting overseas revenue/margin upside. BYD focuses on vertical integration, while Geely is more partnership/KD "asset-light." We see localization as critical to mitigating tariff/regulatory risk. Meanwhile, European OEMs will aim to compete via an "in China, for global" strategy, including exporting select models from China and leveraging the cost-competitive Chinese supply chain to the global supply network.  
- Our BYD store visits at Canary Wharf and the Champs-Élysées: Staff at both stores reported strong demand for PHEVs. We learned about: (1) the launch of the Denza flash charging model in the EU/UK; and (2) wait times of about two to three months for most BYD models in France.

Equity Ratings and Price Targets

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev</td><td>End Date</td></tr><tr><td>BYD Company Limited - H</td><td>1211 HK</td><td>91,987</td><td>HKD</td><td>88.05</td><td>OW</td><td>n/c</td><td>124.00</td><td>Dec-26</td><td>120.00</td><td>n/c</td></tr><tr><td>BYD Company Limited - A</td><td>002594 CH</td><td>109,946</td><td>CNY</td><td>91.19</td><td>OW</td><td>n/c</td><td>124.00</td><td>Dec-26</td><td>120.00</td><td>n/c</td></tr><tr><td>Geely Automobile Holdings Ltd. (0175)</td><td>175 HK</td><td>21,235</td><td>HKD</td><td>18.17</td><td>OW</td><td>n/c</td><td>29.00</td><td>Dec-26</td><td>28.00</td><td>n/c</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 08 Jun 26.

## China

## Head of APAC Auto Research

Nick Lai AC

(65) 6801-3176

nick.yc.lai@JPM.com

JPM Securities Singapore Private

Limited/ JPM Securities (Asia Pacific)

Limited/ JPM Broking (Hong Kong)

Limited

## Jiajie Shen, CFA

(86-21) 6106 6352

jiajie.shen@jpmchase.com

SAC Registration Number: S1730520030006

JPM Securities (China) Company

Limited

## Cathy Liu

(852) 2800-8629

cathy.xiao.liu@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Four strategic highlights from our store visits, Asia auto tour and European Auto Conference

We visited BYD stores in London and Paris along with our annual European Auto Conference in London last week (note). Our recent annual Asia auto tour along with JPM's China summit yielded similar observations (note). We highlight collective strategic takeaways below. Further, to reflect our positive view on Chinese OEMs' expansion in overseas markets, we lift our 2026 overseas sales estimates for BYD and Geely by \~15% and \~30%, respectively.

Chinese OEMs' market share gains are noticeable not only in Europe (note), but also in other parts of the world, such as Southeast Asia (note) and Latin America. For example, the latest data from Europe (including Eastern and Western Europe) suggest that Chinese OEMs' market share in the NEV space (where Chinese brands are very competitive vs. foreign brands) topped $18\%$ in April, more than tripling from $5\%$ during the same time last year.

Figure 1: Chinese OEMs' annual market share in the NEV space in Europe  
![](images/55ce606e13a75f2db5f167df7a60a4a9fcc83a3ce5b19f479c5458060e1ffe8a.jpg)

<details>
<summary>line chart</summary>

| Year | Value (%) |
|---|---|
| 2014 | 0 |
| 2015 | 0 |
| 2016 | 0 |
| 2017 | 0 |
| 2018 | 0 |
| 2019 | 0.3 |
| 2020 | 1.5 |
| 2021 | 2.1 |
| 2022 | 4.2 |
| 2023 | 5.8 |
| 2024 | 5.5 |
| YTD26 | 16.5 |
</details>

Source: Bloomberg Finance L.P., JATO Dynamics.

Figure 3: BYD market share in Europe's NEV market (8% in Apr-26)  
![](images/b9381ceca2c401a9a142c31e11aa160a5029358afa494b95b824d1d2e5a2022c.jpg)

<details>
<summary>line chart</summary>

| Date | Value (%) |
|---|---|
| 5/1/2024 | 1.2 |
| 6/1/2024 | 1.4 |
| 7/1/2024 | 1.9 |
| 8/1/2024 | 1.9 |
| 9/1/2024 | 1.6 |
| 10/1/2024 | 2.3 |
| 11/1/2024 | 2.6 |
| 12/1/2024 | 2.8 |
| 1/1/2025 | 2.8 |
| 2/1/2025 | 3.0 |
| 3/1/2025 | 4.3 |
| 4/1/2025 | 4.5 |
| 5/1/2025 | 4.5 |
| 6/1/2025 | 4.4 |
| 7/1/2025 | 4.5 |
| 8/1/2025 | 4.7 |
| 9/1/2025 | 6.3 |
| 10/1/2025 | 5.1 |
| 11/1/2025 | 5.8 |
| 12/1/2025 | 6.6 |
| 1/1/2026 | 6.3 |
| 2/1/2026 | 6.3 |
| 3/1/2026 | 7.5 |
| 4/1/2026 | 7.6 |
</details>

Source: Bloomberg Finance L.P., JATO Dynamics.

Figure 2: Chinese OEMs' monthly market share in the NEV space in Europe  
![](images/f63460185b350ca25f397f7b63780fedb06eddf79dcf7a4a576ff8dacebd45d2.jpg)

<details>
<summary>line chart</summary>

| Date | Value (%) |
|---|---|
| 5/1/2024 | 5.3 |
| 6/1/2024 | 7.1 |
| 7/1/2024 | 5.8 |
| 8/1/2024 | 4.9 |
| 9/1/2024 | 5.0 |
| 10/1/2024 | 5.5 |
| 11/1/2024 | 5.8 |
| 12/1/2024 | 6.2 |
| 1/1/2025 | 6.1 |
| 2/1/2025 | 6.1 |
| 3/1/2025 | 8.0 |
| 4/1/2025 | 9.0 |
| 5/1/2025 | 9.8 |
| 6/1/2025 | 10.3 |
| 7/1/2025 | 10.7 |
| 8/1/2025 | 10.8 |
| 9/1/2025 | 13.6 |
| 10/1/2025 | 11.8 |
| 11/1/2025 | 13.3 |
| 12/1/2025 | 14.9 |
| 1/1/2026 | 13.8 |
| 2/1/2026 | 15.6 |
| 3/1/2026 | 17.8 |
| 4/1/2026 | 18.3 |
</details>

Source: Bloomberg Finance L.P., JATO Dynamics.

Figure 4: MG (under SAIC) market share in Europe's NEV market (2% by Apr-26)  
![](images/d9de080623a3b17ba1bfaffdd591a667d61a0a86e537286307eccd59385043ac.jpg)

<details>
<summary>line chart</summary>

| Date | Value (%) |
|---|---|
| 5/1/2024 | 3.2 |
| 6/1/2024 | 4.9 |
| 7/1/2024 | 2.8 |
| 8/1/2024 | 1.8 |
| 9/1/2024 | 2.4 |
| 10/1/2024 | 1.9 |
| 11/1/2024 | 1.8 |
| 12/1/2024 | 2.1 |
| 1/1/2025 | 1.7 |
| 2/1/2025 | 1.4 |
| 3/1/2025 | 2.0 |
| 4/1/2025 | 1.6 |
| 5/1/2025 | 1.8 |
| 6/1/2025 | 2.4 |
| 7/1/2025 | 2.5 |
| 8/1/2025 | 2.0 |
| 9/1/2025 | 2.5 |
| 10/1/2025 | 1.9 |
| 11/1/2025 | 2.2 |
| 12/1/2025 | 2.4 |
| 1/1/2026 | 1.3 |
| 2/1/2026 | 1.5 |
| 3/1/2026 | 1.7 |
| 4/1/2026 | 2.3 |
</details>

Source: Bloomberg Finance L.P., JATO Dynamics.

## (1) Europe as a mixed-propulsion transition market: Chinese OEMs are winning by offering a portfolio (BEV + PHEV/HEV) plus a clear brand ladder (mainstream → premium), not a single “cheap BEV export” play

Chinese OEMs (e.g., BYD, Geely) are shifting their overseas strategies toward multi-powertrain portfolios and brand/tech storytelling, with Europe explicitly treated as a transition market, where PHEV demand matters alongside BEV.

Examples (store checks): BYD's Paris and London stores show strong PHEV traction (e.g., Seal U DMi highlighted by sales staff we met as a bestselling PHEV; a meaningful share of store orders are PHEV), while certain BEV models (e.g., Sealion 7) are positioned as “value for money” leaders with long wait times, especially at the Paris store, suggesting that demand exceeds supply in inventory.

Implications for overseas markets: We expect share gains to be driven less by “BEV-only price disruption” and more by a menu that matches local charging readiness and consumer needs, with PHEV acting as a commercialization bridge.

Foreign brands' strategy signal: Incumbents face a tougher value equation because Chinese models often bundle high-feature content as standard, e.g., Level 2 ADAS (vs. options-heavy German pricing), shifting competition toward content-per-euro and monthly payments (as opposed to MSRPs or sticker prices).

JPM view: We are surprised at the speed of overseas volume growth among Chinese brands, driven by competitive product offerings, multi-powertrain options and superior interior/content vs. foreign brands at similar price points. To reflect this positive moment, we raise our overseas volume estimates for BYD and Geely in our earnings models.

## (2) Go-to-market is becoming a retail execution game: Dense channels + after-sales credibility + residual value discipline (i.e., monthly payment competitiveness)

One key observation throughout our visits and meetings is that Chinese OEMs are emphasizing rapid channel buildout (stores/dealers), measurable conversion and deepening after-sales to build trust and residual value, explicitly linking this to monthly payment competitiveness, rather than sticker price warfare.

Examples: BYD's Europe expansion plan targets large physical scale (dealers/stores), and management messaging highlights rapid conversion ( $\sim 45 - 50\%$ ) into orders after test drives and solid demand (especially considering supply tightness in Europe, such as at the Paris store we visited).

Overseas market implications: The winning playbook looks closer to “fast retail rollout + service credibility” than to traditional export-only distribution, raising the bar for incumbents that may be slower to reconfigure dealer economics and inventory strategy.

Foreign brands' strategy response: Foreign OEMs are already adjusting, e.g., German premium OEMs have been consolidating dealer networks in China and rightsizing production capacity in China, signaling a broader shift toward

profitability protection and structural resizing, rather than pure volume defense. Outside China, we notice select global OEMs' strategic shift from “in China, for China” previously to “in China, for global” now, meaning that global OEMs are bringing select China-made products to overseas markets and exploring leveraging cost-competitive Chinese suppliers to their global supply chain networks.

JPM view: Based on our store visits and discussions with management, we believe BYD's focus on residual value discipline (and avoiding price competition) is central to sustaining brand health and monthly-payment positioning as volumes scale.

## (3) The next moat is ecosystem + charging (flash/ultra-fast) paired with premium products – used to lift value propositions and reduce price pressure

We learned at our store visits and European auto conference that BYD is positioning charging infrastructure (including flash charging) as an ownership proposition and commercialization lever; management has stated a target of 3,000 flash-charging posts in Europe by end-2026, including 300 in the UK, and a premium-brand Denza launch in 2H26, which will be the first BYD offering with a “flash charging solution.”

What also surprised us was the Paris store sales staff's comment that there are meaningful orders for the newly launched Denza model and that wait times are now about six months, even though Denza has not been formally launched in Europe and buyers know only an initial indicative price of \~€115,000.

Overseas market implications: If executed, OEM-tied charging could reduce buyer friction (range/charging anxiety), support fleets and shift competition from price to total ownership experience, which is particularly important in Europe, where charging availability varies widely across geographies.

Foreign brands' strategy response: This development pressures incumbents to compete not just on vehicle specs, but also on ecosystem partnerships (charging access, software stacks, service plans), and to rethink what is bundled vs. optioned.

JPM view: We believe the charging rollout, if delivered at scale, could support conversion/acceptance and help BYD avoid pure price competition by strengthening the overall value proposition beyond sticker price.

## (4) The “overseas story” is structurally supported by export mix shifts (NEV/PHEV) and a push toward localization, but execution + policy risk is rising

We expect China PV exports to be increasingly NEV-led (NEVs reaching a majority share), with PHEV becoming a larger component of NEV exports, a pattern that may surprise overseas investors and aligns with Europe's transition-market reality.

Overseas market implications: As the mix shifts to higher-ASP electrified products, overseas could become disproportionately important to revenue/profit (vs. volume), which supports more aggressive investment in channels, charging and local footprints.

Localization divergence (BYD vs. Geely): We see strategic differences between OEMs, with BYD pursuing a more vertically integrated overseas footprint (plants outside China), while Geely leans more toward partnership/KD and “asset-light” pathways.

Foreign brands' strategy response (“in China, for global”): Global OEMs are trying to export China-made models and leverage China’s cost-competitive supply chain globally, an explicit attempt to turn China capabilities into an international countermeasure.

JPM view: Longer-term, we view Chinese OEMs' exports/share gains as structural, rather than cyclical. At the same time, Chinese OEMs' localization will be a decisive strategic variable to mitigate tariff/regulatory risk; examples include BYD's plants in Brazil and Hungary, Geely's partnerships with Porton in Malaysia and with Ford in Spain, Leapmotor's JV with Stellantis, and XPeng's alliance with Magna in Austria. Localized solutions should help potential geopolitical headwinds and tariff/non-tariff barriers facing Chinese brands in their overseas endeavors.

## Summary of our BYD store visits in Paris and London

## Paris store

- Bestselling BEV: Sealion 7 with an MSRP of \~€48,000 and a wait time of three  
to four months; monthly installment around €800 if buyers choose the leasing finance option.  
- Bestselling PHEV: Seal U DMI with a starting MSRP of €40,600 and monthly installments around €600-700. Wait time is around one month, where most buyers also consider Tesla Model Y.  
- Most buyers choose BYD for its value-for-money position: BYD offers many features as standard, e.g., 360 view, seat heating, ADAS level 2 vs. German models, where these features are mostly optional and customers need to pay.  
- What surprises us is BYD's introduction of premium-brand Denza Z9 GT, which will be equipped with the company's latest flash-charging solution (i.e., state of charge (SOC) only 9 minutes from $10\%$ to $97\%$ ). The initial 

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
