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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`NOM`。标题格式建议：`# NOM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## FX Insights

Foreign Exchange - Global

## Summer sell-off for the USD?

Flagging the risks around "US exceptionalism"

- The consensus has turned more bullish on USD, but there are signs that a reversal lower in the USD could be more probable in the next few months.  
- Recent “US exceptionalism” is valid – upside data surprises, firmer US rates, solid US equity performance and subsequent USD gains – but will likely face higher hurdles.  
- When US data surprise have been this positive in the past, the USD has fallen around 75% of the time in the subsequent three months.  
- Positioning has also become more skewed to USD longs, exacerbating pullback risk.

## Tactical USD bull case remains intact

The USD bull case has become more prominent in recent weeks. Strong US data and a repricing of Fed rate hikes in the year ahead support USD gains (Fig. 1). US equities have been outperforming for most of the last few months (albeit with a recent pull back), which has aligned with a resumption of inflows into US capital markets. Upcoming tech IPOs are adding further fuel to the fire regarding potential USD demand for US assets. In addition, ongoing Middle East tensions provide a further source of support for USD, even as energy prices have softened on the hopes of de-escalation. The latest headlines from President Trump about a deal being signed over the coming weekend will obviously test USD resilience in the near term.

We have been tactically aligned with USD strength through our long USD/CAD trade, which we think has scope to reflect the repricing in rate expectations and because there is less downside risk to this pair on any sign of geopolitical de-escalation compared with most other G10 pairs.

Fig. 1: USD still appears slightly low relative to the repricing of front-end interest rates  
![](images/82805eeca003e6108b0ed34245199097987c2abd5b6582aa225392e234d07555.jpg)

<details>
<summary>line chart</summary>

| Date   | USD-G10 equal weight | US 2y yield diff (equal weight) |
|--------|----------------------|----------------------------------|
| Jan-24 | 114                  | 1.0                              |
| Jul-24 | 118                  | 1.3                              |
| Jan-25 | 123                  | 1.5                              |
| Jul-25 | 114                  | 1.0                              |
| Jan-26 | 108                  | 0.7                              |
</details>

Source: Bloomberg, NOM

Fig. 2: USD long positioning has been building but not to the same degree as in early 2025  
![](images/4c8ffb8a938368bafc25a02f3441887e7f2fc569a4dd5563475b496cc9cfc9a1.jpg)

<details>
<summary>bar chart</summary>

IMM non-comm positioning, % of OI
| Currency | Jan 25 (%) | Latest (%) |
| :--- | :--- | :--- |
| USD | 27 | 8 |
| GBP | -1 | -32 |
| EUR | -15 | 11 |
| AUD | -60 | 24 |
| NZD | -70 | -62 |
| CAD | -78 | -55 |
| JPY | -13 | -37 |
| CHF | -72 | -73 |
</details>

Production Complete: 2026-06-12 07:48 UTC  
Source: Bloomberg, NOM

## Research Analysts

## Global FX Strategy

Dominic Bunning - Nlplc

dominic.bunning@NOM.com

+44 (0) 20 7102 4063

Yusuke Miyairi, CFA - NIplc

yusuke.miyairi@NOM.com

+44 (0) 20 7102 4145

## Global Economics

David Seif - NSI

david.seif@NOM.com

+1 212 667 9180

That said, positioning risks may already be starting to turn in the other direction. While USD longs (as measured by CFTC non-commercial positions, Fig. 2) are not that elevated, short positions are being built in a range of other G10 currencies, albeit not to the same extent as in early 2025.

So what could go wrong? At times of increasingly extreme sentiment, we should always consider the counter-argument. We think it is right to question whether sentiment is already turning too bullish on the US again, with the buzzwords of “US exceptionalism” being increasingly mentioned in client meetings and in the media.

## Surprise, surprise

The significant rise in US economic surprises stands out to us, as US data have beaten expectations consistently over the last few months. The Citi US Economic Surprise Index recently hit its highest level in nearly three years, and in the series' 23-year history, there have been few occasions when data surprises have been this positive (Fig. 3). There has also been a significant increase in US growth expectations among economists relative to other DM economies (Fig. 4). This widening suggests the bar to further upside surprises is rising, and there is a growing risk we are close to peak USD optimism.

There was a similar pattern in consensus forecasts in late-2024, as expectations of a Trump election victory and subsequent growth boom increased. As it turned out, the USD topped out a week before Trump's inauguration, nearly a full three months before the short USD narrative gained most traction following the Liberation Day tariff announcements.

Fig. 3: US economic surprises have been exceptional in recent months relative to the last 20 years...  
![](images/49c256295f9c449079758bdffc904e8e21a4ed81b839271e7bbcf216d25b17c4.jpg)

<details>
<summary>line chart</summary>

| Year | US economic surprise index |
| ---- | -------------------------- |
| 03   | ~-120                      |
| 05   | ~-80                       |
| 07   | ~-60                       |
| 09   | ~-140                      |
| 11   | ~-100                      |
| 13   | ~-60                       |
| 15   | ~-40                       |
| 17   | ~-20                       |
| 19   | ~-60                       |
| 21   | ~-150                      |
| 23   | ~-60                       |
| 25   | ~-40                       |
</details>

Source: Bloomberg, NOM

Fig. 4: ... while economists have raised their growth expectations relative to other DM economies  
![](images/375f8fc2bd75213ab666f02e2dccabf6341ce14343787eff66d5b1882f68baf1.jpg)

<details>
<summary>line chart</summary>

| Date   | 2026 US-EZ | 2026 US-GB | 2026 US-JN |
|--------|------------|------------|------------|
| Jun-25 | 0.5        | 0.4        | 0.7        |
| Sep-25 | 0.7        | 0.6        | 0.9        |
| Dec-25 | 0.9        | 0.8        | 1.1        |
| Mar-26 | 1.3        | 1.5        | 1.7        |
| Jun-26 | 1.3        | 1.3        | 1.4        |
</details>

Source: Bloomberg, NOM

## Exceptional US surprises do not precede exceptional USD returns

We looked at the full history of US Economic Surprise Index data and considered occasions in which the index crossed up over the 60 level – where it has been hovering for the last week or so. We found 41 examples. We then examined USD returns versus all G10 currencies and as an equal-weighted index over the subsequent 1 week, 2 weeks, 1 month and 3 months. The data for the first three periods show little of note. But looking at the 3-month return window, we find consistently negative USD performance (Fig. 5, Fig. 6, Fig. 7, Fig. 8).

When we raise the threshold on the US Surprise Index to a slightly higher hurdle level of 70, we find the returns become much more consistently negative across all performance windows. This suggests we are on the cusp of tipping over into increasing downside risks for USD.

Fig. 5: USD has tended to weaken in the 3m after US surprises reached current levels  
![](images/695396b4de07c9b84676f44ed24d6d181264e6fade44d2ddb0116927f6e17813.jpg)

<details>
<summary>line chart</summary>

| Year | 3m return USD/G10 equal weight |
| ---- | ------------------------------ |
| 2003 | -8.5%                          |
| 2004 | 4.0%                           |
| 2005 | -6.0%                          |
| 2006 | -1.0%                          |
| 2007 | -4.0%                          |
| 2008 | -7.0%                          |
| 2009 | 17.5%                          |
| 2010 | -5.5%                          |
| 2011 | -4.5%                          |
| 2012 | 1.5%                           |
| 2013 | -1.5%                          |
| 2014 | -3.0%                          |
| 2015 | -1.0%                          |
| 2016 | -1.5%                          |
| 2017 | -3.5%                          |
| 2018 | -1.5%                          |
| 2019 | -8.5%                          |
| 2020 | 2.5%                           |
| 2021 | -4.5%                          |
| 2022 | 8.5%                           |
| 2023 | 2.5%                           |
| 2024 | -4.5%                          |
</details>

Source: Bloomberg, NOM

Fig. 6: USD/G10 equal weighted returns relative to the level of the US Economic Surprise Index  
![](images/92a9e4b1560c9887ef7b4cc99cdbd122e065dc0de52cfc5a23efda36a0a22139.jpg)

<details>
<summary>scatterplot</summary>

| 3m return USD/G10 equal weight |
| ----------------------------- |
| 60                            |
| 61                            |
| 62                            |
| 63                            |
| 64                            |
| 65                            |
| 66                            |
| 67                            |
| 68                            |
| 69                            |
| 70                            |
| 72                            |
| 74                            |
| 76                            |
| 78                            |
| 80                            |
| 83                            |
</details>

Source: Bloomberg, NOM

Fig. 7: Average returns for USD/G10 pairs and an equal weighted USD/G10 index after US surprises breached current levels Sample size for US Economic Surprise Index breaching the 60 level historically is 41

<table><tr><td>Average</td><td>USDEUR</td><td>USDJPY</td><td>USDGBP</td><td>USDAUD</td><td>USDNZD</td><td>USDCAD</td><td>USDNOK</td><td>USDSEK</td><td>USDCHF</td><td>USD/G10 ew</td></tr><tr><td>1w</td><td>-0.1%</td><td>-0.2%</td><td>-0.2%</td><td>0.0%</td><td>-0.1%</td><td>0.0%</td><td>-0.1%</td><td>0.0%</td><td>0.0%</td><td>-0.1%</td></tr><tr><td>2w</td><td>-0.1%</td><td>-0.3%</td><td>-0.1%</td><td>0.5%</td><td>0.3%</td><td>0.4%</td><td>0.4%</td><td>0.2%</td><td>-0.2%</td><td>0.1%</td></tr><tr><td>1m</td><td>-0.7%</td><td>-0.8%</td><td>-0.4%</td><td>0.1%</td><td>0.2%</td><td>0.4%</td><td>0.3%</td><td>-0.4%</td><td>-0.8%</td><td>-0.3%</td></tr><tr><td>3m</td><td>-1.9%</td><td>-0.7%</td><td>-1.5%</td><td>-2.5%</td><td>-2.2%</td><td>-1.2%</td><td>-1.9%</td><td>-2.2%</td><td>-2.0%</td><td>-1.8%</td></tr></table>

Source: Bloomberg, NOM

Fig. 8: Hit ratio for USD/G10 pairs and an equal-weighted USD/G10 index after US surprises reached current levels  
Sample size for US Economic Surprise Index breaching the 60 level historically is 41

<table><tr><td>Hit Rate</td><td>USDEUR</td><td>USDJPY</td><td>USDGBP</td><td>USDAUD</td><td>USDNZD</td><td>USDCAD</td><td>USDNOK</td><td>USDSEK</td><td>USDCHF</td><td>USD/G10 ew</td></tr><tr><td>1w</td><td>46.3%</td><td>51.2%</td><td>51.2%</td><td>46.3%</td><td>48.8%</td><td>43.9%</td><td>53.7%</td><td>43.9%</td><td>51.2%</td><td>51.2%</td></tr><tr><td>2w</td><td>43.9%</td><td>43.9%</td><td>41.5%</td><td>48.8%</td><td>43.9%</td><td>41.5%</td><td>43.9%</td><td>51.2%</td><td>43.9%</td><td>46.3%</td></tr><tr><td>1m</td><td>48.8%</td><td>39.0%</td><td>39.0%</td><td>48.8%</td><td>48.8%</td><td>41.5%</td><td>53.7%</td><td>36.6%</td><td>43.9%</td><td>43.9%</td></tr><tr><td>3m</td><td>22.0%</td><td>31.7%</td><td>22.0%</td><td>26.8%</td><td>31.7%</td><td>36.6%</td><td>29.3%</td><td>24.4%</td><td>19.5%</td><td>26.8%</td></tr></table>

A hit ratio of 50% would mean that the currency pair was higher and lower an equal number of times at the end of the specified window. Source: Bloomberg, NOM

## Flagging the risks – US employment seasonality, Warsh walkback, tech turnaround

We see three clear risks that could push market sentiment on USD to reverse:

1. US employment data: Our baseline view is that the US labour market is resilient and is likely re-accelerating. But we believe there are risks in the months ahead related to potential residual seasonality in the data, rather than true weakness.

The last three years have all seen significant downside surprises to US employment data in July (this year due for release on 7 August; Fig. 9). This could weigh on the US exceptionalism narrative, even temporarily, especially after three consecutive upside surprises to nonfarm payrolls. Signs of this residual seasonality appear to be showing up already in recent weekly initial jobless claims.

2. Fed Chair Warsh and the Fed reaction function: How new Fed Chair Kevin Warsh interacts with the rest of the FOMC is a big source of uncertainty to markets. He is

likely at the dovish end of the spectrum and could find it challenging to fully fight back against the latest momentum in market pricing. But if he is able to do so and to bring enough FOMC members on side with him, then it is possible that Warsh curbs the latest expectations for rate hikes. Indeed, he may be able to use signs of labour market weakness (see point 1) as a catalyst for a more dovish message.

3. Tech and the AI trade has been fuelling US economic and market optimism. We see AI capex and similar investments adding around 2ppt to US GDP (in gross terms, Fig. 10). But with a swathe of US tech IPOs on the way, more capex being funded through issuance rather than cash flow, and with AI-consuming firms increasingly pushing back on costs of these services, there is a risk that recent hype starts to fade and that the extreme optimism for these firms wanes. This could affect both the consumer (through negative wealth effects/tighter financial conditions if stocks correct significantly) and investment spending, if such spending is no longer deemed positive for share prices (see Oracle's performance on 11 June after announcing larger capex than expected).

Fig. 9: The seasonality of the US nonfarm payrolls  
![](images/ac86ef076e39837a1b08b7d5c49d678352fbc080230a0502fc15d002ebf1f12a.jpg)

<details>
<summary>bar chart</summary>

'000s, (+) = positive surprises
| Month | Pre-Covid average (2015-2019) (%) | Past three year average (2023-25) (%) | 2026 (%) |
|---|---|---|---|
| Jan | 40 | 155 | 65 |
| Feb | 15 | 50 | -145 |
| Mar | -45 | 60 | 115 |
| Apr | 5 | 10 | 50 |
| May | -35 | 85 | 85 |
| Jun | 45 | 10 | 0 |
| Jul | 10 | -35 | 0 |
| Aug | -20 | -15 | 0 |
| Sep | -45 | 115 | 0 |
| Oct | 20 | 10 | 0 |
| Nov | 15 | 10 | 0 |
| Dec | 30 | 35 | 0 |
</details>

Note: Surprises are measured by taking the difference between actual (1st estimate) and Bloomberg's consensus. Source: Macrobond, Bloomberg, NOM

Fig. 10: Gross AI capex could be up to 2ppt of US GDP  
![](images/69a175b2c889fc7499efcda4a56daf1b5bbee8f61104ee4fcd77db35a5422076.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Amazon | Alphabet | Meta | Microsoft | Oracle | Total |
|------|--------|----------|------|-----------|--------|-------|
| 11   | 0      | 0        | 0    | 0         | 0      | 0     |
| 13   | 0      | 0        | 0    | 0         | 0      | 0     |
| 15   | 0      | 0        | 0    | 0         | 0      | 0     |
| 17   | 0      | 0        | 0    | 0         | 0      | 0     |
| 19   | 0      | 0        | 0    | 0         | 0      | 0     |
| 21   | 0      | 0        | 0    | 0         | 0      | 0     |
| 23   | 0      | 0        | 0    | 0         | 0      | 0     |
| 25   | 130    | 110      | 80   | 60        | 40     | 380   |
| 26   | 200    | 180      | 150  | 120       | 80     | 650   |
Current projections
As of Q1 26
Total
</details>

Source: Company filings, Bloomberg, NOM

## Conclusions

USD bullishness has become much more consensus in recent weeks, for good reasons. But there are a number of clear risks to this narrative that we think are worth flagging. Most importantly for us, the recent strength in US data surprises has historically been more closely linked to future USD weakness than to strength, and long USD positioning / short positioning for other currencies is moving into territory that could start to look stretched. Signs of de-escalation in the Middle East would also be a catalyst for a turn in USD.

We are confident in our USD upside exposure through our long USD/CAD trade for the time being, but the rest of our recommendations have less directional beta to the USD – such as short AUD/NZD, long CHF/JPY and long EUR/GBP. And we will be closely watching the above risks, as well as any unexpected events that could flip the path of the least resistance for the USD to the downside from here.

## Appendix A-1

This report has been produced by NOM International plc (NIplc), UK.

See Disclaimers for NOM Group entity details.

## Analyst Certification

I, Dominic Bunning, hereby certify (1) that the views expressed in this Research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of my compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## ADDITIONAL DISCLOSURES REQUIRED IN THE U.S.

Principal Trading: NOM Securities International, Inc and its a

[中间内容因长度限制已省略]

DVISER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International plc, UK. All rights reserved.
"""
