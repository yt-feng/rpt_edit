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
# Global Markets Daily: Japanese Repatriation Flows—What Matters Most for the Yen

Japan Post Bank's CEO recently said that the bank may double its JGB holdings over time, sparking renewed questions on the potential impact and scope for broader repatriation flows. Many have also been arguing that the 10-year JGB yield at multi-decade highs and the Yen at historically cheap levels strengthens the case to return capital home. We think the reality is more nuanced.  
Japanese investors, excluding the MoF, hold nearly \$6tn of foreign assets, with the majority mostly unhedged. As a result, any coordinated reallocation towards domestic securities should be a source of notable JPY appreciation. Japan Post Bank, however, would unlikely be the driver as it tends to invest largely on a hedged basis. Nor do we think it should be indicative of future decisions by unhedged investors. An increase in Post Bank's JGB holdings could matter more for rates markets if it is indeed the result of rotating away from foreign securities rather than simply adjusting its JPY portfolio.  
GPIF is the key Japanese investor that can have the most impact on FX. It is one of the largest holders of foreign assets, it tends to invest mostly unhedged, and private pensions often follow its allocation decisions. GPIF conducts a strategy review every five years and the last one occurred in 2025, leaving any big changes unlikely before 2030. But it can still shift its holdings within target allocation bands. With current holdings close to the midpoint of the range in each asset, there is room for some adjustment.  
That said, we remain skeptical of significant JPY-positive repatriation flows without a more favorable rate differential. In fact, we think the case for any coordinated, unhedged reallocation towards JGBs looks even less compelling now than earlier this year, when Fed cuts were less in question.

## Japanese Repatriation Flows—What Matters Most for the Yen

Japan Post Bank's CEO recently said that the bank may double its JGB holdings over time—back to a level last seen over a decade ago—sparking renewed questions on the potential impact and scope for broader repatriation flows. $^{1}$ Many have also been arguing that the 10-year JGB yield at multi-decade highs and the Yen at historically cheap levels strengthens the case to return capital home. We think the reality is more

Karen Reichgott Fishman

+1(212)855-6006

karen.fishman@gs.com

GS & Co. LLC

Lexi Kanter

+1(212)855-9701

alexandra.kanter@gs.com

GS & Co. LLC

nuanced. Our Investor's Guide to Japanese Portfolio Flows outlines the data to watch and the investors to follow, and how to track and anticipate foreign asset demand. We show that Japanese investors, excluding the MoF, hold nearly \$6tn of foreign assets, with the majority mostly unhedged (Exhibit 1). As a result, any coordinated reallocation towards domestic securities should be a source of notable JPY appreciation. Post Bank, however, would unlikely be the driver as it tends to invest largely on a hedged basis. An increase in Post Bank's JGB holdings could matter more for rates markets if it is indeed the result of rotating away from foreign securities rather than simply adjusting its JPY portfolio. $^{2}$

Exhibit 1: Japanese investors (excluding the MoF) hold nearly \$6tn of foreign assets, with the majority mostly unhedged  
![](images/24a4686fc18e23b9eae406654474d1cd8686c4fb8e696d37ce3f9b880358c04f.jpg)

<details>
<summary>bar chart</summary>

| Commercial Banks | 450 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Japan Post Bank | 550 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Norinchukin Bank | 210 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
</details>

Data from Post Bank and GPIF financial reports, the BoJ's April FSR, and Flow of Funds data (Outward Investment in Securities + Investment Trust Beneficiary Certificates) as of Q4 2025.  
Source: BoJ, Haver Analytics, GPIF, Japan Post Bank, Data compiled by GS Global Investment Research

Post Bank is the biggest single holder of foreign bonds in Japan after the MoF. As of March 2026, according to Post Bank's latest financial statement, it had roughly \$550bn of foreign holdings, mainly in bonds. As a mostly hedged investor, Post Bank should theoretically care most about the gap between JGB yields and hedged foreign yields. While that gap remains positive across key regions, global yields have been rising alongside JGB yields in recent months, leaving the relative attractiveness of JGBs more stable despite multi-decade highs in the 10-year JGB yield (Exhibit 2). The yield differential is also not the only consideration, and some investors may still be hesitant to buy if they see risks of bonds cheapening further, especially due to rising risk premium rather than rate expectations.

Exhibit 2: Due to the rise in global yields, the relative attractiveness of JGBs has been more stable despite multi-decade highs in the 10-year JGB yield  
![](images/5412ada736f6e0a19bf2f0d08a323dc6140557442527d5226fb9a87152f1db3d.jpg)

<details>
<summary>line chart</summary>

| Year | 10y US Treasuries hedged to JPY | OATs hedged to JPY | Bunds hedged to JPY | Gilts hedged to JPY | JPYB10Y Benchmark Yield |
|------|----------------------------------|--------------------|--------------------|--------------------|--------------------------|
| 2013 | ~1.8                             | ~2.2               | ~1.5               | ~1.7               | ~0.8                     |
| 2014 | ~2.8                             | ~2.5               | ~1.8               | ~2.3               | ~0.9                     |
| 2015 | ~2.0                             | ~1.8               | ~1.2               | ~1.5               | ~0.6                     |
| 2016 | ~1.5                             | ~1.2               | ~0.8               | ~1.0               | ~0.4                     |
| 2017 | ~0.5                             | ~0.8               | ~0.3               | ~0.5               | ~0.1                     |
| 2018 | ~0.8                             | ~1.0               | ~0.5               | ~0.7               | ~0.2                     |
| 2019 | ~0.3                             | ~0.5               | ~0.1               | ~0.3               | ~0.0                     |
| 2020 | ~-1.5                            | ~-0.5              | ~-1.0              | ~-0.5              | ~-0.2                    |
| 2021 | ~1.5                             | ~1.8               | ~1.2               | ~1.0               | ~0.3                     |
| 2022 | ~1.8                             | ~2.5               | ~1.5               | ~1.2               | ~0.4                     |
| 2023 | ~-1.5                            | ~-0.5              | ~-1.0              | ~-0.5              | ~-0.3                    |
| 2024 | ~-2.5                            | ~-1.5              | ~-2.0              | ~-1.5              | ~-1.0                    |
| 2025 | ~-1.0                            | ~-0.5              | ~-1.5              | ~-1.0              | ~-0.5                    |
| 2026 | ~1.5                             | ~2.5               | ~1.8               | ~2.0               | ~3.0                     |
</details>

Source: GS FICC and Equities, GS Global Investment Research

If Post Bank were to shift back towards domestic assets, this would be most meaningful for bond investors. As we have previously noted, the first signs of any pivot should appear in the “Banks” flows in the International Transactions in Securities (ITS) data (as reduced foreign asset purchases or outright sales). The flow could then be more comfortably attributed to Post Bank if Financial Institutions for Small Businesses in the subsequent Flow of Funds (FOF) report shows similar selling of foreign securities and buying of JGBs. So far, there have been limited signs of any meaningful repatriation. While the ITS data show that Banks flows have turned negative since the start of the year (Exhibit 3), the more-lagged FOF data have yet to confirm any shift (Exhibit 4). The latest data as of Q4 2025 suggest that while Post Bank bought more JGBs, it also continued buying foreign assets.

Exhibit 3: While the ITS data show that Banks flows have turned negative since the start of the year...  
![](images/6335e7aa3d364a39f1416721fd09d1a28c688f024d6885f8710e7a7bd1c3ebe1.jpg)

<details>
<summary>line chart</summary>

| Year | Net Purchases ($bn) |
|------|---------------------|
| 2015 | ~50                 |
| 2016 | ~90                 |
| 2017 | ~-60                |
| 2018 | ~-70                |
| 2019 | ~80                 |
| 2020 | ~60                 |
| 2021 | ~-30                |
| 2022 | ~-80                |
| 2023 | ~-110               |
| 2024 | ~110                |
| 2025 | ~-20                |
| 2026 | ~-30                |
</details>

Source: MoF, Haver Analytics, GS Global Investment Research

Exhibit 4: ...the more-lagged FOF data have yet to confirm any shift  
![](images/4e2727afa4eecdc7e5d06a7be70662bf56abed1645d6f953db7d09c3f9e5bd52.jpg)

<details>
<summary>line chart</summary>

| Year | Domestic Government Bonds ($bn) | Outward Investment In Securities ($bn) |
|------|----------------------------------|----------------------------------------|
| 2014 | -75                              | 50                                     |
| 2015 | -250                             | 100                                    |
| 2016 | -200                             | 125                                    |
| 2017 | -150                             | 80                                     |
| 2018 | -100                             | 100                                    |
| 2019 | -50                              | 75                                     |
| 2020 | 0                                | 50                                     |
| 2021 | -50                              | 30                                     |
| 2022 | -100                             | 40                                     |
| 2023 | -150                             | 20                                     |
| 2024 | 75                               | 10                                     |
| 2025 | 0                                | 25                                     |
| 2026 | 50                               | 15                                     |
</details>

\*Includes Investment trust beneficiary certificates to capture foreign assets purchased through a domestic asset manager. See Global Markets Analyst: An Investor's Guide to Japanese Investor Flows for more.  
Source: BoJ, Haver Analytics, GS Global Investment Research

The more meaningful shift for FX would be a shift in strategy by GPIF, Japan's public pension fund. It is one of the largest holders of foreign assets (nearly \$1tn in total), it tends to invest mostly unhedged, and private pensions often follow its allocation decisions. GPIF conducts a strategy review every five years and the last one occurred in 2025, leaving any big changes unlikely before 2030. That said, it can still shift its holdings within target allocation bands. The latest reported holdings stand close to the midpoint of the range in each asset class, suggesting room for some adjustment. Theoretically, if GPIF were to cut its foreign bond holdings to the bottom of its allowable range (20%) and shift those proceeds into JGBs (bringing its allocation to 30%), it could total up to \$87bn. Such an adjustment would unlikely occur all at once, but it reflects some scope for notable flows if desired—or directed by the administration. So far, the timeliest data suggest that GPIF and the private pensions have continued buying foreign debt while selling foreign equities (Exhibit 5). $^{3}$

Exhibit 5: The timeliest data suggest that GPIF and the private pensions have continued buying foreign debt while selling foreign equities  
![](images/33c409cb4b9b6f96c6c80dd4776f4d59113c6bcd7cb858c5fe41f5b924a0e560.jpg)

<details>
<summary>bar chart</summary>

| Year | Equities ($bn) | Long-Term Debt ($bn) |
|------|-----------------|----------------------|
| 2018 | ~5              | ~50                  |
| 2019 | ~20             | ~70                  |
| 2020 | ~10             | ~80                  |
| 2021 | ~-150           | ~160                 |
| 2022 | ~-100           | ~50                  |
| 2023 | ~-50            | ~30                  |
| 2024 | ~-100           | ~40                  |
| 2025 | ~-150           | ~50                  |
| 2026 | ~-100           | ~60                  |
</details>

Source: MoF, Haver Analytics, GS Global Investment Research

Importantly though, any shift in Post Bank's allocation should not necessarily be indicative of future GPIF decisions. While the investment calculus for a hedged investor looks more favorable for JGBs, the case for GPIF (an unhedged investor) to reallocate back towards domestic bonds over the near-term looks less compelling. GPIF aims for positive returns—it has a target of nominal wage growth + 1.9%—and therefore should care most about rate differentials when investing unhedged. For example, while JGB yields have risen more than UST yields over the past year, the differential remains negative (Exhibit 6).

Exhibit 6: While JGB yields have risen more than UST yields over the past year, the differential remains negative  
![](images/ed955c66e08116128c52c895d85b93fc9eef1f382de31fc08299b52f6b39e691.jpg)

<details>
<summary>line chart</summary>

| Year | 10y JGB Yield - 10y US Treasuries Hedged to JPY | 10y JGB Yield - 10y US Treasury Yield |
|------|--------------------------------------------------|------------------------------------------|
| 2010 | -2.0                                             | -2.5                                     |
| 2012 | 0.0                                              | -1.0                                     |
| 2014 | -1.5                                             | -2.0                                     |
| 2016 | 0.5                                              | -1.5                                     |
| 2018 | 0.0                                              | -2.5                                     |
| 2020 | 1.5                                              | -1.0                                     |
| 2022 | -1.0                                             | -3.0                                     |
| 2024 | 2.5                                              | -4.0                                     |
| 2026 | 1.0                                              | -2.0                                     |
</details>

Source: GS FICC and Equities, GS Global Investment Research

Without a more favorable rate differential, we remain skeptical of significant JPY-positive repatriation flows. There could still be more notable rotation back towards JGBs among hedged investors, especially if the Fed pivots towards rapid rate hikes, like in 2022. But we think the case for any coordinated, unhedged reallocation towards JGBs looks even less compelling now than earlier this year, when Fed cuts were less in question.

## TRADE IDEAS

## Best Trade Ideas Across Assets

For pricing, charts, and a list of previous recommendations, please visit our Trade Ideas page.

1. Stay short SGD/MYR, opened January 24, 2026, at 3.13, with a target at 2.90 and a stop at 3.30, currently trading at 3.12.  
2. Stay long TRY, NGN and KZT against the USD, as an equally weighted basket, opened February 18, 2026, at 0%, with a total return target of 7.5%, and a revised stop of 0%, currently trading at 2.1%.  
3. Stay long USD/SEK, opened March 20, 2026, at 9.3443, with a target at 9.65 and a stop at 9.00, currently trading at 9.4147.  
4. Stay long 3y France, Spain, Italy vs OIS (equally weighted), opened April 10, 2026, at 0.33, with a target at 0.23 and a revised stop at 0.32, currently trading at 0.30.  
5. Stay long MSCI Korea and Taiwan (equal weight) vs. short MSCI India, Philippines, Thailand (equal weight), opened April 16, 2026, at 100, with a revised target of 155

and a revised stop of 125, currently trading at 142.

6. Stay short EUR/HUF, opened 17 April 2026, at 361, with a target of 350 and a stop of 372, currently trading at 356.  
7. Stay long 3y SOFR swap spread, opened 17 April 2026, at -22.6bp, with a target at -18bp inclusive of carry; and a revised stop at -23bp, currently trading at -20.3bp.  
8. 2s5s CAD steepener, opened 24 April 2026, at 20bp, with a target at 35bp and a revised stop at 20bp, current trading at 22bp.  
9. Stay short USD/EGP, opened 24 April 2026, at 0%, with a total return target at 6% and a stop at -3%, currently trading at 2.8%.  
10. Stay long 5y5y EUR OIS – HICP, opened 01 May 2026, at 1.09%, with a target at 0.88% and a stop at 1.22%, currently trading at 1.03%.  
11. Stay long 5y Receivers on 3m 2s5s10s Receiver Fly (bp running), opened 09 May 2026, at 1bp, with a target at 10bp and a stop at -5bp, currently trading at -1bp.  
12. 1y forward 2s10s GBP OIS steepeners, opened 29 May 2026, at 0.38, with a target at 0.55 and a stop at 0.25, currently trading at 0.34.  
13. Receive 2Y ZAR OIS, opened 03 June 2026, at 7.47%, with a target at 7.00% and a stop at 7.90%.

## G10 FX Strategy Team

## Michael Cahill

+44(20)7552-8314

michael.e.cahill@gs.com

GS International

## Karen Reichgott Fishman

+1(212)855-6006

karen.fishman@gs.com

GS & Co. LLC

## Stuart Jenkins

+44(20)7051-4700

stuart.jenkins@gs.com

GS International

## Lexi Kanter

+1(212)855-9701

alexandra.kanter@gs.com

GS & Co. LLC

## Disclosure Appendix

## Reg AC

We, Karen Reichgott Fishman and Lexi Kanter, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Karen Reichgott Fishman GS & Co. LLC, Lexi Kanter GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory discl

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
