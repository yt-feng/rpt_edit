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
EM ASIA FX/RATES VIEWS

# Asian central banks stepping up response to stem FX weakness

1. Asian central banks step up with hikes and FX policy measures to contain inflation and FX weakness. Asian FX has weakened materially since the start of the Middle East conflict, with all regional currencies except the CNY depreciating against the USD, and USD/KRW, USD/IDR, USD/PHP and USD/INR have all broken prior highs. Given policymakers' and the market's early assumption that the shock would be short-lived, the policymakers' first-order response was to intervene, which is reflected in the broad drawdown in FX reserves. However, as the conflict has entered its fourth month, policy responses have since broadened across Asia. The BSP raised the policy rate by 25bp to $4.50\%$ in April, citing concerns over inflation. BI reiterated its triple intervention policy in March, raised the term structure of interest rates in April, and ultimately hiked by 50bp in May and 25bp in an off-cycle meeting in June. BI also announced a slew of measures aimed at bolstering inflows. The RBI has so far kept policy rates unchanged, but also announced measures to attract inflows in line with our economists' expectations prior to the June meeting. In Korea, where KRW weakness appears more closely tied to portfolio flows, the authorities have leaned more heavily on capital-flow management measures (i.e., encouraging National Pension Service hedging), even as the BoK kept rates on hold while shifting to a more hawkish tone. We think these measures have been somewhat effective, as they put a brake on the slide in Asian FX.

Exhibit 1: FX reserves have dropped in most Asian economies since February  
![](images/7c54cee06b55ec3eb06b56dc0c2ae36f6c3ba7d06b4b96afc99c98703eddc63c.jpg)

<details>
<summary>bar chart</summary>

| Currency | March (%) | April (%) | May (%) |
| :--- | :--- | :--- | :--- |
| PHP | -4.5 | -7.0 | -7.5 |
| INR | -3.8 | -3.2 | -4.8 |
| IDR | -1.8 | -3.0 | -4.0 |
| THB | -3.5 | -0.5 | -0.2 |
| KRW | -0.8 | 0.1 | -0.1 |
| TWD | -1.5 | -0.2 | 0.0 |
| CNY | -2.8 | -0.3 | 0.4 |
| HKD | -1.9 | 0.6 | 1.7 |
| MYR | -1.5 | 1.1 | 2.0 |
| SGD | 0.9 | 2.8 | 3.5 |
2026 gross FX reserve changes since February
</details>

Source: Bloomberg, GS Global Investment Research

2. Policy action helps to stabilize Asian FX, but significant appreciation vs. USD unlikely without resolution of energy shock. Unless there is a clear resolution to the Middle East conflict and oil prices drop significantly, we note that the current

Danny Suwanapruti

+65-6889-1987

danny.suwanapruti@gs.com

GS (Singapore) Pte

Xinquan Chen

+852-2978-2418

xinquan.chen@gs.com

GS (Asia) L.L.C.

Santanu Sengupta

+91(22)6616-9042

santanu.sengupta@gs.com

GS India SPL

Irene Choi

+82(2)3788-1722 | irene.choi@gs.com

GS (Asia) L.L.C., Seoul Branch

Chris Poh

+65-6889-3454 | chris.poh@gs.com

GS (Singapore) Pte

Arjun Varma

+91(22)6616-9043

arjun.varma@gs.com

GS India SPL

Andrew Tilton

+852-2978-1802

andrew.tilton@gs.com

GS (Asia) L.L.C.

market narrative on the broad USD is a supportive one. The energy shock is less adverse to the US economy compared to Europe and Asia. The AI-related investment boom has fueled the US equity market rally. Market Fed rate expectations have turned more hawkish, and our US team has pushed back their Fed cut expectations to 2027, while lifting their US 10Y yield forecasts to $4.4\%$ (from $4.1\%$ ). These macro variables should keep USD/Asia broadly supported, at least until there is more sustained positive news on the war, which could reverse the terms-of-trade outlook for Asia if oil prices drop. In terms of relative performance within EM Asia, we think the RBI's FX measures were meaningful, and given their war chest of reserves, we expect the INR to outperform other high-yield Asian currencies. BI's measures have helped to stabilize the IDR's slide, but a rising domestic risk premium (see below) should curb IDR gains. The PHP should also stay on the defensive (given its reliance on energy imports), but could be one of the region's outperformers if there is a resolution to the war. Among the low-yield currencies, the CNY is on a clear appreciation path, while tech-related currencies (TWD, MYR and KRW) should outperform, while THB underperforms.

3. China - Policy anchor behind the stronger CNY and lower rates. April's activity data came in weaker than expected, which has raised questions whether the PBoC would shift to a more accommodative stance, but our economists think the threshold for broad easing is high. Growth remains bifurcated with exports still supporting headline growth while domestic demand remains soft. Oil-led reflation complicates the case for broad monetary easing. Instead, we think policy support is going to come via fiscal or low-profile easing (such as maintaining ample liquidity). The CNY appreciation trend has persisted throughout the Middle East conflict, despite the broad USD strengthening versus all other Asian currencies. In our view, the PBoC appears comfortable with orderly gradual CNY appreciation against the USD, with a pace of around $4\%$ annualized likely fast enough to offset carry costs for foreign investors, but slow enough to keep the drag on exports competitive and inflation limited. Gradual currency appreciation is also in sync with policymakers pursuit of RMB internationalization, in our view. We acknowledge that the appreciation expectations have become more one-sided, raising exporter's FX conversion ratios. We estimate that exporters converted USD 150bn more FX proceeds than normal since last December (versus our earlier estimate that excess corporate USD hoarding reached a peak of around USD 500bn mid-2025). Going forward, the combination of ongoing export outperformance, significant CNY undervaluation and PBoC's policy preference, we think the CNY will continue on its gradual appreciation path towards 6.70 in 6M and 6.50 in 12M.

Exhibit 2: CNH continued to strengthen vs. USD despite rangebound DXY  
![](images/03d74aaa87063a6d5937efeec92e1515415793e0e0896b07651f498543b42034.jpg)

<details>
<summary>line chart</summary>

| Date   | USDCNH | DXY (right axis) |
|--------|--------|------------------|
| Jan-24 | 7.1    | 102              |
| May-24 | 7.3    | 104              |
| Sep-24 | 7.0    | 106              |
| Jan-25 | 7.4    | 108              |
| May-25 | 7.3    | 106              |
| Sep-25 | 7.1    | 104              |
| Jan-26 | 6.9    | 102              |
| May-26 | 6.8    | 100              |
</details>

DXY: US Dollar Index, which measures the value of the US Dollar vs. a basket of currencies.

Exhibit 3: FX conversion ratio for goods trade balance has generally been rising  
![](images/10903a52c0f809820110a38a822388f05d1e871d12d4e53204ee741b9d137c2e.jpg)

<details>
<summary>line chart</summary>

| Year | FX conversion ratio related to goods trade balance (the ratio of "FX inflows related to goods trade" to "goods trade balance") |
|------|----------------------------------------------------------------------------------|
| 2018 | 105                                                                              |
| 2023 | 15                                                                               |
| 2026 | 56                                                                               |
</details>

The line shows a six-month moving average of FX conversion ratio.  
Source: CEIC, GS Global Investment Research

Source: Bloomberg

## 4. South Korea - AI-driven current account surplus being offset by equity outflows.

The AI-driven export boom has been very supportive for Korean exports, fiscal revenues and growth this year. The BoK kept policy rates unchanged in May, but turned more hawkish. The median dot plot is now projecting two 25 hikes over the next six months, versus none in February. The BoK raised its 2026 real GDP forecast by 0.6pp to $2.6\%$ (vs. GS and Bloomberg consensus: $2.5\%$ ), while raising their headline inflation forecast by 0.5pp to $2.7\%$ . Our economists expect two 25bps hikes (most likely in July and October) versus the market's pricing of six hikes over the next 12-months. We are more dovish because the driver of growth is very concentrated in semi-conductors and not broad-based, which matters for the magnitude of tightening, in our view. Despite the surge in exports and $90\%$ rally in the KOSPI year-to-date, the KRW has counter-intuitively underperformed Asian FX. Last year, heavy portfolio outflows by the National Pension Service (NPS) and retail investors buying overseas assets led to KRW weakness. This year, foreign investors have net sold USD 80bn of Korean equities year-to-date. Our equity strategists note that the recent KOSPI rally has been led by two large semiconductor companies, which pushed their index weight above diversification thresholds, resulting in foreign equity selling, despite higher stocks prices. Our equity strategists believe that equity outflows could ease if the KOSPI rally broadens out beyond just two companies, which would reduce the selling related to concentration risk, while attracting inflows into the broader market. Fundamentally, we are constructive on the KRW via the current account channel, but believe equity outflows would need to abate before the KRW can outperform NJA peers.

Exhibit 4: Net foreign outflows from the KOSPI have reached approximately US\$80bn, largely driven by the two largest semiconductor stocks.  
![](images/2cf3d4b2fad63e5a345e4cb54afb3a430db47182a18dafb5e5bcb52f73ec4a8d.jpg)

<details>
<summary>line chart</summary>

| Date    | KOSPI flows (USD bn) | Samsung and SK Hynix flows (USD bn) |
|---------|----------------------|--------------------------------------|
| Dec-24  | ~0                   | ~0                                   |
| Mar-25  | ~-10                 | ~-5                                  |
| Jun-25  | ~-15                 | ~-10                                 |
| Sep-25  | ~5                   | ~5                                   |
| Dec-25  | ~0                   | ~0                                   |
| Mar-26  | ~-40                 | ~-30                                 |
| Jun-26  | ~-90                 | ~-70                                 |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 5: The rally in two semiconductor stocks pushed their index weights above diversification thresholds under the Investment Company Act of 1940  
![](images/f007d946f8ba6e1b76d05e5ed2e37f3ba24f5300f1766a40d60f07ae614d050e.jpg)

<details>
<summary>line chart</summary>

| Year | SEC weight | Hynix weight |
|------|------------|--------------|
| 06   | 23         | 2            |
| 08   | 13         | 1            |
| 10   | 18         | 2            |
| 12   | 24         | 3            |
| 14   | 27         | 4            |
| 16   | 25         | 5            |
| 18   | 28         | 6            |
| 20   | 33         | 7            |
| 22   | 30         | 8            |
| 24   | 25         | 10           |
| 26   | 35         | 29           |
</details>

Source: Bloomberg, GS Global Investment Research

## 5. Taiwan - Stellar exports drive growth and TWD's relative outperformance.

Taiwan's exports have been growing at a pace of around 40-70% yoy for most of this year. Most recently, May exports rose 51.7% yoy (vs. consensus of 41.2%). Q1 GDP growth rose to 13.7% yoy (well above consensus of 11.3%), reaching the strongest figure since Q2 1987. Our economists have revised up their 2026 current account forecast to 25% of GDP, versus what was a record 20% in 2025, and revised up their 2026 GDP forecast to 10.3% (from 7.0% previously), which would be amongst the highest growth rate since the 1980s. Given the strong growth and rising inflation (GSe: 2.0% by Q2-2026) from 1.2% in Q1, our economists expect the CBC to hike rates twice by 12.5bp in June (out of consensus call) and in Q4, to reach a terminal rate of 2.25% (from 2.0% currently). The TWD has outperformed Asian FX since the start of the Middle East conflict. Taiwan's semi-conductor exports have help to offset the impact of higher oil prices on their terms of trade. Unlike South Korea (which has seen foreign equity outflows all year), foreign equity flows have been more mixed in Taiwan (-USD 14bn year-to-date, but +USD 5bn quarter-to-date). With portfolio flows mixed, the very strong current account surplus is helping to bolster the TWD's performance in a bullish USD environment. Going forward, we expect the TWD to continue outperforming Asian FX, although the pace should be gradual, reflecting the CBC's preference for relative stability.

## 6. India - FX regulations help to stabilize the INR; we recommend going short

THB/INR. Despite the sharp rise in oil prices, India's growth has surprised to the upside. Q1 GDP growth rose 7.8% yoy (versus 8.0% in Q4-25), which was attributed to strong investment. The RBI kept policy rates unchanged in June and retained a “neutral” stance. We expect two 25bps hikes in 2026 (likely in October and December). If inflation accelerates faster than we expect, the risk is that the RBI brings forward the rate hike to August. The RBI also announced a slew of FX measures to encourage capital inflows. These include exemption of tax on capital gains or interest income for foreign investments in government securities, foreign investor access extended to securities further out to ultra-long-end maturities, and exemptions for banks raising foreign currency bonds and deposits. We think the FX measures are meaningful enough to stabilize the USD/INR and like it as a carry play. Carry levels in the INR have increased since the beginning of the US-Iran War, and they are now higher than other Asia high-yielders (IDR and PHP). While the Rupee is still at fair levels on a trade-weighted

basis and rich relative to key currencies like CNY, it now screens among the more undervalued EM currencies versus the Dollar among the higher carry complex on our GSDEER and GSFEER metrics. As such, we recommend going short THB/INR (entry 2.91, target 2.70, stop-loss 3.05. The annualized carry for this pair is approximately $4.7\%$ .

7. Indonesia - BI's larger than expected policy rate hikes and FX measures help to stem IDR depreciation. The IDR has underperformed the Asian FX market this year. To address the currency weakness, Bank Indonesia (BI) hiked rate by 50bps in May and then again by 25bp off-cycle hike in June, whilst announcing some additional measures to encourage FX inflows. BI will raise yields on SRBIs across the 6-, 9-, and 12-month tenors and will reduce the hedging swap rate for foreign investors by $10\%$ , a new tool. The policy action provides some relief for the currency, but does not solve other domestic concerns. First, the government plans to centralize natural resource exports and retain export proceeds in state banks, and business groups are seeking clarity on this policy. While aimed at improving tax revenue and preventing exports under-invoicing, investors are worried that the added bureaucracy can delay exports. Second, Indonesia's parliament passed a law to expand BI's mandate, adding a more explicit pro-growth objective to BI's existing mandate on price and exchange rate stability, leading to investor concerns around the inflation targeting framework. Third, we expect MSCI to provide updated guidance on its treatment of Indonesian equities, including its EM status, by June 23. The above pressures add to the already challenging set of macro-objectives including the President's pro-growth preference, maintaining fuel subsidies, free meal program (1.1% of GDP) and keeping within the 3% fiscal deficit cap. Given these domestic concerns, we remain bearish on the IDR and expect it to underperform NJA FX peers.

Exhibit 6: BI has been raising SRBI yields in an attempt to attract inflows  
![](images/9d498e956fa57af39fc48859b45fbd2e32372e1a3647406dffb562e831472454.jpg)

<details>
<summary>line chart</summary>

| Date   | SRBI yields | BI Policy rate |
|--------|-------------|----------------|
| Jan-24 | 6.9         | 6.0            |
| Jul-24 | 7.5         | 6.0            |
| Jan-25 | 7.3         | 5.8            |
| Jul-25 | 6.0         | 5.0            |
| Jan-26 | 4.8         | 4.8            |
| Jul-26 | 7.7         | 5.5            |
</details>

Source: Bloomberg, GS Global Investment Research

8. Philippines – BSP likely to remain vigilant on inflation and maintain hawkish bias. The inflation pass-through has been rapid, as fuel prices are largely market determined, with April and May CPI printing at 7.2% yoy and 6.8% yoy, respectively, well above the BSP’s target of 3%. During our recent visit to Manila, policymakers shared that based on their 2022 experience, second round effects on inflation tends to peak two quarters after the initial shock. Given their vigilance, the BSP was the first regional central bank to hike rates by 25bps to 4.50% in April, and we expect four more consecutive 25bp hikes to a terminal rate of 5.50%. Economic growth has been weak since H2-2025, partly

reflecting disruptions from the flood-control corruption scandal, which led to a slowdown in public investment. Real GDP growth printed a soft 2.8% yoy in Q1. Policymakers expect investment to recover in H2-2026, although we (and local investors we met in the Philippines) remain more cautious. Our observation of anti-corruption measures in other economies suggests that the recovery in investments usually takes time. Fiscal consolidation remains a priority, making broad-based fiscal stimulus unlikely. The PHP has underperformed NJA FX this year, as the economy is amongst the most exposed to the energy shock. If oil prices stay elevated (USD 90-100/bbl), then we expect the PHP to stay under pressure. However, if there is resolution in the Middle East and oil prices fall, then we think the PHP local markets could be one of the region's outperformers, as the terms of trade should improve more for the Philippines versus other markets.

Exhibit 7: Inflation pass through in the Philippines has been swift, prompting BSP to be hawkish  
![](images/cbe0362491e9a1581c20722af1ea47d2153fdde1b0741b20dac350f9a1a3e36b.jpg)

<details>
<summary>line chart</summary>

| Date   | Headline CPI | Core CPI |
|--------|--------------|----------|
| Jan-12 | 4.0          | 3.5      |
| Jan-14 | 4.5          | 3.0      |
| Jan-16 | -0.5         | 1.0      |
| Jan-18 | 7.0          | 4.5      |
| Jan-20 | 0.5          | 3.0      |
| Jan-22 | 8.5      

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
