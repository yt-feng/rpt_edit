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
# China FX/Rates Monitor: The Policy Anchor Behind a Stronger CNY and Lower Rates

Our monitor tracks the latest developments and identifies key indicators for China FX and rates, including valuations/policy stance, technicals, flows, and fundamentals. Below we summarize our key takeaways on the China FX and rates markets.

Broad easing requires clearer evidence of growth weakness. The April data miss raised questions about whether policymakers would step up easing, but we think the threshold for broad easing is high. Growth has become more uneven, with exports still supporting headline growth while domestic demand, proxied by retail sales and fixed asset investment, softened notably. The April weakness may bring Q2 yoy GDP growth closer to the lower end of the 4.5-5% target range, but we do not think it marks an abrupt deterioration in the underlying growth trend. Part of the weakness reflected technical or policy-related factors, including residual seasonality and slower fiscal spending after a strong start to the year. Retail sales were also weighed down by the fading boost from consumer goods trade-in subsidies and the increase in EV purchase taxes. Some of these drags could fade, while fiscal support may catch up later this year as government bond issuance re-accelerates and policy financial instruments start to provide additional support. Oil-led reflation complicates the case for broad monetary easing. If oil prices stabilize, PPI inflation could peak around late Q2, but uncertainty around the reopening of the Strait of Hormuz keeps imported inflation risks elevated. Policy rate cuts therefore look difficult under elevated imported inflation. Instead, monetary policy is more likely to accommodate fiscal implementation through low-profile easing, such as keeping interbank liquidity ample, with interbank repo rates below the OMO target, and targeted credit easing, including more relending at lower rates. A sharper export slowdown or a more persistent deterioration in domestic demand would be the necessary triggers for a broader policy response.

Policy anchor behind CNY appreciation. CNY appreciation has remained resilient even through periods of renewed Dollar strength. In March, when the Middle East energy shock initially triggered broad Dollar strength, USD/CNY only partially retraced its earlier decline and stabilized around 6.90, from around 6.82 before the shock. The appreciation trend resumed later, with USD/CNY spot breaking below 6.80 in late May despite renewed Dollar strength since mid-May. Policy signals from the PBOC remain key to interpreting the move. In our view, the central bank appears comfortable with orderly and gradual CNY appreciation against the USD, with a pace around 4% annualized likely fast enough to offset carry costs for foreign investors but slow enough to keep the drag on export

Xinquan Chen

+852-2978-2418

xinquan.chen@gs.com

GS (Asia) L.L.C.

Danny Suwanapruti

+65-6889-1987

danny.suwanapruti@gs.com

GS (Singapore) Pte

competitiveness and inflation limited. However, appreciation expectations have become more one-sided and have triggered stronger exporters' FX conversion. We estimate exporters have converted around US\$150bn more FX proceeds than normal since last December, against our earlier estimate that excess corporate USD hoarding reached around US\$500bn by mid-2025, the peak of this USD-hoarding cycle. This makes CNY appreciation more choppy and event-driven, with fixing changes easily read as policy signals. We expect CNY appreciation to continue (USD/CNY spot reaching 6.50 in 12 months), with some near-term overshooting risk; periods of Dollar strength may reduce near-term downside pressure on USD/CNY spot.

Liquidity anchor behind lower rates. The recent rally in CGBs and decline in IRS rates have puzzled many investors, especially as oil-shock reflation has pushed inflation expectations higher. Our model-implied fair value for 10y CGB yields has risen to above 2%, mostly reflecting higher one-year-ahead CPI inflation expectations, while the 10y CGB yield has fallen to around 1.70%. The front end rates also look difficult to square with a no-cut baseline: 1y IRS is trading only around 3bp above the 1.4% OMO policy rate, while the 1y CGB yield is much lower at around 1.15%. Meanwhile, expectations for high-profile monetary policy easing, such as policy rate cuts, are low. Overnight repo rates (DR001) have also traded close to the lower bound of the interest rate corridor in April and even risen somewhat in May. Taken together, these developments would normally suggest limited downside to bond yields and IRS rates. The missing factor, in our view, is the asset-allocation pressure created by weak credit demand and limited alternative investable assets onshore. Soft loan demand leaves banks with more balance-sheet capacity for bond investment. In previous episodes of very low CGB yields and strong bank demand for bonds, the PBOC tended to warn against idle funds circulating within the financial system. This time, however, the PBOC's Q1 monetary policy report explicitly stated that banks' bond investment, like credit extension, is an important channel of financing the real economy and money creation. At the same time, limited room for domestic institutions to increase overseas investment keeps demand concentrated in onshore fixed-income assets. These flows can push CGB yields below model-implied fair value, even without policy rate cuts. For swaps, although the room for repo fixing to decline further is increasingly limited, wider swap spreads may attract receivers when spreads approach historical highs.

A sustained selloff requires higher repo rates. We still expect China rates to remain low and see room for yields to move lower in the medium term if growth weakness becomes clearer or the liquidity anchor stays in place. That said, correction risks could rise into late June, given quarter-end liquidity demand and the market sensitivity to recent OMO operations. The PBOC's zero 7-day reverse repo operation earlier this week was read by markets as a warning of potential liquidity tightening. However, OMO injections resumed shortly after and demand for OMO funding may be low given its relatively high cost compared with interbank repos. In our view, the room for a sustained rates selloff should also be limited unless the PBOC is willing to repeat the 2020/2022 episodes of pushing repo rates above the OMO target. This looks like a high bar: repo rates are currently not far below the OMO rate (which was not the case in 2020/2022), domestic demand and credit demand remain soft, and uncertainty around the Middle East energy shock is still elevated.

## 1. Valuations and policy stance

Exhibit 1: CNY appreciated against USD by more than 3% year-to-date as of the end of May  
![](images/027b39b173c2a4c6499da8f6433cfb302b768bae4d2eee3603295fc7685ec6ce.jpg)

<details>
<summary>line chart</summary>

| Year | CNY vs. CFETS basket | USD/CNY (right axis, reverse scale) |
|------|----------------------|-------------------------------------|
| 2016 | ~100                 | ~6.4                                |
| 2017 | ~94                  | ~6.6                                |
| 2018 | ~104                 | ~6.8                                |
| 2019 | ~98                  | ~7.0                                |
| 2020 | ~92                  | ~7.2                                |
| 2021 | ~102                 | ~7.4                                |
| 2022 | ~108                 | ~7.6                                |
| 2023 | ~100                 | ~7.4                                |
| 2024 | ~102                 | ~7.2                                |
| 2025 | ~100                 | ~7.0                                |
| 2026 | ~101                 | ~7.4                                |
</details>

Source: Bloomberg, Wind

Exhibit 2: USD/CNH spot broke below 6.8 by mid-May despite a stronger Dollar  
![](images/1703fb92f828f0cf07cce5f84c52a4d1f66a61202c832b37866a9ed23771e173.jpg)

<details>
<summary>line chart</summary>

| Date   | USDCNH | DXY (right axis) |
|--------|--------|------------------|
| Jan-24 | 7.2    | 104              |
| May-24 | 7.3    | 106              |
| Sep-24 | 7.1    | 102              |
| Jan-25 | 7.4    | 110              |
| May-25 | 7.3    | 108              |
| Sep-25 | 7.1    | 104              |
| Jan-26 | 6.9    | 100              |
| May-26 | 6.8    | 98               |
</details>

DXY: US Dollar Index, which measures the value of the US Dollar vs. a basket of currencies.  
Source: Bloomberg

Exhibit 3: Countercyclical factor remained elevated at above +400pips in May, signaling PBOC's tendency to slow RMB appreciation against the Dollar  
![](images/bcaba48c98e333c11c257a2eb6d5153cc0deef9a89da4a4d3f1cb9c667a5c148.jpg)

<details>
<summary>line chart</summary>

| Date    | Single day | 10 days moving average |
|---------|------------|------------------------|
| Apr 9th |            |                        |
</details>

We measure the countercyclical factor by calculating the difference between the official daily CNY fixing and our estimation of the fixing based on official documents of CNY fixing mechanism.

Exhibit 4: USD/CNH Tom/Next points moved sideways over the past few months  
![](images/1f8b7b586cbdb5da81e1a00c65a7041e176d55a92c15e868a298d7068cafe664.jpg)

<details>
<summary>line chart</summary>

| Date    | Single day | 5dma |
|---------|------------|------|
| Jan-23  | ~0         | ~0   |
| Jul-23  | ~-10       | ~-10 |
| Jan-24  | ~10        | ~10  |
| Jul-24  | ~-10       | ~-10 |
| Jan-25  | ~10        | ~10  |
| Jul-25  | ~-10       | ~-10 |
| Jan-26  | ~-10       | ~-10 |
</details>

Tom/Next (Tomorrow next) is a short-term FX swap allowing investors to roll over their spot position. Positive (negative) Tom/Next points mean negative (positive) carry returns of long USD short CNH. Red circles indicate the timing of front-end CNH liquidity shortage (potential CNH liquidity management by the authorities).  
Source: Bloomberg, Data compiled by GS Global Investment Research  
Source: Bloomberg, Data compiled by GS Global Investment Research

## 2. Technicals

Exhibit 5: Carry-to-vol ratio for EUR/CNH picked up in Apr-May 2026  
![](images/9204184144a5e6eb8430fc208b698c0a7e6702f51907bff555772dcc163194d1.jpg)

<details>
<summary>line chart</summary>

| Year | Carry-to-vol ratio (USD/CNH) | Carry-to-vol ratio (EUR/CNH) |
|------|------------------------------|------------------------------|
| 19   | 0.0                          | -0.6                         |
| 20   | -0.3                         | -0.9                         |
| 21   | -0.6                         | -0.7                         |
| 22   | -1.2                         | -0.9                         |
| 23   | 0.6                          | -0.3                         |
| 24   | 1.2                          | 0.3                          |
| 25   | 0.8                          | 0.6                          |
| 26   | 1.2                          | 0.3                          |
</details>

Carry is defined as annualized carry returns of 3m USD/CNH / EUR/CNH forward, and volatility refers to 3-month rolling realized volatility of FX total returns.  
Source: Bloomberg, GS Global Investment Research

Exhibit 6: Momentum to buy CNH and sell EUR picked up over the past two months  
![](images/0e3c1fe923a79311923005fba3cc5a878c223940558cd084a9fb32bc794108b9.jpg)

<details>
<summary>line chart</summary>

| Year | Short CNH | Momentum-to-vol ratio (USD/CNH) | Short CNH |
|------|-----------|----------------------------------|-----------|
| 2021 | -         | 9.5                              | -         |
| 2022 | -         | -                                | -         |
| 2023 | -         | -                                | -         |
| 2024 | -         | -                                | -         |
| 2025 | -         | -                                | -         |
| 2026 | -         | -                                | -         |
</details>

Momentum is defined as 3-month cumulative FX total returns, and volatility refers to 3-month rolling realized volatility of FX total returns.  
Source: Bloomberg, GS Global Investment Research

Exhibit 7: CNH/CNY basis remained at around -300pips in Apr-May 2026  
![](images/e3c5b82560c798533c77247a2878c008cd531c593638c2810778e508a55cf04b.jpg)

<details>
<summary>line chart</summary>

| Year | CNH/CNY basis: 1m | CNH/CNY basis: 3m |
|------|-------------------|-------------------|
| 22   | ~0                | ~0                |
| 23   | ~600              | ~300              |
| 24   | ~1500             | ~1000             |
| 25   | ~1200             | ~800              |
| 26   | ~-300             | ~-300             |
</details>

CNH/CNY basis is defined as the difference between deliverable forward of USD/CNH and non-deliverable forward of USD/CNY.  
Source: Bloomberg, GS Global Investment Research

Exhibit 8: Cross-currency swap rate fell below NDIRS rate as CNH funding conditions eased  
![](images/58c51dab10b55932b86777fd186f20dac22e13bfbf7dd2e2a26e49e2f975e114.jpg)

<details>
<summary>line chart</summary>

| Date   | CNH FX implied yield | NDIRS/CCS spread |
|--------|----------------------|------------------|
| Jan-22 | ~3.5                 | ~1.8             |
| Jul-22 | ~3.7                 | ~2.0             |
| Jan-23 | ~2.8                 | ~1.5             |
| Jul-23 | ~4.1                 | ~2.8             |
| Jan-24 | ~3.0                 | ~1.5             |
| Jul-24 | ~4.3                 | ~2.5             |
| Jan-25 | ~3.5                 | ~1.0             |
| Jul-25 | ~1.5                 | ~0.0             |
| Jan-26 | ~1.0                 | ~-0.5            |
</details>

NDIRS/CCS spread: CNH cross-currency swap rate minus CNY non-deliverable interest rate swap rate.  
Source: Bloomberg, GS Global Investment Research

Exhibit 9: USD/CNY fixing descent accelerated somewhat in late May  
![](images/6ec0d0b616846e5ca3a37a723f26ba1fa54068f7aa39099a7c7f147ef0c6f612.jpg)

<details>
<summary>line chart</summary>

| Date       | USD/CNY Fixing |
| ---------- | -------------- |
| 5/12/25    | 7.24           |
| 7/7/25     | 7.16           |
| 9/1/25     | 7.12           |
| 10/27/25   | 7.08           |
| 12/22/25   | 7.04           |
| 2/16/26    | 6.96           |
| 4/13/26    | 6.88           |
| 6/8/26     | 6.80           |
</details>

Source: PBOC

## 3. Fundamentals

Exhibit 10: China's trade balance fell from Jan-Feb to Mar-Apr on lower goods trade surplus  
![](images/0feda56002f9a702101439ec38454d17ce6d97ec552c2b73de418555251c5764.jpg)

<details>
<summary>bar-line hybrid chart</summary>

Trade balance
| Year | Goods trade balance (USD bn, sa) | Services trade balance: travel (USD bn, sa) | Services trade balance: non-travel (USD bn, sa) | Total (USD bn, sa) |
|---|---|---|---|---|
| 19 | 30 | -5 | -20 | 20 |
| 20 | 40 | -5 | -15 | -25 |
| 21 | 60 | -5 | -10 | 40 |
| 22 | 65 | -5 | -10 | 50 |
| 23 | 60 | -5 | -15 | 45 |
| 24 | 55 | -5 | -15 | 35 |
| 25 | 80 | -5 | -15 | 70 |
| 26 | 120 | -5 | -15 | 90 |
</details>

Source: Haver Analytics, GS Global Investment Research

Exhibit 11: China's travel exports stood at about $198\%$ of 2019 levels in April 2026, and travel imports were around $96\%$ of 2019 levels  
![](images/e5d48ab081e4a1976ec6ae5ffcb228812e274353444c60234b2da76417301a78.jpg)

<details>
<summary>line chart</summary>

| Year | Exports | Imports |
|------|---------|---------|
| 16   | 140     | 100     |
| 17   | 130     | 110     |
| 18   | 120     | 130     |
| 19   | 110     | 120     |
| 20   | 40      | 50      |
| 21   | 30      | 40      |
| 22   | 35      | 45      |
| 23   | 40      | 50      |
| 24   | 80      | 90      |
| 25   | 130     | 110     |
| 26   | 220     | 180     |
</details>

Travel imports are defined as the overseas spending of China's residents for tourism, education and medical services; travel exports are defined as non-residents' spending in China. Both include tourism spending.  
Source: Haver Analytics, GS Global Investment Research

Exhibit 12: Both banks' net external assets and official FX reserves rose from March to April  
![](images/163afd9136f3b0968ae3404ea24c90c842743780134df1eb8f4b7dd324d92498.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date | Commercial banks' net external asset changes (Billion USD) | Official FX reserve changes (adjusted for FX valuation effect*) (Billion USD) | Sum (Billion USD) |
|---|---|---|---|
| Jan-22 | 30 | -15 | 10 |
| Jul-22 | 10 | 50 | -20 |
| Jan-23 | -10 | 40 | 70 |
| Jul-23 | -15 | -20 | -40 |
| Jan-24 | 70 | 45 | 80 |
| Jul-24 | 35 | 25 | 30 |
| Jan-25 | 70 | -40 | 30 |
| Jul-25 | -10 | 30 | 50 |
| Jan-26 | 60 | 40 | 100 |
| Jul-26 | -60 | -60 | -80 |
</details>

\* GS estimates based on IMF global reserve composition data. We do not adjust for asset price valuation effect due to data limitation  
Source: PBOC, CEIC, Data compiled by GS Global Investment Research

Exhibit 13: As of April 2026, China's official FX reserves stood at USD 3411bn, while commercial banks held USD 1491bn net external assets  
![](images/9f319124d60586d6b8aec14c7f7e6c80db876bde54a14945019eff5cae8989cb.jpg)

<details>
<summary>area chart</summary>

| Year | FX reserves (Billion USD) | Banks' net assets overseas (Billion USD) |
|------|---------------------------|------------------------------------------|
| 11   | ~3,000                    | ~3,500                                   |
| 12   | ~3,200                    | ~3,700                                   |
| 13   | ~3,400                    | ~3,800                                   |
| 14   | ~3,600                    | ~3,900                                   |
| 15   | ~3,800                    | ~4,000                                   |
| 16   | ~3,500                    | ~3,800                                   |
| 17   | ~3,200                    | ~3,600                                   |
| 18   | ~3,100                    | ~3,700                                   |
| 19   | ~3,150                    | ~3,800                                   |
| 20   | ~3,200                    | ~3,900                                   |
| 21   | ~3,250                    | ~4,000                                   |
| 22   | ~3,300                    | ~4,100                                   |
| 23   | ~3,250                    | ~4,200                                   |
| 24   | ~3,300       

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
