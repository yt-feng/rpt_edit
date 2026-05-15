你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Global Gas

# Storage rebuilds uneven

# Firmer prompt-led TTF; limited LNG cargoes exit the Gulf

Front-month TTF is grinding higher toward €50/MWh, with the curve remaining prompt-led and the seasonal spread hovering to flat to slightly negative (up to -€1.5), limiting EU storage injections. Several LNG tankers have recently exited the Gulf (link), but the additional volumes remain insufficient to ease market balances. Meanwhile, The JKM-TTF spreads persist at \$1-2/mmBtu, maintaining Asia's competitiveness for marginal US cargoes. Should current disruptions persist, further tightening of the summer market is likely. Relief from Chinese LNG resales is diminishing: following a surge in March (10 resales) and a sharp slowdown in April (down to 1), activity remains subdued in May. Meanwhile, China is poised to resume direct imports of US LNG, with three cargoes expected to arrive between mid and late June (link), potentially signalling an improvement in energy relations between the two countries.

# LNG cargo trackers: US export to Asia remains robust

Asian LNG imports fell by 5% w/w, and were 1% lower than a year ago (Figure 11), with arrivals over the past four weeks down 9% y/y, as per UBS Evidence Lab's waterborne data (>Access Dataset). The most recent datapoint on an arrival basis is as of 10 May. US exports to Asia decreased by 21%, though they remain more than 60% above last year's level based on data from the past four weeks. US LNG exports to Europe dominate at nearly 60%, but the share of flows to Asia has increased by >10% to reach 33% compared to pre-conflict periods.

# EU injections slows on lower LNG arrivals

As of 12 May, European gas storage is $36\%$ full, vs. $43\%$ a year ago and $48\%$ for the five-year average. Net injections over the past week amounted to 1.5bcm, below last year's 1.8bcm and the seasonal norm of 2.0bcm. LNG arrivals were down $6\%$ w/w and $11\%$ y/y for the week. At the current injection rate, we estimate that EU storage would reach about $86\%$ full before next winter. However, we anticipate the pace will slow as the market tightens, and our base case forecast storage levels at $80\%$ full. (Agsi+, UBS)

# US gas stocks injection in line with consensus

The EIA reported US natgas storage injection of +85Bcf, in line with consensus. As of 8 May, inventories stood at 2,290Bcf, with storage utilisation 54% (vs. the 5-year average of 50%). Japan's METI reported utility gas stocks were slightly up to 2.9bcm as of 10 May broadly in line with the seasonal norm. (EIA, Datastream, METI, UBS)

Figure 1: Gas storage utilisation levels in the EU   
![](images/6dcf06b5f25a91ce951d731b036e83e7636dc29d3f317227bef17dabfe6cd89c.jpg)

<details>
<summary>line</summary>

| Month | 10-year range 2015-2024 | 10-year average | 2024 | 2025 | 2026 |
|-------|--------------------------|-----------------|------|------|------|
| Jan   | ~85%                     | ~70%            | ~85% | ~70% | ~60% |
| Feb   | ~75%                     | ~60%            | ~75% | ~60% | ~45% |
| Mar   | ~65%                     | ~50%            | ~65% | ~50% | ~35% |
| Apr   | ~60%                     | ~45%            | ~60% | ~45% | ~30% |
| May   | ~65%                     | ~50%            | ~65% | ~50% | ~35% |
| Jun   | ~70%                     | ~55%            | ~70% | ~55% | ~40% |
| Jul   | ~75%                     | ~60%            | ~75% | ~60% | ~50% |
| Aug   | ~80%                     | ~65%            | ~80% | ~65% | ~60% |
| Sep   | ~85%                     | ~70%            | ~85% | ~70% | ~75% |
| Oct   | ~90%                     | ~75%            | ~90% | ~75% | ~80% |
| Nov   | ~95%                     | ~80%            | ~95% | ~80% | ~80% |
| Dec   | ~90%                     | ~75%            | ~90% | ~75% | ~70% |
</details>

Source: AGSI+, UBS

# Equities

Global

Energy

Nayoung Kim

Analyst

nayoung.kim@UBS.com

+44-20-7568 4010

Henri Patricot, CFA

Analyst

henri.patricot@UBS.com

+33-14-888 3033

Joshua Stone

Analyst

joshua.stone@UBS.com

+44-20-7901 5588

Josh Silverstein

Analyst

josh.silverstein@UBS.com

+1-212-713 3513

Ellinor Cederstroem Palliotto

Associate Analyst

ellinor-cederstroem.palliotto@UBS.com

+44-20-7567 1823

Leo Currie

Associate Analyst

leo.currie@UBS.com

+44-20-7567 0642

Figure 2: Gas storage utilisation levels in the US   
![](images/537792b0b50490b59eed30307d7afcde1b97e894978e824403cc1c1332f263e7.jpg)

<details>
<summary>line</summary>

| Month | Range 2021-2025 | 2025 | 2026 | 5-year average |
|-------|-----------------|------|------|----------------|
| Jan   | ~75%            | ~80% | ~78% | ~76%           |
| Feb   | ~65%            | ~70% | ~68% | ~66%           |
| Mar   | ~45%            | ~40% | ~42% | ~43%           |
| Apr   | ~50%            | ~48% | ~49% | ~47%           |
| May   | ~55%            | ~58% | ~56% | ~54%           |
| Jun   | ~60%            | ~65% | ~63% | ~61%           |
| Jul   | ~65%            | ~70% | ~68% | ~66%           |
| Aug   | ~70%            | ~75% | ~73% | ~71%           |
| Sep   | ~75%            | ~80% | ~78% | ~76%           |
| Oct   | ~80%            | ~85% | ~83% | ~81%           |
| Nov   | ~85%            | ~90% | ~88% | ~86%           |
| Dec   | ~75%            | ~80% | ~78% | ~76%           |
</details>

Source: EIA, UBS

# GAS STORAGE CHARTS

Figure 3: European gas balance through winter 2025/2026 and Summer 2026 (bcm)   
![](images/370b30cb1deaaa7a0ffd8bd60934f0d001bba6b74ab25c8bd2c5b376db2d2881.jpg)

<details>
<summary>bar</summary>

| Category | Value |
| :--- | :--- |
| End storage Oct-25 | 85 |
| Total supply | 176 |
| Total demand | -233 |
| End storage Mar-26 | 28 |
| Production | 35 |
| Russian piped gas | 6 |
| Ex-Russian piped gas | 94 |
| LNG | 89 |
| Power | -57 |
| Industry | -55 |
| Household | -31 |
| Other | -27 |
| End storage Oct-26 | 83 |
</details>

Source: AGSI+, UBS Evidence Lab (> Access Dataset), ENTSOG TP, USGS, UBS estimates

Figure 4: Gas storage weekly injection/withdrawal rates on a rolling basis (bcm)   
![](images/680b0a695c3382234b565af5298927eabbf2752418a08b7f08be91d5db3a8d4e.jpg)

<details>
<summary>line</summary>

| Month | 2024 | 2025 | 2026 |
|-------|------|------|------|
| Jan   | -1.0 | -3.0 | -4.0 |
| Feb   | -3.0 | -5.0 | -6.0 |
| Mar   | -2.0 | -4.0 | -3.0 |
| Apr   | 0.0  | -1.0 | 0.0  |
| May   | 2.0  | 1.0  | 1.5  |
| Jun   | 3.0  | 2.0  | 2.5  |
| Jul   | 2.0  | 2.0  | 2.0  |
| Aug   | 2.0  | 2.0  | 2.0  |
| Sep   | 1.0  | 1.5  | 1.5  |
| Oct   | 0.0  | 0.5  | 0.5  |
| Nov   | -1.0 | -1.5 | -1.5 |
| Dec   | -3.0 | -4.0 | -4.0 |
</details>

Source: AGSI+, UBS estimates

Figure 5: European gas injections run rate and implications for European storage levels   
![](images/9f977a9654fc550cd96ca35ac7969937b2b44006a059c4576d2c040a96a2c1ce.jpg)

<details>
<summary>line</summary>

| Date     | Weekly injections (LHS) | 10-year average (LHS) | Required (seasonally adjusted, LHS) | Storage | Path on current run rate (RHS) |
|----------|--------------------------|------------------------|-------------------------------------|---------|-------------------------------|
| 01-Apr   | 1.2                      | 0.0                    | 1.3                                 | 0.0     | 30%                           |
| 01-May   | 2.1                      | 1.6                    | 2.4                                 | 0.2     | 40%                           |
| 01-Jun   | 2.5                      | 2.6                    | 3.0                                 | 0.5     | 50%                           |
| 01-Jul   | 2.4                      | 2.4                    | 2.8                                 | 1.0     | 60%                           |
| 01-Aug   | 2.3                      | 2.4                    | 2.9                                 | 1.5     | 70%                           |
| 01-Sep   | 2.0                      | 2.4                    | 2.8                                 | 2.0     | 75%                           |
| 01-Oct   | 1.0                      | 1.2                    | 1.5                                 | 2.5     | 80%                           |
</details>

Source: AGSI+, UBS Evidence Lab (> Access Dataset), ENTSOG TP, USGS, UBS estimates. Note: Current run rate reflects pace since early May.

Figure 6: EU countries' current storage levels 

<table><tr><td rowspan="2"></td><td rowspan="2">Storage Capacity (bcm)</td><td rowspan="2">Previous report 06 May</td><td rowspan="2">Current Levels As of 12 May</td><td colspan="2">w/w change</td></tr><tr><td>%</td><td>mcm</td></tr><tr><td>Austria</td><td>9.0</td><td>40.6%</td><td>42.5%</td><td>1.9%</td><td>169</td></tr><tr><td>Belgium</td><td>0.7</td><td>24.4%</td><td>23.8%</td><td>-0.6%</td><td>-5</td></tr><tr><td>Bulgaria</td><td>0.6</td><td>22.7%</td><td>22.6%</td><td>0.0%</td><td>0</td></tr><tr><td>Czech Republic</td><td>4.1</td><td>30.6%</td><td>32.5%</td><td>1.9%</td><td>76</td></tr><tr><td>Germany</td><td>22.3</td><td>27.2%</td><td>28.1%</td><td>0.9%</td><td>199</td></tr><tr><td>Denmark</td><td>0.8</td><td>39.5%</td><td>42.4%</td><td>2.9%</td><td>27</td></tr><tr><td>Spain</td><td>3.2</td><td>65.5%</td><td>66.2%</td><td>0.7%</td><td>23</td></tr><tr><td>France</td><td>11.1</td><td>34.9%</td><td>36.6%</td><td>1.8%</td><td>212</td></tr><tr><td>Croatia</td><td>0.4</td><td>19.7%</td><td>21.9%</td><td>2.2%</td><td>9</td></tr><tr><td>Hungary</td><td>6.1</td><td>36.2%</td><td>38.3%</td><td>2.1%</td><td>127</td></tr><tr><td>Italy</td><td>18.3</td><td>51.5%</td><td>53.5%</td><td>2.0%</td><td>364</td></tr><tr><td>Latvia</td><td>2.2</td><td>26.9%</td><td>27.3%</td><td>0.4%</td><td>9</td></tr><tr><td>Netherlands</td><td>12.9</td><td>11.0%</td><td>11.8%</td><td>0.9%</td><td>111</td></tr><tr><td>Poland</td><td>3.3</td><td>46.4%</td><td>48.9%</td><td>2.4%</td><td>82</td></tr><tr><td>Portugal</td><td>0.3</td><td>91.3%</td><td>91.3%</td><td>0.0%</td><td>0</td></tr><tr><td>Romania</td><td>3.0</td><td>29.2%</td><td>31.6%</td><td>2.4%</td><td>73</td></tr><tr><td>Sweden</td><td>0.0</td><td>9.9%</td><td>9.9%</td><td>0.0%</td><td>0</td></tr><tr><td>Slovakia</td><td>3.3</td><td>24.9%</td><td>26.5%</td><td>1.6%</td><td>53</td></tr><tr><td>Total EU</td><td>101.8</td><td>34.3%</td><td>35.7%</td><td>1.5%</td><td>1,512</td></tr></table>

Source: Agsi+, UBS

Figure 7: EU weekly gas consumption on a 4-week rolling average basis (bcm)   
![](images/bc3307bdc6ba9429d3694cae07e8e77b083f780e8dc38ec612b5cc1f35a65d53.jpg)

<details>
<summary>area</summary>

| Month | Range 2020-2024 | 2024 | 2025 | 2026 | 5-year average (2021-2025) |
|-------|-----------------|------|------|------|----------------------------|
| Jan   | ~9.5            | ~7.5 | ~9.0 | ~9.5 | ~8.8                       |
| Feb   | ~11.0           | ~8.5 | ~10.5| ~10.5| ~9.3                       |
| Mar   | ~10.5           | ~7.0 | ~9.5 | ~9.0 | ~8.5                       |
| Apr   | ~7.5            | ~5.5 | ~6.0 | ~5.0 | ~6.0                       |
| May   | ~4.5            | ~4.0 | ~4.0 | ~4.0 | ~3.5                       |
| Jun   | ~3.5            | ~3.0 | ~3.5 | ~3.5 | ~3.0                       |
| Jul   | ~3.5            | ~3.0 | ~3.5 | ~3.5 | ~3.0                       |
| Sep   | ~3.5            | ~3.0 | ~3.5 | ~3.5 | ~3.0                       |
| Oct   | ~4.0            | ~4.0 | ~4.5 | ~4.5 | ~4.0                       |
| Nov   | ~6.0            | ~5.5 | ~6.5 | ~6.5 | ~6.0                       |
| Dec   | ~8.0            | ~8.5 | ~9.5 | ~9.5 | ~8.5                       |
</details>

Source: Eurostat, AGSI+, ESRI, UBS Evidence Lab ( $>$ Access Dataset), ENTSOG TP, USGS, UBS estimates

Figure 8: EU weekly pipeline gas imports on a 4-week rolling average basis (bcm)   
![](images/d430e866799520496b1d6258e15872fccc1cea1f4a53c699e80c428e90785984.jpg)

<details>
<summary>area</summary>

| Month | Range 2020-2024 | 2024 | 2025 | 2026 | 5-year average (2021-2025) |
|-------|-----------------|------|------|------|-----------------------------|
| Jan   | ~4.3            | ~2.5 | ~2.6 | ~2.5 | ~3.1                        |
| Feb   | ~4.4            | ~2.5 | ~2.6 | ~2.7 | ~3.1                        |
| Mar   | ~4.5            | ~2.5 | ~2.6 | ~2.8 | ~3.2                        |
| Apr   | ~4.4            | ~2.6 | ~2.6 | ~2.7 | ~3.3                        |
| May   | ~4.3            | ~2.6 | ~2.6 | ~2.6 | ~3.1                        |
| Jun   | ~4.4            | ~2.7 | ~2.6 | ~2.5 | ~3.0                        |
| Jul   | ~4.3            | ~2.6 | ~2.8 | ~2.6 | ~3.0                        |
| Aug   | ~4.3            | ~2.6 | ~2.7 | ~2.5 | ~3.0                        |
| Sep   | ~4.3            | ~2.5 | ~2.6 | ~2.4 | ~3.0                        |
| Oct   | ~4.3            | ~2.0 | ~2.1 | ~2.1 | ~2.7                        |
| Nov   | ~4.1            | ~2.6 | ~2.6 | ~2.6 | ~2.9                        |
| Dec   | ~4.0            | ~2.6 | ~2.6 | ~2.6 | ~2.9                        |
</details>

Source: UBS Evidence Lab (> Access Dataset), ENTSOG TP, USGS

Figure 9: EU weekly LNG imports on a 4-week rolling average basis (bcm)   
![](images/8954e06483c073ab37b92b9fdaeeade01a1a7169614978fe90070acbcbedf9b4.jpg)

<details>
<summary>area</summary>

| Month | Range 2020-2024 | 2024 | 2025 | 2026 | 5-year average (2021-2025) |
|-------|-----------------|------|------|------|-----------------------------|
| Jan   | ~0.6            | ~2.1 | ~2.1 | ~2.7 | ~1.7                        |
| Feb   | ~0.4            | ~2.1 | ~2.3 | ~2.8 | ~1.7                        |
| Mar   | ~1.4            | ~2.3 | ~2.5 | ~3.0 | ~1.9                        |
| Apr   | ~1.5            | ~2.1 | ~2.7 | ~2.8 | ~2.1                        |
| May   | ~1.3            | ~1.9 | ~2.8 | ~2.7 | ~2.0                        |
| Jun   | ~1.0            | ~1.8 | ~2.8 | ~2.6 | ~1.9                        |
| Jul   | ~0.8            | ~1.7 | ~2.5 | ~2.4 | ~1.8                        |
| Aug   | ~0.7            | ~1.6 | ~2.3 | ~2.1 | ~1.7                        |
| Sep   | ~0.7            | ~1.5 | ~2.1 | ~2.1 | ~1.6                        |
| Oct   | ~0.8            | ~1.7 | ~2.4 | ~2.5 | ~1.8                        |
| Nov   | ~0.9            | ~1.9 | ~2.7 | ~2.8 | ~2.0                        |
| Dec   | ~1.0            | ~2.3 | ~2.7 | ~2.7 | ~2.1                        |
</details>

Source: UBS Evidence Lab (> Access Dataset), ENTSOG TP, USGS

Figure 10: Japan's LNG stocks held by utils (bcm)   
![](images/5ba138a3f25820900c110acb704521b34970e31c0b75c212b308db91c6db448f.jpg)

<details>
<summary>area</summary>

| Month | 5-yr range | 2025 | 2026 | 5-yr average |
|-------|------------|------|------|--------------|
| Jan   | 3.8        | 3.1  | 3.2  | 3.0          |
| Feb   | 4.0        | 3.3  | 3.1  | 3.1          |
| Mar   | 3.7        | 2.7  | 2.6  | 2.9          |
| Apr   | 3.4        | 2.9  | 3.2  | 2.8          |
| May   | 3.5        | 2.7  | 2.9  | 3.0          |
| Jun   | 3.4        | 3.2  | 2.8  | 2.9          |
| Jul   | 3.2        | 2.6  | 2.7  | 2.8          |
| Aug   | 3.5        | 2.8  | 2.9  | 2.9          |
| Sep   | 3.1        | 2.4  | 2.5  | 2.7          |
| Oct   | 3.0        | 2.6  | 2.7  | 2.8          |
| Nov   | 3.3        | 3.1  | 2.9  | 3.0          |
| Dec   | 3.8        | 3.3  | 3.2  | 3.2          |
</details>

Source: Datastream, METI,

Figure 11: Global LNG exports to Asia (on an arrival basis; DWT in million)   
![](images/7cc5ec048d3c5b7851f7fb5b4fe2d36ed2961b5539add08f7a2d41b9ba9da09e.jpg)

<details>
<summary>line</summary>

| Month | 2024 | 2025 | 2026 |
|-------|------|------|------|
| Jan   | 8.3  | 7.9  | 7.7  |
| Feb   | 8.0  | 6.3  | 8.9  |
| Mar   | 7.8  | 8.3  | 8.1  |
| Apr   | 8.0  | 7.0  | 6.0  |
| May   | 7.8  | 6.5  | 5.9  |
| Jun   | 7.5  | 7.8  | -    |
| Jul   | 7.3  | 7.5  | -    |
| Aug   | 8.5  | 6.5  | -    |
| Sep   | 7.5  | 9.5  | -    |
| Oct   | 8.3  | 7.5  | -    |
| Nov   | 7.8  | 7.0  | -    |
| Dec   | 9.5  | 8.8  | -    |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Figure 12: US exports to Asia (DWT in million)   
![](images/718cc5cebf5294c0a5d08d5b838bc601c8071ef87ade3be2d7e7aab40a90d7f7.jpg)

<details>
<summary>area</summary>

| Month | Range | 2025 | 2026 | 5-year average (2021-25) |
|-------|-------|------|------|--------------------------|
| Jan   | 1.3   | 0.9  | 0.85 | 0.8                      |
| Feb   | 1.2   | 0.45 | 0.75 | 0.55                     |
| Mar   | 1.3   | 0.6  | 0.3  | 0.6                      |
| Apr   | 0.9   | 0.75 | 0.65 | 0.4                      |
| May   | 0.6   | 0.3  | 1.05 | 0.4                      |
| Jun   | 0.8   | 0.65 | -    | 0.6                      |
| Jul   | 1.1   | 0.5  | -    | 0.7                      |
| Aug   | 0.8   | 0.75 | -    | 0.5                      |
| Sep   | 0.9   | 0.65 | -    | 0.7                      |
| Oct   | 1.1   | 0.75 | -    | 0.6                      |
| Nov   | 1.3   | 0.95 | -    | 0.85                     |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Figure 13: US exports to Europe (DWT in million)   
![](images/5ea46ccbcf8e86549fe67a9c3a17100c1f449db05d36bba40448fd5984983585.jpg)

<details>
<summary>area</summary>

| Month | Range | 2025 | 2026 | 5-year average (2021-25) |
|-------|-------|------|------|--------------------------|
| Jan   | 0.8   | 1.5  | 2.4  | 1.0                      |
| Feb   | 0.1   | 1.9  | 1.8  | 1.1                      |
| Mar   | 0.4   | 1.7  | 2.3  | 1.2                      |
| Apr   | 0.6   | 2.5  | 1.7  | 1.4                      |
| May   | 0.5   | 1.8  | 1.5  | 1.3                      |
| Jun   | 0.3   | 1.6  | -    | 1.1                      |
| Jul   | 0.2   | 1.7  | -    | 1.0                      |
| Aug   | 0.1   | 1.8  | -    | 0.9                      |
| Sep   | 0.3   | 1.9  | -    | 1.0                      |
| Oct   | 0.4   | 2.0  | -    | 1.1                      |
| Nov   | 0.5   | 2.1  | -    | 1.2                      |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Figure 14: LNG tanker arrivals in Japan (DWT in million)   
![](images/17da9654129a5af09ff5a538d7fbca40c4f7135f53e3d16ac7f5f0ea68e3156d.jpg)

<details>
<summary>line</summary>

| Month | 5-year range | 2025 | 2026 | 5-year average |
|-------|--------------|------|------|----------------|
| Jan   | ~2.4         | ~2.4 | ~1.1 | ~2.1           |
| Feb   | ~2.9         | ~1.8 | ~2.5 | ~2.3           |
| Mar   | ~2.6         | ~1.5 | ~1.9 | ~2.0           |
| Apr   | ~2.1         | ~1.4 | ~1.3 | ~1.7           |
| May   | ~1.9         | ~1.3 | ~1.1 | ~1.6           |
| Jun   | ~1.8         | ~1.4 | ~1.4 | ~1.5           |
| Jul   | ~2.0         | ~1.5 | ~1.5 | ~1.7           |
| Aug   | ~2.1  

[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, sUBSidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.UBS.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its sUBSidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/46958a323a85853b016e8714d99665d5008cb7322b42c90763352c06862f80ff.jpg)
"""
