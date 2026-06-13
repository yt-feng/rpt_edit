你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

7. Indonesia - BI's larger than expected policy rate hikes and FX measures help to stem IDR depreciation. The IDR has underperformed the Asian FX market this year. To address the currency weakness, Bank Indonesia (BI) hiked rate by 50bps in May and then again by 25bp off-cycle hike in June, whilst announcing some additional measures to encourage FX inflows. BI will raise yields on SRBIs across the 6-, 9-, and 12-month tenors and will reduce the hedging swap rate for foreign investors by $10\%$ , a new tool. The policy action provides some relief for the currency, but does not solve other domestic concerns. First, the government plans to centralize natural resource exports and retain export proceeds in state banks, and business groups are seeking clarity on this policy. While aimed at improving tax revenue and preventing exports under-invoicing, investors are worried that the added bureaucracy can delay exports. Second, Indonesia's parliament passed a law to expand BI's mandate, adding a more explicit pro-growth objective to BI's existing mandate on price and exchange rate stability, leading to investor concerns around the inflation targeting framework. Third, we expect MSCI to provide updated guidance on its treatment of Indonesian equities, including its EM status, by June 23. The above pressures add to the already challenging set of macro-objectives including the President's pro-growth preference, maintaining fuel subsidies, free meal program (1.1% of GDP) and keeping within the 3% fiscal deficit cap. Given these domestic concerns, we remain bearish on the IDR and expect it to underperform NJA FX peer

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
