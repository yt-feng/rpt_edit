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
# Japan Electronic Components/Semiconductors: NVDA results read-across: bullish on Ibiden, Murata, Yuden, Renesas, MARUWA

On May 21 (early morning JST), NVIDIA (NVDA, covered by US

Semiconductor/Semiconductor Equipment analyst James Schneider, Ph.D.) announced its 1QFY27 (February-April) results. Revenue of US\$81.6 bn (+20% qoq) beat GSe of US\$80.0 bn, the Bloomberg consensus of US\$78.9 bn, and the midpoint of guidance of US\$78.0 bn. NVDA guided for 2Q (May-July) revenue of US\$91.0 bn at the midpoint (GSe US\$87.7 bn, Bloomberg consensus US\$86.3 bn), assuming revenue growth for the 15th consecutive quarter. The company assumes revenue growth will be primarily driven by Data Center. Vera Rubin is progressing to production shipment in 2H of this year (from 3Q). The company expressed confidence in its plan for US\$1 tn in sales for Blackwell and Rubin from CY25 to CY27. The company also noted that it has visibility on nearly US\$20 bn in stand-alone CPU sales this year and commented that the Vera CPU will open up a new US\$200 bn market for the company. NVDA's share price was down around -1.2% in after-hours trading (as of 18:00 local time).

Overall, we believe NVDA's results and guidance confirm robust fundamentals, with generally positive implications for the Asian supply chain related to AI servers. For our Japan Electronics Components/Semiconductors coverage, we highlight four takeaways. (1) Ibiden (Buy): At its full-year results briefing, the company disclosed a medium-term plan for its electronics business of ¥330.0 bn in sales (23% OPM) for FY3/27, ¥460.0 bn (29% OPM) for FY3/28, and ¥800.0 bn (35% OPM) for FY3/31, versus sales of ¥243.3 bn (19% OPM) for FY3/26. The company also commented that further increases in capacity are needed to meet demand. We expect strong demand and improved profitability heading into 2030. (2) Murata

Mfg (Buy, on CL)/Taiyo Yuden (Buy): At its full-year results briefing, Murata raised its demand volume outlook for MLCCs for AI servers to a CAGR of +80% from +30% previously, and also announced it would add capacity with an additional investment of ¥80.0 bn. Capacity is set to be increased by +20-25% in FY3/28 (vs. the previous pace of +10%), and we believe the company will fully benefit from the expansion of the highly profitable market for MLCCs for AI servers. Meanwhile, Taiyo Yuden also assumes its sales to AI servers will grow +80% yoy in FY3/27. (3) Renesas

Electronics (Buy): In addition to NVDA-related PMICs (1/3-1/2 share), ASIC-related PMICs are expanding rapidly, and the company sees AI-related revenue doubling yoy.

The company is supply-constrained, and in addition to initiatives to resolve bottlenecks, it has also decided to enhance its in-house production capacity, centered on DC/AI. (4) MARUWA (Buy): The new plant, which is expected to produce mainly for AI applications, is forecast to contribute to earnings from 2H of

Daiki Takayama

+81(3)4587-9870

daiki.takayama@gs.com

GS Japan Co., Ltd.

Mitsuhiro Icho

+81(3)4587-9836

mitsuhiro.x.icho@gs.com

GS Japan Co., Ltd.

Makoto Takahara

+81(3)4587-4270

makoto.takahara@gs.com

GS Japan Co., Ltd.

Yuji Hidaka

+81(3)4587-3656 | yuji.hidaka@gs.com

GS Japan Co., Ltd.

this fiscal year. We assume rapid growth in sales for this application, with the company-specific factor of capacity expansion contributing on top of market growth (GSe: more than double yoy).

# Price Target Risks and Methodologies

# Price Target Risks and Methodology - Ibiden

Valuation methodology: We are Buy rated on Ibiden with a 12-month price target of ¥9,600. Our target price is based on FY3/28E EV/GCI vs. CROCI/WACC, applying a 50% premium to the sector average EV/DACF multiple of 8X (our target price implies FY3/28E P/E of 30.4X).

Key risks include road map changes of main customers, weaker PC and server demand, and a reduction in diesel vehicle sales.

# Price Target Risks and Methodology - Murata Mfg.

Valuation methodology: We are Buy rated on Murata Mfg. with a 12-month price target of ¥5,400. Our target price is based on FY3/28E EV/GCI vs. CROCI/WACC, applying a 50% premium to our sector multiple of 8X (implies FY3/27E P/E of 23X).

Key risks: Decline in smartphone production volume, deterioration in MLCC supply/demand, and yen appreciation.

# Price Target Risks and Methodology - Taiyo Yuden

Valuation methodology: We are Buy rated on Taiyo Yuden with a 12-month price target of ¥7,100. Our target price is based on FY3/28E EV/GCI vs. CROCI/WACC, applying a 30% premium to our sector multiple of 8X (our TP implies FY3/28E P/E of 22X).

Key risks: Weaker-than-expected smartphone demand, deterioration in MLCC supply/demand, and yen appreciation.

# Price Target Risks and Methodology - Renesas Electronics

We are Buy rated on Renesas. Our 12-month target price of ¥3,800 is based on FY12/27E EV/GCI vs. CROCI/WACC, applying an EV/DACF multiple of 12X (50% premium to the sector average, implying a FY12/26E target P/E of 14X). Key risks include a slowdown or delayed recovery in consumer electronics-related demand, stagnant automobile production, protracted reduction in semiconductor inventories, delayed recovery for industrial equipment applications, and yen appreciation.

# Price Target Risks and Methodology - MARUWA

We are Buy rated on MARUWA. Our 12-month target price is ¥70,000 (implies FY27 P/E of 23x). Our target price is based on FY27E EBITDA, and we derive the applied multiple of 12.1x from the historical correlation between the EBITDA margin and the EV/EBITDA multiple. Key risks include lower investment in applications that support final demand (including AI/general-purpose servers, xEV, SPE), lower demand for end products due to supply chain disruptions and inventory adjustments, and the emergence of alternative technology.

# Disclosure Appendix

# Reg AC

We, Daiki Takayama, Mitsuhiro Icho, Makoto Takahara and Yuji Hidaka, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Daiki Takayama GS Japan Co., Ltd., Mitsuhiro Icho GS Japan Co., Ltd., Makoto Takahara GS Japan Co., Ltd., Yuji Hidaka GS Japan Co., Ltd..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

# GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

# M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

# Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

# Disclosures

The rating(s) for Ibiden, MARUWA, Murata Mfg., Renesas Electronics and Taiyo Yuden is/are relative to the other companies in its/their coverage universe: Alps Alpine, Dai Nippon Printing, Hirose Electric, IRISO Electronics, Ibiden, Japan Aviation Electronics Industry, Kohoku Kogyo, Kyocera, MARUWA, Mabuchi Motor, Maxell Ltd., MinebeaMitsumi Inc., Murata Mfg., NGK Corp., Nichicon, Nidec, Nippon Ceramic, Niterra, Nitto Denko, Renesas Electronics, Rohm, TDK, TOPPAN Holdings, Taiyo Yuden

# Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Ibiden (¥15,640), MARUWA (¥67,630), Renesas Electronics (¥3,500) and Taiyo Yuden (¥7,861)

GS has received compensation for investment banking services in the past 12 months: Murata Mfg. (¥6,164) and Renesas Electronics (¥3,500)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Ibiden (¥15,640), Murata Mfg. (¥6,164), Renesas Electronics (¥3,500) and Taiyo Yuden (¥7,861)

GS has received compensation for non-investment banking services during the past 12 months: Murata Mfg. (¥6,164)

GS had an investment banking services client relationship during the past 12 months with: Ibiden (¥15,640), Murata Mfg. (¥6,164), Renesas Electronics (¥3,500) and Taiyo Yuden (¥7,861)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Murata Mfg. (¥6,164) and Renesas Electronics (¥3,500)

GS had a non-securities services client relationship during the past 12 months with: Ibiden (¥15,640) and Renesas Electronics (¥3,500)

# Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td></tr></table>

<table><tr><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)   
![](images/8dd50bf9a8eaf81d290d1f959656c77ccb833af4271a2750f5b02a6360a633dd.jpg)  
Source: GS Investment Research for ratings and price targets; FactSet closing prices as of 3/31/2026.   
Rating   
Covered by Daiki Takayama   
Price target   
✗ Price target at removal — Not covered by current analyst   
TOPIX   
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/5e4151ed40df652834182607701e98c1281c889d9d6db02c2d6a03846686f26b.jpg)  
Source: GS Investment Research for ratings and price targets; FactSet closing prices as of 3/31/2026.   
Rating   
Covered by Daiki Takayama   
Price target   
\* Price target at removal    - - Not covered by current analyst   
TOPIX   
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/9dea23cc365d8fdf6dea20f5b8276c5fa8bd53deb39f9ef2147a7b2c76eefdb2.jpg)

<details>
<summary>line</summary>

| Date       | Stock Price | Index Price | Rating     | Target     |
|------------|-------------|-------------|------------|------------|
| 2023 M     | 2100        | 2200        |            | 2100       |
| 2023 J     | 3300        | 3300        |            | 3300       |
| 2023 A     | 3000        | 3000        |            | 3000       |
| 2023 S     | 2900        | 2900        |            | 2900       |
| 2023 O     | 3300        | 3300        |            | 3300       |
| 2023 N     | 3400        | 3400        |            | 3400       |
| 2023 D     | 3800        | 3800        |            | 3800       |
| 2024 J     | 3400        | 3400        |            | 3400       |
| 2024 A     | 2900        | 2900        |            | 2900       |
| 2024 S     | 2600        | 2600        |            | 2600       |
| 2024 O     | 2700        | 2700        |            | 2700       |
| 2024 N     | 2900        | 2900        |            | 2900       |
| 2024 D     | 2500        | 2500        |            | 2500       |
| 2025 J     | 2900        | 2900        |            | 2900       |
| 2025 A     | 3300        | 3300        |            | 3300       |
| 2025 M     | 3600        | 3600        |            | 3600       |
| 2026 J     |             |             |            |            |
| 2026 F     |             |             |            |            |
| 2026 M     |             |             |            |            |
| 2026 B     |             |             |            |            |
| 2026 A     |             |             |            |            |
| 2026 S     |             |             |            |            |
| 2026 O     |             |             |            |            |
| 2026 N     |             |             |            |            |
| 2026 D     |             |             |            |            |
| 2026 J     |             |             |            |            |
| 2026 F     |             |             |            |            |
| 2026 M     |             |             |            |            |
| 2026 B     |             |             |            |            |
| Source: GS Investment Research for ratings and price targets; FactSet closing prices as of 3/31/2026.
TOPIX
</details>

The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/07487c5de6de6636133f8d46b7b0c4f6060e0adc1fc872b78114ad53f697051d.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/054d5f2b62bbb5720af10d11df3cb789844aa472badc4a649b4cef92741a08b9.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

Target price history table(s)   
Taiyo Yuden (6976.T) 

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>08-May-26</td><td>7,100</td><td>6,663</td></tr><tr><td>23-Mar-26</td><td>4,900</td><td>3,926</td></tr><tr><td>12-Jan-26</td><td>4,300</td><td>3,405</td></tr><tr><td>02-Oct-25</td><td>3,800</td><td>3,382</td></tr><tr><td>05-Aug-25</td><td>3,200</td><td>2,841</td></tr><tr><td>07-Jul-25</td><td>3,100</td><td>2,488</td></tr><tr><td>09-May-25</td><td>3,200</td><td>2,202</td></tr><tr><td>31-Mar-25</td><td>3,400</td><td>2,467</td></tr><tr><td>07-Nov-24</td><td>3,600</td><td>2,781</td></tr><tr><td>01-Oct-24</td><td>4,100</td><td>3,081</td></tr><tr><td>02-Jul-24</td><td>4,800</td><td>4,105</td></tr><tr><td>08-May-24</td><td>4,000</td><td>3,643</td></tr><tr><td>07-Feb-24</td><td>4,100</td><td>3,431</td></tr><tr><td>06-Dec-23</td><td>4,500</td><td>3,627</td></tr><tr><td>07-Nov-23</td><td>4,400</td><td>3,695</td></tr><tr><td>04-Oct-23</td><td>4,800</td><td>3,963</td></tr><tr><td>03-Aug-23</td><td>4,900</td><td>4,164</td></tr><tr><td>04-Jul-23</td><td>5,000</td><td>4,330</td></tr></table>

Renesas Electronics

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
