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
ASIA IN FOCUS

# India: A More Favourable Balance of Payments Outlook

The INR's recent weakness appears larger than what balance of payments (BoP) fundamentals would suggest. Despite softer capital inflows, India posted a \$7.2bn BoP surplus in Q1 CY26, supported by stronger remittances, robust services exports and low oil imports. In our view, this reflects precautionary dollar demand amid heightened Middle-East uncertainty. Going forward, higher oil prices will likely widen India's current account deficit, but the deterioration is likely to be less severe than in past energy shock episodes.

India's oil intensity has declined steadily since 1990s, reflecting improved energy efficiency, rising transport electrification, and a shift toward less energy-intensive growth. Post-pandemic, oil import volumes also appear more price-sensitive, with volumes now declining more when oil rises above \$80/bbl. As a result, higher oil prices may not translate into a proportionate increase in India's oil import bill. Separately, policymakers have often used import duties and administrative curbs to contain gold imports during episodes of external stress. Historically, duty hikes have begun to weigh on gold import volumes with a 1-2 month lag, and we expect the same in this cycle.

## A BoP surplus year, after two consecutive years of deficit: The RBI's

comprehensive set of measures to incentivize dollar inflows, including concessional forex swap rates for banks and quasi-sovereigns to raise USD funding, together with exemptions on interest and capital gains tax on G-Sec for FPIs, should underpin capital inflow revival and support the INR. Meanwhile, incorporating our lower oil and gold import assumptions, and better-than-expected Q1 data we lower our current account deficit forecast to 1.3% of GDP in CY26 and 1.7% of GDP in FY27 from 2.0% of GDP and 2.1% of GDP earlier. With our estimate of \$60bn of additional capital inflows from the RBI's measures, we expect India to record a balance of payments surplus of around 0.6% of GDP in CY26 FY27 each.

## Depreciation pressure on the INR should ease, but we don't see material

appreciation: An improved balance of payments outlook should help lower depreciation pressures on the INR. While the currency appears broadly fairly valued on a trade-weighted basis, we expect any renewed dollar inflows to be largely absorbed by the RBI through reserve accumulation and unwind the short forward book, limiting the scope for significant appreciation.

## Arjun Varma

+91(22)6616-9043

arjun.varma@gs.com

GS India SPL

## Santanu Sengupta

+91(22)6616-9042

santanu.sengupta@gs.com

GS India SPL

## Andrew Tilton

+852-2978-1802

andrew.tilton@gs.com

GS (Asia) L.L.C.

## Reassessing the balance of payments outlook

Recently, the INR has depreciated by more than India's external fundamentals would imply. Despite the energy shock and concerns around weaker capital inflows, India's balance of payments (BoP) posted a surplus of around \$7.2bn in Q1 CY26. The current account recorded a surplus of \$7bn, supported by record-high remittance inflows, a robust services trade surplus and a lower-than-expected oil import bill. In our view, the apparent divergence between the INR's weak performance and the strong underlying BoP position suggests that the recent pressure on the currency was driven more by precautionary and speculative demand for dollars amid heightened geopolitical uncertainty than by a deterioration in India's fundamental external position.

In this report, we reassess India's external balances. We examine how oil volumes may respond to higher prices, using evidence from oil intensity, historical demand elasticity, and fuel-price pass-through to domestic consumption. We further assess if gold imports could adjust lower, comparing recent import duty hikes to prior policy interventions. Finally, we evaluate the RBI's recent measures to incentivize dollar inflows, and update our overall balance of payments outlook.

## Lower oil intensity may help mitigate the impact of higher oil prices

India's oil intensity has declined steadily over the past three decades, reflecting improvements in energy efficiency, greater electrification of transportation and a gradual shift towards less energy-intensive sources of growth (Exhibit 1). As a result, increase in oil prices is likely to have a smaller impact on economic activity than in previous oil shock episodes. Despite the Middle-East driven energy shock, and lower oil (volume) imports, economic activity was resilient in Q1, partly due to fiscal and quasi-fiscal absorption of higher oil prices, and partly due to inventory drawdown.

Exhibit 1: India's oil intensity has declined over the last three decades  
![](images/a199daff55a4aa6bbad107847acd4bc524f06e38c98f1de36dd7219767df8419.jpg)

<details>
<summary>line chart</summary>

Oil consumption intensity (Tonnes/INR mn)
| Year | Oil consumption intensity (Tonnes/INR mn) |
|---|---|
| 1991 | 10.0 |
| 1993 | 8.5 |
| 1995 | 7.0 |
| 1997 | 5.5 |
| 1999 | 4.0 |
| 2001 | 5.0 |
| 2003 | 4.5 |
| 2005 | 4.0 |
| 2007 | 3.5 |
| 2009 | 3.0 |
| 2011 | 2.5 |
| 2013 | 2.0 |
| 2015 | 1.8 |
| 2017 | 1.6 |
| 2019 | 1.4 |
| 2021 | 1.2 |
| 2023 | 1.0 |
| 2025 | 0.8 |
</details>

Source: CEIC, GS Global Investment Research

To assess the implications of a lower oil consumption intensity for the current account, we focus on net oil imports, in volume terms (crude oil imports plus petroleum product imports less petroleum product exports), which provides a better measure of India's underlying oil import requirement than crude oil imports alone. This is important, as a part of India's crude oil imports are processed and exported as refined petroleum products.

The relationship between Brent crude oil price and net crude oil import volumes appears non-linear: volume imports generally rose as prices increased from low levels. Beyond a threshold (around \$75-\$80/bbl), however, price increases were associated with lower import volumes $^{1}$ .

Including post-pandemic observations (excluding 2020 and 2021), the responsiveness of net crude import volume to changes in oil prices has increased across most price levels relative to the pre-pandemic period. The price threshold at which import volumes begin to decline has also moved higher to about \$75-80/bbl (from around \$60/bbl pre-pandemic), likely reflecting lower oil intensity and a greater economic capacity to absorb higher oil prices (Exhibit 2).

Exhibit 2: India's net crude oil import volumes have become more elastic (vs. the pre-pandemic period)  
![](images/be656524a756478860b1ccc732d4584cee718944ebf24d5a7435e53029e217f8.jpg)

<details>
<summary>line chart</summary>

| Brent crude oil price ($/bbl) | Pre-pandemic (2011-2019) | Full sample (2011-2025) |
|---|---|---|
| 50 | 0.0 | 0.4 |
| 60 | -0.1 | 0.3 |
| 70 | -0.3 | 0.1 |
| 80 | -0.5 | -0.3 |
| 90 | -0.7 | -0.6 |
| 100 | -1.0 | -1.1 |
| 110 | -1.5 | -2.0 |
| 120 | -2.5 | -3.3 |
</details>

Source: CEIC, GS Global Investment Research

One channel through which higher oil prices can reduce import volumes is weaker domestic fuel demand, given the recent fuel price hikes. As shown in Exhibit 3, higher fuel prices have weighed on fuel consumption demand in the past. Depending on the duration of the energy shock, sustained higher oil prices may necessitate further fuel price hikes, weighing on consumption and, in turn, net oil import volumes. Based on our estimates, every $10\%$ increase in fuel prices, lowers petrol and diesel consumption growth by around $3\%$ on an average over the next 12 months.

Exhibit 3: Domestic fuel price hikes likely to weigh on fuel consumption demand going forward  
![](images/68a27edd5cf5a5537e98e6f4af1558771a2405bab8208372c605db36fed11e29.jpg)

<details>
<summary>line chart</summary>

| Year | Petrol+Diesel consumption | Fuel price (weighted average) |
|------|---------------------------|-------------------------------|
| 13   | ~5                        | ~15                           |
| 14   | ~0                        | ~10                           |
| 15   | ~5                        | ~-20                          |
| 16   | ~10                       | ~-10                          |
| 17   | ~5                        | ~30                           |
| 18   | ~5                        | ~25                           |
| 19   | ~5                        | ~-10                          |
| 20   | ~-10                      | ~-10                          |
| 21   | ~-15                      | ~30                           |
| 22   | ~10                       | ~-5                           |
| 23   | ~10                       | ~-5                           |
| 24   | ~5                        | ~0                            |
| 25   | ~5                        | ~0                            |
| 26   | ~5                        | ~5                            |
</details>

Source: CEIC, GS Global Investment Research

While higher oil prices mechanically lift India's oil import bill, but as discussed above import volumes are likely to respond more to a given level of oil price, given the lower oil consumption intensity. With Brent crude oil prices averaging around \$90/bbl in CY26 (vs. about \$70/bbl pre-conflict), our estimates imply a 10% price rise is associated with around a 6% decline in net import volumes. Alongside lower oil intensity and fuel-price pass-through weighing on demand, softer volumes should partly offset the trade-balance hit from higher prices.

## Gold import duties likely to curb gold imports

Historically, gold imports have remained elevated during periods of external stress, reflecting gold's role as a store of value during episodes of financial market volatility and geopolitical tensions. Gold imports averaged $1\%$ to $3\%$ of GDP during previous stress episodes. Gold imports are tracking at around $2.2\%$ of GDP in 2026 Q1, levels comparable to those observed during some of India's previous external stress episodes.

Given the share of gold imports in India's trade deficit, policymakers have historically relied on import duties to curb imports (See Appendix). As shown in Exhibit 4, higher import duties were typically followed by a decline in gold import volumes. The impact typically started to materialize 1-2 months after the import duty hike, with the full effect unfolding over 5-6 months (\~40-50% decline). Other policy and regulatory measures also weighed on gold imports. For instance, gold imports declined sharply in 2016-17 following demonetization, which disrupted cash-intensive jewellery purchases and temporarily weakened retail demand.

Exhibit 4: Gold import volumes typically weaken within 1-2 months of duty hikes, with the full impact materializing over 5-6 months  
![](images/ab23a5eaffd9122aeb62cd7b44ec3bb9827d263a30b252bbfe6e9d951055f93a.jpg)

<details>
<summary>line chart</summary>

| Year | Gold imports: Volume (12-month moving total) | Gold import duty (RHS) |
|------|-----------------------------------------------|------------------------|
| 12   | ~1100                                         | ~2                     |
| 13   | ~1200                                         | ~4                     |
| 14   | ~500                                          | ~8                     |
| 15   | ~1000                                         | ~8                     |
| 16   | ~1050                                         | ~8                     |
| 17   | ~900                                          | ~6                     |
| 18   | ~1000                                         | ~8                     |
| 19   | ~1050                                         | ~8                     |
| 20   | ~800                                          | ~8                     |
| 21   | ~400                                          | ~8                     |
| 22   | ~1050                                         | ~8                     |
| 23   | ~800                                          | ~14                    |
| 24   | ~750                                          | ~6                     |
| 25   | ~700                                          | ~6                     |
| 26   | ~750                                          | ~6                     |
</details>

Source: CEIC, GS Global Investment Research

Recent media reports suggest that the May 2026 import duty hike has started to weigh on gold imports and retail demand. However, elevated geopolitical uncertainty and record-high gold prices suggest that any adjustment in gold imports may prove temporary, particularly as jewellery demand typically strengthens during the wedding season (November-February). Moreover, while higher duties may help moderate official gold imports in the near term, they could potentially increase unofficial gold imports.

## Reassessing India's current account balance

India posted a current account surplus of \$7.0bn in Q1 CY26 (vs. our expectation of a deficit), mainly driven by a) lower-than-expected oil import bill, b) higher remittance receipts, and c) higher services trade surplus.

First, the oil import bill declined significantly in March — despite higher Brent crude oil prices — reflecting lower oil import volumes (-15% yoy) amidst supply disruptions from the Strait of Hormuz due to the Middle-East conflict. Second, remittance receipts rose to a record high of \$41bn in Q1 (4% of GDP), likely reflecting precautionary transfers by non-resident Indians due to the Middle-East conflict, contrary to our expectations of a slowdown amidst the Middle-East conflict. Third, services exports remained strong, led by robust software and business services exports (Exhibit 5).

Exhibit 5: Current account balance came in at a surplus (vs. our expectation of a deficit) mainly on lower oil imports and higher remittance receipts  
![](images/5236c622bfc597c1b64131d9396b21e097a65398a20fbb98655854eeb5033f5b.jpg)

<details>
<summary>bar chart</summary>

India Q1 CY26 current account deficit change (GSe vs. actual)
| Category | Value (%) |
|---|---|
| GSe | -1.2 |
| Lower oil imports | 0.9 |
| Higher remittances | 0.8 |
| Higher services trade surplus | 0.2 |
| Actual | 0.7 |
</details>

Source: RBI, GS Global Investment Research

Given the better-than-expected current account balance, we reassess our outlook on the current account deficit for CY26, incorporating the Q1 print and the implications of the above analysis into our forecasts.

Oil: First, incorporating the lower-than-expected oil import bill in Q1, and a softer outlook for oil demand, we revise down our CY26 oil import forecast to \$220bn (5.6% of GDP) (vs. \$244bn earlier, 6.3% of GDP). Our revised forecast assumes around 2% lower oil import volume growth, reflecting increased sensitivity of oil demand to higher prices, the IEA's estimate of weaker oil demand growth in India since the onset of the conflict, and the recent moderation in petrol and diesel consumption following domestic fuel price hikes.  
Gold: Second, historically, gold import duty hikes have been followed by a decline in import volumes, with a 1-2 month lag. Given the recent increase in import duties and the early signs of moderation in imports, we revise down our CY26 gold import forecast to \$56bn (1.4% of GDP), from \$64bn (1.6% of GDP) earlier.  
■ Remittances: Third, we nudge up our CY26 remittance forecast to US\$136bn (vs. \$134bn earlier), reflecting the stronger-than-expected inflows in Q1. While precautionary transfers amid heightened uncertainty in the Gulf likely boosted remittance inflows in the first quarter, we assume a moderation in inflows over Q2-Q4, consistent with slower growth across GCC economies.

Taken together, we revise our current account deficit forecast for CY26 to \$46bn (1.3% of GDP), vs. \$78bn (2.0% of GDP earlier), while our FY27 forecast is lowered by 0.4pp to 1.7% of GDP (Exhibit 6).

Exhibit 6: We expect current account deficit to average around $1.3\%$ of GDP in CY26 and $1.7\%$ of GDP in FY27  
![](images/d63be50bdecc6fc5ec514eed7b131b899513f82f5d5684d72147d3050488f21f.jpg)

<details>
<summary>bar chart</summary>

| Date | Percent of GDP |
|---|---|
| Mar-24 | 0.5 |
| Jun-24 | -0.5 |
| Sep-24 | -2.5 |
| Dec-24 | -1.0 |
| Mar-25 | 1.3 |
| Jun-25 | -0.3 |
| Sep-25 | -1.5 |
| Dec-25 | -1.5 |
| Mar-26 | 0.7 |
| Jun-26 | -2.0 |
| Sep-26 | -2.0 |
| Dec-26 | -1.8 |
| Mar-27 | -0.9 |
</details>

Source: GS Global Investment Research

We introduce our 2027 forecasts for the current account deficit here as well. Incorporating our commodities team, new brent crude oil price path (\$80/bbl average), we expect current account deficit to remain at around 1.1% of GDP, underpinned by strong services exports and remittance receipts (Please see Appendix).

## Revisiting our capital flow assumptions

In line with our earlier research, the RBI, in coordination with the Government, announced a set of measures to attract foreign capital inflows, including concessional forex swap rate for quasi-sovereign companies and authorized dealer banks to raise USD funding through December 31, 2026, and full hedging support for fresh 3-5 year foreign currency deposits by banks through September 30, 2026. It also expanded the Fully Accessible Route (FAR)-eligible universe to include all new 15-year, 30-year, and 40-year G-Sec issuances and restored the export-proceeds realization period to nine months from 15-months earlier. We incorporate these measures into our capital account forecasts and reassess our balance of payments outlook for CY26 and CY27.

Foreign currency non-resident deposit (FCNR (B)) scheme: The RBI announced the FCNR (B) scheme with a similar framework used during 2013. The RBI will provide a full hedging support for fresh 3-5 year deposits through September 30, 2026 (Please see Appendix for details). We estimate around \$30-50bn of inflows from this scheme in CY26, all of which we expect to materialize by Q3. Some state and private sector banks have already raised the FCNR (B) deposit rates by around 2-4%.

■ External commercial borrowings (ECBs): The RBI announced a concessional forex swap rate of 1.5% (vs. the market prevailing rate of around 3%) for quasi sovereigns to raise USD funding through December 31, 2026 —reducing hedging costs and improving the economics of offshore funding relative to domestic borrowing. We estimate that ECB-related inflows could amount to around \$5-15bn over the next six months.

Foreign investment in government securities (G-Sec): The RBI has expanded 

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
