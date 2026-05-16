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
# GLOBAL CREDIT TRADER

# State of Play for Leveraged Finance Defaults

As we highlighted recently, absent a sharp deterioration in the growth backdrop, we believe the peak in aggregate default activity in the syndicated credit market (leveraged loans and HY bonds) is likely behind us. That said, under the surface, there are several key default-related themes for corporate credit investors to monitor—consistent with the broader theme of market dispersion.

In this week's Global Credit Trader, we examine the state of play for defaults in the US and European leveraged finance markets and highlight several key themes.

1. The direction: The absolute level of defaults has been trending higher from the very low levels that persisted in 2022/23 but remains near historical median levels. The one exception is the floating rate broadly syndicated loan (BSL) market, where defaults peaked in late 2024 and have been declining.   
2. Structures: Distressed exchanges, or liability management exercises (LMEs), remain the vehicle of choice for reorganizing the liability side of a firm's balance sheet. However, these are increasingly leading to a ‘repeat defaulter’ phenomenon.   
3. Ultimate losses: Recovery rates have continued to trend lower—extending the longer-term pattern. We partially attribute this dynamic to the rise of repeat defaults and ‘loan-only’ capital structures.   
4. Sector patterns: In contrast to the prevailing market narrative related to potential disruption of Software-focused firms, the sector composition mix still skews heavily towards capital industries and consumer-facing businesses.   
5. The view ahead: The growth backdrop is the key signpost to watch, in our view. Looking ahead, none of the metrics we monitor signal a near-term uptick in expected defaults in the US. In Europe, we still envision a modest increase in defaults through year-end, owing to a more challenging growth, inflation, monetary policy mix. That said, we still expect defaults to remain below the local peak. The loan market is more vulnerable than HY, in our view.

# Amanda Lynam, CPA

+1(212)934-1895

amanda.lynam@gs.com

GS & Co. LLC

# Spencer Rogers, CFA

+1(801)884-1104

spencer.rogers@gs.com

GS & Co. LLC

# Sara Grut

+44(20)7774-8622 | sara.grut@gs.com

GS International

# Shamshad Ali

+1(212)902-6712

shamshad.ali@gs.com

GS & Co. LLC

# State of Play for Leveraged Finance Defaults

Over the past several years, defaults have exhibited divergent trends across regions and asset classes. Exhibits 1 and 2 illustrate the 12-month trailing, issuer-weighted default rates in the US and European HY and leveraged loan markets (inclusive of distressed exchanges). While US HY defaults have been oscillating in a narrow band between 3% and 4% for the last couple of years, the US BSL market has demonstrated a discernible deceleration from the funding-cost-driven spike of 2023 and 2024, with the default rate falling to 5.1% from a peak of 7.4%. In Europe, both HY bond and BSL defaults show signs of trending higher, consistent with a more challenging growth, inflation, and monetary policy mix related to the ongoing commodity market disruptions.

Exhibit 1: US HY defaults have oscillated in a narrow band while US BSL defaults are still decelerating from their recent peak   
12-month trailing issuer-weighted default rates in the US HY bond and leveraged loan markets   
![](images/30d596129074446824dbbabb26c21c77153fd66e7da0da1e8aaf6455481ec0a1.jpg)

<details>
<summary>line</summary>

| Year | US HY | US Leveraged Loans |
|------|-------|---------------------|
| 99   | ~3.5  | ~1.5                |
| 00   | ~4.5  | ~2.5                |
| 01   | ~6.0  | ~4.0                |
| 02   | ~11.5 | ~6.5                |
| 03   | ~7.0  | ~5.0                |
| 04   | ~6.5  | ~4.5                |
| 05   | ~3.0  | ~2.5                |
| 06   | ~2.5  | ~2.0                |
| 07   | ~2.0  | ~1.5                |
| 08   | ~1.5  | ~1.0                |
| 09   | ~3.0  | ~2.5                |
| 10   | ~15.0 | ~11.0               |
| 11   | ~2.5  | ~1.5                |
| 12   | ~3.0  | ~2.0                |
| 13   | ~2.5  | ~1.5                |
| 14   | ~2.0  | ~1.0                |
| 15   | ~2.5  | ~1.5                |
| 16   | ~4.0  | ~3.0                |
| 17   | ~8.0  | ~4.0                |
| 18   | ~6.0  | ~3.5                |
| 19   | ~4.0  | ~3.0                |
| 20   | ~8.0  | ~4.5                |
| 21   | ~8.5  | ~6.0                |
| 22   | ~1.0  | ~1.5                |
| 23   | ~3.0  | ~3.5                |
| 24   | ~4.0  | ~5.0                |
| 25   | ~3.5  | ~4.5                |
| 26   | ~3.0  | ~4.0                |
</details>

Note: As of April 2026 (most recent as of May 14, 2026).   
Source: Moody's, GS Global investment Research

Exhibit 2: The path of European defaults is likely higher owing to a challenging growth, inflation and policy mix 12-month trailing issuer-weighted default rates in the European HY bond and leveraged loan markets   
![](images/a6ce6cdfe685d81311125e69e311272e2f9d982f100f0e74674350ab508f4d29.jpg)

<details>
<summary>line</summary>

| Year | European HY | European Leveraged Loans |
|------|-------------|--------------------------|
| 99   | 0           | 0                        |
| 00   | 6           | 0                        |
| 01   | 4           | 0                        |
| 02   | 18          | 4                        |
| 03   | 18          | 7                        |
| 04   | 2           | 0                        |
| 05   | 2           | 0                        |
| 06   | 2           | 0                        |
| 07   | 4           | 2                        |
| 08   | 4           | 2                        |
| 09   | 12          | 4                        |
| 10   | 12          | 4                        |
| 11   | 4           | 2                        |
| 12   | 4           | 2                        |
| 13   | 5           | 4                        |
| 14   | 5           | 4                        |
| 15   | 5           | 4                        |
| 16   | 5           | 4                        |
| 17   | 5           | 4                        |
| 18   | 5           | 4                        |
| 19   | 5           | 4                        |
| 20   | 5           | 4                        |
| 21   | 7           | 4                        |
| 22   | 7           | 4                        |
| 23   | 5           | 4                        |
| 24   | 5           | 4                        |
| 25   | 5           | 4                        |
| 26   | 5           | 4                        |
</details>

Note: As of April 2026 (most recent as of May 14, 2026).   
Source: Moody's, GS Global Investment Research

A defining theme of the current cycle is the structural shift away from traditional in-court restructurings and towards distressed exchanges and, to a lesser extent, pre-packaged Chapter 11s. As Exhibits 3 and 4 highlight, the shares of defaults that were classified as distressed exchanges or pre-packaged Chapter 11 filings have surged in recent years and are currently hovering in the 70-80% range, depending on the market. On average, we find that LMEs tend to preserve recovery values better than in-court restructurings initially—which often makes such transactions the preferred path for private equity sponsors. For example, in 2025, US HY senior unsecured recovery rates for distressed exchanges averaged around 60% vs. roughly 10% for the handful of ‘hard’ defaults that occurred.

Exhibit 3: The LME share of US defaults continues to rise
Annual share of defaults in the US HY and BSL markets classified as distressed exchanges or ‘pre-pack’ Chapter 11 filings   
![](images/3abab720427b5c62d37ca2b2d8e230938ff82aede19f6c07a967266fc3d99e9e.jpg)

<details>
<summary>bar</summary>

| Year | Distressed exchange/pre-pack Ch. 11 share of US HY defaults (%) | Distressed exchange/pre-pack Ch. 11 share of US BSL defaults (%) |
|---|---|---|
| 08 | 35 | 11 |
| 09 | 54 | 41 |
| 10 | 52 | 45 |
| 11 | 49 | 30 |
| 12 | 53 | 53 |
| 13 | 29 | 37 |
| 14 | 50 | 38 |
| 15 | 59 | 50 |
| 16 | 59 | 44 |
| 17 | 54 | 48 |
| 18 | 55 | 68 |
| 19 | 46 | 41 |
| 20 | 54 | 57 |
| 21 | 54 | 72 |
| 22 | 53 | 63 |
| 23 | 65 | 65 |
| 24 | 78 | 68 |
| 25 | 72 | 67 |
| 26 | 67 | 80 |
</details>

Note: As of April 2026 (most recent as of May 14, 2026).   
Source: Moody's, GS Global Investment Research

Exhibit 4: The distressed exchange share of European defaults is also elevated   
Annual share of defaults in the European HY and BSL markets classified as distressed exchanges or ‘pre-pack’ Chapter 11 filings   
![](images/c3ef425a668e2a8283f7ee7bc1a897d61641f3ccfff8ab1a851526e4956d149b.jpg)

<details>
<summary>bar</summary>

| Year | Distressed exchange/pre-pack Ch. 11 share of European HY defaults (%) | Distressed exchange/pre-pack Ch. 11 share of European BSL defaults (%) |
| :--- | :--- | :--- |
| 09 | 42 | 27 |
| 10 | 38 | 25 |
| 11 | 70 | 100 |
| 12 | 60 | 44 |
| 13 | 52 | 57 |
| 14 | 38 | 33 |
| 15 | 53 | 0 |
| 16 | 47 | 67 |
| 17 | 41 | 45 |
| 18 | 33 | 80 |
| 19 | 24 | 16 |
| 20 | 39 | 56 |
| 21 | 67 | 60 |
| 22 | 37 | 71 |
| 23 | 38 | 64 |
| 24 | 54 | 52 |
| 25 | 87 | 83 |
| 26 | 62 | 67 |
</details>

Note: As of April 2026 (most recent as of May 14, 2026).   
Source: Moody's, GS Global Investment Research

The dominance of LMEs comes with an important caveat: they are often an iterative process, and for many corporate borrowers a single distressed exchange fails to place their debt burden on a sustainable path. This ‘incomplete’ balance sheet relief results in a visible trend of ‘repeat defaults.’

Exhibits 5 through 8 show the annual share of repeat defaults (across various markets) involving distressed exchanges vs. in-court restructurings, using a three-year window to define a repeat default. The main takeaway is that in-court restructurings are rarely followed by a repeat default, while distressed exchanges lead to repeat defaults roughly 50% of the time. As we have documented in previous research, these iterative defaults systematically erode recovery outcomes with each successive restructuring.

Exhibit 5: LMEs are often iterative and lead to ‘repeat defaults’ much more often than in-court restructurings...   
Share of US HY distressed exchanges (left panel) and in-court restructurings (right panel) in each year that defaulted again within three years   
![](images/344729a4d78334a82e87e37a29697a1ffee49812e1f6ec0e50bdd80d5cb846bf.jpg)

<details>
<summary>bar_line</summary>

| YTD | Count | Share that defaulted again within 3 years (RHS) |
| --- | --- | --- |
| 10 | 17 | 20 |
| 11 | 10 | 10 |
| 12 | 13 | 40 |
| 13 | 4 | 50 |
| 14 | 10 | 40 |
| 15 | 25 | 80 |
| 16 | 37 | 50 |
| 17 | 22 | 40 |
| 18 | 16 | 70 |
| 19 | 18 | 50 |
| 20 | 28 | 30 |
| 21 | 4 | 20 |
| 22 | 9 | 80 |
| 23 | 23 | 40 |
| 24 | 27 | 20 |
| 25 | 23 | - |
| 26 | 3 | - |
</details>

Note: As of April 2026 (most recent as of May 14, 2026).

![](images/18456b7d581c78f8f18d70e15bb8457b6384e27ecf035afa1e76db57af109d30.jpg)

<details>
<summary>bar_line</summary>

| YTD | Count | Share that defaulted again within 3 years (RHS) (%) |
|---|---|---|
| 10 | 25 | 2 |
| 11 | 20 | 0 |
| 12 | 18 | 3 |
| 13 | 14 | 0 |
| 14 | 10 | 0 |
| 15 | 29 | 0 |
| 16 | 40 | 2 |
| 17 | 22 | 5 |
| 18 | 16 | 0 |
| 19 | 24 | 0 |
| 20 | 37 | 2 |
| 21 | 4 | 0 |
| 22 | 7 | 0 |
| 23 | 13 | 0 |
| 24 | 7 | 15 |
| 25 | 7 | 0 |
| 26 | 6 | 0 |
</details>

Source: Moody's, GS Global Investment Research

Exhibit 6: ...the same is true in the broadly syndicated loan market   
Share of US leveraged loan distressed exchanges (left panel) and in-court restructurings (right panel) in each year that defaulted again within three years   
![](images/91bd02277859fd47e4fde70bffc88a89ca0b5e42168e82130a15079de5b9b456.jpg)  
Note: As of April 2026 (most recent as of May 14, 2026).   
Source: Moody's, GS Global Investment Research

Exhibit 7: The same pattern holds in European HY...   
Share of European HY distressed exchanges (left panel) and in-court restructurings (right panel) in each year that defaulted again within three years   
![](images/4f1d751455d9340faf14681fd9b31df777c02067ba41bc93c193c00515513d12.jpg)

<details>
<summary>bar_line</summary>

| YTD | Count | Share that defaulted again within 3 years (RHS) (%) |
|-----|-------|------------------------------------------------------|
| 10  | 3     | 11                                                   |
| 11  | 9     | 7                                                    |
| 12  | 8     | 8                                                    |
| 13  | 12    | 3                                                    |
| 14  | 3     | 11                                                   |
| 15  | 9     | 11                                                   |
| 16  | 8     | 13                                                   |
| 17  | 9     | 11                                                   |
| 18  | 5     | 0                                                    |
| 19  | 4     | 50                                                   |
| 20  | 15    | 11                                                   |
| 21  | 6     | 6                                                    |
| 22  | 14    | 5                                                    |
| 23  | 7     | 4                                                    |
| 24  | 11    | 44                                                   |
| 25  | 18    | 46                                                   |
| 26  | 5     | -                                                    |

| YTD | Count | Share that defaulted again within 3 years (RHS) (%) |
|-----|-------|--------------------------------------------------------|
| 10  | -     | -                                                      |
| 11  | -     | -                                                      |
| 12  | -     | -                                                      |
| 13  | -     | -                                                      |
| 14  | -     | -                                                      |
| 15  | -     | -                                                      |
| 16  | -     | -                                                      |
| 17  | -     | -                                                      |
| 18  | -     | -                                                      |
| 19  | -     | -                                                      |
| 20  | -     | -                                                      |
| 21  | -     | -                                                      |
| 22  | -     | -                                                      |
| 23  | -     | -                                                      |
| 24  | -     | -                                                      |
| 25  | -     | -                                                      |
| 26  | -     | -                                                      |

| YTD | Count | Share that defaulted again within 3 years (RHS) (%) |
|-----|-------|--------------------------------------------------------|
| 10  | -     | -                                                      |
| 11  | -     | -                                                      |
| 12  | -     | -                                                      |
| 13  | -     | -                                                      |
| 14  | -     | -                                                      |
| 15  | -     | -                                      |
| 16  | -     | -                                                      |
| 17  | -     | -                                                      |
| 18  | -     | -                                                      |
| 19  | -     | -                                                      |
| 20  | -     | -                                                      |
| 21  | -     | -                                                      |
| 22  | -     | -                                                      |
| 23  | -     | -                                                      |
| 1    | -     | -                                                      |
| 2    | -     | -                                                      |
| 3    | -     | -                                                      |
| ... | ...   | ...                                                    |
| YTD : Count (Distressed exchanges) / In-court restructurings (RHS) / Share that defaulted again within 3 years (RHS) (%) (Count) / Share that defaulted again within 3 years (RHS) (%) (Share) (Count) / Share that defaulted again within 3 years (RHS) (%) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Share) (Count) (Count) (Share) (Count) (Count) (Share) (Count) (Count) (Share) (Count) (Count) (Share) (Count) (Count) (Share) (Count) (Count) (Share) (Count) (Count) (Share) (Count) (Count) (Share) (Count) (Count) (Share) (Count) (Count) (Share) (Count) (Count) (Share) (Count)
</details>

Note: As of April 2026 (most recent as of May 14, 2026).   
Source: Moody's, GS Global Investment Research

Exhibit 8: ...and in the European leveraged loan market   
Share of European leveraged loan distressed exchanges (left panel) and in-court restructurings (right panel) in each year that defaulted again within three years   
![](images/1beb5c1af4dca9c3f60a9b40fdf910f052f2c9b5738b46803a1a6ec095947754.jpg)  
Note: As of April 2026 (most recent as of May 14, 2026).   
Source: Moody's, GS Global Investment Research

The rise of repeat default activity has coincided somewhat with a broader aggregate decline in recovery values in the USD market (in Europe, where the data is more sparse, we have not observed a similar trend). Exhibit 9 tracks the 12-month trailing recovery rate for US senior unsecured bonds vs. $1^{\text{st}}$ lien loans over the past 20 years. While the acceleration in repeat defaults is likely one contributing factor to this erosion in average recovery values, we would also point to two other drivers.

First, the proliferation of ‘loan-only’ capital structures has reduced the subordination cushion that HY bonds used to provide in ‘mixed’ capital structures that had both loans and bonds outstanding. We estimate that over 70% of loans are now issued by loan-only capital structures, up from just 45% in 

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
