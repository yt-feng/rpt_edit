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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Agribusiness | Latin America

# Because You Asked: What If We Have a Super El Niño This Year?

NOAA has confirmed an El Niño for this year & raised the probability of a very strong event to 63%. It could rank among the strongest El Niños ever, with especially large implications for commodities, inflation, growth, FX, equities & regional economies. We take a first look at what may be ahead.

## Key Takeaways

NOAA's probability of a very strong El Nino during Nov-Jan has increased significantly, to 63% (from 37%); it could rank among the strongest such events ever.  
Tail risk has increased ... but some experts caution about extrapolating to “super El Niño” as confidence declines further out the curve.  
As we gain clarity on the scale of El Niño, we intend to work with our global colleagues to address the implications for commodities, FX, equities & economies.  
Commodity implications mixed: Upside risk is clearest for sugar, palm oil, cotton (El Niño drought tightening supply); timing should be key for corn and soy.  
Equity implications vary meaningfully: Possible beneficiaries SMTO3 and ADECO; higher risks for SLCE3 and RAIL3.

El Niño has officially formed. NOAA's US Climate Prediction Center issued an El Niño Advisory this morning, confirming that Pacific Ocean surface temperatures have warmed sufficiently to trigger an atmospheric response while the strength distribution has shifted toward stronger outcomes.

El Niño is moving from weather noise to investment signal. According to NOAA's latest framework there is a $63\%$ chance it evolves into a very strong event — potentially one of the strongest on record. The market is asking the right question — not simply whether El Niño will form, but whether it will strengthen early enough to hit the crop windows that matter for sugar, soybeans, corn, logistics volumes, and listed agribusiness equities.

Recent rapid ocean warming explains more extreme model outputs, and tail risk has increased, though the probability-weighted guidance does not predict a record event yet and some experts caution about extrapolating to super El Niño as confidence declines further out the curve. As we gain clarity on the scale of El Niño, we intend to work with our global colleagues to address the implications for commodities, FX, equities, and regional economies.

MS C.T.V.M. S.A.+

## Julia Rizzo

Equity Analyst and Commodities Strategist

Julia.Rizzo@morganstanley.com

+55 11 3048-6114

## Julia Habermann

Research Associate

Julia.Habermann.Oliveira@morganstanley.com

+55 11 3048-6096

## LATAM AGRIBUSINESS

## Latin America

Industry View

In-Line

Exhibit 3: The event is still in its early stages, but forecasters broadly expect conditions to worsen materially through late 2026.

<table><tr><td>Segment</td><td>Implication</td><td>Investor Takeaway</td></tr><tr><td>Ag (Softs)</td><td>Analogues point to tighter sugar/palm supply (dryness), with more mixed coffee dynamics.</td><td>Bullish softs skew, led by sugar/palm; coffee more path-dependent.</td></tr><tr><td>India Monsoon</td><td>Downside rainfall risk; tighter supply.</td><td>Support for sugar prices. India is world&#x27;s 2nd largest sugar producer.</td></tr><tr><td>Food</td><td>Adds to already elevated food inflation (supply + tariff backdrop).</td><td>Upward pressure on grocery prices into 2027.</td></tr><tr><td>Fishing (Peru)</td><td>Warming waters disrupting anchovy harvest.</td><td>Fishmeal supply risk, feeds into livestock costs.</td></tr><tr><td>Shipping (Panama Canal)</td><td>Risk of renewed water constraints; contingency planning underway.</td><td>Tail risk to trade flows/freight costs.</td></tr><tr><td>Ag (South Africa)</td><td>Drought risk into key planting window.</td><td>Incremental upside to global crop prices.</td></tr><tr><td>Wildfires</td><td>Already elevated activity; conditions likely to worsen. Brazil CS sugar crop.</td><td>Rising physical risk exposure across assets.</td></tr></table>

Source: MS.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Exhibit 1: Central/eastern Pacific SST anomalies are now clearly positive, confirming the ocean-side setup for a likely very strong El Niño  
Relative SST Anomalies (°C)  
03 JUN 2026  
![](images/03843a9c81852c58ebb79c55fca05fa90de551bf7af88aa6e2b82da1e358a5e7.jpg)

<details>
<summary>heatmap</summary>

| Latitude | Longitude | Value |
| -------- | --------- | ----- |
| 30N      | 120E      | -3    |
| 30N      | 140E      | -2    |
| 30N      | 160E      | -1    |
| 30N      | 180E      | 0     |
| 30N      | 160W      | 0.5   |
| 30N      | 140W      | 1     |
| 30N      | 120W      | 2     |
| 30N      | 100W      | 3     |
| 30N      | 80W       | 3     |
| 20N      | 120E      | -3    |
| 20N      | 140E      | -2    |
| 20N      | 160E      | -1    |
| 20N      | 180E      | 0     |
| 20N      | 160W      | 0.5   |
| 20N      | 140W      | 1     |
| 20N      | 120W      | 2     |
| 20N      | 100W      | 3     |
| 20N      | 80W       | 3     |
| 10N      | 120E      | -3    |
| 10N      | 140E      | -2    |
| 10N      | 160E      | -1    |
| 10N      | 180E      | 0     |
| 10N      | 160W      | 0.5   |
| 10N      | 140W      | 1     |
| 10N      | 120W      | 2     |
| 10N      | 100W      | 3     |
| 10N      | 80W       | 3     |
| EQ       | 120E      | -3    |
| EQ       | 140E      | -2    |
| EQ       | 160E      | -1    |
| EQ       | 180E      | 0     |
| EQ       | 160W      | 0.5   |
| EQ       | 140W      | 1     |
| EQ       | 120W      | 2     |
| EQ       | 100W      | 3     |
| EQ       | 80W       | 3     |
| 10S      | 120E      | -3    |
| 10S      | 140E      | -2    |
| 10S      | 160E      | -1    |
| 10S      | 180E      | 0     |
| 10S      | 160W      | 0.5   |
| 10S      | 140W      | 1     |
| 10S      | 120W      | 2     |
| 10S      | 100W      | 3     |
| 10S      | 80W       | 3     |
| 20S      | 120E      | -3    |
| 20S      | 140E      | -2    |
| 20S      | 160E      | -1    |
| 20S      | 180E      | 0     |
| 20S      | 160W      | 0.5   |
| 20S      | 140W      | 1     |
| 20S      | 120W      | 2     |
| 20S      | 100W      | 3     |
| 20S      | 80W       | 3     |
| 30S      | 120E      | -3    |
| 30S      | 140E      | -2    |
| 30S      | 160E      | -1    |
| 30S      | 180E      | 0     |
| 30S      | 160W      | 0.5   |
| 30S      | 140W      | 1     |
| 30S      | 120W      | 2     |
| 30S      | 100W      | 3     |
| 30S      | 80W       | 3     |
</details>

Source: NOAA.

The current setup points to a strong to very strong event that peaks in late 2026 / early 2027 (ONDJ), similar to very strong events analogs in 1982/83, 1997/98, and 2015/16. Tail risk has increased, but the historical “super” comparison still requires confirmation through summer ocean-atmosphere coupling, observed Niño 3.4 warming, and model convergence after the spring predictability barrier. A key open question is whether the event can exceed a +2.5°C anomaly and surpass past extremes; by definition, El Niño reflects sustained warming in the central equatorial Pacific, with global spillovers via shifts in rainfall patterns and temperature distributions

Early signals point to meaningful weather disruption in Brazil — excess rainfall in the South/Center-South and irregular precipitation elsewhere — creating downside risk to crop timing and yields (soy delays, second-crop corn vulnerability) and early evidence of quality losses in key crops (sugar, coffee, cotton) as out-of-season rains persist.

Sugar is the most sensitive to El Nino effects. In theory, sugar has the clearest upside skew because potential drought in Asia — down the curve (27/28), since in the short-term prices may still be pressured by ample supply from ongoing Brazilian harvest. Soybeans are more complicated: In Brazil, 26/27 Mato Grosso and MATOPIBA carry downside risk, while Rio Grande do Sul and Argentina often benefit. Corn is a timing trade on Brazil safrinha (second corn harvest; 80% of national production) compression and US summer stress.

Equity implications vary meaningfully: All else equal, El Niño can be constructive for São Martinho (higher sugar prices) and Adecoagro (improved Argentina rainfall), while more challenging for Rumo and a weather-risk factor for SLC Agrícola. For Rumo and SLC, investors should closely monitor Mato Grosso / MATOPIBA rainfall, planting pace, and the safrinha setup.

What to watch for? Three things. First, whether the event keeps strengthening through the North Hemisphere summer. Second, whether sugar supply risk starts to materialize through India/SE Asia crop stress or weaker Brazil crush execution. Third, whether grain risk becomes tangible through US summer stress and Brazil planting delays

Exhibit 2: NOAA/CPC now assigns a 63% (up from 37%) probability to a very strong El Niño in Nov-Jan, making intensity the key watchpoint  
NOAA CPC ENSO Strength Probabilities (issued June 2026)  
![](images/511eee916e661c6b3da7c7cc970dd8753ecb1acebf18aab83070ba0a82ecf46e.jpg)

<details>
<summary>stacked bar chart</summary>

based on thresholds in ERSSTv5 Relative Niño-3.4 index/RONI
| Season | Very Strong El Niño index ≥ 2.0°C (%) | Strong El Niño 1.5°C ≤ index < 2.0°C (%) | Moderate El Niño 1.0°C ≤ index < 1.5°C (%) | Weak El Niño 0.5°C ≤ index < 1.0°C (%) | Neutral -0.5°C < index < 0.5°C (%) | Weak La Niña -0.5°C ≥ index > -1.0°C (%) | Moderate La Niña -1.0°C ≥ index > -1.5°C (%) | Strong La Niña -1.5°C ≥ index > -2.0°C (%) | Very Strong La Niña Index ≤ -2.0°C (%) |
|---|---|---|---|---|---|---|---|---|---|
| MJJ | 0 | 0 | 86 | 13 | 3 | 0 | 0 | 0 | 0 |
| JJA | 0 | 0 | 90 | 27 | 0 | 0 | 0 | 0 | 0 |
| JAS | 0 | 0 | 92 | 28 | 0 | 0 | 0 | 0 | 0 |
| ASO | 0 | 0 | 73 | 19 | 5 | 0 | 0 | 0 | 0 |
| SON | 48 | 34 | 16 | 14 | 0 | 0 | 0 | 0 | 0 |
| OND | 68 | 24 | 11 | 6 | 0 | 0 | 0 | 0 | 0 |
| NDJ | 78 | 27 | 12 | 6 | 0 | 0 | 0 | 0 | 0 |
| DJF | 78 | 34 | 16 | 6 | 0 | 0 | 0 | 0 | 0 |
| JFM | 28 | 37 | 11 | 6 | 1 | 0 | 0 | 0 | 0 |
Stronger events can make it more likely that certain impacts could occur.
</details>

Source: NOAA.

## What investors will find inside

- Why Markets Are Talking About a “Super El Niño” Now: stronger NOAA probabilities, higher subsurface heat, aggressive model tails, and memories of 2015/16.  
- Analog years commodity implications.  
• What to Watch Next.

## Why Markets Are Talking About a 'Super El Niño' Now

The market is reacting to a fatter upper tail risk. NOAA's strength distribution now assigns meaningful odds to strong or very strong El Niño outcomes later this year. That has pushed "super El Niño" language into the market conversation, even though official guidance remains probability-weighted and does not yet confirm a record event.

## The trigger is the combination of probability, subsurface heat, and model dispersion.

The internal work highlights rapid Pacific warming, high subsurface heat, and improving atmospheric alignment as reasons some dynamic models have moved toward more aggressive outcomes. The same work also stresses that spring forecasts are less reliable, keeping the “super” outcome as tail risk rather than central case.

The recent precedent is 2015/16, but the comparison may also include the 2023/24 — and even the 1877/78 event that is considered the most extreme El Niño ever. The 2015/16 event matters because it generated a powerful sugar-price cycle and meaningful agricultural disruption. But the internal analog work suggests current conditions also look closer to the gradual 2023/24 trajectory versus a confirmed 2015/16-style extreme.

The market likely prices El Niño probability, but not the crop-window distribution. Investors already know El Niño can alter rainfall patterns. What is less fully priced is whether the event hits the exact windows that matter: India's monsoon, Brazil's Center-South cane crush, Mato Grosso / MATOPIBA soybean planting, and the safrinha corn calendar.

Exhibit 4: El Niño is now confirmed, while very-strong odds increased to 63% in Nov-Jan from 37% in the prior update

<table><tr><td>Topic</td><td>Prior update</td><td>June update</td><td>Implication</td></tr><tr><td>ENSO status</td><td>El Niño Watch / transition risk rising</td><td>El Niño Advisory / conditions now present</td><td>Formation risk is largely de-risked</td></tr><tr><td>El Niño probability</td><td>82% in MJJ; 96% in DJF</td><td>97% in MJJ; 99% in DJF; 99–100% JJA–NDJ</td><td>Persistence into winter is now high confidence</td></tr><tr><td>Strength</td><td>37% very strong in Nov-Jan; 33% in Oct-Dec; 31% in Dec-Feb</td><td>63% very strong in Nov-Jan; 62% in Oct-Dec; 46% in Dec-Feb</td><td>Very strong scenario is now material</td></tr><tr><td>Ocean signal</td><td>Niño 3.4 +0.4°C; Niño 4 +0.5°C; Niño 1+2 +1.0°C</td><td>Niño 3.4 +0.7°C; Niño 4 +0.7°C; Niño 1+2 +2.1°C</td><td>Warming has broadened and intensified</td></tr><tr><td>Atmosphere</td><td>Coupling still pending</td><td>Westerly low-level wind anomalies, negative SOI and convection changes</td><td>Ocean-atmosphere coupling now supports advisory</td></tr><tr><td>Commodity read-through</td><td>Sugar cleanest channel; grains conditional</td><td>Same hierarchy, but stronger ENSO backdrop</td><td>Sugar remains first monitor; grains still need local weather confirmation</td></tr></table>

Source: MS.

Exhibit 5: El Niño strength distribution remains wide  
![](images/5446129aa4a864c36cb7fd7f9326141d6d815fc024c70b8de343e0e22805630f.jpg)

<details>
<summary>line chart</summary>

|  |  |  | Statistic Model Values |
| --- | --- | --- | --- |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Models |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statastic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
|  |  |  | Statistic Model Values |
| ) |  | Value* |  |
|  |  |  | Statistic Model Values(1) |
|  |  |  | Statistic Model Values(2) |
|  |  |  | Statistic Model Values(3) |
|  |  |  | Statistic Model Values(4) |
|  |  |  | Statistic Model Values(5) |
|  |  |  | Statistic Model Values(6) |
|  |  |  | Statistic Model Values(7) |
|  |  |  | Statistic Model Values(8) |
|  |  |  | Statistic Model Values(9) |
|  |  |  | Statistic Model Values(10) |
|  |  |  | Statistic Model Values(11) |
|  |  |  | Statistic Model Values(12) |
|  |  |  | Statistic Model Values(13) |
|  |  |  | Statistic Model Values(14) |
|  |  |  | Statistic Model Values(15) |
|  |  |  | Statistic Model Values(16) |
|  |  |  | Statistic Model Values(17) |
|  |  |  | Statistic Model Values(18) |
|  |  |  | Statistic Model Values(19) |
|  |  |  | Statistic Model Values(20) |
|  |  |  | Statistic Model Values(21) |
|  |  |  | Statistic Model Values(22) |
|  |  |  | Statistic Model Values(23) |
|  |  |  | Statistic Model Values(24) |
|  |  |  | Statistic Model Values(25) |
|  |  |  | Statistic Model Values(26) |
|  |  |  | Statistic Model Values(27) |
|  |  |  | Statistic Model Values(28) |
|  |  |  | Statistic Model Values(29) |
|  |  |  | Statistic Model Values(30) |
|  |  |  | Statistic Model Values(31) |
|  |  |  | Statistic Model Values(32) |
|  |  |  | Statistic Model Values(33) |
|  |  |  | Statistic Model Values(34) |
|  |  |  | Statistic Model Values(35) |
|  |  |  | Statistic Model Values(36) |
|  |  |  | Statistic Model Values(37) |
|  |  |  | Statistic Model Values(38) |
|  |  |  | Statistic Model Values(39) |
|  |  |  | Statistic Model Values(40) |
|  |  |  | Statistic Model Values(41) |
|  |  |  | Statistic Model Values(42) |
|  |  |  | Statistic Model Values(43) |
|  |  |  | Statistic Model Values(44) |
|  |  |  | Statistic Model Values(45) |
|  |  |  | Statistic Model Values(46) |
|  |  |  | Statistic Model Values(47) |
|  |  |  | Statistic Model Values(48) |
|  |  |  | Statistic Model Values(49) |
|  |  |  | Statistic Model Values(50) |


[中间内容因长度限制已省略]

 and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital

Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: LatAm Agribusiness

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/10/2026)</td></tr><tr><td colspan="3">Javier Martinez de Olcoz Cerdan</td></tr><tr><td>Sociedad Quimica y Minera de Chile S.A. (SQM.N)</td><td></td><td>US$80.44</td></tr><tr><td colspan="3">Julia Rizzo</td></tr><tr><td>ADECOAGRO S.A. (AGRO.N)</td><td>E (03/16/2026)</td><td>US$11.69</td></tr><tr><td>Rumo SA (RAIL3.SA)</td><td>E (03/30/2025)</td><td>R$13.30</td></tr><tr><td>Sao Martinho SA (SMTO3.SA)</td><td>O (02/02/2026)</td><td>R$16.90</td></tr><tr><td>SLC Agricola S.A. (SLCE3.SA)</td><td>E (09/17/2025)</td><td>R$14.89</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
