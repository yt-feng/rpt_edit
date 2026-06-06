你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Asia Insights

Economics - Asia ex-Japan

## China: The emerging impact of raw materials supply disruptions

We see supply disruptions from the Middle East affecting China's industrial production (IP) and estimate about half of the sharp IP growth slowdown in April was caused by the oil and chemical sectors, which jointly account for $15\%$ of the overall industrial sector and $40\%$ of the raw materials sector. As President Trump warned the blockade of the Strait of Hormuz could remain in place until September, we believe the supply bottleneck will likely continue over the next few months. We expect IP growth to remain subdued at around $4\%$ y-o-y in May and maintain our below-consensus Q2 GDP growth forecast of $4.1\%$ y-o-y (Consensus: $4.7\%$ ). Though China's stable power supply could provide a buffer, the supply shock as a result of the energy crisis will still inflict pain on China's economy via shortages and higher prices. It is imperative for Beijing to secure alternative sources and tap strategic reserves to ease the supply shortages for key raw materials.

## A closer look at IP growth in April

Activity data broadly missed market expectations in April, especially IP data. IP growth slowed sharply to 4.1% y-o-y in April from 5.7% in March (Figure 1), far below the market consensus forecast of 6.0% and even weaker than our more cautious forecast of 5.2%. This 4.1% growth reading was the lowest monthly print in nearly three years. A sectoral breakdown analysis reveals a material impact from global supply disruptions on oil and chemical sectors.

## Oil and chemicals were major drags

In detail, IP growth in the “oil, coal and other fuel processing” sector fell sharply to -0.9% y-o-y in April, the lowest reading since August 2024, from 8.1% in March. Processing volumes of crude oil contracted by 5.8% y-o-y in April (Figure 2), worsening from the 2.2% decline in March. Output volumes of asphalt, a byproduct of crude oil used for building roads, plummeted by 40.1% y-o-y in April, widening significantly from the 19.7% decline in March.

As crude oil and LNG are crucial raw materials for chemical products, and with a natural shift to the strategy of “guaranteeing oil while reducing chemical production (保油减化)” and a slump in imports of chemical raw materials from the Middle East, IP growth of the chemical raw materials and product sector also slowed notably in April to 5.3% y-o-y from 9.0% in March. Constrained by the limited supply of raw materials, IP growth for chemical fiber manufacturing dropped to 2.2% y-o-y in April, the lowest reading since March 2023. Due to the acute shortage of sulfur, a byproduct of petroleum refining and natural gas purification (desulfurization), output growth of sulfuric acid, hailed as the “mother of the chemical industry”, fell sharply to -2.2% y-o-y in April from 6.2% in March. As raw material supplies tighten, output growth of primary plastics and chemical fibers dropped to -4.4% y-o-y and -3.9%, respectively, in April from 4.3% and 2.2% in March.

We estimate the direct drag on IP growth from oil and chemical sectors was about 0.70pp y-o-y in April. As oil and chemical sectors account for about 40% of the raw material industry, and adding indirect impacts, we believe the supply disruptions to oil and chemical sectors might have contributed about half of the sharp IP slowdown in April. Amid the global AI supercycle, IP growth of computers, communication equipment and other electronic equipment accelerated to 15.6% y-o-y in April from 12.5% in March, contributing a 0.4pp y-o-y boost to IP growth in April. In other words, without the boost from the tech-related sector, IP growth would have dropped below 4%.

## Research Analysts

Asia Economics

Jing Wang - NIHK

jing.wang@NOM.com

+852 2252 1011

Ting Lu - NIHK

ting.lu@NOM.com

+852 2252 1306

Fig. 1: IP growth of oil and chemical sectors  
![](images/257b3d8d79cee14aaba0ed6939c4734c9fbdf3b9f143fee613a7755f07c8505e.jpg)

<details>
<summary>line chart</summary>

| Date   | Oil, coal and other fuel processing | Chemical raw materials and products | Overall IP |
|--------|-------------------------------------|--------------------------------------|------------|
| Apr-22 | -5                                  | 0                                    | -5         |
| Oct-22 | -10                                 | 10                                   | 5          |
| Apr-23 | 0                                   | 5                                    | 0          |
| Oct-23 | 15                                  | 15                                   | 5          |
| Apr-24 | 5                                   | 10                                   | 5          |
| Oct-24 | -5                                  | 5                                    | 0          |
| Apr-25 | 0                                   | 5                                    | 5          |
| Oct-25 | 10                                  | 5                                    | 5          |
| Apr-26 | -5                                  | 5                                    | 5          |
</details>

Source: NBS, Wind, NOM Global Economics.

Fig. 2: Output volume growth of key oil related products  
![](images/4fabc0a77293bc6c8315752604e26483a0a4c16226d79bec7b897ef4718258b3.jpg)

<details>
<summary>line chart</summary>

| Date   | Processing volume of crude oil | Asphalt |
|--------|----------------------------------|---------|
| Apr-11 | 0                                | 0       |
| Apr-12 | 0                                | -20     |
| Apr-13 | 5                                | 40      |
| Apr-14 | 0                                | 20      |
| Apr-15 | 0                                | 10      |
| Apr-16 | 0                                | 15      |
| Apr-17 | 0                                | 30      |
| Apr-18 | 5                                | 40      |
| Apr-19 | 0                                | 20      |
| Apr-20 | 10                               | 50      |
| Apr-21 | 0                                | 30      |
| Apr-22 | -10                              | -30     |
| Apr-23 | 20                               | -20     |
| Apr-24 | 0                                | 10      |
| Apr-25 | 0                                | 25      |
| Apr-26 | -5                               | -40     |
</details>

Source: NBS, Wind, NOM Global Economics.

## The supply disruptions might have extended to May

High-frequency data for May, including factory operating rates and PMI data, point to continued weakness in oil and chemical sectors. As the oil and chemical sectors jointly contribute 40% of the output of raw material sector, the disruptions to their production will have ripple effects and could trigger a compounding impact across the broader economy.

## Evidence from weekly factory operating rates

- The operating rate of Shandong oil teapot refineries dropped to 54.7% at end-May and further down to 53.6% in early June from 60.0% at end-April (Figure 3). Its monthly average operating rate fell further to 6.2pp above last year's May rate from 7.0pp above in April and 9.7pp above in March. China's teapot refineries are small, independent processors based primarily in Shandong that manage roughly 25% of the country's refining capacity.  
- The operating rate of asphalt factories dipped to 16.0% at end-May and further down to 13.3% in early June from 16.2% at end-April and 19.3% at end-March (Figure 4). Its monthly average opening rate dropped to 14.6pp below last year's May rate from 11.2pp below in April and 5.7pp below in March. As asphalt is a key material for road construction, its declining output and rising price will likely depress infrastructure construction activity.  
- The operating rate of purified terephthalic acid (PTA) factories fell sharply to 59.3% at end-May from 69.0% at end-April (Figure 5), before rebounding moderately to 66.4% in early June. The monthly average operating rate dropped further to 8.9pp below last year's May rate from 5.2pp below in April and 2.6pp above in March. As a crude oil derivative, PTA is primarily used to produce plastics and fabrics.  
- As PTA supplies run short, the downstream polyester and textile manufacturing chain in also disrupted. The operating rate of polyester filament yarns (PFY) factories in Jiangsu and Zhejiang provinces fell to 79.2% at end-May from 81.9% at end-April (Figure 6). The monthly average operating rate fell further to 10.3pp below last year's May rate from 10.1pp below in April and 7.3pp below in March.

## PMI data corroborate the extended supply damage in May

The official manufacturing PMI dropped to 50.0 in April from 50.3 in March, in line with market consensus. However, adjusting for distortions due to a higher suppliers' delivery time sub-index, which is an inverted index, the headline PMI might have already dipped below 50, closer to our forecast of 49.9. Moreover, according to the NBS, major drags for May's PMI include the petroleum, coal and other fuel processing, chemical fibres and rubber and plastic products, for which both production and new orders subindices have remained below the 50-mark, pointing to sustained weakness in both demand and supply.

Fig. 3: Weekly operating rate of Shandong teapot refineries  
![](images/64c2d978b6ab15ae92d8f18ad0f728e16be498c9b745a93ff1ec0091f60f9cb2.jpg)

<details>
<summary>line chart</summary>

| Month   | 2022 | 2023 | 2024 | 2025 | 2026 |
|---------|------|------|------|------|------|
| 1-Jan   |      |      |      |      |      |
| 1-Feb   |      |      |      |      |      |
| 1-Mar   |      |      |      |      |      |
| 1-Apr   |      |      |      |      |      |
| 1-May   |      |      |      |      |      |
| 1-Jun   |      |      |      |      |      |
| 1-Jul   |      |      |      |      |      |
| 1-Aug   |      |      |      |      |      |
| 1-Sep   |      |      |      |      |      |
| 1-Oct   |      |      |      |      |      |
| 1-Nov   |      |      |      |      |      |
| 1-Dec   |      |      |      |      |      |
</details>

Source: Wind, NOM Global Economics.

Fig. 4: Weekly operating rate of asphalt factories  
![](images/819f79bb8a04f007ccfb229345b70ec9f3302bc593e267b385abab322622a58c.jpg)

<details>
<summary>line chart</summary>

| Month   | 2022 | 2023 | 2024 | 2025 | 2026 |
|---------|------|------|------|------|------|
| 1-Jan   | ~30  | ~30  | ~30  | ~30  | ~30  |
| 1-Feb   | ~30  | ~30  | ~30  | ~30  | ~28  |
| 1-Mar   | ~30  | ~30  | ~30  | ~30  | ~25  |
| 1-Apr   | ~35  | ~35  | ~35  | ~35  | ~22  |
| 1-May   | ~35  | ~35  | ~35  | ~35  | ~20  |
| 1-Jun   | ~35  | ~35  | ~35  | ~35  | ~15  |
| 1-Jul   | ~35  | ~35  | ~35  | ~35  | ~15  |
| 1-Aug   | ~40  | ~40  | ~40  | ~40  | ~15  |
| 1-Sep   | ~45  | ~45  | ~45  | ~45  | ~15  |
| 1-Oct   | ~45  | ~45  | ~45  | ~45  | ~15  |
| 1-Nov   | ~40  | ~40  | ~40  | ~40  | ~15  |
| 1-Dec   | ~35  | ~35  | ~35  | ~35  | ~15  |
</details>

Source: Wind, NOM Global Economics.

Fig. 5: Weekly operating rate of PTA refineries  
![](images/0246f89894560d42b51556d66f2ccd8302e8810eb20b4f8ddcfdc78967e3ef51.jpg)

<details>
<summary>line chart</summary>

| Month   | 2022 | 2023 | 2024 | 2025 | 2026 |
|---------|------|------|------|------|------|
| 1-Jan   | 68   | 63   | 83   | 82   | 78   |
| 1-Feb   | 86   | 74   | 80   | 81   | 79   |
| 1-Mar   | 84   | 78   | 81   | 83   | 84   |
| 1-Apr   | 80   | 79   | 77   | 81   | 82   |
| 1-May   | 75   | 76   | 74   | 78   | 70   |
| 1-Jun   | 70   | 75   | 70   | 75   | 56   |
| 1-Jul   | 75   | 85   | 78   | 80   | -    |
| 1-Aug   | 70   | 80   | 75   | 78   | -    |
| 1-Sep   | 75   | 85   | 80   | 82   | -    |
| 1-Oct   | 70   | 80   | 75   | 78   | -    |
| 1-Nov   | 65   | 75   | 70   | 75   | -    |
| 1-Dec   | 60   | 70   | 65   | 70   | -    |
</details>

Source: Wind, NOM Global Economics.

Fig. 6: Weekly operating rate of PFY factories in East Coast  
![](images/78bcd1a159e190cdf85edf2404e0d3e8eed0f461e7abb96b15ceeca051eae39c.jpg)

<details>
<summary>line chart</summary>

| Month   | 2022 | 2023 | 2024 | 2025 | 2026 |
|---------|------|------|------|------|------|
| 1-Jan   | 75   | 48   | 85   | 85   | 90   |
| 1-Feb   | 80   | 50   | 80   | 80   | 85   |
| 1-Mar   | 85   | 60   | 85   | 85   | 85   |
| 1-Apr   | 90   | 70   | 90   | 95   | 85   |
| 1-May   | 85   | 75   | 85   | 90   | 80   |
| 1-Jun   | 80   | 75   | 85   | 90   | 75   |
| 1-Jul   | 75   | 75   | 85   | 90   | 75   |
| 1-Aug   | 70   | 75   | 85   | 90   | 75   |
| 1-Sep   | 75   | 75   | 85   | 90   | 75   |
| 1-Oct   | 70   | 75   | 85   | 90   | 75   |
| 1-Nov   | 65   | 75   | 85   | 90   | 75   |
| 1-Dec   | 60   | 75   | 85   | 90   | 75   |
</details>

Source: Wind, NOM Global Economics.

## The import disruptions of crude oil and LNG

Before the Iran war, $50\%$ of China's oil imports and $16\%$ of its natural gas imports passed through the Strait of Hormuz (SoH). Due to the severe damage to a wide range of energy facilities in the Middle East and the blockage of the SoH, the supply disruptions are starting to be reflected in China's import data. In April, China's import volume of crude oil slumped by $20.0\%$ y-o-y to its lowest level since August 2022 (Figure 7). The replacement from Russia appears limited so far, as oil import volumes from Russia slowed to $11.3\%$ y-o-y in April and $13.8\%$ in March, following a $40.9\%$ spike in January-February.

As a refined product of crude oil, naphtha's import volumes plunged by $51.3\%$ y-o-y in April, worsening from a $35.7\%$ drop in March. Naphtha is a lightly refined petroleum product, also known as crude gasoline, primarily used to produce chemicals like ethylene and propylene, which in turn are used to produce plastics, fibers and rubbers. China's import reliance on naphtha is about $17\%$ , with about $40\%$ of its imports from Persian Gulf.

On LNG, import volumes tumbled by $23.1\%$ y-o-y in April to its lowest monthly reading since April 2018 (Figure 8), as imports from Qatar crashed by $99.4\%$ y-o-y in April, due to the significant damage to Qatar's Ras Laffan export capacity caused by Iranian retaliatory missile strikes.

Fig. 7: Russian oil seems insufficient to fully fill the gap  
![](images/473569324043cd835509aaa583b2113b0e56150799234c2d44e44c28c7832ba4.jpg)

<details>
<summary>line chart</summary>

| Date   | Overall oil imports (mn tonnes) | Oil imports from Russia (mn tonnes) |
|--------|----------------------------------|-------------------------------------|
| Apr-06 | ~12                              | ~1                                  |
| Apr-08 | ~15                              | ~1                                  |
| Apr-10 | ~18                              | ~1                                  |
| Apr-12 | ~22                              | ~2                                  |
| Apr-14 | ~25                              | ~3                                  |
| Apr-16 | ~30                              | ~4                                  |
| Apr-18 | ~35                              | ~5                                  |
| Apr-20 | ~45                              | ~7                                  |
| Apr-22 | ~50                              | ~8                                  |
| Apr-24 | ~52                              | ~9                                  |
| Apr-26 | ~55                              | ~10                                 |
</details>

Source: China Customs, Wind, NOM Global Economics.

Fig. 8: LNG imports from Qatar tumbled to almost zero  
![](images/ef7eed08066e34912a9c4f3a84c422730f751e934fcfaef708ef3d319ca2b8aa.jpg)

<details>
<summary>line chart</summary>

| Date   | Overall LNG imports (mn tonnes) | LNG imports from Qatar (mn tonnes) |
|--------|----------------------------------|------------------------------------|
| Apr-12 | ~1.0                             | ~0.5                               |
| Apr-13 | ~1.5                             | ~0.6                               |
| Apr-14 | ~2.5                             | ~0.8                               |
| Apr-15 | ~1.8                             | ~0.7                               |
| Apr-16 | ~2.0                             | ~0.9                               |
| Apr-17 | ~3.5                             | ~1.0                               |
| Apr-18 | ~4.5                             | ~1.2                               |
| Apr-19 | ~5.5                             | ~1.3                               |
| Apr-20 | ~6.5                             | ~1.4                               |
| Apr-21 | ~8.5                             | ~1.5                               |
| Apr-22 | ~7.5                             | ~1.6                               |
| Apr-23 | ~6.0                             | ~1.7                               |
| Apr-24 | ~8.0                             | ~1.8                               |
| Apr-25 | ~7.0                             | ~1.9                               |
| Apr-26 | ~3.5                             | ~2.0                               |
</details>

Source: China Customs, Wind, NOM Global Economics.

## The import disruptions of chemical raw materials

For sulfur, import volumes crashed by $72.4\%$ y-o-y in April to its lowest monthly reading since October 2008 (Figure 9), and the supply shortage worsened even further after April. Inventories of sulfur at China's major ports slumped by another $26\%$ from end-April to early June (Figure 10), after a $28\%$ dip in March-April, with its prices jumping by $94.4\%$ since end-February. China's import dependence on sulfur is around $50\%$ , with about $55\%$ of its imports sourced from the Middle East. Globally, $80 - 90\%$ of all sulfur ultimately goes into the production of sulfuric acid. Notably, China ranks as the world's top producer and exporter of sulfuric acid. $55\%$ to $60\%$ of total sulfuric acid consumption is subsequently channelled into fertilizer production, mainly phosphate fertilizer.

Fig. 9: Imports of sulfur slumped to the lowest since 2008  
![](images/b3b065085ac1969876bf81c023d883303acc5bd969754dd663abf848174cde68.jpg)

<details>
<summary>line chart</summary>

| Date    | Sulfur imports (mn tonnes) |
|---------|-----------------------------|
| Apr-96  | 0.0                         |
| Apr-98  | 0.1                         |
| Apr-00  | 0.3                         |
| Apr-02  | 0.5                         |
| Apr-04  | 0.7                         |
| Apr-06  | 0.9                         |
| Apr-08  | 1.1                         |
| Apr-10  | 1.5                

[中间内容因长度限制已省略]

34. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
