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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## KOREA WEEKLY KICKSTART

# KOSPI ended the week down moderately amid continued volatility and the US core CPI below consensus

KOSPI ended the week down moderately amid continued volatility and the US core CPI below consensus. The Construction, Leisure and Machinery sectors outperformed this week, while Software, Auto and Securities sectors underperformed the most (Exhibit 7).  
■ Foreign investors continued to sell the KOSPI market, driven by outflows for KOSPI Tech and Shipbuilding (Exhibit 34).  
KOSPI 12m-forward EPS was revised up by +1.2%. The Chemicals sector saw the strongest upward earnings revisions, while the Leisure sector was revised down the most this week (Exhibit 21).  
The KRW strengthened 2.8% vs. USD this week. It also strengthened by 2.6% vs. JPY and 2.3% vs. EUR.  
The latest Korea Equity Risk Barometer (GSSRKERB Index) is at -2.1, falling further into a risk-adverse territory.

Charts of the Week: KOSDAQ Tactical Opportunity Amid Diverging Flows, Earnings, and Valuations

■ KOSDAQ Tactical Opportunity Amid Diverging Flows, Earnings, and Valuations : Although KOSDAQ has recently outperformed KOSPI amid heightened market volatility, it has significantly underperformed since August 2023. We believe this has been driven primarily by divergences in earnings revisions and valuations. KOSPI earnings upgrades have been materially stronger than KOSDAQ earnings revisions. Despite KOSDAQ's significant underperformance, its valuations remain more elevated than KOSPI's 12-month forward P/E, even as its earnings revisions have been considerably weaker. Against this backdrop, KOSDAQ has attracted stronger foreign inflows year to date, while KOSPI has seen significant foreign outflows. In KOSPI, we believe these outflows have been largely driven by portfolio rebalancing related to diversification requirements, with the two largest semiconductor stocks accounting for much of the selling. Meanwhile, foreign inflows into KOSDAQ have been concentrated in the information technology and health care sectors. While KOSPI has outperformed KOSDAQ by a wide margin since 2023, tactical rotation into KOSDAQ—particularly in semiconductor components and equipment—may offer investors alpha opportunities that are thematically aligned with the broader market narrative.

Timothy Moe, CFA

+65-6889-1199 | timothy.moe@gs.com

GS (Singapore) Pte

John Kwon

+65-6654-6337

jongmin.kwon@gs.com

GS (Singapore) Pte

## Table of Contents

Charts of the week: KOSDAQ Tactical Opportunity Amid Diverging Flows, Earnings, and Valuations 3  
Summary 5  
Investment flows 6  
Macro Indicators 7  
Performance 8  
Valuations 10  
Valuation discount relative to Global and Asia regional peers 12  
Flows 13  
Currency, rates and commodities 15  
Korea ERB, Credit and Market Technicals 16  
Disclosure Appendix 17

## Charts of the week: KOSDAQ Tactical Opportunity Amid Diverging Flows, Earnings, and Valuations

Exhibit 1: KOSDAQ has significantly underperformed since August 2023  
![](images/ad820a87f1c1bf44326305fd9c91cd671afd91948f6dbba4a460cd3db0f60a12.jpg)

<details>
<summary>line chart</summary>

| Date    | KOSPI vs. KOSDAQ Relative Performance |
|---------|--------------------------------------|
| Jun-16  | 100.0                                |
| Dec-16  | 85.0                                 |
| Jun-17  | 75.0                                 |
| Dec-17  | 100.0                                |
| Jun-18  | 105.0                                |
| Dec-18  | 95.0                                 |
| Jun-19  | 85.0                                 |
| Dec-19  | 90.0                                 |
| Jun-20  | 105.0                                |
| Dec-20  | 95.0                                 |
| Jun-21  | 85.0                                 |
| Dec-21  | 95.0                                 |
| Jun-22  | 85.0                                 |
| Dec-22  | 95.0                                 |
| Jun-23  | 100.0                                |
| Dec-23  | 95.0                                 |
| Jun-24  | 85.0                                 |
| Dec-24  | 75.0                                 |
| Jun-25  | 65.0                                 |
| Dec-25  | 55.0                                 |
| Jun-26  | 35.0                                 |
</details>

Source: FactSet, GS Global Investment Research

Exhibit 2: KOSPI earnings upgrades have been materially stronger than KOSDAQ earnings revisions  
![](images/4186f55e0d4e93ed2351beabe9e2767d83c4d44f90122a55e78a284c962e6bf6.jpg)

<details>
<summary>line chart</summary>

| Date   | KOSPI (KRW/Share) | KOSDAQ (KRW/Share) |
|--------|-------------------|--------------------|
| Jun-16 | ~8,000            | ~9,500             |
| Jun-17 | ~8,500            | ~10,500            |
| Jun-18 | ~8,500            | ~11,500            |
| Jun-19 | ~8,000            | ~11,000            |
| Jun-20 | ~8,500            | ~13,000            |
| Jun-21 | ~9,000            | ~15,000            |
| Jun-22 | ~9,500            | ~17,000            |
| Jun-23 | ~9,500            | ~16,500            |
| Jun-24 | ~10,000           | ~17,500            |
| Jun-25 | ~11,000           | ~18,500            |
| Jun-26 | ~23,000           | ~21,500            |
</details>

Source: Quantiwise, GS Global Investment Research

Exhibit 3: KOSDAQ valuations remain more elevated than KOSPI's 12-month forward P/E  
![](images/b9c60d8fd88f42494461258c7ffcf377cc9caabeeaa4a9b23200065acbded773.jpg)

<details>
<summary>line chart</summary>

| Date   | KOSPI | KOSDAQ | Average Since 2010 |
|--------|-------|--------|---------------------|
| Jan-11 | ~9    | ~10    | -30%                |
| Jan-12 | ~8    | ~10    | -30%                |
| Jan-13 | ~9    | ~11    | -30%                |
| Jan-14 | ~10   | ~12    | -30%                |
| Jan-15 | ~10   | ~13    | -30%                |
| Jan-16 | ~10   | ~15    | -30%                |
| Jan-17 | ~10   | ~16    | -30%                |
| Jan-18 | ~10   | ~17    | -30%                |
| Jan-19 | ~10   | ~18    | -30%                |
| Jan-20 | ~10   | ~19    | -30%                |
| Jan-21 | ~10   | ~20    | -30%                |
| Jan-22 | ~10   | ~21    | -30%                |
| Jan-23 | ~10   | ~22    | -30%                |
| Jan-24 | ~10   | ~23    | -30%                |
| Jan-25 | ~10   | ~24    | -30%                |
| Jan-26 | ~8    | ~30    | -30%                |
</details>

Source: Quantiwise, GS Global Investment Research

Exhibit 4: However, KOSDAQ has seen stronger foreign inflows year-to-date, while KOSPI has experienced significant foreign outflows  
![](images/45e3abc0b38e4014937886e6b6a9ffbedd29c5e39ea27bc0250f7cf5d5fd05a7.jpg)

<details>
<summary>line chart</summary>

| Date   | KOSPI Flows (KRWbn) | KOSDAQ Flows (KRWbn) |
|--------|----------------------|-----------------------|
| Jan-08 | ~0                   | ~0                    |
| Jan-09 | ~-50,000             | ~-100,000             |
| Jan-10 | ~-100,000            | ~-150,000             |
| Jan-11 | ~-50,000             | ~-100,000             |
| Jan-12 | ~0                   | ~-50,000              |
| Jan-13 | ~5,000               | ~-10,000              |
| Jan-14 | ~10,000              | ~-5,000               |
| Jan-15 | ~15,000              | ~-10,000              |
| Jan-16 | ~20,000              | ~-5,000               |
| Jan-17 | ~25,000              | ~-10,000              |
| Jan-18 | ~30,000              | ~-5,000               |
| Jan-19 | ~35,000              | ~5,000                |
| Jan-20 | ~40,000              | ~10,000               |
| Jan-21 | ~35,000              | ~5,000                |
| Jan-22 | ~30,000              | ~-1,000               |
| Jan-23 | ~25,000              | ~-5,000               |
| Jan-24 | ~20,000              | ~-1,5,000             |
| Jan-25 | ~15,000              | ~-5,000               |
| Jan-26 | ~10,000              | ~9,5,566              |
</details>

Source: Quantiwise, GS Global Investment Research

Exhibit 5: Foreign outflows from KOSPI have been largely driven by the two largest semiconductor stocks  
![](images/d4fff0f2ccaca35c27b024380862f1e840daf4daff8c48b7782f977b8a7d5496.jpg)

<details>
<summary>line chart</summary>

| Date   | KOSPI Flows | Samsung and SK Hynix Flows |
|--------|-------------|-----------------------------|
| Jan-25 | 0           | 0                           |
| Feb-25 | -5          | -3                          |
| Mar-25 | -10         | -8                          |
| Apr-25 | -15         | -12                         |
| May-25 | -20         | -18                         |
| Jun-25 | -25         | -22                         |
| Jul-25 | -30         | -28                         |
| Aug-25 | -35         | -32                         |
| Sep-25 | -40         | -38                         |
| Oct-25 | -45         | -42                         |
| Nov-25 | -50         | -48                         |
| Dec-25 | -55         | -52                         |
| Jan-26 | -60         | -58                         |
| Feb-26 | -70         | -68                         |
| Mar-26 | -80         | -78                         |
| Apr-26 | -90         | -88                         |
| May-26 | -100        | -98                         |
| Jun-26 | -110        | -108                        |
</details>

Source: Quantiwise, GS Global Investment Research

Exhibit 6: Foreign inflows into KOSDAQ have been concentrated in the information technology and health care sectors  
![](images/522638cbe004228e48f1899a38b6a057927e04716fc48cb44d8ce0d3c0b82a77.jpg)

<details>
<summary>line chart</summary>

| Date   | KSQ Health Care | KSQ Information Technology | KOSDAQ |
|--------|-----------------|----------------------------|--------|
| Jun-26 | 1.3             | 1.9                        | 4.0    |
</details>

Source: Quantiwise, GS Global Investment Research

## Summary

Exhibit 7: Summary of the past week's performance

<table><tr><td colspan="5">Equity Market Performance</td></tr><tr><td></td><td>P/E 2026E</td><td></td><td></td><td>1-wk chg</td></tr><tr><td>KOSPI</td><td>7.1</td><td>8,123.62</td><td>↓</td><td>(0.5)</td></tr><tr><td>KOSDAQ</td><td>28.8</td><td>1,029.05</td><td>↑</td><td>2.7</td></tr><tr><td>MSCI Korea</td><td>6.1</td><td>3,017.40</td><td>↓</td><td>(0.5)</td></tr><tr><td colspan="5">KOSPI Performance by sector</td></tr><tr><td>Top 3</td><td>wk chg (%)</td><td>Bottom 3</td><td></td><td>1wk chg (%)</td></tr><tr><td>Construction</td><td>10.8</td><td>Software</td><td></td><td>(9.3)</td></tr><tr><td>Leisure</td><td>4.4</td><td>Auto</td><td></td><td>(5.3)</td></tr><tr><td>Machinery</td><td>2.8</td><td>Securities</td><td></td><td>(3.9)</td></tr><tr><td colspan="5">Market Flows</td></tr><tr><td colspan="2">Equities (KRW bn)</td><td>1-wk flow</td><td></td><td>in std dev*</td></tr><tr><td colspan="2">KOSPI Flows: Foreigners</td><td>(4,400)</td><td>↓</td><td>-0.8</td></tr><tr><td></td><td>Institutions</td><td>83</td><td>↑</td><td>0.0</td></tr><tr><td></td><td>Individuals</td><td>3,803</td><td>↑</td><td>0.7</td></tr><tr><td></td><td>Pensions</td><td>(677)</td><td>↓</td><td>-2.5</td></tr><tr><td colspan="2">KOSDAQ Flows: Foreigners</td><td>67</td><td>↑</td><td>0.1</td></tr><tr><td></td><td>Institutions</td><td>1,222</td><td>↑</td><td>0.8</td></tr><tr><td></td><td>Individuals</td><td>(1,154)</td><td>↓</td><td>-0.7</td></tr><tr><td></td><td>Pensions</td><td>103</td><td>↑</td><td>1.0</td></tr><tr><td colspan="5">FX/Interest Rate</td></tr><tr><td></td><td></td><td>Current</td><td></td><td>1-wk chg</td></tr><tr><td colspan="2">USDKRW</td><td>1,515</td><td>↓</td><td>(2.8)</td></tr><tr><td colspan="2">JPYKRW</td><td>9.47</td><td>↓</td><td>(2.6)</td></tr><tr><td colspan="2">USDKRW 1M Risk Reversal/ATM vc</td><td>0.08</td><td>↓</td><td>-7bp</td></tr><tr><td colspan="2">USDKRW 1yr swap basis</td><td>(85)</td><td>↑</td><td>4bp</td></tr><tr><td colspan="2">3-year KTB</td><td>3.81</td><td>↓</td><td>-7bp</td></tr><tr><td colspan="2">10-year KTB</td><td>4.20</td><td>↓</td><td>-6bp</td></tr></table>

Up (↑) = Up wow vs. the previous week  
Asterisk (\*) = Expressed in standard deviation of 1-wk change in 1-year

Source: Bloomberg

## Exhibit 8: Summary of year-to-date flows

Year-to-date Foreign Inflows to Korea  
![](images/4a493a93d973b5ce334b67cd54801c679263f6d4d1c1dbbb9f0071bf84dbcc25.jpg)

<details>
<summary>area chart</summary>

| Year | Korea Equities (LHS) (USDbn) | Korea Bonds (USDbn) | AEJ Equities (LHS) (USDbn) | AEJ Bonds (USDbn) |
|------|----------------------------------|----------------------|------------------------------|--------------------|
| 17   | ~5                               | ~5                   | ~0                           | ~0                 |
| 18   | ~10                              | ~30                  | ~20                          | ~70                |
| 19   | ~-5                              | ~45                  | ~-40                         | ~50                |
| 20   | ~-10                             | ~45                  | ~-20                         | ~60                |
| 21   | ~-20                             | ~60                  | ~-60                         | ~40                |
| 22   | ~-30                             | ~90                  | ~-60                         | ~100               |
| 23   | ~-10                             | ~50                  | ~-60                         | ~50                |
| 24   | ~10                              | ~60                  | ~-40                         | ~70                |
| 25   | ~-10                             | ~45                  | ~-60                         | ~60                |
| 26   | ~-30                             | ~90                  | ~-60                         | ~100               |
</details>

Source: Bloomberg

## Investment flows

Exhibit 9: Equity inflows to 5 AEJ markets  
4-week rolling sum  
![](images/014ea8ca1220167eb29750c736ec113cf5687fc3623f9e8499dc2f42eaf6b895.jpg)

<details>
<summary>line chart</summary>

| Date   | Korea | Indonesia | Taiwan | Thailand | India |
|--------|-------|-----------|--------|----------|-------|
| Jan-18 | -1.5  | -0.5      | 2.0    | -1.0     | 0.5   |
| Jul-18 | -1.0  | -0.5      | 1.5    | -0.5     | 0.0   |
| Jan-19 | -0.5  | 0.0       | 3.0    | 0.0      | 1.0   |
| Jul-19 | 0.0   | 1.0       | 4.0    | 0.5      | 2.0   |
| Jan-20 | -1.0  | -0.5      | 2.5    | -0.5     | 1.5   |
| Jul-20 | -2.0  | -1.0      | 1.0    | -1.5     | 0.5   |
| Jan-21 | -3.0  | -2.0      | 9.0    | -2.5     | 4.0   |
| Jul-21 | -4.0  | -3.0      | 6.0    | -3.5     | 2.5   |
| Jan-22 | -5.0  | -4.0      | 7.0    | -4.5     | 3.5   |
| Jul-22 | -6.0  | -5.0      | 8.0    | -5.5     | 4.5   |
| Jan-23 | -7.0  | -6.0      | 9.0    | -6.5     | 5.5   |
| Jul-23 | -8.0  | -7.0      | 10.0   | -7.5     | 6.5   |
| Jan-24 | -9.0  | -8.0      | 11.0   | -8.5     | 7.5   |
| Jul-24 | -10.0 | -9.0      | 12.0   | -9.5     | 8.5   |
| Jan-25 | -11.0 | -10.0     | 13.0   | -10.5    | 9.5   |
| Jul-25 | -12.0 | -11.0     | 14.0   | -11.5    | 10.5  |
| Jan-26 | -13.0 | -12.0     | 15.0   | -12.5    | 11.5  |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 10: Equity inflows to 5 AEJ markets  
![](images/d9c56fab70e2c5b9229775357f341201e15497fcf592c3f21ea478abb3b3b617.jpg)

<details>
<summary>line chart</summary>

| Year | Korea | Thailand | Indonesia | India | Taiwan |
|------|-------|----------|------------|-------|--------|
| 2017 | 0     | 0        | 0          | 0     | 0      |
| 2018 | 10    | 5        | -5         | 5     | 5      |
| 2019 | 5     | 0        | -10        | 10    | 10     |
| 2020 | 0     | -5       | -15        | 15    | 15     |
| 2021 | -20   | -10      | -20        | 20    | -20    |
| 2022 | -25   | -15      | -25        | -25   | -25    |
| 2023 | -10   | -5       | -10        | -10   | -10    |
| 2024 | 15    | 0        | 5          | 15    | 15     |
| 2025 | 5     | -5       | -5         | 5     | -5     |
| 2026 | -30   | -10      | -15        | -30   | -30    |
</details>

Source: Bloomberg

Exhibit 11: Bond inflows to 4 AEJ markets  
4-week rolling sum  
![](images/2f9cc4084ba65fd354976e5f5eac5c633f6f61a923ce56e4045b3386fb2ca6b6.jpg)

<details>
<summary>line chart</summary>

| Date    | Korea (USD bn) | Thailand (USD bn) | Indonesia (USD bn) | India (USD bn) |
|---------|----------------|-------------------|--------------------|----------------|
| Jan-18  | ~7             | ~2                | ~0                 | ~0             |
| Jul-18  | ~6             | ~2                | ~0                 | ~0             |
| Jan-19  | ~5             | ~2                | ~0                 | ~0             |
| Jul-19  | ~9             | ~2                | ~0                 | ~0             |
| Jan-20  | ~7             | ~2                | ~0                 | ~0             |
| Jul-20  | ~9             | ~2                | ~0                 | ~0             |
| Jan-21  | ~10            | ~2                | ~0                 | ~0             |
| Jul-21  | ~12            | ~2                | ~0                 | ~0             |
| Jan-22  | ~10            | ~3                | ~0                 | ~0             |
| Jul-22  | ~9             | ~3                | ~0                 | ~0             |
| Jan-23  | ~3             | ~2                | ~0                 | ~0             |
| Jul-23  | ~12            | ~2                | ~0                 | ~0             |
| Jan-24  | ~3             | ~2                | ~0                 | ~0             |
| Jul-24  | ~9             | ~2                | ~0                 | ~0             |
| Jan-25  | ~10            | ~2                | ~0                 | ~0             |
| Jul-25  | ~13            | ~2                | ~0                 | ~0             |
| Jan-26  | ~14            | ~2                | ~0                 | ~0             |
</details>

Source: Bloomberg, Haver Analytics, GS Global Investment Research

Exhibit 12: Bond inflows to 4 AEJ markets  
![](images/7624f1243155960331e810520717009e3eff1c0eaec5b3ccbfc79058bef8d4fa.jpg)

<details>
<summary>line chart</summary>

| Year | Korea | Thailand | Indonesia | India |
|------|-------|----------|------------|-------|
| 2017 | 0     | 0        | 0          | 0     |
| 2018 | 30    | 5        | 10         | 20    |
| 2019 | 45    | 5        | 5          | 5     |
| 2020 | 45    | 5        | 10         | 5     |
| 2021 | 60    | 5        | -5         | -10   |
| 2022

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
