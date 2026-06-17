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
# China alt-data trackers chartpack (Series 57)

Exports still the bright spot, oil supply recovery limited

April domestic activity weakness tilted 2Q growth risks to the downside. Incoming May data have been mixed, with trade beating expectations but credit demand remaining soft. May–June data will be key to recalibrating 2Q growth momentum. While we await May domestic hard-activity indicators, we update our alt-data trackers (vs. our last update) and our key takeaways are below.

- Exports: Port tracking shows departing container (+8.9%) and bulk (+10.8) shipping deadweight tonnage both increased m/m nsa mtd in June. Annual growth held up further. In aggregate, departing shipments deadweight tonnage (excluding tankers) rose 17.9% oya mtd in June (vs. 7.7% in May), suggesting volume growth is picking-up alongside recent price gains. Oil tanker arrivals remained subdued mtd in June, at a similar level to May.  
- CCFI to USEC, USWC rose 6.5%, 9.1%, respectively, compared to two weeks ago; CCFI to the Persian Gulf/Red Sea route increased by another 8.6%.  
China's domestic and int'l flight cancelation rate remained elevated.  
Production: Processed crude oil production contraction may have deepened in May, with further decline in June (vs -5.8% oya in April) as petroleum asphalt plants' operating rates declined further. Auto IP growth may have improved modestly in May, with a slowdown in June (vs -2.6% oya in Apr). Steel IP contraction may have deepened in May but may narrow in June (vs -1.7% oya in Apr). Coke oven plants ticked down mtd in June.  
- Fiscal: Government bond issuance moderated to 616bn yuan in June mtd (vs. 1140bn yuan in May). CGB issuance slipped to 164bn yuan while special LGB issuance picked up only modestly to 212bn yuan. Absent a month-end jump, fiscal delivery will remain less front-loaded by June. If domestic demand weakness persists, we expect an acceleration in government bond issuance and fund deployment in 3Q.  
- Monetary: PBOC net injected 410bn yuan of liquidity via pledged OMO in June mtd, while it withdrew 300bn yuan via outright OMO. A cut could become more likely in 2H if growth headwinds intensify and outweigh inflation risks.  
- Auto sales remained a drag on retail sales. Passenger car retail sales fell 22% oya in May, partially on lower per-car trade-in subsidies and purchase tax exemptions, and higher fuel costs. NEV sales fell a narrower 7.5%. In the first week of June, passenger car sales fell 23% oya and NEV sales fell 14%.  
- Housing: Home sales in both new and secondary home markets outperformed the same period last year in June mtd, with some momentum easing lately. Uncertainty remains over whether this marks a housing market bottoming-out.  
- Inflation: Gasoline, diesel and LPG prices continued to moderate in the first ten days of June, while LNG prices ticked up mildly. Coal prices rose further to the highest level in nearly 20 months, also on summer seasonal demand. Some petrochemical products moderated from recent peaks, while sulfuric acid stayed elevated. Agricultural food prices fell $0.1\%$ oya in June mtd, narrowing the drag on headline CPI. Pork wholesale prices contraction remained elevated, as overcapacity in the industry prolongs.

## Emerging Markets Asia, Economic and Policy Research

## Tingting Ge

(852) 2800-0143

tingting.ge@JPM.com

## Jiayi Li

(852) 2800-5229

jiayi.c.li@JPM.com

## Tongfang Yuan

(852) 2800-0085

tongfang.yuan@JPM.com

## Feng Zhu

(852) 2800 1745

feng.zhu@JPM.com

JPM Chase Bank, N.A., Hong Kong Branch

## 1. Mapping: High-frequency trackers --> official activity

Regarding the mapping efforts from high-frequency data to monthly official activity tracking:

- Operating rates for petroleum asphalt plants suggest processed crude oil production contraction may have deepened in May, with further decline in June (vs -5.8% oya in April).  
- Operating rates for tire plants suggest auto IP growth may have improved modestly in May, followed by slowdown in June (vs -2.6% oya in Apr).  
- Operating rates for steel rebar suggest that steel IP contraction may have deepened in May but may narrow in June (vs -1.7% oya in Apr).  
- Housing transactions for 30 major cities gained $4.0\%$ oya mtd in June (vs $-1.4\%$ in May).  
- Port tracking shows that departing container and bulk shipping deadweight tonnage both increased m/m nsa, mtd in June. Over-year-ago growth mtd also improved. In aggregate, departing shipments deadweight tonnage (excluding tankers) rose 17.9% oya mtd in June (vs. 7.7% in May).

Figure 1.1: Industrial production - Processed crude oil  
![](images/7f52b58a20c6351bb25e541d88e7847e889235f0c1c49feb8d54fe7ad44392ac.jpg)

<details>
<summary>line chart</summary>

| Year | Weekly tracking (operating rate) 1/ | Monthly from the NBS (RHS) |
|------|-------------------------------------|----------------------------|
| 17   | ~-10                                | ~5                         |
| 18   | ~-30                                | ~10                        |
| 19   | ~-40                                | ~5                         |
| 20   | ~-20                                | ~15                        |
| 21   | ~50                                 | ~20                        |
| 22   | ~-50                                | ~-10                       |
| 23   | ~-30                                | ~15                        |
| 24   | ~-20                                | ~5                         |
| 25   | ~-10                                | ~0                         |
| 26   | ~-50                                | ~-10                       |
</details>

Source: CEIC, Wind, JPM; 1/ Latest for June 2026.

Figure 1.2: Industrial production - Auto  
![](images/024c6a9096c49b7723afe97ff5d508197864f7987c78412552b0d0b757dd1636.jpg)

<details>
<summary>line chart</summary>

| Year | Monthly from NBS | Weekly tracking (full-steel tire) 1/ |
|------|------------------|--------------------------------------|
| 17   | ~10              | ~40                                  |
| 18   | ~0               | ~0                                   |
| 19   | ~-10             | ~-10                                 |
| 20   | ~-50             | ~-50                                 |
| 21   | ~75              | ~50                                  |
| 22   | ~-30             | ~-30                                 |
| 23   | ~60              | ~25                                  |
| 24   | ~-10             | ~-10                                 |
| 25   | ~10              | ~0                                   |
| 26   | ~-10             | ~-10                                 |
</details>

Source: CEIC, Wind, JPM; 1/ Latest for June 2026.

Figure 1.3: Industrial production - Steel  
![](images/d2b5320c11b53045ec1bbbb074ddbab753488f173c073c9abdc387508d5f8c83.jpg)

<details>
<summary>line chart</summary>

| Year | Weekly tracking (operating rate) 1/ (%) | Monthly from the NBS (RHS) (%) |
|------|------------------------------------------|---------------------------------|
| 17   | -20                                      | 0                               |
| 18   | 15                                       | 5                               |
| 19   | 5                                        | 10                              |
| 20   | -10                                      | 5                               |
| 21   | 20                                       | 25                              |
| 22   | -30                                      | -10                             |
| 23   | -10                                      | 10                              |
| 24   | 5                                        | 5                               |
| 25   | -20                                      | 0                               |
| 26   | -5                                       | -5                              |
</details>

Source: CEIC, Wind, JPM; 1/ Latest for June 2026.

Figure 1.4: China exports  
![](images/fdaee79ee11b476bb7c3eacedfa16ec977927751ed057cbd21c9407e2069b035.jpg)

<details>
<summary>line chart</summary>

| Year | Export volume from China Customs (%) | Deadweight daily tracking of departing ships (lhs) 1/ (%) |
|------|----------------------------------------|----------------------------------------------------------|
| 2020 | -15                                    | 15                                                       |
| 2021 | 50                                     | 18                                                       |
| 2022 | -5                                     | -15                                                      |
| 2023 | -10                                    | 10                                                       |
| 2024 | 20                                     | 5                                                        |
| 2025 | 15                                     | -5                                                       |
| 2026 | 45                                     | 10                                                       |
</details>

Source: Elane Shipping, China Customs, JPM; 1/ Latest for June 2026, excl. tankers

## 2. Trade

China's outbound container costs rose further across major routes. By destination, CCFI to USEC, USWC rose $6.5\%$ , $9.1\%$ , respectively, compared to two weeks ago; CCFI to the Persian Gulf/Red Sea route increased by another $8.6\%$ . Baltic Dry Index ticked down after several weeks of increases since April. US-bound shipping edged up $0.4\%$ oya or rose $7.1\%$ m/m nsa mtd in June (vs $27.8\%$ oya or $2.9\%$ m/m nsa in May).

\- Container ships usually carry consumer goods, as well as some machinery equipment and electronics. Departing container ships' deadweight tonnage rose 5.0% oya or 8.9% m/m nsa mtd in June. Arriving container ships' deadweight tonnage fell 1.3% oya or up 5.7% m/m nsa.

- Bulk carriers transport unpackaged bulk cargo for grain, coal, iron ore, steel, etc., in their cargo holds. Departing bulk ships' deadweight tonnage rose 21.7% oya mtd (or 10.8%m/m nsa), while arriving bulk ships' deadweight tonnage rose 24.3% oya or 8.8%m/m nsa.  
- Oil tanker arrivals remained subdued mtd in June, at a similar level to May.

China's domestic and international flight cancelation rates remained elevated mtd in June at above $25\%$ and $20\%$ , respectively, partly due to still high jet fuel costs and airfares. Flight execution edged lower in June.

China's soybean imports increased in May, following seasonal trend. Purchases from the US have been rising. The Ministry of Commerce confirmed the agreement with the US to purchase 200 Boeing aircraft, as well as engines and spare parts. The White House statement said China would purchase at least US\$17bn US agricultural products annually from 2026 to 2028.

![](images/80a4027e9172eb3183ea01a55c15bd71774a091040abe364a66017963dcf1b97.jpg)

<details>
<summary>line chart</summary>

| Date   | Mediterranean | USEC  | USWC  | Europe | Red Sea | South America |
|--------|--------------|-------|-------|--------|---------|---------------|
| Jan 24 | 3,000        | 1,000 | 800   | 2,500  | 1,500   | 700           |
| May 24 | 3,500        | 1,200 | 900   | 3,000  | 2,000   | 800           |
| Sep 24 | 3,800        | 1,500 | 1,000 | 3,500  | 2,500   | 900           |
| Jan 25 | 3,200        | 1,300 | 950   | 3,200  | 2,200   | 850           |
| May 25 | 2,800        | 1,100 | 850   | 2,800  | 2,000   | 750           |
| Sep 25 | 2,500        | 1,000 | 800   | 2,500  | 1,800   | 700           |
| Jan 26 | 2,200        | 950   | 750   | 2,200  | 1,600   | 650           |
| May 26 | 2,800        | 1,100 | 850   | 2,800  | 2,500   | 750           |
</details>

Source: Wind, JPM

Figure 2.3: Deadweight tonnage of departing ships - Container  
![](images/d92d4cbb1994ade8e5cafe9de2e35eebedd9120a97a09b5f6c54b024fc491972.jpg)

<details>
<summary>line chart</summary>

| Month | 19-24 range | 19-24 avg. | 2025 | 2026 |
|-------|-------------|------------|------|------|
| Jan   | ~0.8        | ~0.7       | ~0.9 | ~1.2 |
| Feb   | ~0.7        | ~0.6       | ~0.8 | ~1.0 |
| Mar   | ~0.6        | ~0.6       | ~0.7 | ~0.8 |
| Apr   | ~0.7        | ~0.7       | ~0.9 | ~1.0 |
| May   | ~0.8        | ~0.7       | ~1.0 | ~1.1 |
| Jun   | ~0.8        | ~0.7       | ~1.0 | ~1.1 |
| Jul   | ~0.8        | ~0.7       | ~1.0 | ~1.0 |
| Aug   | ~0.7        | ~0.6       | ~0.9 | ~0.9 |
| Sep   | ~0.7        | ~0.6       | ~1.0 | ~1.0 |
| Oct   | ~0.7        | ~0.6       | ~1.0 | ~1.0 |
| Nov   | ~0.7        | ~0.6       | ~1.1 | ~1.1 |
| Dec   | ~0.7        | ~0.6       | ~1.0 | ~1.0 |
</details>

Source: Elane Shipping Statistics, JPM.

Figure 2.5: Deadweight tonnage of departing ships - Bulk  
![](images/c4a4b1c762de24ad023c3c08abc9a6d58173b0bafdde8287f6200dee705f7989.jpg)

<details>
<summary>line chart</summary>

| Month | 19-24 range | 19-24 ave. | 2025 | 2026 |
|-------|-------------|------------|------|------|
| Jan   | ~8.5        | ~9.5       | ~8.5 | ~8.5 |
| Feb   | ~8.5        | ~9.0       | ~7.0 | ~10.5 |
| Mar   | ~8.5        | ~8.5       | ~8.0 | ~9.5 |
| Apr   | ~8.5        | ~8.5       | ~9.0 | ~11.0 |
| May   | ~8.5        | ~8.5       | ~9.5 | ~10.5 |
| Jun   | ~8.5        | ~8.5       | ~9.5 | ~12.0 |
| Jul   | ~8.5        | ~8.5       | ~9.5 | ~11.5 |
| Aug   | ~8.5        | ~8.5       | ~9.5 | ~10.5 |
| Sep   | ~8.5        | ~8.5       | ~9.5 | ~10.0 |
| Oct   | ~8.5        | ~8.5       | ~9.5 | ~10.0 |
| Nov   | ~8.5        | ~8.5       | ~9.5 | ~10.0 |
| Dec   | ~8.5        | ~8.5       | ~9.5 | ~10.0 |
</details>

Source: Elane Shipping Statistics, JPM.

Figure 2.2: BEISL freight index  
![](images/2b424ff0f294ab90d38ea2b0eecd11a82c3c8ee8a53b2855ab09abf267b287ba.jpg)

<details>
<summary>line chart</summary>

| Year | Baltic Exchange Dry Index | Global Container Freight Index (RHS) |
|------|---------------------------|---------------------------------------|
| 20   | ~500                      | ~1000                                 |
| 21   | ~1500                     | ~3000                                 |
| 22   | ~5500                     | ~10000                                |
| 23   | ~1000                     | ~2000                                 |
| 24   | ~3500                     | ~4000                                 |
| 25   | ~1500                     | ~3000                                 |
| 26   | ~3000                     | ~2000                                 |
</details>

Source: Baltic Exchange Information Services Limited, JPM

Figure 2.4: Deadweight tonnage of arrived ships - Container  
![](images/c6948b851c712071c919c82882dea828a68dc2a899b1b3f389e26307101ebcd1.jpg)

<details>
<summary>line chart</summary>

| Month | 19-24 range | 19-24 ave. | 2025 | 2026 |
|-------|-------------|------------|------|------|
| Jan   | ~0.8        | ~0.75      | ~0.9 | ~0.95 |
| Feb   | ~0.7        | ~0.7       | ~0.8 | ~0.95 |
| Mar   | ~0.6        | ~0.65      | ~0.7 | ~0.8 |
| Apr   | ~0.7        | ~0.75      | ~0.85| ~0.9 |
| May   | ~0.75       | ~0.75      | ~0.9 | ~0.95|
| Jun   | ~0.8        | ~0.75      | ~0.95| ~1.0 |
| Jul   | ~0.8        | ~0.75      | ~1.0 | ~1.0 |
| Aug   | ~0.75       | ~0.75      | ~0.95| ~0.95|
| Sep   | ~0.7        | ~0.75      | ~0.9 | ~0.95|
| Oct   | ~0.7        | ~0.75      | ~1.05| ~1.05|
| Nov   | ~0.7        | ~0.75      | ~1.05| ~1.05|
| Dec   | ~0.7        | ~0.75      | ~0.95| ~0.95|
</details>

Source: Elane Shipping Statistics, JPM.

Figure 2.6: Deadweight tonnage of arrived ships - Bulk  
![](images/255c5e021cd3eac15ad1e31880dbae53f5b7eaea5210fcaacdb18ad58176936b.jpg)

<details>
<summary>line chart</summary>

| Month | 19-24 range | 19-24 ave. | 2025 | 2026 |
|-------|-------------|------------|------|------|
| Jan   | ~9.5        | ~9.5       | ~9.0 | ~6.0 |
| Feb   | ~9.0        | ~8.5       | ~7.5 | ~9.5 |
| Mar   | ~8.5        | ~8.0       | ~8.0 | ~7.0 |
| Apr   | ~9.0        | ~8.5       | ~8.5 | ~10.0 |
| May   | ~9.5        | ~9.0       | ~9.0 | ~10.5 |
| Jun   | ~10.0       | ~9.5       | ~9.5 | ~12.0 |
| Jul   | ~9.5        | ~9.0       | ~9.0 | ~10.0 |
| Aug   | ~9.0        | ~8.5       | ~8.5 | ~9.5 |
| Sep   | ~9.5        | ~9.0       | ~9.0 | ~10.0 |
| Oct   | ~10.0       | ~9.5       | ~9.5 | ~10.5 |
| Nov   | ~9.5        | ~9.0       | ~9.0 | ~10.0 |
| Dec   | ~9.0        | ~8.5       | ~8.5 | ~9.5 |
</details>

Source: Elane Shipping Statistics, JPM.

Figure 2.7: Deadweight tonnage of arrived ships - Oil Tanker  
![](images/cc705ae49c736526331a0cd0042abf8928e198482d9a47098f585e1301278e46.jpg)

<details>
<summary>line chart</summary>

| Month | 19-24 range | 19-24 ave. | 2025 | 2026 |
|-------|-------------|------------|------|------|
| Jan   | ~2.8        | ~2.7       | ~2.6 | ~3.0 |
| Feb   | ~2.9        | ~2.8       | ~2.7 | ~3.5 |
| Mar   | ~3.0        | ~2.9       | ~2.8 | ~4.0 |
| Apr   | ~2.8        | ~2.7       | ~2.7 | ~3.0 |
| May   | ~2.7        | ~2.6       | ~2.6 | ~1.7 |
| Jun   | ~2.8        | ~2.7       | ~2.7 | ~2.0 |
| Jul   | ~3.0        | ~2.8       | ~2.8 | ~3.0 |
| Aug   | ~3.5        | ~3.0       | ~3.0 | ~3.5 |
| Sep   | ~3.8        | ~3.2       | ~3.2 | ~3.8 |
| Oct   | ~3.5        | ~3.0       | ~3.0 | ~4.0 |
| Nov   | ~3.8        | ~3.2       | ~3.5 | ~4.0 |
| Dec   | ~3.5        | ~3.0       | ~3.0 | ~3.5 |
</details>

Source: Elane Shipping Statistics, JPM.

Figure 2.8: Deadweight tonnage of departing ships - Oil Tanker  
![](images/2039b27edc4f405ffbf4f1417773f50eb4849c623104060b2f326de80037faea.jpg)

<details>
<summary>line chart</summary>

| Month | 19-24 range | 19-24 ave. | 2025 | 2026 |
|-------|-------------|------------|------|------|
| Jan   | ~3.0        | ~2.8       | ~2.7 | ~3.4 |
| Feb   | ~3.0        | ~2.7       | ~2.6 | ~3.3 |
| Mar   | ~3.0        | ~2.6       | ~2.5 | ~3.5 |
| Apr   | ~3.0        | ~2.5       | ~2.6 | ~3.1 |
| May   | ~3.0        | ~2.4       | ~2.5 | ~1.5 |
| Jun   | ~3.0        | ~2.5       | ~2.6 | ~1.8 |
| Jul   | ~3.0        | ~2.6       | ~2.7 | ~2.0 |
| Aug   | ~3.0        | ~2.7       | ~2.8 | ~2.2 |
| Sep   | ~3.0        | ~2.8       | ~2.9 | ~2.4 |
| Oct   | ~3.0        | ~2.9       | ~3.0 | ~2.6 |
| Nov   | ~3.0        | ~3.0       | ~3.1 | ~3.0 |
| Dec   | ~3.0        | ~3.1       | ~3.2 | ~3.1 |
</details>

Source: Elane Shipping Statistics, JPM.

Figure 2.9: China flight execution  
![](images/cb605051521e6bd6da946d757d16d342abd037d8133eca38c3104fe92e13aff3.jpg)

<details>
<summa

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market

conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 16 Jun 2026 01:55 AM HKT

Disseminated 16 Jun 2026 01:55 AM HKT
"""
