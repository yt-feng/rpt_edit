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
# Japan Shipbuilding: Nikkei reports Imabari/KHI/Namura to resume LNG carrier construction; potential to capture stable medium to LT demand

On June 15, the Nikkei reported that Imabari Shipbuilding (private), Kawasaki Heavy Industries, and Namura Shipbuilding will jointly resume construction of LNG carriers (link). The main details and implications are as follows:

Details of the article: Imabari Shipbuilding, Kawasaki Heavy Industries, and Namura Shipbuilding to jointly resume the construction of LNG carriers around 2035. Per the article, the companies will share their LNG carrier design technologies and the welders involved in the construction. The leading proposal is to utilize Kawasaki Heavy Industries' Sakaide Works as the production base. They aim to build three to five vessels annually. Around 100 vessels are currently in operation to supply LNG to Japan, and assuming they are replaced every 20 years, building five vessels a year could secure the capacity needed for LNG imports, all else equal. The article also notes that the Japanese government will consider supporting this by providing introduction subsidies to shipowners with plans to include these details in the “Public-Private Investment Roadmap” to be formulated in June 2026.

Implications for the Japan shipbuilding industry and our coverage: In the Japanese shipbuilding industry, the construction of LNG carriers has not taken place since the last delivery in 2019, as companies withdrew due to low-price offensives by Chinese and South Korean competitors. The current unit price for a 170,000 cubic meter class LNG carrier is around US\$250 mn (¥40 bn based on a forex rate of ¥160/US\$). If three to five vessels are built annually as the article states, this could generate stable replacement demand of ¥120 bn-¥200 bn annually for the Japanese shipbuilding industry (we estimate the market size for the Japanese shipbuilding industry, limited to commercial vessels, to be around ¥1.3 tn-¥1.5 tn as of FY2025). If confirmed, for our coverage companies, Namura Shipbuilding (Buy) and Kawasaki Heavy Industries (Neutral), we would view the development positively as it provides scope for the companies to capture stable medium- to long-term demand. However, for Kawasaki Heavy Industries, the product mix would likely need to be closely examined for potential margin implications. We also think the development could be positive for Mitsui E&S (Buy), which provides marine engines for domestic shipbuilders.

Norihiro Miyazaki

+81(3)4587-9842

norihiro.miyazaki@gs.com

GS Japan Co., Ltd.

Yuichiro Isayama

+81(3)4587-9806

yuichiro.isayama@gs.com

GS Japan Co., Ltd.

Ryohei Kurita

+81(3)4587-1799

ryohei.kurita@gs.com

GS Japan Co., Ltd.

Takato Enoki

+81(3)4587-1739

takato.enoki@gs.com

GS Japan Co., Ltd.

## Price Target Risks and Methodology - Kawasaki Heavy Industries (7012.T)

Our 12-month target price of ¥3,900 is based on a FY3/28E EV/EBITDA, applying the Japan Aerospace & Defense subsector-average multiple of 14X and a 20% sector-relative discount.

The key upside and downside risks include (1) yen depreciation/appreciation relative to our assumed exchange rate, (2) faster-/slower-than-expected expansion of defense order and revenue momentum, (3) lower-/higher-than-expected cost variability in PS&E, particularly promotional expenses in the North American four-wheeler business, and (4) faster-/slower-than-expected progress on portfolio restructuring and the turnaround of low-profitability segments, with implications for the conglomerate discount.

## Price Target Risks and Methodology - Namura Shipbuilding Co.

Our 12-month target price of ¥5,600 is based on a target P/B of 2.6X applied to our end-FY3/30E BPS estimate, discounted back to FY3/27E using a cost of equity of 9.8%.

Key risks include a sudden increase in production capacity in the shipbuilding industry, higher steel prices, production problems, and a decline in vessel prices.

## Disclosure Appendix

## Reg AC

We, Norihiro Miyazaki, Yuichiro Isayama, Ryohei Kurita and Takato Enoki, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Norihiro Miyazaki GS Japan Co., Ltd., Yuichiro Isayama GS Japan Co., Ltd., Ryohei Kurita GS Japan Co., Ltd., Takato Enoki GS Japan Co., Ltd..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

## Rating and pricing information

Mitsui E&S Co. (Buy, ¥4,157)

The rating(s) for Namura Shipbuilding Co. is/are relative to the other companies in its/their coverage universe: ANYCOLOR, Cover Corp., Japan Airport Terminal, Kotobuki Spirits Co., Kyoritsu Maintenance, Mitsui E&S Co., Namura Shipbuilding Co., Rakus Co., Sansan Inc., Visional, giftee Inc.

The rating(s) for Kawasaki Heavy Industries is/are relative to the other companies in its/their coverage universe: AeroEdge, CKD, Daifuku, Daikin Industries, Fanuc, Harmonic Drive Systems, Hoshizaki, IHI, Japan Steel Works, Kawasaki Heavy Industries, Keyence, Makita, Misumi Group, Mitsubishi Heavy Industries, Okuma, Omron, SKY Perfect JSAT Corp, SMC, THK, Yaskawa Electric

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Kawasaki Heavy Industries (¥2,834)

GS beneficially owned 5% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Namura Shipbuilding Co. (¥3,545)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Kawasaki Heavy Industries (¥2,834)

GS had an investment banking services client relationship during the past 12 months with: Kawasaki Heavy Industries (¥2,834)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Kawasaki Heavy Industries (¥2,834)

GS had a non-securities services client relationship during the past 12 months with: Kawasaki Heavy Industries (¥2,834)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td></tr></table>

<table><tr><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/3adb0820034182b2a8168c4deb222cfb16928c00efc85bed66408bc0d315c77c.jpg)

<details>
<summary>line chart</summary>

| Date       | Stock Price | Rating | Target Price |
|------------|-------------|--------|--------------|
| Sep 12     | NA          | B      | 2800         |
| Jun 2024   | NA          | B      | 2200         |
| May 2025   | NA          | B      | 2000         |
| Apr 2025   | NA          | B      | 2200         |
| Mar 2025   | NA          | B      | 2000         |
| Feb 2025   | NA          | B      | 3000         |
| Jan 2025   | NA          | B      | 3400         |
| Dec 2025   | NA          | B      | 4000         |
| Nov 2025   | NA          | B      | 3400         |
| Oct 2025   | NA          | B      | 3000         |
| Sep 2025   | NA          | B      | 2800         |
| Aug 2025   | NA          | B      | 2600         |
| Jul 2025   | NA          | B      | 2400         |
| Jun 2025   | NA          | B      | 2200         |
| May 2025   | NA          | B      | 2000         |
| Apr 2025   | NA          | B      | 1800         |
| Mar 2025   | NA          | B      | 1600         |
| Feb 2025   | NA          | B      | 1400         |
| Jan 2025   | NA          | B      | 1200         |
| Dec 2025   | NA          | B      | 1000         |
| Jan 2026   | NA          | B      | 800          |
| Feb 2026   | NA          | B      | 600          |
| Mar 2026   | NA          | B      | 400          |
| Apr 2026   | NA          | B      | 200          |
| May 2026   | NA          | B      | 100          |
| Jun 2026   | NA          | B      | 50           |
| Jul 2026   | NA          | B      | 25           |
| Aug 2026   | NA          | B      | 15           |
| Sep 2026   | NA          | B      | 10           |
| Oct 2026   | NA          | B      | 5            |
| Nov 2026   | NA          | B      | 2            |
| Dec 2026   | NA          | B      | 1            |
| Jan 2027   | NA          | B      | 1            |
| Feb 2027   | NA          | B      | 1            |
| Mar 2027   | NA          | B      | 1            |
| Apr 2027   | NA          | B      | 1            |
| May 2027   | NA          | B      | 1            |
| Jun 2027   | NA          | B      | 1            |
| Jul 2027   | NA          | B      | 1            |
| Aug 2027   | NA          | B      | 1            |
| Sep 2027   | NA          | B      | 1            |
| Oct 2027   | NA          | B      | 1            |
| Nov 2027   | NA          | B      | 1            |
| Dec 2027   | NA          | B      | 1            |
| Jan 2028   | NA          | B      | 1            |
| Feb 2028   | NA          | B      | 1            |
| Mar 2028   | NA          | B      | 1            |
| Apr 2028   | NA          | B      | 1            |
| May 2028   | NA          | B      | 1            |
| Jun 2028   | NA          | B      | 1            |
| Jul 2028   | NA          | B      | 1            |
| Aug 2028   | NA          | B      | 1            |
| Sep 2028   | NA          | B      | 1            |
| Oct 2028   | NA          | B      | 1            |
| Nov 2028   | NA          | B      | 1            |
| Dec 2028   | NA          | B      | 1            |
| Jan 2029   | NA          | B      | 1            |
| Feb 2029   | NA          | B      | 1            |
| Mar 2029   | NA          | B      | 1            |
| Apr 2029   | NA          | B      | 1            |
| May 2029   | NA          | B      | 1            |
| Jun 2029   | NA          | B      | 1            |
| Jul 2029   | NA          | B      | 1            |
| Aug 2029   | NA          | B      | 1            |
| Sep 2029   | NA          | B      | 1            |
| Oct 2029   | NA          | B      | 1            |
| Nov 2029   | NA          | B      | 1            |
| Dec 2029   | NA          | B      | 1            |
| Jan 21    | NA          | B      | 1            |
| Feb 21    | NA          | B      | 1            |
| Mar 21    | NA          | B      | 1            |
| Apr 21    | NA          | B      | 1            |
| May 21    | NA          | B      | 1            |
| Jun 21    | NA          | B      | 1            |
| Jul 21    | NA          | B      | 1            |
| Aug 21    | NA          | B      | 1            |
| Sep 21    | NA          | B      | 1            |
| Oct 21    | NA          | B      | 1            |
| Nov 21    | NA          | B      | 1            |
| Dec 21    | NA          | B      | 1            |
| Jan 22    | NA          | B      | 1            |
| Feb 22    | NA          | B      | 1            |
| Mar 22    | NA          | B      | 1            |
| Apr 22    | NA          | B      | 1            |
| May 22    | NA          | B      | 1            |
| Jun 22    | NA          | B      | 1            |
| Jul 22    | NA          | B      | 1            |
| Aug 22    | NA          | B      | 1            |
| Sep 22    | NA          | B      | 1            |
| Oct 22    | NA          | B      | 1            |
| Nov 22    | NA          | B      | 1            |
| Dec 22    | NA          | B      | 1            |
| Jan     (Dec)|
| Feb     (Dec)|
| Mar     (Dec)|
| Apr     (Dec)|
| May     (Dec)|
| Jun     (Dec)|
| Jul     (Dec)|
| Aug     (Dec)|
| Sep     (Dec)|
| Oct     (Dec)|
| Nov     (Dec)|
| Dec     (Dec)|
| Jan     (Mar)|<chart_precise>
</details>

Source: GS Investment Research for ratings and price targets; FactSet closing prices as of 3/31/2026.
□ Rating
■ Price target
✗ Price target at removal
— TOPIX
Covered by Yuichiro Isayama, as of Sep 12, 2024
Not covered by current analyst  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/61f3d54bf025cfc6385241b50459ac973e0bf9b16d0a6744f08c7d40de81cd2f.jpg)

<details>
<summary>line chart</summary>

| Date       | Stock Price | Index Price |
|------------|-------------|-------------|
| Jun 24     | 3,750       | 6,000       |
| Jun 24     | 3,700       | 5,600       |
</details>

Source: GS Investment Research for ratings and price targets; FactSet closing prices as of 3/31/2026.
□ Rating — Covered by Norihiro Miyazaki, as of Jun 24, 2025
■ Price target
× Price target at removal \*\* Not covered by current analyst
— TOPIX  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

Target price history table(s)  
Namura Shipbuilding Co. (7014.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>16-Dec-25</td><td>5,600</td><td>3,645</td></tr><tr><td>27-Oct-25</td><td>6,000</td><td>5,390</td></tr><tr><td>07-Aug-25</td><td>3,750</td><td>3,340</td></tr><tr><td>24-Jun-25</td><td>3,700</td><td>2,708</td></tr></table>

Kawasaki Heavy Industries (7012.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>03-Apr-26</td><td>3,900</td><td>3,161</td></tr><tr><td>06-Mar-26</td><td>20,000</td><td>3,268</td></tr><tr><td>09-Feb-26</td><td>17,000</td><td>3,391</td></tr><tr><td>10-Oct-25</td><td>15,000</td><td>1,945</td></tr><tr><td>18-Jun-25</td><td>14,000</td><td>2,137

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
