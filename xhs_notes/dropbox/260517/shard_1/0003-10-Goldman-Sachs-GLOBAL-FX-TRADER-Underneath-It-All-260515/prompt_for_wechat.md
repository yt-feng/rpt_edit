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
GLOBAL FX TRADER

Underneath It All

# Our thoughts on USD, GBP, BRL, JPY, Terms of Trade, HUF, ARS, and Dollar Drivers.

USD: Two shocks at the same time. While the broad Dollar is close to flat over the last few months, that obscures larger shifts under the surface and quietly building Dollar appreciation pressure. We have been emphasizing that terms of trade have been a key differentiator for FX returns in this more divided Dollar environment, and it is increasingly clear that two major forces—the energy shock and AI-driven demand—are responsible for the shortages causing that move (more in the ToT bullet below). Our economists have laid out how these factors have opposing effects on growth—we think the AI boom is one reason why global growth has slowed only moderately so far despite a longer disruption to global energy flows—but reinforce each other on the inflation side, at least in the near term. This is consistent with the direction of our macro forecasts: our global growth expectations have been roughly stable since the middle of March (Exhibit 1), despite a longer conflict, while inflation projections have continued to drift higher (Exhibit 2). We think this helps explain the Dollar’s strength over the last week following upside US inflation surprises that helped push global bond yields higher. Still-restricted energy flows, with limited relevant macro news from the Trump-Xi summit, have helped put these vulnerabilities—and the Dollar’s relative insulation—back into focus. We have attributed the more range-bound Dollar to the fact that it is caught between the more cyclical, commodity-forward currencies on the one hand and more stringent FX management on the other. As this past week has demonstrated, we think the clearest risk for a stronger Dollar is if a wider energy shock begins to pressure growth, policy, and prospective returns in other developed countries, particularly Europe.

Kamakshya Trivedi

+44(20)7051-4005

kamakshya.trivedi@gs.com

GS International

Michael Cahill

+44(20)7552-8314

michael.e.cahill@gs.com

GS International

Danny Suwanapruti

+65-6889-1987

danny.suwanapruti@gs.com

GS (Singapore) Pte

Teresa Alves

+44(20)7051-7566

teresa.alves@gs.com

GS International

Karen Reichgott Fishman

+1(212)855-6006

karen.fishman@gs.com

GS & Co. LLC

Stuart Jenkins

+44(20)7051-4700

stuart.jenkins@gs.com

GS International

Victor Engel

+44(20)7051-3862

victor.engel@gs.com

GS International

Lexi Kanter

+1(212)855-9701

alexandra.kanter@gs.com

GS & Co. LLC

Exhibit 1: Our global growth expectations have been roughly stable since the middle of March...   
![](images/a04ba4871933fdcbde4ecb66ff53fa75522f3b7c8bf260df2c850c8196113984.jpg)

<details>
<summary>line</summary>

| Date   | GS    | Bloomberg Consensus |
|--------|-------|---------------------|
| Jul-25 | 2.3   | 2.4                 |
| Sep-25 | 2.5   | 2.4                 |
| Nov-25 | 2.8   | 2.5                 |
| Jan-26 | 3.0   | 2.7                 |
| Mar-26 | 2.9   | 2.8                 |
| May-26 | 2.4   | 2.5                 |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 2: ...while inflation projections have continued to drift higher   
![](images/4b72ed01b38a1a4e722e7fb09320685c151d373bbb4d3c6a4cc2141bdc611f6f.jpg)

<details>
<summary>line</summary>

| Date   | GS   | Bloomberg Consensus |
|--------|------|---------------------|
| Jul-25 | 2.5  | 2.5                 |
| Sep-25 | 2.5  | 2.5                 |
| Nov-25 | 2.5  | 2.5                 |
| Jan-26 | 2.5  | 2.5                 |
| Mar-26 | 2.5  | 2.5                 |
| May-26 | 3.5  | 3.5                 |
</details>

Source: Bloomberg, GS Global Investment Research

GBP: Pressures coming together. UK political newsflow has picked up following last week's local elections and, as is often the case, a rise in political uncertainty has been accompanied by FX underperformance. Heading into this week, we saw relatively little risk premium in the currency, with EUR/GBP moving closely in line with our GSBEER model of cyclical fundamentals. That has changed in recent days, with the cross now incorporating about 1ppt of fiscal premium according to this model, but the newly reintroduced premium is still light compared to most of last year when it regularly traded about $2\%$ above its fitted value (Exhibit 3). We think that represents a reasonable near-term target at least until there is more clarity on the policy plans. What would follow a leadership transition, and whether it would see any material shift in fiscal policy, also remains far from clear. In this context, it is worth noting that prediction market pricing of a leadership transition by year-end has already been elevated for some time, so we attribute the recent underperformance mostly to a narrowing in the timeline, as well as the confluence of realising this political pressure with macro factors that are already challenging the UK fiscal outlook at this point. Our economists note that the macro repercussions of the energy shock have already driven a further erosion of fiscal headroom, and energy futures have continued to move higher for the rest of the year. This presents a more durable risk to Sterling, and can also amplify the pass-through from political uncertainty relative to last year. It is also less clear to us that recent sources of Sterling resilience, namely a sharp rebound in global risk sentiment and larger-than-usual cross-border M&A inflows, can remain as supportive as they have been over the past few weeks. On net, we continue to see near-term upside risks to EUR/GBP from these levels, but with clearer value versus the forwards in Sterling downside versus the likes of AUD or USD over the coming months, which offer exposure to further terms of trade differentiation from the energy shock, as well as to domestic UK macro and premium risks.

Exhibit 3: Recent divergence between actual and model-implied EUR/GBP demonstrates a partial reintroduction of political premium in Sterling   
![](images/12c2a71850d0a0a7b21b10b84d7487980710f21c7ff71947259dd2b980fcd1ae.jpg)

<details>
<summary>line</summary>

| Date     | EUR/GBP Actual | EUR/GBP Fitted | Nominal 2y Rate Differential | Credit Spreads | Nominal 2y Rate Differential | Constant |
|----------|----------------|----------------|-------------------------------|----------------|------------------------------|----------|
| 1-Jan    | -0.8           | -0.3           | -0.6                          | -0.1           | -0.7                         | -0.1     |
| 15-Jan   | -0.6           | -0.2           | -0.5                          | -0.1           | -0.6                         | -0.1     |
| 29-Jan   | -0.4           | -0.1           | -0.4                          | -0.1           | -0.5                         | -0.1     |
| 12-Feb   | -0.2           | 0.0            | -0.3                          | -0.1           | -0.4                         | -0.1     |
| 26-Feb   | 0.5            | 0.3            | 0.2                           | 0.1            | 0.2                          | 0.1      |
| 12-Mar   | -0.8           | -0.5           | -0.7                          | -0.2           | -0.6                         | -0.2     |
| 26-Mar   | -1.2           | -0.8           | -1.5                          | -0.3           | -1.3                         | -0.3     |
| 9-Apr    | -0.6           | -0.4           | -0.9                          | -0.2           | -0.8                         | -0.2     |
| 23-Apr   | -0.8           | -0.6           | -1.1                          | -0.3           | -1.0                         | -0.3     |
| 7-May    | -1.5           | -1.2           | -1.8                          | -0.4           | -1.6                         | -0.4     |
</details>

Source: GS FICC and Equities, GS Global Investment Research

BRL: Caught in a noise slide. After outperforming for most of the year, the Real has been a clear underperformer this week. Today's BRL depreciation likely reflects the broader decline in risk sentiment amid heavy long positioning. But domestic developments were the key driver earlier in the week when a media report regarding presidential candidate Flavio Bolsonaro drove USD/BRL more than 2% higher. The last time election-related headlines drove BRL weaker in December 2025, we noted that Real underperformance relative to other market developments was contained, and that it was difficult to gauge effectively what different developments meant for the election outcomes so far in advance. As these developments come closer to the election date (the first round is on October $4^{\text{th}}$ ), their impact could be more meaningful, especially given crowded positioning. Still, we think that the implications for polling and the odds of different election outcomes are what will ultimately matter for BRL. Recent reports suggest a growing lead for President Lula in the latest tracking, but there is limited information for now. While BRL will likely be responsive to any shift in election odds, we would also note that most of the Real's year-to-date appreciation has been driven by global factors and not domestic premium shifts. Using our cyclical model, we find that BRL's typical beta to Brazil's terms of trade and US equity performance explains most of its performance over the past few months (Exhibit 4). Instead, our proxy for Brazil-specific risk (a residual of Brazil's CDS after stripping out the impact of the other model inputs) has seen more limited moves this year. All in, BRL's performance looks broadly aligned with the model's inputs. Looking ahead, the lack of a large outperformance gap would suggest BRL is not as vulnerable in a less favourable backdrop beyond what its typical betas would imply. Here, an environment of higher-for-longer energy prices is a structural tailwind for the Real, but increasing political noise and weaker global risk sentiment could weigh on performance over the near-term.

Exhibit 4: The Real's typical beta to Brazil's terms of trade and US equity performance explains most of its performance over the past few months   
![](images/24276a7693f1f4e934fdbe952eb16893384f91e92c58a804570e44a8ffe8035a.jpg)

<details>
<summary>line</summary>

| Date     | Actual returns | Predicted returns | CDS residual | Residual | US 10-year real yields | S&P Index | Terms of Trade |
|----------|----------------|-------------------|--------------|----------|------------------------|-----------|----------------|
| 01-Feb   | 0.0            | 0.0               | 0.0          | 0.0      | 0.0                    | 0.0       | 0.0            |
| 10-Feb   | 0.5            | 0.3               | 0.2          | 0.4      | 0.1                    | 0.2       | 0.3            |
| 19-Feb   | 1.0            | 0.6               | 0.4          | 0.7      | 0.3                    | 0.5       | 0.6            |
| 02-Mar   | 1.5            | 0.8               | 0.6          | 1.0      | 0.5                    | 0.7       | 0.8            |
| 11-Mar   | -1.0           | -0.5              | -0.3         | -0.8     | -1.2                   | -0.6      | -1.1           |
| 20-Mar   | -2.0           | -1.5              | -1.2         | -1.8     | -2.5                   | -1.8      | -2.2           |
| 31-Mar   | -1.5           | -1.0              | -0.8         | -1.5     | -2.0                   | -1.5      | -1.8           |
| 09-Apr   | 2.0            | 1.5               | 1.0          | 1.5      | 1.0                    | 1.2       | 1.4            |
| 20-Apr   | 3.0            | 2.5               | 1.8          | 2.5      | 1.8                    | 2.0       | 2.2            |
| 29-Apr   | 4.0            | 3.5               | 2.5          | 3.5      | 2.5                    | 2.8       | 3.0            |
| 08-May   | 5.0            | 4.5               | 3.5          | 4.5      | 3.5                    | 3.8       | 4.2            |
|        |                |                   |              |          |                        |           |                |
</details>

BRL returns series displayed until May 14, 2026. Sensitivities estimated on weekly data over last 18 months

Source: Bloomberg, GS Global Investment Research

JPY: Not enough. The Yen weakened versus the Dollar over the past week, reflecting the continued depreciation pressures on the currency despite recent intervention. The comments by FM Katayama and Secretary Bessent following their meeting in Tokyo disappointed hopes for any sign of more active support from the US and stopped short of explicitly endorsing the latest intervention. The biggest headwind to JPY, however, continues to be the broader backdrop of elevated oil prices, US growth outperformance, higher-for-longer rates, and constructive risk sentiment—each of which tend to push up USD/JPY. Currency-negative fundamentals likely explain what appears to be the smaller impact of intervention on USD/JPY per \$bn over the two weeks since April 30 compared to the interventions in October 2022 and July 2024, when macro conditions were also pushing in the same direction (Exhibit 5). Prior interventions are not exactly comparable since the operations were done on two consecutive days rather than over the course of several days, like in this latest episode, and we estimate its total size based on the BoJ's funds supply/demand data since the official intervention data have not yet been released. But this exercise broadly reinforces our view that the 2026 intervention most closely echoes April 2024 and its less sustained impact versus other rounds. Even hawkish comments from BoJ board member Masu on Thursday struggled to support the currency. While we have said that faster and steeper hikes by the BoJ would be a meaningful catalyst for sustained Yen strength, an exceptionally gradual hiking cycle, including a hike in June hike that is already nearly 80% priced, would likely not be enough to dominate other factors—just as the hike in December that was pulled forward from January did little to halt Yen weakness thereafter. Overall, we continue to be skeptical that intervention can be successful in driving USD/JPY sustainably lower without a shift towards greater recession concerns or much more hawkish BoJ

policy.

Exhibit 5: Currency-negative fundamentals likely explain what appears to be the smaller impact of intervention on USD/JPY since April 30   
![](images/923d822219ca71ee109c723f9f3ced73a174c60ac95f494406bc9a186315e229.jpg)

<details>
<summary>bar</summary>

Spot Move in USD/JPY Over 2 Weeks Following the First Day of Intervention Scaled by Total Size in $bn
| First Day of Intervention | Basis points |
| :--- | :--- |
| 21-Oct-22 | -5.5 |
| 29-Apr-24 | -2.1 |
| 11-Jul-24 | -13.7 |
| 30-Apr-26 | -2.3 |
</details>

Source: GS Global Investment Research, BoJ, Bloomberg

ToT: Dealing with a double shock. We have been arguing that terms of trade have been a key driver of FX returns since the start of the energy shock. And we have been emphasizing that moves in Dollar crosses understate terms of trade dynamics compared to near-neighbor crosses like NOK/SEK, AUD/NZD, and BRL/CLP, which have moved much further. We attribute part of the broad Dollar's more muted response to this conflict to the fact that its impact has fallen most severely on less central US trading partners and those with heavily-managed currencies—particularly in Asia. Indeed, we find that Asia FX returns have tracked terms of trade moves less closely than elsewhere in EM and the G10 (Exhibit 6). Besides more stringent currency management, this also reflects that commodity terms of trade do not capture the recent boost from higher-value tech exports, overstating the deterioration for the likes of KRW, TWD, and CNY; we find that incorporating tech exports alongside commodity terms of trade better explains recent Asia FX performance (Exhibit 7). More broadly, we find FX returns over shorter horizons have tracked less well with changes in terms of trade than they have over the entirety of the conflict period. This seems in part due to the fact commodity exporters like AUD have seen asymmetric outperformance on days when energy prices increase. We think this dynamic helps reveal investor sentiment and an expectation that the current environment should remain one of higher-for-longer energy prices. And though we expect that commodity exporters would see relative underperformance on a sustained de-escalation, terms of trade should remain relevant in the more medium term. Beyond any initial relief, the more lasting inflation and growth impacts these ToT shifts help capture should continue to influence FX returns over time, leaving us most constructive on currencies with both commodity and cyclical

exposure.

Exhibit 6: Asia FX returns have tracked terms of trade moves less closely than elsewhere in EM and the G10   
![](images/70f4716f95cc34b440d1c99d1879d83316d8243388891925fe6472f02e5bd1c0.jpg)

<details>
<summary>scatter</summary>

| Currency | Spot Return (%) | % ToT (Std Dev) |
|----------|-----------------|-----------------|
| HUF      | 4.0             | -               |
| GBP      | 0.5             | -               |
| EUR      | -1.0            | -               |
| NZD      | -1.5            | -               |
| MXN      | 0.0             | -               |
| ZAR      | -3.5            | -               |
| SEK      | -3.0            | -               |
| CHF      | -2.0            | -               |
| CZK      | -1.5            | -               |
| PLN      | -1.8            | -               |
| CLP      | -2.5            | -               |
| TRY      | -3.2            | -               |
| NOK      | 3.5             | 4.0             |
| AUD      | 2.0             | 2.5             |
| BRL      | 2.5             | 3.0             |
| CAD      | -0.5            | 4.5             |
| COP      | -1.0            | 5.0             |
| CAND     | -1.2            | 5.5             |
| MXN      | -2.0            | 6.0             |
| EUR      | -1.2            | 6.5             |
| NZD      | -1.8            | 7.0             |
| CHF      | -2.2            | 7.5             |
| ZAR      | -3.0            | 8.0             |
| SEK      | -3.5            | 8.5             |
</details>

Source: GS Global Investment Research, GS FICC and Equities

Exhibit 7: Incorporating tech exports alongside commodity terms of trade better explains recent Asia FX performance   
![](images/c7223bdcd26bba8bfdb9195

[中间内容因长度限制已省略]

me have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
