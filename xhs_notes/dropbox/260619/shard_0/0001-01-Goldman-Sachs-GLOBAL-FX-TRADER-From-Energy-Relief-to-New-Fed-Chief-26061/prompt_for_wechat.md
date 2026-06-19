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

# From Energy Relief to New Fed Chief

## Our thoughts on USD, EM Carry, JPY, CHF, AUD & NZD and EGP

USD: Something new and some things we’re used to. This FOMC meeting was very different from the last one, and from what was expected. We think, on net, the more hawkish FOMC stance matters more than the US-Iran MOU for the near-term Dollar outlook because it comes as a bigger surprise (after all, there has always been a baseline that the Conflict would come to a resolution at some point, and markets never priced a significant amount of stress), and because rate differentials have a larger and more consistent correlation with the Dollar than oil prices. So unless the Fed’s more hawkish stance proves fleeting as oil prices move lower, we see this as replacing one positive Dollar factor with another, more powerful one. And in this context we think it is worth noting that, while oil prices were the initial catalyst for FOMC participants to begin their reassessment, strong AI-led US demand has been a major factor behind higher growth, inflation and pricing for the neutral rate since the start of the year. This degree of Fed support is new, but comes in part from factors that we believe have been helping Dollar demand for some time. This can create some indigestion for procyclical carry trades, but typically bear flattening puts most of the pressure on lower yielding currencies. Finally, it is worth noting that the message delivery was very different to what we have come to expect from the FOMC, but from an FX perspective we have seen a number of iterations of global central banks that have offered less transparency and a greater tendency to surprise. It can lead to higher volatility on the day of policy decisions. This could be more disruptive for the Fed given the Dollar’s global role, which is a key reason why the Fed has generally tried to limit hawkish policy surprises even in times when it was providing less policy guidance. If communication about future policy decisions will be more limited on meeting days, it should transfer the volatility to both data releases and other forms of communication like policy speeches. That said, we expect that the less-centralized format of the FOMC will lead to less of a “regime shift” around both speeches and what data will drive policy decisions compared to some leadership transitions at other central banks.

EM Carry: From trade tailwinds to hike headwinds. EM currencies have been on a round-trip over the last week, initially rallying on a conflict resolution but then depreciating following the more hawkish-than-expected FOMC (Exhibit 1). There is some correlation between the relative outperformance and subsequent

## Kamakshya Trivedi

+44(20)7051-4005

kamakshya.trivedi@gs.com

GS International

## Michael Cahill

+44(20)7552-8314

michael.e.cahill@gs.com

GS International

## Danny Suwanapruti

+65-6889-1987

danny.suwanapruti@gs.com

GS (Singapore) Pte

## Teresa Alves

+44(20)7051-7566

teresa.alves@gs.com

GS International

## Karen Reichgott Fishman

+1(212)855-6006

karen.fishman@gs.com

GS & Co. LLC

## Stuart Jenkins

+44(20)7051-4700

stuart.jenkins@gs.com

GS International

## Victor Engel

+44(20)7051-3862

victor.engel@gs.com

GS International

## Lexi Kanter

+1(212)855-9701

alexandra.kanter@gs.com

GS & Co. LLC

underperformance, but notably lower-yielding currencies such as KRW, CZK and MYR have depreciated by more than they had appreciated on the resolution. We think this is consistent with the typical implications of a front-end-led US rates repricing, which is more negative for lower-yielding currencies. In this context, we think carry strategies can continue to deliver positive total returns even as the Fed path reprices further, as long as risk remains supported. However, the choice of funder becomes even more important in this setup: as we have shown before, in an ‘equities up, rates down’ regime, USD-funding typically outperforms, but in an ‘equities up, rates up’ backdrop, low-yielding funders like EUR or JPY help deliver positive spot returns (and higher total returns). Within EM, currencies like CLP and ILS can help neutralise the risk exposure and USD beta of carry baskets without a decline in carry returns. And, looking back, this divergence in high- vs. low-yielding currencies was a key feature of the 2021-2023 hiking cycles. One noteworthy feature of yesterday’s price action was the relative outperformance of MXN, consistent with its broad Dollar beta. We have argued for including the Peso in a diversified carry basket given its sensitivity to US-specific cyclical pricing, and we think this is increasingly a stronger proposition if US relative outperformance remains in focus. The upcoming USMCA discussions are the main risk to this MXN outperformance view, but we have argued that this should be a more important driver for CAD than MXN. Elsewhere in LatAm, we think it makes sense to rotate some BRL length into COP if Colombian local developments remain supportive after the second round this weekend, whereas in Brazil, we expect rising political noise ahead of the October elections to lead to a deterioration of carry-to-vol ratios. And, to the extent that a hawkish COPOM has been an anchor of BRL stability, a more dovish delivery this week raises the risks of less central bank support into a noisier period.

Exhibit 1: EM currencies have been on a round-trip over the last week, initially rallying on a conflict resolution but then depreciating following the more hawkish-than-expected FOMC  
![](images/fe496a61ceb00c7455e0dbb70109317d459e3cff8e44387942e401e7c7d0e465.jpg)

<details>
<summary>bar chart</summary>

Spot returns vs USD
| Currency | June 10 - June 16 (%) | June 16 - June 18 (%) |
| :--- | :--- | :--- |
| COP | 3.6 | -0.5 |
| CLP | 3.05 | -1.7 |
| HUF | 2.7 | -2.4 |
| ZAR | 2.3 | -1.5 |
| ILS | 1.9 | -0.9 |
| BRL | 1.85 | -1.6 |
| PHP | 1.75 | -0.4 |
| IDR | 1.35 | -0.05 |
| MXN | 1.25 | -0.9 |
| THB | 1.05 | -0.6 |
| PLN | 0.9 | -1.8 |
| KRW | 0.8 | -2.0 |
| CZK | 0.75 | -1.5 |
| INR | 0.7 | 0.25 |
| PEN | 0.7 | -0.05 |
| CNH | 0.35 | -0.3 |
| TWD | 0.3 | -0.05 |
| MYR | 0.0 | -1.2 |
</details>

Source: Bloomberg, GS Global Investment Research

JPY: Grinding weaker. The BoJ hiked rates at its June meeting and continued to signal additional hikes, but the pace remains too slow to offset broader JPY-negative fundamentals. Higher odds of more imminent Fed hikes have now added further upward pressure to USD/JPY. The Yen tends to weaken less versus the Dollar than most other currencies in a hawkish policy shock given the offsetting impulses of higher yields and weaker equities. But our GSBEER model suggests that the Yen still outperformed by roughly 15bp what fundamentals would have implied. That said, it underperformed the subsequent day—consistent with the diminishing effect from elevated intervention risk over the past month and likely in part due to the lack of policy response above 160 (Exhibit 2). The potential for additional operations still leaves outright USD/JPY longs less attractive though, despite the broader backdrop arguing for a weaker Yen. For that reason, we have preferred being short JPY against high-carry EM currencies. We continue to see the risks as skewed to the upside in USD/JPY as the incoming US data have remained resilient, the odds of Fed hikes have gone up, and domestic fiscal risks remain. A sharp reversal lower would likely require a rise in recession risk or shift towards a more hawkish BoJ, both of which continue to feel less imminent.

Exhibit 2: As macro fundamentals continue to justify a weaker Yen the impact of intervention risk has diminished  
![](images/c7abd9fd05b31e2ff1ab950d8bb95672fcae2d87a474f0dc2c5f3f195d2d74ea.jpg)

<details>
<summary>line chart</summary>

| Date     | USD/JPY Actual | USD/JPY GSBEER Model Implied |
|----------|----------------|------------------------------|
| 01-Apr   | 0.0            | 0.0                          |
| 08-Apr   | 0.6            | 0.2                          |
| 15-Apr   | 0.3            | -0.2                         |
| 22-Apr   | 0.5            | 0.1                          |
| 29-Apr   | 1.0            | 1.0                          |
| 06-May   | -1.5           | 0.5                          |
| 13-May   | -0.5           | 1.5                          |
| 20-May   | 0.2            | 2.5                          |
| 27-May   | 0.4            | 1.8                          |
| 03-Jun   | 0.8            | 1.6                          |
| 10-Jun   | 1.1            | 1.4                          |
| 17-Jun   | 1.3            | 1.5                          |
</details>

Source: GS FICC and Equities, Bloomberg, GS Global Investment Research

CHF: A tweak too weak. The SNB remained on hold for a fifth consecutive meeting this week, in line with our economists' forecast and consensus expectations. We noted that we would be focused on the meeting statement for any incremental shift towards a more neutral currency stance though it was likely too soon to remove the CHF weaker bias completely given the still-low level of inflation. The SNB did soften its intervention bias slightly, adding "if necessary" to the previous language that it has an increased willingness to intervene to counter CHF appreciation. However, as we had outlined, this marginal change is likely insufficient to provide any tailwind to the Franc. In a backdrop where many other central banks are hiking or considering hikes, a firmly on hold stance puts the SNB on the dovish end of the central bank spectrum and this dovish divergence should weigh on currency performance. In fact, Chair Schlegel noted that interest rate differentials to other major central banks had widened and were exerting downward pressure on the Franc. We agree and think the language change will prove mostly symbolic as it is not enough to shift this dynamic and expect continued CHF underperformance in the near term.

AUD & NZD: New headwinds. The RBA unanimously voted to remain on-hold at the June meeting and maintained a tightening bias in the statement. Focus remained on upside risks to inflation while the recent string of softer activity and labor market data was somewhat discounted. Governor Bullock argued that slower growth should not be alarming and is necessary to lower inflation, but left the timing of any further tightening data-dependent, noting that “if inflation doesn’t respond in the way we expect it to, we might have to do more.” Our economists note that the RBA’s latest projections were calibrated on one additional hike in this cycle, and they maintain their call for a final 25bp hike in August. The deterioration in recent Australian macro data and an RBA nearing the peak of its cycle stand in contrast to New Zealand. There, data has improved, including the recent GDP print which showed an encouraging economic recovery prior to the energy shock and more hikes are priced for the RBNZ this year than for any other G10 central bank. Relative domestic conditions pushing in the same direction as a relaxation in energy prices is key to our view that AUDNZD should trend lower in the more medium term. But AUDUSD has moved more in line with fundamentals recently (Exhibit 3) while NZDUSD looks to have more room for catch up (Exhibit 4), making NZD longs vs the Dollar look more tactically attractive on de-escalation in our view. That said, NZD is typically an underperformer in a hawkish policy shock backdrop that sees equities move lower alongside higher yields, and yesterday’s FOMC meeting introduced a new headwind to any NZD outperformance.

Exhibit 3: AUDUSD has moved more in line with fundamentals recently...  
![](images/c7e852b58df311f1a36a2cd24e890c6cd742305830298b734307f3b6a49e8e2c.jpg)

<details>
<summary>line chart</summary>

| Date    | US Equities | Copper | Credit Spreads | Nominal 2y Rate Differential | Constant | AUD/USD | Fitted |
|---------|-------------|--------|----------------|------------------------------|----------|---------|--------|
| Feb-27  | ~0.5        | ~0.3   | ~0.1           | ~0.2                         | ~0.1     | ~0.0    | ~0.0   |
| Mar-11  | ~0.8        | ~0.6   | ~0.3           | ~0.4                         | ~0.2     | ~-0.5   | ~-0.5  |
| Mar-23  | ~0.2        | ~0.1   | ~-0.5          | ~0.0                         | ~-0.5    | ~-1.5   | ~-1.5  |
| Apr-02  | ~-0.5       | ~-0.8  | ~-1.0          | ~-0.8                        | ~-1.0    | ~-2.5   | ~-2.5  |
| Apr-14  | ~0.5        | ~0.3   | ~0.2           | ~0.4                         | ~0.1     | ~0.8    | ~0.8   |
| Apr-24  | ~1.0        | ~0.8   | ~0.6           | ~0.7                         | ~0.3     | ~1.2    | ~1.2   |
| May-06  | ~1.5        | ~1.2   | ~1.0           | ~1.1                         | ~0.5     | ~1.8    | ~1.8   |
| May-18  | ~1.8        | ~1.5   | ~1.3           | ~1.4                         | ~0.7     | ~2.0    | ~2.0   |
| May-28  | ~2.0        | ~1.8   | ~1.5           | ~1.6                         | ~0.9     | ~2.2    | ~2.2   |
| Jun-09  | ~2.2        | ~2.0   | ~1.7           | ~1.8                         | ~1.1     | ~2.5    | ~2.5   |
</details>

Source: GS FICC and Equities, GS Global Investment Research

Exhibit 4: ...while NZDUSD looks to have more room for catch up  
![](images/3c2acaff938f6897b494f9b6fba9d691f11c921b47d1ceb16f48a68df5562997.jpg)

<details>
<summary>line chart</summary>

| Date    | US Equities | Copper | Credit Spreads | Nominal 2y Rate Differential | Constant | NZD/USD | Fitted |
|---------|-------------|--------|----------------|------------------------------|----------|---------|--------|
| Feb-27  | -0.5        | -0.3   | -0.2           | -0.1                         | -0.4     | -0.6    | -0.7   |
| Mar-11  | 0.2         | 0.1    | 0.3            | 0.2                          | 0.0      | -0.8    | -0.9   |
| Mar-23  | 0.5         | 0.4    | 0.6            | 0.5                          | 0.2      | -1.2    | -1.3   |
| Apr-02  | 0.8         | 0.7    | 0.9            | 0.8                          | 0.4      | -1.5    | -1.6   |
| Apr-14  | 1.2         | 1.1    | 1.3            | 1.2                          | 0.6      | -1.8    | -1.9   |
| Apr-24  | 1.5         | 1.4    | 1.6            | 1.5                          | 0.8      | -2.0    | -2.1   |
| May-06  | 1.8         | 1.7    | 1.9            | 1.8                          | 1.0      | -2.2    | -2.3   |
| May-18  | 2.0         | 1.9    | 2.1            | 2.0                          | 1.2      | -2.4    | -2.5   |
| May-28  | 2.2         | 2.1    | 2.3            | 2.2                          | 1.4      | -2.6    | -2.7   |
| Jun-09  | 2.5         | 2.4    | 2.6            | 2.5                          | 1.6      | -2.8    | -2.9   |
</details>

Source: GS FICC and Equities, GS Global Investment Research

■ EGP: More upside, but more gradually from here. We stepped back into a long Egyptian Pound (EGP) view after the ceasefire announcement in April given limited retracement and still solid fundamentals for a carry trade. In anticipation of an Iran-US deal earlier this week, EGP had partly retraced its war-related weakening, falling from \~52 to \~50 against the Dollar, i.e. more than 3%, in two sessions, albeit moving back a touch post the hawkish Fed. We remain constructive on EGP in the medium term, and reflecting this, we have introduced USD/EGP forecasts for a gradual appreciation, at 49/48/46 in 3/6/12 months (Exhibit 5). We see three reasons justifying further appreciation from here. First, even with the recent appreciation, EGP has only partly retraced its weakening since the war began, which was one of the largest on a volatility-adjusted basis in the EM and Frontier FX space. Second, despite the recent strengthening, EGP is still significantly undervalued according to our GSDEER and REER metrics. And third, in a good, but not great, macro backdrop for EM carry, Egypt's fundamentals and carry levels justify further increases in foreign positioning in local markets, supporting spot returns. The major risks to our view stem from a sustained hawkish pivot from the Fed and renewed focus on deep-tail growth and geopolitical risks. But we think the likelihood of a more front-footed rate hiking response to higher inflation and the resilience of external fundamentals (Exhibit 6) through the shock can limit spot volatility in such a scenario. Further, a high level of carry, particularly in local debt instruments, can amplify spot returns in the current benign environment and support total returns in a ‘muddle through’ scenario in which spot returns remain contained but tail-risk probabilities compress further, and we have extended the total return target of our short USD/EGP trade recommendation.

Exhibit 5: We forecast a gradual appreciation in EGP against the Dollar, and therefore see it outperforming forwards over the medium term  
![](images/9387ad4966e00ba01ab410790bdaecae6968a95bbc5f4ad0ac47acc5c1e55d08.jpg)

<details>
<summary>line chart</summary>

| Date       | Official USD/EGP | ADR-implied USD/EGP | NDF-implied path | GS forecasts |
| ---------- | ---------------- | ------------------- | ---------------- | ------------ |
| 28 Feb 2026| -                | -                   | -                | 48           |
| Jan-27     | -                | -                   | -                | 48           |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 6: Key measures of Egypt's external fundamentals have remained strong despite the Iran war  
![](images/29c6c444ac8b9ebc4ead6ea4ccc84f6bdddc9950a1ac382081a63b81e46b1d69.jpg)

<details>
<summary>line chart</summary>

| Date       | Worker remittances | Banking system NFAs | Net international reserves (RHS) | Suez Canal receipts (RHS) |
| ---------- | ------------------ | ------------------- | --------------------------------- | ------------------------- |
| Jun-24     | 100                | 100                 | 100                               | 100                       |
| Dec-24     | 120                | 130                 | 110                               | 90                        |
| Jun-25     | 140                | 150                 | 120                               | 110                       |
| Dec-25     | 160                | 250                 | 170                               | 130                       |
| May 2024   | 180                | 260                 | 170   

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
