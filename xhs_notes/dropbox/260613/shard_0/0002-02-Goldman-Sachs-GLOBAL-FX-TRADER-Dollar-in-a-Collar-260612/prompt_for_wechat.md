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
GLOBAL FX TRADER

Dollar in a Collar

## Our thoughts on USD, CNY, GBP, JPY, NJA FX, CHF & ILS

USD: Oil off the boil keeps the Dollar in a collar. We have been arguing recently that the combination of two global themes—an AI boom and an energy supply bust—are both net positive for the Dollar, but strong cyclical forces and policy measures push in the other direction for key parts of the currency complex. That cyclicality, and the US’s relative isolation, keep the Dollar captive to ceasefire headlines, but we think the trendline keeps pointing higher in the near term as the fallout from a more sustained energy shortfall grows. At the same time, a growing realization of a smaller-than-expected oil deficit has helped keep growth expectations from diverging further even as the disruption drags on longer. In this context, we view the recent moves as trimming some of the dovish Dollar tail around next week’s FOMC, as pricing for the next few meetings now shows a more limited premium for hikes. But even beyond next week, we think more restrained energy moves limit the opportunity for USD volatility to climb out of the doldrums despite elevated macro uncertainty. We have noted that global factors like equity and commodity prices could explain the majority of FX moves in March and April (Exhibit 1), but lately more domestic factors—like rate differentials—are starting to become more important once again (Exhibit 2). Consistent with the shift in macro pricing on resolution announcements, a smaller commodity shock will limit the scope for that divergence. But we think the duration of the disruption also puts a floor under the Dollar as long as a deal is close but the Strait is (mostly) closed.

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

Exhibit 1: Global factors like equity and commodity prices could explain the majority of FX moves in March and April  
![](images/48be75811b4b9550d6af6f11d9932f9c534492de92f0d9d41044a1e13c600e6c.jpg)

<details>
<summary>line chart</summary>

| Date     | Constant | Move Implied by Beta to Risk | Move Implied by Beta to European Nat Gas | Total Implied Move | Actual Move |
|----------|----------|------------------------------|------------------------------------------|--------------------|-------------|
| 27-Feb   | 0        | 0                            | 0                                        | 0                  | 0           |
| 10-Mar   | -1       | -1                           | -1                                       | -1                 | -1          |
| 19-Mar   | -2       | -2                           | -2                                       | -2                 | -2          |
| 30-Mar   | -3       | -3                           | -3                                       | -3                 | -3          |
| 8-Apr    | -1       | -1                           | -1                                       | -1                 | -1          |
| 17-Apr   | 0        | 0                            | 0                                        | 0                  | 0           |
| 28-Apr   | 0        | 0                            | 0                                        | 0                  | 0           |
| 7-May    | 0        | 0                            | 0                                        | 0                  | 0           |
| 18-May   | 0        | 0                            | 0                                        | 0                  | 0           |
| 27-May   | 0        | 0                            | 0                                        | 0                  | 0           |
| 5-Jun    | 0        | 0                            | 0                                        | 0                  | 0           |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 2: ...but lately more domestic factors—like rate differentials—are starting to become more important once again  
![](images/420a5b8e16215cf99b08be8fb28e8ce929cca9486adca0e4143a60de87e6338d.jpg)

<details>
<summary>line chart</summary>

| Date    | EUR/USD Actual | EUR/USD Fitted | Nominal 2y Rate Differential | EU Sovereign Spreads | Copper Prices | Credit Spreads |
|---------|----------------|----------------|-------------------------------|----------------------|---------------|----------------|
| 9-Apr   | 0.0            | 0.0            | 0.0                           | 0.0                  | 0.0           | 0.0            |
| 17-Apr  | 0.8            | 0.6            | -0.2                          | 0.4                  | 0.5           | 0.3            |
| 27-Apr  | 0.2            | 0.1            | -0.4                          | 0.1                  | 0.3           | 0.2            |
| 5-May   | 0.6            | 0.4            | -0.6                          | 0.7                  | 0.6           | 0.5            |
| 13-May  | 0.4            | 0.3            | -0.8                          | 0.5                  | 0.4           | 0.3            |
| 21-May  | -0.2           | -0.1           | -1.0                          | -0.1                 | -0.2          | -0.1           |
| 29-May  | -0.4           | -0.3           | -1.2                          | -0.3                 | -0.4          | -0.2           |
| 8-Jun   | -1.5           | -1.4           | -1.6                          | -1.7                 | -1.6          | -1.5           |
</details>

Source: GS FICC and Equities, GS Global Investment Research

CNY: Trading stronger. Persistent CNY strength has been one of the factors that has held back broader Dollar appreciation, and we expect CNY strength to extend in the months ahead. Given the highly undervalued levels of the currency and China's trade competitiveness, policymakers should be, and are proving, more tolerant of gradual currency strength. And so far at least, the ructions in the global economy as a result of the Iran-US war and the modest real appreciation of the currency have proved to be a hiccup rather than a setback to the trade engine. Latest data from May suggested that the trade surplus increased after a drop in April, back above the US\$100bn mark, to US\$105.6bn in May (seasonally adjusted), vs. US\$97.7bn in April. Looking across major destinations also paints a picture of relatively resilient growth despite the energy shock, with nominal exports increasing to most parts of the world with the exception of Europe and Latin America, although most of that increase reflected an increase in prices of tech-related products. Stepping back, while China's trade surplus may face some near-term headwinds from renewed opportunistic diversification into gold, rising energy/semiconductor import costs, and higher PPI inflation, the structural story across the green technology chain and broader manufacturing competitiveness seems intact as does the deep currency undervaluation (of more than 20% on our GSDEER & GSFEER metrics). So even as the pace of the move and total returns have flattened out over the past month (Exhibit 3), the past week has marked another year-to-date low in the USD/CNY fix and offshore spot, and we continue to target 6.50 in 12m.

Exhibit 3: Even as the pace of total returns has flattened out over the past month, the past week has marked another year-to-date low in the USD/CNY fix  
![](images/9d3a7c2a100ac09b1fb21a6c55997159c95e22ef8168f545513b2d9ebf91e310.jpg)

<details>
<summary>line chart</summary>

| Month    | Short USD/CNH total return (one-month, rolling) | Short USD/CNH spot return (one-month, rolling) | Average total return since June 2025 |
|----------|--------------------------------------------------|--------------------------------------------------|--------------------------------------|
| Jun-25   | ~0.5                                             | ~0.8                                             | ~0.3                                 |
| Jul-25   | ~0.0                                             | ~0.3                                             | ~0.3                                 |
| Aug-25   | ~-1.0                                            | ~-0.5                                            | ~0.3                                 |
| Sep-25   | ~1.0                                             | ~1.2                                             | ~0.3                                 |
| Oct-25   | ~-0.5                                            | ~-0.2                                            | ~0.3                                 |
| Nov-25   | ~0.5                                             | ~0.7                                             | ~0.3                                 |
| Dec-25   | ~1.0                                             | ~1.1                                             | ~0.3                                 |
| Jan-26   | ~1.2                                             | ~1.3                                             | ~0.3                                 |
| Feb-26   | ~0.8                                             | ~0.9                                             | ~0.3                                 |
| Mar-26   | ~1.1                                             | ~1.2                                             | ~0.3                                 |
| Apr-26   | ~-1.5                                            | ~-1.8                                            | ~0.3                                 |
| May-26   | ~1.0                                             | ~1.1                                             | ~0.3                                 |
| Jun-26   | ~0.5                                             | ~0.7                                             | ~0.3                                 |
</details>

Source: Bloomberg, GS Global Investment Research

GBP: Make-or-breakerfield. Next Thursday's Makerfield by-election is a pivotal moment in Manchester Mayor Andy Burnham's path to a potential Labour party leadership contest, but we see the event risk for Sterling as being fairly narrow. Political and fiscal risk premium in the currency remains light on our measure, despite a Burnham-led government (and the associated risks of potential adjustments to the UK's fiscal stance) now priced in prediction markets as more likely than not by year-end. Shifts in these odds have weighed on GBP in bouts over recent months rather than providing a sustained headwind even when prediction markets moved firmly towards Burnham in recent weeks (Exhibit 4). To see premium expand again and weigh materially on Sterling, we think the onus is now either on an announcement of policy plans that lead markets to question the UK's fiscal trajectory, or for political uncertainty to rise and linger for longer. And even under such a scenario, we expect other, more fundamental factors to continue to dominate price action. The evolution of the energy shock remains key to that. We continue to think the current window of unresolved energy supply risks and limited political premium priced in Sterling offers decent value in GBP downside versus terms of trade winners such as USD or AUD, but in our view these expressions are best suited to more tactical horizons or tail hedges. Sterling should be a top performer on a resolution to the conflict in the Middle East on account of its procyclical and energy importer attributes, and we think a reversal of the terms of trade impact on Sterling should easily outweigh any further bouts of political premium ahead.

Exhibit 4: Modest Sterling reactions to rising odds of a Burnham led government  
![](images/d3a209537728ccf1c6e41f89788d48975741cb311d36645ffb4eed519bc90fec.jpg)

<details>
<summary>line chart</summary>

| Date     | EUR/GBP (Left) | Polymarket Probability of Burham-Led Government by End-2026 (Right) |
|----------|----------------|------------------------------------------------------------------|
| 2-Apr    | 0.872          | 5                                                                |
| 12-Apr   | 0.871          | 5                                                                |
| 22-Apr   | 0.868          | 10                                                               |
| 2-May    | 0.863          | 20                                                               |
| 12-May   | 0.867          | 40                                                               |
| 22-May   | 0.863          | 50                                                               |
| 1-Jun    | 0.868          | 60                                                               |
| 11-Jun   | 0.855          | 70                                                               |
</details>

Source: Bloomberg, Polymarket, GS Global Investment Research

JPY: Policy limits. The BoJ looks set to hike by 25bp at its June meeting, continuing with its very gradual pace of tightening. Governor Ueda's recent speech—combined with the dissents, projections, and statement of the April meeting—essentially previewed the hike, so the bar for a hawkish surprise is high. Though with Ueda not able to deliver the press conference (Deputy Governor Uchida will be filling in), it may be harder to decipher whether any marginal communication shift is intentional or not. But in any case, without a guide towards a faster pace of hikes, markets will remain most focused on the JPY-negative fundamentals of constrained monetary policy, higher-for-longer US yields, US growth outperformance, and domestic fiscal risks. Current balance sheet policy is also set to be reassessed at this meeting, and some have speculated that the Board may consider an increase to JGB purchases to contain long-end yields. But we think that would only add to the downward pressure on the currency (which the MoF wants to avoid), especially since rising fiscal risk premium has been the driver of higher yields rather than supply. For that reason and the fact that bond market functioning has been improving, our economists think the BoJ will stick to its previously decided plan to reduce purchases to a pace of ¥200bn per quarter. Overall, we continue to think that if our and market expectations for domestic monetary policy prove correct (i.e., only gradual tightening), it should have relatively limited impact on the Yen relative to the broader macro backdrop and US outlook, keeping the currency on the back-foot.

NJA FX: Carry re-emerging in India, recommend going short THB/INR. We argued last week that there is a growing case for the INR to be added to diversified carry baskets. Carry levels in the INR have increased since the beginning of the US-Iran War, and they are now higher than other Asia high-yielders (IDR and PHP) and higher than some other popular carry candidates across EM such as ZAR and MXN. While the Rupee is still at fair levels on a trade-weighted basis and rich relative to key

currencies like CNY, it now screens among the more undervalued EM currencies versus the Dollar among the higher carry complex on our GSDEER and GSFEER metrics. The RBI also announced a slew of measures to encourage capital inflows, which alongside increasing prospects of a resolution in the Middle East, have helped to stabilize USD/INR over the past week. And even though the balance of payments is likely to be in better shape given lower energy intensity of the economy, we do not expect significant spot appreciation (since any renewed capital inflows should be absorbed through unwind of the short forward book and reserve rebuild). Still, the Rupee is now a more viable carry candidate with the central bank likely to hike rates a couple of times before year-end. On the other side, we do not expect the Bank of Thailand to raise rates this year. Given Thailand's longer term structural economic challenges, the authorities' efforts to de-link the correlation between gold and THB, and preference for a weaker currency, we think the THB will likely remain a laggard vs the region even if oil prices drop. Taken together, we recommend going short THB/INR (entry 2.91, target 2.70, stop-loss 3.05). The annualized carry for this pair is approximately $4.7\%$ .

CHF: The SNB and me. The Swiss Franc has not performed in its typical role as a geopolitical, inflation, and European cyclical hedge as it did in the 2022 energy shock. Given the lower starting point for inflation, and a stronger starting point for the currency, the SNB has maintained its bias toward countering CHF appreciation. We had argued that a reacceleration in Swiss inflation would suffice to see the SNB revert back to a neutral intervention bias, as was the case in 2022. But, despite headline inflation tracking above the SNB's latest projections, so far the pass-through from higher energy prices has been limited. Nevertheless, we will be focused on the June 18 meeting statement for any incremental shift towards a more neutral currency stance, either on the intervention language or (more passively) by referencing the real exchange rate. We have shown that the SNB tends to take a more hands-off approach to intervention when inflation is in this range, and our economists estimate that the SNB did not intervene much in April, so the “increased” willingness language may be adjusted. Moreover, the inflation differential matters for the real exchange rate, so the increase in EA inflation is also relevant. We think markets may be too complacent after Chair Schlegel’s recent comments echoed the same intervention language, as that is standard practice for SNB communication. However, without a clearer shift in the currency bias—which the SNB may feel is unwarranted given the still-low level of inflation—we see a risk of further CHF underperformance ahead. In a market searching for funders, dovish divergence can quickly weigh on currency performance, as the recent moves in CAD help demonstrate. We therefore revise our EUR/CHF forecasts to 0.91, 0.90 and 0.88 in 3, 6 and 12 months (from 0.89, 0.90 and 0.91 previously). Our new forecasts reflect a more persistent global i

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
