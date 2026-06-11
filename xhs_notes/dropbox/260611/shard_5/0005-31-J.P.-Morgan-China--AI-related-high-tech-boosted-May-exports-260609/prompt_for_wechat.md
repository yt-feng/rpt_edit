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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

| Year | China reported exports to US (US$bn) | US reported imports from China (US$bn) |
|------|----------------------------------------|------------------------------------------|
| 00   | ~5                                     | ~5                                       |
| 01   | ~7                                     | ~7                                       |
| 02   | ~9                                     | ~9                                       |
| 03   | ~11                                    | ~11                                      |
| 04   | ~13                                    | ~13                                      |
| 05   | ~15                                    | ~15                                      |
| 06   | ~17                                    | ~17                                      |
| 07   | ~19                                    | ~19                                      |
| 08   | ~21                                    | ~21                                      |
| 09   | ~23                                    | ~23                                      |
| 10   | ~25                                    | ~25                                      |
| 11   | ~27                                    | ~27                                      |
| 12   | ~29                                    | ~29                                      |
| 13   | ~31                                    | ~31                                      |
| 14   | ~33                                    | ~33                                      |
| 15   | ~35                                    | ~35                                      |
| 16   | ~37                                    | ~37                                      |
| 17   | ~39                                    | ~39                                      |
| 18   | ~41                                    | ~41                                      |
| 19   | ~43                                    | ~43                                      |
| 20   | ~45                                    | ~45                                      |
| 21   | ~47                                    | ~47                                      |
| 22   | ~49                                    | ~49                                      |
| 23   | ~51                                    | ~51                                      |
| 24   | ~53                                    | ~53                                      |
| 25   | ~55                                    | ~55                                      |
| 26   | ~57                                    | ~57                                      |
</details>

Source: China Customs, Census Bureau, JPM

China: Major export categories  
![](images/e73c5f6c37ad37280c2d02e57b139ca9a03eb2abf77ea54e

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market

conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 09 Jun 2026 02:54 PM HKT

Disseminated 09 Jun 2026 02:54 PM HKT
"""
