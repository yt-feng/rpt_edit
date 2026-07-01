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
# GS DRAM Sentiment Indicator: June 2026: Positive DDR5 pricing trends, while more constructive on 2027 HBM pricing

Our DRAM sentiment indicator for June 2026 is pointing in a moderately positive direction (same as April). Notable highlights include: 1) DDR5 pricing showing positive trend since May (+20% vs. 1 May price), 2) China smartphone shipment showed 2 consecutive months of yoy growth recording +19% yoy in May, and 3) Nanya Tech's monthly revenue (+730% yoy in May) continued 10 consecutive months of triple-digit yoy growth, and 4) investors' expectations for 2027 HBM pricing continues to rise, likely due to the expectations that the currently strong conventional DRAM pricing could be taken into account when discussing HBM pricing for next year.

Exhibit 1: GS DRAM Sentiment Indicator

<table><tr><td>Indicators</td><td>Period</td><td>Sequential change</td><td>yoy change</td><td>Direction</td><td>Previous</td></tr><tr><td>DRAM spot pricing trend (daily)</td><td>6/26/2026</td><td>0%</td><td>672%</td><td>↑↑↑</td><td>↑↑</td></tr><tr><td>Server ODM monthly revenue trend (monthly)</td><td>May</td><td>-3%</td><td>53%</td><td>↑↑↑</td><td>↑↑↑</td></tr><tr><td>Aspeed monthly revenue trend (monthly)</td><td>May</td><td>0%</td><td>69%</td><td>↑↑↑</td><td>↑↑↑</td></tr><tr><td>Korea monthly DRAM export revenue (monthly)</td><td>May</td><td>21%</td><td>370%</td><td>↑↑↑</td><td>↑↑↑</td></tr><tr><td>China smartphone shipment (monthly)</td><td>May</td><td>7%</td><td>19%</td><td>↑</td><td>↓</td></tr><tr><td>Nanya monthly revenue trend (monthly)</td><td>May</td><td>9%</td><td>730%</td><td>↑↑↑</td><td>↑↑↑</td></tr><tr><td>Supreme monthly revenue trend (monthly)</td><td>May</td><td>54%</td><td>253%</td><td>↑↑↑</td><td>↑↑↑</td></tr><tr><td>Second derivative of SEC DRAM ASP (quarterly)</td><td>2Q26E</td><td>-48%</td><td></td><td>↓↓↓</td><td>↓↓↓</td></tr><tr><td>GS view based on channel checks and feedback</td><td></td><td></td><td></td><td>↑↑</td><td>↑↑</td></tr><tr><td>Overall</td><td></td><td></td><td></td><td>↑↑</td><td>↑↑</td></tr></table>

Source: Company data, DRAMeXchange, TRASS, GS Global Investment Research

Giuni Lee
+82(2)3788-1177 | giuni.lee@gs.com
GS (Asia) L.L.C., Seoul Branch

Daiki Takayama
+81(3)4587-9870 |
daiki.takayama@gs.com
GS Japan Co., Ltd.

Taeyong Lee
+82(2)3788-0981 | taeyong.lee@gs.com
GS (Asia) L.L.C., Seoul Branch

## Details of data points

DRAM spot pricing: DDR4 pricing has been showing a moderate upward trend since early May (+11% vs. 1 May price) and is trading at a +45% premium over May contract pricing. DDR5 pricing has also demonstrated a positive trend for the same period (+20% vs. 1 May price) and is trading at a +25% premium over May contract pricing.

Server ODM and Aspeed revenue: May server ODM (Inventec, Quanta, Wiwynn, Wistron) monthly revenue rose +53% yoy on the back of rack-level AI servers shipment ramp up and strong growth in ASIC AI servers shipment, and Aspeed's monthly revenue also showed solid yoy growth (+69% yoy) despite the high base of +75% yoy in May 2025.

Korea DRAM export: May DRAM exports again reached a record high, beating the previous-high in March by 21% with +370% yoy thanks to rising memory price and solid demand from Big Tech firms in major export markets (U.S. and China).

China smartphones: China smartphone shipment showed 2 consecutive months of yoy growth recording +19% yoy in May. 2026 YTD shipment is nearly on par with 2025 numbers, and our China team expects 2Q26 shipment to decline by 14% yoy mainly due to rising memory prices dragging down end demand.

Nanya Tech revenue: Taiwanese DRAM supplier Nanya Tech's May revenue increased by $+730\%$ yoy, showing 10 consecutive months of triple-digit% yoy growth driven by strong DDR4 pricing growth.

Supreme Electronics revenue: Taiwanese distributor Supreme Electronics' May revenue increased +253% yoy and +54% mom.

Second derivative of SEC DRAM ASP: As our latest 2Q26E DRAM ASP estimate for SEC is for an around +46% qoq increase, we estimate the second derivative of ASP growth during the quarter to be around -48%p.

GS view based on channel checks and feedback: Based on discussion with investors, the sentiment on the industry continues to be constructive, on the back of incrementally improving spot pricing, higher expectation for near-term conventional memory contract pricing, and the significant improvement in HBM pricing expectations for 2027. We have revised up our 2027E HBM pricing growth estimate for SEC to +44% yoy (from +14% yoy), however we believe there could be additional upside risk to our estimate considering the tight HBM S/D and the widening gap between conventional DRAM and HBM pricing.

## Components of GS DRAM sentiment indicator

Through the analysis of data points, including 1) daily DRAM spot pricing, 2) monthly server ODM revenue, 3) monthly revenue of Aspeed (largest BMC supplier for servers globally), 4) monthly Korea DRAM export revenue, 5) monthly China smartphone shipments, 6) monthly revenue of Nanya Tech, 7) monthly revenue of Supreme Electronics, 8) our forecast of the second derivative of SEC DRAM ASP for the forward quarter, and 9) our view on the sentiment in the DRAM market based on our channel checks and conversations with investors, our DRAM sentiment indicator for June 2026 is pointing in a moderately positive direction (Same as April).

Exhibit 2: DDR5 pricing has been showing an upward trend since early May and is trading at +25% premium over May contract pricing
DDR5 16Gb spot pricing trend  
![](images/e24f40fe2b4199b245229bba03e7224b200e5ecdd70efdb5a0cb79f4c3af4480.jpg)  
\* DRAM spot pricing as of June 26  
Source: DRAMeXchange

Exhibit 3: DDR4 pricing has been showing an upward trend since early May and is trading at +45% premium over May contract pricing
DDR4 8Gb spot pricing trend  
![](images/ba5206f0737510dd2f0e95bb937602b40582e5e218b2973861d157dab92ce69a.jpg)  
\* DRAM spot pricing as of June 26  
Source: DRAMeXchange

Exhibit 4: Taiwan server ODM monthly revenue rose by +53% yoy (-3% mom) in May
Taiwan server ODM monthly revenue trend  
![](images/653baae8312dfe0f31b928ffbc5915e0f6831e77381c40a4b495dd60dae8cb86.jpg)  
Source: Company data

Exhibit 5: Aspeed's monthly revenue increased by $+69\%$ yoy $(+0\%$ mom) in May Aspeed monthly revenue trend  
![](images/e93d42efa2bfb5fb525677772bbd0f1383c3dc1e7ea91232a890217e108554e0.jpg)  
Source: Company data

Exhibit 6: Korea DRAM exports up by +370% yoy (+21% mom) in May
Korea monthly DRAM export revenue trend  
![](images/225d9cef3a2b2cb17be78da1065f8a82f692d12e31cf7fc30d95a40766a6cada.jpg)  
Source: TRASS

Exhibit 7: China smartphone shipment increased by +19% yoy (+7% mom) in May
China smartphone shipment trend  
![](images/b0fbe4663726ce56782f49501d856c0721cf04ed83fccfd3dd8e11a89edc52d9.jpg)  
Source: CAICT

SEC DRAM pricing growth assumptions

Exhibit 8: Nanya's monthly revenue increased by $+730\%$ yoy $(+9\%$ mom) in May Nanya monthly revenue trend  
![](images/bd2f5c4aee490b093c95540b35da575eca22bdb9081a693f5d77ec91479be77f.jpg)  
Source: Company data

Exhibit 9: Supreme's monthly revenue increased $+253\%$ yoy $(+54\%$ mom) in May  
Supreme monthly revenue trend  
![](images/f56eaa1f6cafc75dd174c1a285c0f076925a248fc6e681cde10d60d10ad52090.jpg)  
Source: Company data  
Exhibit 10: As our latest 2Q26E DRAM ASP estimate for SEC is for an around +46% qoq increase, we estimate the second derivative of ASP growth during the quarter to be around -48%p

![](images/86c9a3e695b4001f5848c46d3190fb8e072e5992cd1f72a2fe459e5bc62534fe.jpg)  
Source: Company data, GS Global Investment Research

Price Target Risks and Methodology - Samsung Electronics

Valuation methodology: Our 12m 2026-2027E EV/EBITDA-based SOTP target price for the common share is W480,000. Our 12-month target price for the preference share is W360,000, which is based on our target pref to common shares discount of 25%, derived from averaging: 1) the pref discount of the 2-factor model and 2) the average preference share discount to common shares during the past 1 month. We are Buy rated on both the common and preference shares.

Key downside risks: 1) major deterioration in memory supply/demand, 2) sharp contraction in smartphone margins, and 3) mobile OLED market share loss.

## Disclosure Appendix

## Reg AC

We, Giuni Lee, Daiki Takayama and Taeyong Lee, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Giuni Lee GS (Asia) L.L.C., Seoul Branch, Daiki Takayama GS Japan Co., Ltd., Taeyong Lee GS (Asia) L.L.C., Seoul Branch.

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

Samsung Electronics (Buy, W323,000) and Samsung Electronics (Pref) (Buy, W210,500)

The rating(s) for Samsung Electronics and Samsung Electronics (Pref) is/are relative to the other companies in its/their coverage universe: Hansol Chemical, LG Display, LG Electronics, LG Innotek Co., SK Hynix Inc., SKC, Samsung Electro-Mechanics, Samsung Electronics, Samsung Electronics (Pref)

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Samsung Electronics (W323,000) and Samsung Electronics (Pref) (W210,500)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Samsung Electronics (W323,000) and Samsung Electronics (Pref) (W210,500)

GS had an investment banking services client relationship during the past 12 months with: Samsung Electronics (W323,000) and Samsung Electronics (Pref) (W210,500)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Samsung Electronics (W323,000) and Samsung Electronics (Pref) (W210,500)

GS had a non-securities services client relationship during the past 12 months with: Samsung Electronics (W323,000) and Samsung Electronics (Pref) (W210,500)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td colspan="3">Rating Distribution</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>50%</td><td>34%</td><td>16%</td></tr></table>

<table><tr><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/7ed0a7752b03b0e5bbd8dbd16f721622e3ea7fe1cb722876aa84be0898b296b1.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/e3fa58fbc5f3985b963e38300e7b97e8e3b64f3882bbd6e495a94b00f8817279.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## Samsung Electronics (Pref) (005935.KS)

Samsung Electronics (005930.KS)

<table><tr><td>Date of report</td><td>Target price (W)</td><td>Closing price (W)</td><td>Date of report</td><td>Target price (W)</td><td>Closing price (W)</td></tr><tr><td>31-May-26</td><td>360,000</td><td>202,500</td><td>31-May-26</td><td>480,000</td><td>317,000</td></tr><tr><td>30-Apr-26</td><td>245,000</td><td>158,300</td><td>30-Apr-26</td><td>320,000</td><td>220,500</td></tr><tr><td>07-Apr-26</td><td>220,000</td><td>130,900</td><td>07-Apr-26</td><td>285,000</td><td>196,500</td></tr><tr><td>11-Mar-26</td><td>200,000</td><td>138,900</td><td>11-Mar-26</td><td>260,000</td><td>190,000</td></tr><tr><td>29-Jan-26</td><td>159,000</td><td>115,600</td><td>29-Jan-26</td><td>205,000</td><td>160,700</td></tr><tr><td>08-Jan-26</td><td>142,000</td><td>101,900</td><td>08-Jan-26</td><td>180,000</td><td>138,800</td></tr><tr><td>16-Dec-25</td><td>110,000</td><td>79,800</td><td>16-Dec-25</td><td>140,000</td><td>102,800</td></tr><tr><td>30-Oct-25</td><td>99,000</td><td>82,500</td><td>30-Oct-25</td><td>123,000</td><td>104,100</td></tr><tr><td>14-Oct-25</td><td>89,000</td><td>72,300</td><td>14-Oct-25</td><td>109,000</td><td>91,600</td></tr><tr><td>22-Sep-25</td><td>78,000</td><td>66,700</td><td>22-Sep-25</td><td>96,000</td><td>83,500</td></tr><tr><td>31-Jul-25</td><td>69,000</td><td>57,600</td><td>31-Jul-25</td><td>84,000</td><td>71,400</td></tr><tr><td>01-May-25</td><td>61,000</td><td>46,850</td><td>01-May-25</td><td>74,000</td><td>55,500</td></tr><tr><td>01-Apr-25</td><td>64,000</td><td>47,700</td><td>01-Apr-25</td><td>77,000</td><td>58,800</td></tr><tr><td>02-Feb-25</td><td>59,000</td><td>43,000</td><td>02-Feb-25</td><td>72,000</td><td>52,400</td></tr><tr><td>08-Jan-25</td><td>60,000</td><td>46,800</td><td>08-Jan-25</td><td>73,000</td><td>57,300</td></tr><tr><td>16-Dec-24</td><td>63,000</td><td>46,550</td><td>16-Dec-24</td><td>75,000</td><td>55,600</td></tr><tr><td>31-Oct-24</td><td>68,000</td><td>47,950</td><td>31-Oct-24</td><td>82,000</td><td>59,200</td></tr><tr><td>08-Oct-24</td><td>71,000</td><td>49,900</td><td>08-Oct-24</td><td>86,000</td><td>60,300</td></tr><tr><td>23-Sep-24</td><td>78,000</td><td>52,400</td><td>23-Sep-24</td><td>95,000</td><td>62,600</td></tr><tr><td>31-Jul-24</td><td>88,000</td><td>64,900</td><td>31-Jul-24</td><td>110,000</td><td>83,900</td></tr><tr><td>05-Jul-24</td><td>87,000</td><td>68,000</td><td>05-Jul-24</td><td>108,000</td><td>87,100</td></tr><tr><td>05-Apr-24</td><td>85,000</td><td>69,000</td><td>01-Jul-24</td><td>105,000</td><td>81,800</td></tr><tr><td>21-Mar-24</td><td>81,000</td><td>65,800</td><td>30-Apr-24</td><td>103,000</td><td>77,500</td></tr><tr><td>17-Dec-23</td><td>77,000</td><td>59,300</td><td>05-Apr-24</td><td>102,000</td><td>84,500</td></tr><tr><td>31-Oct-23</td><td>75,000</td><td>53,600</td><td>21-Mar-24</td><td>97,000</td><td>79,300</td></tr><tr><td>20-Sep-23</td><td>76,000</td><td>56,100</td><td>17-Dec-23</td><td>95,000</td><td>73,300</td></tr><tr><td></td><td></td><td></td><td>20-Sep-23</td><td>93,000</td><td>69,600</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures

[中间内容因长度限制已省略]

 or may discuss in this report, trading strategies that reference catalysts or events that may have a near-term impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

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
