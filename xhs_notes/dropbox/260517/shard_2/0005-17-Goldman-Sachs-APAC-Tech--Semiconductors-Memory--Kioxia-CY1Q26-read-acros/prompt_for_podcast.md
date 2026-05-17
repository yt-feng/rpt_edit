你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# APAC Tech: Semiconductors Memory: Kioxia CY1Q26 read-across; strong guidance likely implies NAND ASP/OPM upside; Buy SEC/Hynix

On May 15, Japanese NAND producer Kioxia (covered by Shuhei Nakamura, Neutral, most recent close: ¥44,450) reported its CY1Q26 (FY4Q25 or March quarter) earnings, and we provide read-across to our covered Korean memory suppliers, SK Hynix (Hynix, Buy - most recent close: W1,819,000) and Samsung Electronics (SEC, Buy - most recent close: W270,500). Key takeaways include: 1) Stronger ASP growth and higher NAND OPM for SEC/Hynix likely implied from CY2Q26 guidance, 2) Maintains bullish market outlook, expecting supply tightness to continue in 2027, and 3) Potential ADR listing of Kioxia could be positive for Hynix sentiment.

■ Stronger ASP growth and higher NAND OPM for SEC/Hynix likely implied from CY2Q26 guidance: In CY1Q26, Kioxia USD-based blended ASP more than doubled with like-for-like pricing movement similar to blended ASP, while bit shipment decreased 10% qoq due to equipment maintenance and sale of inventory in CY4Q25. At the same time, data center SSD bits still increased qoq. Kioxia provided USD-based revenue growth guidance of 70% qoq for CY2Q26 and commented bit shipment will increase although its impact would be marginal, implying ASP increase will be the primary driver of high revenue growth. Given that ASP is expected to drive the bulk of the 70% growth projected for CY2Q26, we believe this signals higher potential for further upside in our SEC and Hynix NAND ASP growth which are currently forecasted at +55% qoq and +45% qoq respectively. In addition, Kioxia's CY2Q26 operating margin guidance of 74% also suggests that our current NAND OPM forecast for the Korean companies at around 60% may be too conservative (given the OPM were similar for all three companies in CY1Q26).

\- Maintains bullish market outlook, expecting supply tightness to continue in 2027: Kioxia maintained its bullish stance on the NAND market outlook. The company commented that 1) NAND market will be very tight for both 2026 and 2027 which is in line with Samsung's comments on tighter supply in 2027 mentioned during 1Q26 conference call, 2) NAND market bit growth is expected to be in the high-teens % for CY2026 and undersupply expected to continue in CY2027, 3) NAND will continue to grow at a mid-to-long term CAGR of $20\%$ (same as previous guidance), and 4) demand for NAND is increasing in all applications but primarily driven by increasing demand for AI data centers and enterprise.

# Giuni Lee

+82(2)3788-1177 | giuni.lee@gs.com

GS (Asia) L.L.C., Seoul

Branch

# Daiki Takayama

+81(3)4587-9870

daiki.takayama@gs.com

GS Japan Co., Ltd.

# Taeyong Lee

+82(2)3788-0981|taeyong.lee@gs.com

GS (Asia) L.L.C., Seoul

Branch

■ Potential ADR listing of Kioxia could be positive for Hynix sentiment: Kioxia announced that it is preparing an ADR listing to grow its investor base and increase its corporate value. Further details haven't been disclosed. The potential listing for Kioxia could be positive for Hynix sentiment given the company owns a meaningful stake in Kioxia through a consortium.

Exhibit 1: SEC/Hynix/Kioxia NAND key metrics trend 

<table><tr><td colspan="2">(%)</td><td>CY1Q24</td><td>CY2Q24</td><td>CY3Q24</td><td>CY4Q24</td><td>CY1Q25</td><td>CY2Q25</td><td>CY3Q25</td><td>CY4Q25</td><td>CY1Q26</td><td>CY2Q26E</td></tr><tr><td rowspan="3">ASP qoq% (in USD)</td><td>SEC NAND</td><td>31%</td><td>22%</td><td>7%</td><td>-6%</td><td>-15%</td><td>-5%</td><td>5%</td><td>24%</td><td>89%</td><td>55%</td></tr><tr><td>Hynix NAND</td><td>30%</td><td>17%</td><td>15%</td><td>-4%</td><td>-20%</td><td>-9%</td><td>11%</td><td>31%</td><td>71%</td><td>45%</td></tr><tr><td>Kioxia</td><td>around 20%</td><td>mid-teens%</td><td>MSD%</td><td>-LSD%</td><td>-20%</td><td>HSD%</td><td>-LSD%</td><td>+low-teens%</td><td>100%+</td><td></td></tr><tr><td rowspan="3">Bit shipment qoq%</td><td>SEC NAND</td><td>-3%</td><td>-5%</td><td>-7%</td><td>-3%</td><td>-10%</td><td>27%</td><td>10%</td><td>-10%</td><td>8%</td><td>1%</td></tr><tr><td>Hynix NAND</td><td>0%</td><td>-2%</td><td>-15%</td><td>-4%</td><td>-17%</td><td>71%</td><td>-4%</td><td>10%</td><td>-13%</td><td>14%</td></tr><tr><td>Kioxia</td><td>+HSD%</td><td>+low-teens%</td><td>+10%</td><td>-LSD%</td><td>-10%</td><td>flat</td><td>+high-30%</td><td>+MSD%</td><td>-10%</td><td></td></tr><tr><td rowspan="3">Revenue qoq% (in USD)</td><td>SEC NAND</td><td>27%</td><td>16%</td><td>0%</td><td>-9%</td><td>-23%</td><td>21%</td><td>15%</td><td>11%</td><td>104%</td><td>57%</td></tr><tr><td>Hynix NAND</td><td>30%</td><td>14%</td><td>-3%</td><td>-8%</td><td>-34%</td><td>55%</td><td>7%</td><td>44%</td><td>48%</td><td>65%</td></tr><tr><td>Kioxia</td><td>22%</td><td>27%</td><td>14%</td><td>-4%</td><td>-25%</td><td>5%</td><td>29%</td><td>17%</td><td>82%</td><td>70%</td></tr><tr><td rowspan="3">OPM%</td><td>SEC NAND</td><td>11%</td><td>23%</td><td>13%</td><td>3%</td><td>-2%</td><td>-5%</td><td>9%</td><td>25%</td><td>58%</td><td>62%</td></tr><tr><td>Hynix NAND</td><td>6%</td><td>15%</td><td>20%</td><td>13%</td><td>2%</td><td>-1%</td><td>7%</td><td>30%</td><td>57%</td><td>59%</td></tr><tr><td>Kioxia</td><td>14%</td><td>29%</td><td>35%</td><td>27%</td><td>11%</td><td>13%</td><td>19%</td><td>27%</td><td>60%</td><td>74%</td></tr></table>

Kioxia CY2Q26E is based on the company's guidance   
Source: Company data, GS Global Investment Research

# Price Target Risks and Methodology - SK Hynix Inc.

Valuation methodology: Our 2026E/27E avg. P/B-based 12m TP is W1,800,000, applying a target P/B multiple of 2.9X.

Key risks: Key risks include 1) major deterioration in memory supply/demand and delay in technology migration, 2) weaker demand for smartphones/PCs/servers which would impact overall conventional memory demand, 3) Samsung's positive HBM business progress which would impact HBM revenue and profit, 4) lower AI-related capex which would impact overall HBM demand, and thus HBM revenue/profit for the company.

# Price Target Risks and Methodology - Samsung Electronics

Valuation methodology: Our 12m 2026E EV/EBITDA-based SOTP target price for the common share is W320,000. Our 12-month target price for the preference share is W245,000, which is based on our target pref to common shares discount of $23\%$ , derived from averaging: 1) the pref discount of the 2-factor model and 2) the average preference share discount to common shares during the past 1 month. We are Buy rated on both the common and preference shares.

Key downside risks: 1) major deterioration in memory supply/demand, 2) sharp contraction in smartphone margins, and 3) mobile OLED market share loss.

# Disclosure Appendix

# Reg AC

We, Giuni Lee, Daiki Takayama and Taeyong Lee, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Giuni Lee GS (Asia) L.L.C., Seoul Branch, Daiki Takayama GS Japan Co., Ltd., Taeyong Lee GS (Asia) L.L.C., Seoul Branch.

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

The rating(s) for SK Hynix Inc., Samsung Electronics and Samsung Electronics (Pref) is/are relative to the other companies in its/their coverage universe: Hansol Chemical, LG Display, LG Electronics, LG Innotek Co., SK Hynix Inc., SKC, Samsung Electro-Mechanics, Samsung Electronics, Samsung Electronics (Pref)

The rating(s) for Kioxia Holdings is/are relative to the other companies in its/their coverage universe: Advantest, DISCO, Ebara, HOYA, JEOL, Kioxia Holdings, Kokusai Electric, Lasertec, SCREEN Holdings, Tokyo Electron, Tokyo Seimitsu, Ulvac

# Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Kioxia Holdings (¥44,450)

GS has received compensation for investment banking services in the past 12 months: Kioxia Holdings (¥44,450), Samsung Electronics (W270,500) and Samsung Electronics (Pref) (W179,400)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Kioxia Holdings (¥44,450), Samsung Electronics (W270,500), Samsung Electronics (Pref) (W179,400) and SK Hynix Inc. (W1,819,000)

GS had an investment banking services client relationship during the past 12 months with: Kioxia Holdings (¥44,450), Samsung Electronics (W270,500), Samsung Electronics (Pref) (W179,400) and SK Hynix Inc. (W1,819,000)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Samsung Electronics (W270,500) and Samsung Electronics (Pref) (W179,400)

GS had a non-securities services client relationship during the past 12 months with: Samsung Electronics (W270,500), Samsung Electronics (Pref) (W179,400) and SK Hynix Inc. (W1,819,000)

GS has managed or co-managed a public or Rule 144A offering in the past 12 months: Kioxia Holdings (¥44,450)

# Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)   
![](images/a769da1110272bc42095f715bbd491de5ce463e117d4073166d7d7b14b02a784.jpg)

<details>
<summary>line</summary>

| Date       | Stock Price | Index Price | Rating     | Price Target |
|------------|-------------|-------------|------------|--------------|
| Mar 2023   | 155000      | 2,000       |            |              |
| Jun 2023   | 160000      | 2,500       |            |              |
| Sep 2023   | 170000      | 3,000       |            |              |
| Dec 2023   | 180000      | 3,500       |            |              |
| Feb 2024   | 185000      | 4,000       |            |              |
| May 2024   | 210000      | 4,500       |            |              |
| Aug 2024   | 255000      | 5,000       |            |              |
| Nov 2024   | 290000      | 5,500       |            |              |
| Dec 2024   | 280000      | 6,000       |            |              |
| Feb 2025   | 285000      | 6,500       |            |              |
| May 2025   | 290000      | 7,000       |            |              |
| Aug 2025   | 310000      | 7,500       |            |              |
| Oct 2025   | 300000      | 8,000       |            |              |
| Dec 2025   | 70000       | 8,500       |            |              |
| Feb 2026   | 135000      | 9,500       |            |              |
| Apr 2026   | 120000      | 1.3M        |            |              |
| Jun 2026   |             |             |            |              |
| Aug 2026   |             |             |            |              |
| Oct 2026   |             |             |            |              |
| Dec 2026   |             |             |            |              |
Source: GS Investment Research for ratings and price targets; FactSet closing prices as of 3/31/2026.
</details>

The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/64f5e637c0c67726374c5d4012cdc60e21827d8b6649911f6939d65e803785f0.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/81ca89cc9f5c4dc05bcf96a2d20a78e3dc6cfc4ad354a016b3f78ee36d7a0731.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/2ec2f46e121223cfc6b74dd5f018f7050218cd24c01b5d9340d91ffb28d18c8a.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

# Target price history table(s)

Samsung Electronics (Pref) (005935.KS) 

<table><tr><td>Date of report</td><td>Target price (W)</td><td>Closing price (W)</td></tr><tr><td>30-Apr-26</td><td>245,000</td><td>158,300</td></tr><tr><td>07-Apr-26</td><td>220,000</td><td>130,900</td></tr><tr><td>11-Mar-26</td><td>200,000</td><td>138,900</td></tr><tr><td>29-Jan-26</td><td>159,000</td><td>115,600</td></tr><tr><td>08-Jan-26</td><td>142,000</td><td>101,900</td></tr><tr><td>16-Dec-25</td><td>110,000</td><td>79,800</td></tr><tr><td>30-Oct-25</td><td>99,000</td><td>82,500</td></tr><tr><td>14-Oct-25</td><td>89,000</td><td>72,300</td></tr><tr><td>22-Sep-25</td><td>78,000</td><td>66,700</td></tr><tr><td>31-Jul-25</td><td>69,000</td><td>57,600</td></tr><tr><td>01-May-25</td><td>61,000</td><td>46,850</td></tr></table>

Kioxia Holdings (285A.T) 

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>15-May-26</td><td>48,000</td><td>44,450</td></tr><tr><td>28-Apr-26</td><td>36,000</td><td>36,320</td></tr><tr><td>25-Mar-26</td><td>26,000</td><td>22,445</td></tr><tr><td>12-Feb-26</td><td>24,000</td><td>21,175</td></tr><tr><td>30-Jan-26</td><td>13,000</td><td>21,360</td></tr><tr><td>06-Jan-26</td><td>11,400</td><td>11,600</td></tr><tr><td>29-Oct-25</td><td>10,000</td><td>10,080</td></tr><tr><td>23-Sep-25</td><td>5,000</td><td>4,820</td></tr><tr><td>08-Aug-25</td><td>2,700</td><td>2,364</td></tr><tr><td>30-Jun-25</td><td>2,500</td><td>2,503</td></tr><tr><td>01-Jun-25</td><td>2,300</td><td>2,099</td></tr></table>

Samsung Electronics (Pref) (005935.KS)

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
