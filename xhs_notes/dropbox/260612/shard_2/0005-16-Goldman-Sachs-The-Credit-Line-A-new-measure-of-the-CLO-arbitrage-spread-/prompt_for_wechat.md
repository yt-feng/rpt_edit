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
THE CREDIT LINE

# A new measure of the CLO arbitrage spread

## Deal-matched arbitrage spread shows a more structurally compressed USD opportunity set

For collateralized loan obligation (CLO) investors and managers, the arbitrage spread is a common proxy for the attractiveness of origination, performance, and valuation of CLO equity investments. Traditional CLO arbitrage metrics compare new-issue leveraged loan spreads with CLO weighted average cost of debt, but they miss the actual excess spread embedded in newly created CLOs. Using deal- and tranche-level data, we construct a deal-matched arbitrage measure for USD and EUR CLOs. While it broadly tracks traditional measures, it also shows a more pronounced secular tightening in USD broadly syndicated loan CLO arbitrage as the market has matured. In our view, the growing role of captive equity capital is an important driver, leaving EUR equity optically cheaper, though not necessarily more attractive once weaker regional fundamentals are considered.

## Resets are printing tighter

Matching original vintages to subsequent reset and refinancing activity shows that tighter liabilities do not automatically translate into better economics. Since 2023, USD asset spread tightening has generally kept pace with, and in many cases exceeded, liability spread improvement, limiting the benefit of resets. In EUR, reset economics have held up better, helped by less aggressive asset spread compression vs. the USD market.

## Lower liability costs do not require sacrificing arbitrage spread

Across manager tiers, tighter liabilities have not consistently come at the expense of lower excess spread. In USD, higher-tier managers have generally printed slightly wider arbitrage spreads, while in EUR lower-tier managers have tended to do so. In our view, this reflects greater liability dispersion in USD vs. greater asset spread dispersion in EUR.

## Shamshad Ali

+1(212)902-6712

shamshad.ali@gs.com

GS & Co. LLC

## Amanda Lynam, CPA

+1(212)934-1895

amanda.lynam@gs.com

GS & Co. LLC

## Arun Manohar

+1(212)902-8763

arun.manohar@gs.com

GS & Co. LLC

## Spencer Rogers, CFA

+1(801)884-1104

spencer.rogers@gs.com

GS & Co. LLC

## Sara Grut

+44(20)7774-8622 | sara.grut@gs.com

GS International

## Ben Shumway

+1(801)578-2553

ben.shumway@gs.com

GS & Co. LLC

## Neth Karunamuni

+1(212)934-0799

neth.karunamuni@gs.com

GS & Co. LLC

## A new measure of the CLO arbitrage spread

For CLO investors and managers, the arbitrage spread is a common proxy for the attractiveness of origination, performance, and valuation of CLO equity investments. Traditionally, measures of the arbitrage spread take the difference between new issue loans and the weighted-average cost of CLO debt. While this captures the prevailing differential, it does not capture the actual excess spread at which managers are printing transactions, particularly once resets and refinancings are included. Using deal- and tranche-level data from Intex, we construct a deal-level measure of CLO arbitrage spreads for USD and EUR transactions at origination. Three conclusions stand out.

First, arbitrage spreads have compressed in both USD and EUR broadly syndicated loan CLOs, but the compression has been more pronounced in USD over the past two years. In our view, this likely reflects the increasing presence of captive equity capital in the USD market. As a result, we think this makes EUR equity valuations structurally cheaper, but we are cautious about drawing too sanguine of a conclusion from the wider differential given a less supportive fundamental backdrop in the region.

Second, when looking at resets and refinancings, the change in arbitrage is less straightforward than is often assumed. Liability spreads typically tighten when deals are reset, but asset spreads can tighten as well, particularly in periods of heavy repricing activity. This is because CLO issuers typically tend to reprice their structures during risk-on periods, or when investor sentiment is receptive because other ‘new money’ investment opportunities may be less plentiful (and are eager to stay invested). Over recent vintages, we find that asset spread tightening has generally kept pace with, and in many USD cases exceeded, liability spread improvement. The result is that reset economics have become less favorable in USD than the tightening in tranche liability spreads alone would imply. In EUR, by contrast, reset economics have generally held up better.

Third, comparing arbitrage outcomes across manager tiers suggests that lower debt costs do not necessarily come at the expense of lower excess spread. In the USD market, higher-tier managers have generally printed deals with slightly wider arbitrage spreads than lower-tier peers. In EUR, the opposite pattern holds, with lower-tier managers tending to print a wider arbitrage. The underlying reason appears to be that USD manager differentiation is more visible on the liability side, while EUR dispersion is greater on the asset side (possibly due to the smaller size of the EUR market).

## Deal-level CLO arbitrage spread

Using deal level data from Intex, we construct the CLO arbitrage spread for USD and EUR CLOs. The deal-level spreads generally track the traditional measure of new issue arbitrage spreads, which is calculated by taking the difference between new issue loan and CLO debt spreads (Exhibit 1). However, especially in the USD market, we note a secular trend towards tighter arbitrage spreads as the space has matured and more CLO managers now participate in the USD and EUR markets (Exhibit 2). Deal-matched arbitrage spreads also allow us to look at the arbitrage for Middle Market, or private credit USD CLOs. In the absence of new direct lending market spreads, we can use deal-level liabilities and asset spreads to construct a series that generally matches direct lending spreads (Exhibit 3).

## Exhibit 1: The deal-level arbitrage spreads generally correlate with the new issue calculations

Deal-matched arbitrage spread is trailing 3-month deal-weighted figure; new Issue spread uses new issue loan spreads net monthly new issue weighted average cost of CLO debt (3-months smoothed)

![](images/11f2ea34b48c93cc3331e5f87b67b34fee1688404418268c9462436316ad54a7.jpg)

<details>
<summary>line chart</summary>

USD CLO arbitrage spread
| Year | New Issue Spread (bp) | Deal-matched (bp) |
|---|---|---|
| 13 | 180 | 310 |
| 14 | 155 | 270 |
| 15 | 225 | 290 |
| 16 | 220 | 260 |
| 17 | 160 | 240 |
| 18 | 170 | 230 |
| 19 | 190 | 145 |
| 20 | 105 | 50 |
| 21 | 255 | 185 |
| 22 | 240 | 210 |
| 23 | 150 | 105 |
| 24 | 160 | 130 |
| 25 | 185 | 145 |
| 26 | 190 | 130 |
</details>

![](images/383f60291dbafe5fe473b97038abe1c4ce0717395628d6eea0abb1ef7af01049.jpg)

<details>
<summary>line chart</summary>

| Year | New Issue Spread | Deal-matched |
|------|------------------|--------------|
| 15   | 270              | 230          |
| 16   | 250              | 300          |
| 17   | 240              | 280          |
| 18   | 220              | 230          |
| 19   | 210              | 200          |
| 20   | 150              | 180          |
| 21   | 210              | 200          |
| 22   | 230              | 210          |
| 23   | 180              | 150          |
| 24   | 200              | 80           |
| 25   | 170              | 160          |
| 26   | 160              | 150          |
</details>

Source: Intex, PitchBook LCD, GS Global Investment Research

Exhibit 2: The trend towards tighter arbitrage spreads coincides with more managers in a more mature market  
![](images/48f03d336999712e7e992c1dfcf1fb73a878f1c3ea2a3cf736d7381b3ef45655.jpg)

<details>
<summary>line chart</summary>

| Year | US Managers | Euro Managers (RHS) |
|------|-------------|---------------------|
| 15   | 50          | 20                  |
| 16   | 30          | 15                  |
| 17   | 45          | 25                  |
| 18   | 55          | 30                  |
| 19   | 60          | 35                  |
| 20   | 50          | 30                  |
| 21   | 65          | 40                  |
| 22   | 80          | 70                  |
| 23   | 55          | 20                  |
| 24   | 75          | 30                  |
| 25   | 80          | 35                  |
| 26   | 85          | 30                  |
</details>

Source: PitchBook LCD, GS Global Investment Research

## Exhibit 3: USD Middle Market CLO arbitrage spreads have tightened towards 300bp

Direct Lending spread calculated as difference between CDLI yield-to-maturity and 3-month LIBOR (SOFR after December 2020)

![](images/27a03667bc35b2da4b104ef6a9cd45ff53dee6c9e4244d5a3b475e2a21f0bbb2.jpg)

<details>
<summary>line chart</summary>

USD Middle Market CLO arbitrage spread vs. Direct Lending Spread
| Year | Middle Market CLO arbitrage spread (%) | Direct Lending spread (RHS) (%) |
|---|---|---|
| 21 | 3.5 | 10.5 |
| 22 | 4.4 | 7.8 |
| 23 | 3.1 | 6.9 |
| 24 | 2.8 | 7.1 |
| 25 | 3.7 | 6.8 |
| 26 | 3.4 | 6.5 |
</details>

Source: Intex, Cliffwater, GS Global Investment Research

That tightening in BSL arbitrage spreads has been especially visible in the USD market. Part of the explanation is cyclical, including a stronger technical demand and lower net loan supply. But we think an important structural driver has been the growth of captive equity funds. These vehicles, which typically commit capital across multiple vintages and cede manager selection and deployment discretion to the originating firm, have altered the behavior of the equity base in the USD market. Market participants have increasingly pointed to captive equity as a force that reduces the sensitivity of equity demand to spot arbitrage conditions. In effect, vintage diversification and continuity of deployment have become more important than maximizing entry spread on any single transaction.

For equity investors, the presence of non-return seeking participants should depress equity returns, all else equal. To be clear, the relationship between spot arbitrage and realized CLO equity returns is far from mechanical. But less attractive starting spreads reduce the headroom for credit losses available to equity investors who opt to both

trade and choose their equity investments on a deal-by-deal basis.

## Wider EUR arbitrage spreads are not a free lunch

This dynamic has not yet become as entrenched in the EUR market, which is one reason EUR equity can appear optically cheaper. While this structural reason should favor EUR equity, and has led to higher equity returns in the past, the key tension is the relatively worse fundamental picture in the EUR loan market, in our view. Default rates have generally risen over the past two years, whereas USD rates have come off their 2024 peak. Given our forecast for slightly higher EUR defaults from here (owing to a less favorable policy and macroeconomic mix), and loan prices which are rich relative to their USD peers, we think some of the excess spread will serve as compensation for credit losses. While software and other asset-light businesses feature more prominently in the USD loan market, there is still significant asset-light exposure in the EUR market, with maturity walls ramping in 2028.

As wider EUR arb spreads come from both wider debt costs and asset spreads, we do not automatically see a wider arb spread as negative for EUR CLO liabilities. Across the stack, we think EUR IG tranches can offer positive carry relative to their USD peers (Exhibit 4).

Exhibit 4: EUR IG tranches offer a spread pickup relative to USD  
EUR/USD tranche spread ratios (adjusted with 5-year cross-currency basis); median since 2021  
![](images/0564f43459926a263fb2a6a579ea8926b47b4c2c7627d43f6942664603d4099a.jpg)

<details>
<summary>bar chart</summary>

EUR/USD primary tranche spread ratio
| Rating | Current | Median |
| :--- | :--- | :--- |
| AAA | 1.06 | 1.07 |
| AA | 1.16 | 1.19 |
| A | 1.14 | 1.21 |
| BBB | 0.96 | 1.09 |
| BB | 0.95 | 1.04 |
</details>

![](images/80d1005fcfcdbd155a95678309e735607062850258b66530ad707f7f2f877c60.jpg)

<details>
<summary>bar chart</summary>

EUR/USD secondary tranche spread ratio
| Rating | Current | Median |
| :--- | :--- | :--- |
| AAA | 0.97 | 0.85 |
| AA | 1.13 | 0.99 |
| A | 1.18 | 1.05 |
| BBB | 1.05 | 1.04 |
| BB | 0.78 | 0.89 |
</details>

Source: PitchBook LCD, Palmer Square, GS Global Investment Research

## Tighter resets

A key benefit of the deal-level framework is that it allows us to track how the economics of a transaction evolve when it is reset or refinanced. Here the contrast between the USD and EUR markets has been notable. In USD, the repricing wave in the loan market has been much more pronounced, and that has meant tighter asset spreads on reset portfolios. As a result, the improvement in liability costs has often been partly or fully offset by reduced asset income. For deals issued since 2023, reset economics in USD have improved only modestly (Exhibit 5).

Conversely, the EUR market deal economics have improved by 50bp for new issues from 2023 onward (Exhibit 6). That likely reflects three factors, in our view. First, loan spread compression has been less aggressive because repricing activity has been slightly more muted vs. the USD market (Exhibit 7). Second, loan supply has generally been somewhat more supportive for redeployment. Third, we think captive funds are more likely to reset CLOs, extend reinvestment periods, and continue to attract management fees at tighter deal economics.

Exhibit 5: USD deal economics have improved by less than 20bp on reset since 2023  
![](images/63e0b321f1ac97b41c656b4f03d542d73cc596a4724c5a72c72a1609daf713a8.jpg)

<details>
<summary>bar chart</summary>

Change in USD CLO arbitrage spread for resets by new issue vintage
| New issue vintage | Asset change (bp) | Liability change (inverted) (bp) | Net change (bp) |
| :--- | :--- | :--- | :--- |
| Q1 2019 | 50 | 10 | 60 |
| Q2 2019 | 35 | 15 | 55 |
| Q3 2019 | 30 | 15 | 50 |
| Q4 2019 | 25 | 15 | 45 |
| Q1 2020 | 15 | 70 | 80 |
| Q2 2020 | -10 | 100 | 105 |
| Q3 2020 | -20 | 55 | 45 |
| Q4 2020 | -15 | 20 | 15 |
| Q1 2021 | -60 | 5 | -70 |
| Q2 2021 | -70 | 5 | -80 |
| Q3 2021 | -75 | 5 | -85 |
| Q4 2021 | -80 | 15 | -90 |
| Q1 2022 | -90 | 15 | -95 |
| Q2 2022 | -100 | 15 | -100 |
| Q3 2022 | -85 | 55 | -35 |
| Q4 2022 | -50 | 80 | 30 |
| Q1 2023 | -30 | 85 | 45 |
| Q2 2023 | -60 | 75 | 35 |
| Q3 2023 | -65 | 75 | 35 |
| Q4 2023 | -65 | 75 | 30 |
| Q1 2024 | -60 | 55 | -5 |
| Q2 2024 | -45 | 35 | -15 |
</details>

Source: Intex, GS Global Investment Research

Exhibit 6: Whereas EUR deals have improved by nearly 50bp over the same period  
![](images/7edbde95f811f485b34bfd5b5439b55637f27b152149640cf9e9e8bcfa648aae.jpg)

<details>
<summary>bar chart</summary>

Change in EUR CLO arbitrage spread for resets by new issue vintage
| New issue vintage | Asset change (bp) | Liability change (inverted) (bp) | Net change (bp) |
| :--- | :--- | :--- | :--- |
| Q1 2019 | -10 | 15 | 20 |
| Q2 2019 | -20 | 20 | -5 |
| Q3 2019 | -30 | 35 | 5 |
| Q4 2019 | -80 | 5 | -75 |
| Q1 2020 | -50 | 40 | 65 |
| Q2 2020 | -10 | 50 | -15 |
| Q3 2020 | -60 | 60 | -15 |
| Q4 2020 | -80 | 40 | -35 |
| Q1 2021 | -60 | 20 | -35 |
| Q2 2021 | -50 | 25 | -15 |
| Q3 2021 | -60 | 55 | -5 |
| Q4 2021 | -70 | 15 | -15 |
| Q1 2022 | -80 | 45 | -45 |
| Q2 2022 | -110 | 60 | -55 |
| Q3 2022 | -30 | 105 | 70 |
| Q4 2022 | -30 | 105 | 70 |
| Q1 2023 | -30 | 70 | 45 |
| Q2 2023 | -30 | 75 | 45 |
| Q3 2023 | -30 | 65 | 45 |
| Q4 2023 | -30 | 55 | 45 |
| Q1 2024 | -30 | 45 | 25 |
| Q2 2024 | -30 | 45 | 90 |
| Q3 2024 | -30 | 45 | 35 |
| Q4 2024 | -30 | 65 | 55 |
</details>

Source: Intex, GS Global Investment Research  
Trailing 6-month repricing volumes scaled by index notional for USD and EUR BSL market

Exhibit 7: EUR new issue loan spreads have lagged the tightening impulse, in part because of lower repricing volumes

![](images/097bd5c03179324f5c6591b8d2fe04704e0a6835721a8a662a15eb7620820ad2.jpg)

<details>
<summary>line chart</summary>

Repricing volumes scaled by market notional
| Date | USD (%) | EUR (%) |
|---|---|---|
| 11 | 0.0 | 0.0 |
| 12 | 0.0 | 0.0 |
| 13 | 0.0 | 0.8 |
| 14 | 0.0 | 0.9 |
| 15 | 0.0 | 1.2 |
| 16 | 1.4 | 1.2 |
| 17 | 6.2 | 1.3 |
| 18 | 4.7 | 0.2 |
| 19 | 0.8 | 0.8 |
| 20 | 2.5 | 1.3 |
| 21 | 2.5 | 1.5 |
| 22 | 0.8 | 0.8 |
| 23 | 0.0 | 0.0 |
| 24 | 2.8 | 2.5 |
| 25 | 6.3 | 4.3 |
| 26 | 2.0 | 2.7 |
</details>

Source: Pitchbook LCD, GS Global Investment Research

## How are managers faring?

In prior work, we have used market pricing to develop CLO manager tiers. Given our tiers are based on liability pricing, the implicit assumption is that the arbitrage spread is roughly similar or proportional across these managers (i.e., managers with tighter liability spreads invest in lower spread assets and vice versa), translating to arbitrage spreads flat across tiers. However, the data supports a more nuanced view.

Using deals from 2026, we find that higher-tiered (tier 1) managers actually have slightly wider arbitrage spreads in the USD market. Conversely, lower-tiered managers (tier 4) in the EUR market have wider arbitrage spreads (Exhibit 8). In the USD BSL market there is both less variation in asset spreads and larger variation in liability spreads across manger tiers, both of which have meant higher-tiered managers are able to capture lower debt costs without forgoing excess spread. Meanwhile, AAA spreads across manager tiers separated by less than 6bp in EUR BSL market, and asset spreads have been more dispersed; the median tier 4 manager asset spread is nearly 50bp wider than that for tier 1 managers.

Exhibit 8: Arbitrage spreads are slightly wider for most defensive managers, while EUR CLO spreads exhibit the opposite pattern  
![](images/8ccb8a93be1b3c689565219e15d9275ff51caf438171052c912497ee67e48e48.jpg)

<details>
<summary>bar chart</summary>

BSL arbitrage spread by manager tier
| Tier | USD (%) | EUR (%) |
|---|---|---|
| 1 | 1.37 | 1.54 |
| 2 | 1.33 | 1.55 |
| 3 | 1.34 | 1.56 |
| 4 | 1.34 | 1.65 |
</details>

Source: PitchBook LCD, Intex, GS Global Investment Research

We thank Patricia Pacheco for her contribution to this report.

## Disclosure Appendix

## Reg AC

We, Shamshad Ali, Amanda Lynam, CPA, Arun Manohar, Spencer Rogers, CFA, Sara Grut, Ben Shumway and Neth Karunamuni, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by

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
