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
# Global Markets Daily: Why Always Gilts?

Gilt underperformance in recent years has been driven by a large increase in term premium. We argue that this is consistent with the macro performance of the UK economy — growth has been weak, inflation high, and survey measures of uncertainty are the highest among major economies.

■ Additionally, the rise in Gilt yields has occurred alongside a significant increase in global term premium. On various measures of long-end premium, Gilts have actually shown some improvement vs peer bond markets in recent quarters, suggesting Gilts are not always the source of bond bearish news. The evidence suggests that the underperformance in recent months is related to the repricing of the BoE policy path rather than a higher risk premium.

By our analysis, the underperformance of Gilts since 2022 has also been driven by the changes in supply and demand dynamics in the Gilt market. Large fiscal deficits and BoE QT have contributed to high supply, while the domestic pension system is no longer as significant as a source of demand.

■ Shifting expectations around forward bond supply could be a source of upside risk to our Gilt forecasts, and ongoing fiscal pressure from higher rates will likely result in relatively sticky Gilt risk premium in the near term. However, we continue to think that the macro outlook will be the main driver of Gilt yields — while uncertainty remains high, macro data consistent with the BoE on hold in 2026, and potentially cutting in 2027 (as per our economists' forecasts), would be a source of lasting relief for Gilts.

# Why Always Gilts?

The 30y Gilt yield traded above $5.8\%$ this week, a level last seen in 1998 (Exhibit 1). Gilt yields are high vs other developed economies, with the underperformance in recent years driven by a significant rise in UK term premium (Exhibit 2).

# George Cole

+44(20)7552-1214

george.cole@gs.com

GS International

# Loic Mathys

+44(20)7051-1664

loic.mathys@gs.com

GS International

Exhibit 1: Gilt yields are the highest among major DM bond markets   
G4 30y yields, GS fitted yields   
![](images/3dc0d5fdee81dc071c34bca3d44d405dab333b6567e9f7365ce66fe74acd17ca.jpg)

<details>
<summary>line</summary>

| Year | UK 30y | US  | DE  | JP  |
|------|--------|-----|-----|-----|
| 2000 | 5.5    | 7.0 | 5.8 | 2.5 |
| 2002 | 5.2    | 6.5 | 5.5 | 2.3 |
| 2004 | 4.8    | 6.0 | 5.2 | 2.1 |
| 2006 | 4.5    | 5.5 | 4.9 | 1.9 |
| 2008 | 4.2    | 5.0 | 4.6 | 1.7 |
| 2010 | 3.8    | 4.5 | 4.2 | 1.5 |
| 2012 | 3.5    | 4.0 | 3.8 | 1.3 |
| 2014 | 3.0    | 3.5 | 3.3 | 1.1 |
| 2016 | 2.5    | 3.0 | 2.8 | 0.9 |
| 2018 | 2.0    | 2.5 | 2.3 | 0.7 |
| 2020 | 1.5    | 2.0 | 1.8 | 0.5 |
| 2022 | 1.0    | 1.5 | 1.3 | 0.3 |
| 2024 | 1.5    | 2.0 | 1.8 | 0.5 |
| 2026 | 2.0    | 2.5 | 2.3 | 1.0 |
</details>

Source: GS Global Investment Research, GS FICC and Equities

Exhibit 2: UK term premium has increased most since 2022 Changes in G4 term premium, GS estimates   
![](images/ef650c1dae8a5e4938be1ab90c52a2dfdecb1fdefc7e4fd9ccdfc24e900699ae.jpg)

<details>
<summary>line</summary>

| Date   | UK 10y term premium | US  | EA  | JP  |
|--------|---------------------|-----|-----|-----|
| Jan-22 | -50                 | -50 | -50 | -50 |
| Oct-22 | 180                 | 100 | 100 | 50  |
| Jul-23 | 50                  | 150 | 150 | 75  |
| Apr-24 | 100                 | 175 | 175 | 100 |
| Jan-25 | 200                 | 200 | 200 | 150 |
| Oct-25 | 250                 | 225 | 225 | 175 |
| Jul-26 | 275                 | 250 | 250 | 200 |
</details>

Source: GS Global Investment Research

With renewed focus on the Gilt market given ongoing policy uncertainty, the key question is whether these levels of yields and risk premium are justified. The first place to look for an explanation is the macro performance of the UK economy. Over recent years, UK growth has been weak relative to other economies, but inflation has been the highest. This combination of low growth and high inflation justifies an elevated risk premium as this attenuates the correlation of bonds with growth and weakens their hedge value for risk asset portfolios. In addition, Exhibit 3 and Exhibit 4 show that while macro uncertainty is well off its peak, the UK still exhibits the highest surveyed macro uncertainty among major economies. This has deeper roots in the structure of the UK economy and the nature of recent shocks — for example, a high dependence on gas in the UK energy mix, coupled with a relatively high level of inflation indexation across wages and prices.

Exhibit 3: UK growth forecast uncertainty highest in G4... Cross-sectional standard deviation of forecast panel   
![](images/c780c5479226d755e1970dd4b0985e79b269456c65738c9085da0c69ec976a2e.jpg)

<details>
<summary>line</summary>

| Year | UK    | US    | EA    | JP    |
|------|-------|-------|-------|-------|
| 2005 | 0.4   | 0.3   | 0.3   | 0.4   |
| 2006 | 0.5   | 0.4   | 0.4   | 0.5   |
| 2007 | 0.6   | 0.5   | 0.5   | 0.6   |
| 2008 | 0.7   | 0.6   | 0.6   | 0.7   |
| 2009 | 0.8   | 0.7   | 0.7   | 0.8   |
| 2010 | 0.9   | 0.8   | 0.8   | 0.9   |
| 2011 | 1.0   | 0.9   | 0.9   | 1.0   |
| 2012 | 1.1   | 1.0   | 1.0   | 1.1   |
| 2013 | 1.2   | 1.1   | 1.1   | 1.2   |
| 2014 | 1.3   | 1.2   | 1.2   | 1.3   |
| 2015 | 1.4   | 1.3   | 1.3   | 1.4   |
| 2016 | 1.5   | 1.4   | 1.4   | 1.5   |
| 2017 | 1.6   | 1.5   | 1.5   | 1.6   |
| 2018 | 1.7   | 1.6   | 1.6   | 1.7   |
| 2019 | 1.8   | 1.7   | 1.7   | 1.8   |
| 2020 | 2.5   | 2.4   | 2.4   | 2.5   |
| 2021 | 1.8   | 1.7   | 1.7   | 1.8   |
| 2022 | 1.5   | 1.4   | 1.4   | 1.5   |
| 2023 | 1.3   | 1.2   | 1.2   | 1.3   |
| 2024 | 1.1   | 1.0   | 1.0   | 1.1   |
| 2025 | 0.9   | 0.8   | 0.8   | 0.9   |
| 2026 | 0.7   | 0.6   | 0.6   | 0.7   |
| 2027 | 0.5   | 0.4   | 0.4   | 0.5   |
</details>

Source: GS Global Investment Research, Consensus Economics

Exhibit 4: ...and also highest inflation uncertainty in G4 Cross-sectional standard deviation of forecast panel   
![](images/00111f865fcf1f598a1d73314cbdfdcfb6d87c7f03dc2ee3c8d5ffd0309933e4.jpg)

<details>
<summary>line</summary>

| Year | UK    | US    | EA    | JP    |
|------|-------|-------|-------|-------|
| 2005 | 0.15  | 0.25  | 0.18  | 0.22  |
| 2006 | 0.18  | 0.28  | 0.20  | 0.25  |
| 2007 | 0.20  | 0.30  | 0.22  | 0.28  |
| 2008 | 0.25  | 0.35  | 0.25  | 0.32  |
| 2009 | 0.80  | 1.00  | 0.40  | 0.50  |
| 2010 | 0.55  | 0.60  | 0.35  | 0.45  |
| 2011 | 0.45  | 0.50  | 0.30  | 0.40  |
| 2012 | 0.40  | 0.45  | 0.28  | 0.35  |
| 2013 | 0.35  | 0.40  | 0.25  | 0.32  |
| 2014 | 0.38  | 0.42  | 0.27  | 0.33  |
| 2015 | 0.42  | 0.48  | 0.30  | 0.38  |
| 2016 | 0.38  | 0.45  | 0.28  | 0.35  |
| 2017 | 0.35  | 0.42  | 0.25  | 0.32  |
| 2018 | 0.38  | 0.45  | 0.27  | 0.33  |
| 2019 | 0.42  | 0.48  | 0.30  | 0.35  |
| 2020 | 0.48  | 0.55  | 0.35  | 0.42  |
| 2021 | 0.65  | 0.75  | 0.55  | 0.68  |
| 2022 | 1.20  | 1.15  | 1.18  | 1.17  |
| 2023 | 1.15  | 1.18  | 1.15  | 1.16  |
| 2024 | 1.18  | 1.15  | 1.18  | 1.17  |
| 2025 | 1.15  | 1.18  | 1.15  | 1.16  |
| 2026 | 1.18  | 1.15  | 1.18  | 1.17  |
| 2027 | 1.20  | 1.18  | 1.15  | 1.16  |
</details>

Source: GS Global Investment Research, Consensus Economics

Risk premium is related to this macro uncertainty and volatility. Realised volatility in UK rates has also been much higher than other economies, and although GBP implied rates vol had fallen ahead of the war in Iran, it is now back to being the highest in major markets. This volatility is also visible from a policy point of view — Exhibit 5 shows the realised volatility of movements in front-end rates on G4 central bank meeting days

since 2022. The market prices larger and more volatile moves in front-end rates, suggesting that it is not just elevated levels of macro uncertainty affecting the UK curve, but reaction function uncertainty as well.

Exhibit 5: Front-end rates have highest vol on BoE meeting days   
G4 mean (absolute change) and standard deviation of rate change on meeting days   
![](images/12f1e04e30db5e2a199ad9e233a7720c2913b20e51095c26726603c5cba884d6.jpg)

<details>
<summary>bar</summary>

| Country | Meeting day mean absolute change of 1y OIS (bp) | Standard deviation (bp) |
| :--- | :--- | :--- |
| JP | 0.9 | 1.1 |
| EA | 3.0 | 5.0 |
| US | 4.8 | 6.0 |
| UK | 6.5 | 9.7 |
</details>

Source: GS Global Investment Research, GS FICC and Equities, Haver Analytics

Exhibit 6: Gilts have cheapened vs swaps, but so have all G4 bonds   
10y OIS - 10y CMT G4 yields   
![](images/393513bbd99d01d6458a6dade38dbb70e715918975d6dde0e78852ef68519862.jpg)

<details>
<summary>line</summary>

| Date   | UK 10y OIS swap spread | US  | DE  | JP  |
|--------|------------------------|-----|-----|-----|
| Jan-22 | ~30 bp                | ~-20 bp | ~40 bp | ~0 bp |
| Oct-22 | ~80 bp                | ~-10 bp | ~70 bp | ~20 bp |
| Jul-23 | ~40 bp                | ~-30 bp | ~50 bp | ~10 bp |
| Apr-24 | ~20 bp                | ~-40 bp | ~30 bp | ~0 bp |
| Jan-25 | ~-40 bp               | ~-60 bp | ~-20 bp | ~-20 bp |
| Oct-25 | ~-60 bp               | ~-50 bp | ~-30 bp | ~-10 bp |
| Jul-26 | ~-70 bp               | ~-60 bp | ~-40 bp | ~-20 bp |
</details>

Source: GS Global Investment Research, GS FICC and Equities

Given the UK has the highest growth, inflation and policy uncertainty, this — alongside higher levels of inflation and policy rates (UK policy rates were among the highest in the 2022-2024 cycle among the G10) — goes some way to explain the relative underperformance of Gilts in recent years. But the focus on elevated Gilt yields needs to be put in the context of a global repricing of long-end yields and risk premium. 30y JGB yields are at multi-decade highs, 30y Bund yields are at the highest levels post-sovereign crisis, and 30y UST yields are near the highs of the cycle. On other measures of relative bond pricing, such as swap spreads (Exhibit 6) and the 10s30s curve (Exhibit 7), Gilts are currently comparable to other curves, and have actually shown improvement in recent quarters on a relative basis. But, as we have shown (see here and here), the risk premium in Gilts has not increased much in recent months, despite Gilt yields rising more than in other bond markets. This is because the drivers of Gilt yields in recent months have been the shift in the fundamental outlook for inflation and central bank policy.

Exhibit 7: Gilt 10s30s steep, but not an outlier  
G4 10s30s curve spread   
![](images/ad62a8bd99a1115dfefad77382e47f3230056fa099c7f9bbc91c74da3018800f.jpg)

<details>
<summary>line</summary>

| Date   | UK 10s30s | US  | DE  | JP  |
|--------|-----------|-----|-----|-----|
| Jan-22 | ~40       | ~40 | ~40 | ~60 |
| Oct-22 | ~-40      | ~-20| ~-20| ~100|
| Jul-23 | ~40       | ~20 | ~20 | ~80 |
| Apr-24 | ~60       | ~40 | ~40 | ~100|
| Jan-25 | ~60       | ~60 | ~60 | ~120|
| Oct-25 | ~70       | ~60 | ~60 | ~140|
| Jul-26 | ~60       | ~60 | ~60 | ~110|
</details>

Source: GS Global Investment Research, GS FICC and Equities

Exhibit 8: Gilts have seen a reduction in pension and BoE bond holdings   
Pension fund and BoE holdings as share of debt   
![](images/50d6ca7b7011ce2943a3f70805a8591bc7854aecb7c434e9e1eff0d1ee5ef978.jpg)

<details>
<summary>line</summary>

| Date | Pension fund Gilts holdings (%) | BoE Holdings (%) |
|---|---|---|
| Sep-19 | 32.5 | 23.5 |
| Jun-20 | 31.0 | 24.0 |
| Mar-21 | 26.0 | 35.0 |
| Dec-21 | 26.5 | 37.0 |
| Sep-22 | 18.0 | 34.0 |
| Jun-23 | 16.0 | 31.0 |
| Mar-24 | 16.5 | 27.0 |
| Dec-24 | 15.0 | 23.0 |
| Sep-25 | 13.0 | 18.0 |
</details>

Source: GS Global Investment Research, ONS, Haver Analytics, BoE

The global repricing of long-end yields is consistent with the features of the post-pandemic hiking cycles, namely a significant repricing higher of inflation risk, tighter monetary policy both via higher policy rates and smaller balance sheets, together with loose fiscal policy and high bond supply. Supply-demand imbalances have affected all curves but are also a contributor to Gilt underperformance through 2022-2025, as the BoE swung from a buyer of duration to a seller, and demand from UK pension funds fell structurally in the wake of the 2022 Gilt crisis (Exhibit 8). The rise in duration-adjusted bond free-float (Exhibit 9) — the stock of bonds available to the private sector — and the change of ownership to more price-sensitive bond holders (Exhibit 10) have likely also affected the behaviour and level of Gilt risk premium. However, it is less clear that these factors are worsening and so they are unlikely to be a clear reason for elevated risk in the near term.

Exhibit 9: Gilt free-float has increased sUBStantially, especially duration-weighted   
US vs UK pp change in free float and 10y-equivalent free float   
![](images/28f1f4d55daaf8a54c7ebda2290e4a7f1bd18aef3af0938a0551e74a6f38d56d.jpg)

<details>
<summary>line</summary>

| Date | UK free-float (%) | UK 10y equivalent (%) | US free-float (%) | US 10y equivalent (%) |
|---|---|---|---|---|
| Dec-21 | -0.5 | -0.8 | 1.5 | 0.3 |
| Sep-22 | 2.0 | 3.5 | 1.0 | 1.5 |
| Jun-23 | 7.0 | 8.0 | 4.0 | 3.0 |
| Mar-24 | 10.0 | 11.0 | 8.0 | 5.0 |
| Dec-24 | 14.0 | 15.0 | 12.0 | 6.0 |
| Sep-25 | 19.0 | 16.0 | 14.0 | 7.0 |
| Jun-26 | 21.0 | 15.5 | 15.0 | 7.5 |
</details>

Source: GS Global Investment Research, DMO, BoE, Federal Reserve, US Treasury, Haver Analytics

Exhibit 10: Repo financing has decreased in pension funds  
Net repo positioning (borrowing)   
![](images/434a6f2d95114ddfe46df8feb9f7f71d8d78b374bca8185174e1425e3f12aa23.jpg)

<details>
<summary>area</summary>

| Year | Hedge Fund (GBP bn) | Money Market Funds (MMFs) (GBP bn) | Insurers, Pension Schemes, and LDI Funds (GBP bn) | Other (GBP bn) |
|---|---|---|---|---|
| 2020 | -10 | -30 | 180 | 0 |
| 2021 | 240 | -20 | 210 | 0 |
| 2022 | -60 | -10 | 210 | 0 |
| 2023 | -90 | -10 | 130 | 0 |
| 2024 | 130 | -10 | 130 | 0 |
| 2025 | 190 | -10 | 140 | 0 |
| 2026 | 250 | -10 | 150 | 0 |
</details>

Source: GS Global Investment Research, BoE

To look at the drivers of Gilt risk premium in more detail, we expand on the term premium valuation framework outlined here. We estimate a model with various drivers of term premium. We use the free-float (the share of Gilts available to the private sector), a policy uncertainty measure, the unemployment gap, BoE Gilt holdings and the

G3 term premium, orthogonalised to BoE Gilt holdings $^{1}$ . Exhibit 11 shows the decomposition of Gilt term premium into those various drivers. Our model has a good fit by design, due in part to the inclusion of the (orthogonalised) global term premium. Our European economics team showed that, based on fiscal fundamentals, UK risk premium was high vs peers, but in this exercise we use this good fit to quantify the drivers of Gilt term premium rather than longer-run macro valuation $^{2}$ . We find that supply factors, including from BoE QT, as well as the broader increase in bond supply alongside the repricing in G3 term premium, explain the bulk of the repricing. We do find a modest role for policy uncertainty in boosting the UK term premium in previous years, but by nature of the index used (which remains low at the current period) it has had little impact recently.

Exhibit 11: QT, supply and global factors have driven UK term premium higher 10y UK term premium vs model fit and contributions to fit   
![](images/11416631bf2fd8cddfebd6cd09ed65a41df8b2b043953f25d0735f46688d4ae0.jpg)

<details>
<summary>bar_line</summary>

| Date | Unemployment Gap (bp) | G3 Term Premium (% GDP) (bp) | Gilt Free Float (% GDP) (bp) | Policy Uncertainty (EPU) (bp) | BoE Gilt Holdings (%GDP) (bp) | Residual (bp) |
|---|---|---|---|---|---|---|
| Jan-22 | -5 | -10 | -5 | -5 | -10 | 0 |
| May-22 | -10 | 10 | 5 | 5 | 10 | 10 |
| Sep-22 | -5 | 15 | 10 | 10 | 40 | 30 |
| Jan-23 | 0 | 10 | 5 | 5 | 80 | 40 |
| May-23 | 5 | 15 | 10 | 10 | 60 | -30 |
| Sep-23 | 10 | 30 | 20 | 15 | 90 | -70 |
| Jan-24 | 15 | 35 | 25 | 20 | 100 | -75 |
| May-24 | 20 | 40 | 30 | 25 | 110 | -80 |
| Sep-24 | 25 | 45 | 35 | 30 | 120 | -85 |
| Jan-25 | 30 | 50 | 40 | 35 | 130 | -90 |
| May-25 | 35 | 55 | 45 | 40 | 140 | -95 |
| Sep-25 | 40 | 60 | 50 | 45 | 150 | -100 |
| Jan-26 | 45 | 65 | 55 | 50 | 160 | -105 |
| May-26 | 50 | 70 | 60 | 55 | 170 | -110 |

| Δ Fitted (bp) / Change in UK 10y term premium (bp) |
|---

| Unemployment Gap (bp) |
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
<fcel>G3 Term Premium (orth. to QE) (bp) |
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
|---|
</details>

Source: GS Global Investment Research, GS FICC and Equities, Haver Analytics, FRED, AMECO, BoE

This analysis helps show why Gilt yields and the Gilt term premium are at historical highs. First, all major bond markets have seen significant weakness in long-end bonds among a generalised repricing of growth and inflation risk. Second, the UK has experienced the highest levels of inflation, the greatest macro and policy uncertainty (by a range of measures). And finally, the model above shows the largest duration-adjusted increase in supply amid a shifting composition of demand.

In the near term political and fiscal risks may re-emerge, and the analysis above would suggest that any pressure on supply expectations could exacerbate the already-elevated Gilt risk premium. This is most likely to come from a loosening of fiscal policy — for example, debates about higher defence spending commitments and the challenge of

incorporating this into existing fiscal rules could be a source of this risk. We estimate that a 1pp increase in the medium-term deficit is worth around 30-40bp higher Gilt yields. The pressure on fiscal policy via high interest rates and ongoing policy uncertainty make it difficult for Gilt risk premium to compress.

However, some of the factors that have driven higher yields over recent years should ultimately fade. Quantitative tightening will eventually slow as the BoE's balance sheet shrinks, and fiscal deficits under current policy settings are due to narrow gradually. As discussed above, relative measures of Gilt performance, such as swap spreads and long-end curve shape, indicate these factors are already improving. And 

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
