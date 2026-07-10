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
# Japan Electronic Components: Expert call: reconfirming sustained strength in nearline HDDs; we maintain Buy on TDK and HOYA

On July 7, we held a conference call with Techno Systems Research (TSR) to discuss the outlook for the HDD industry. Key points are as follows (unless otherwise noted, views are TSR's). (1) Nearline HDDs: 2026 TAM is expected to be 129 mn units (+4% yoy), of which nearline HDDs will account for 75.6 mn units (+12% yoy). The demand outlook is very strong, and robust production is expected to continue. (2) Price trends: The actions of HDD manufacturers in 2026 show a tendency to be more proactive in increasing capacity per unit (= average unit price increase) and raising prices on a same-product basis, rather than just increasing nearline HDD volumes/production capacity. Talk of LTAs heading toward 2030 has already emerged, and price increases are expected to continue. (3) HDD components: Bottlenecks for component/materials manufacturers are not as severe as they were at one point, but there are several materials that could become bottlenecks in the future. While ASP increases due to technological changes are possible, there have been no notable moves to raise prices on a same-product basis. (4) HDD heads: Outsourcing to TDK from WDC/STX (in-house heads) is expected to increase significantly from the April-June quarter (TDK has already disclosed guidance for a 40% increase in HDD head volumes in FY3/27, of which volumes for nearline HDDs are expected to increase 50%).

Bottom line: We reconfirmed the healthy and tight supply-demand situation for nearline HDDs. Component/materials manufacturers that (1) benefit from higher component counts, (2) benefit from ASP increases due to technological changes, and (3) can increase market share in nearline HDDs should strengthen their earnings growth potential. We maintain our Buy rating on TDK for HDD heads and suspensions, and HOYA for glass substrates.

Daiki Takayama  
+81(3)4587-9870 |  
daiki.takayama@gs.com  
GS Japan Co., Ltd.

Shuhei Nakamura  
+81(3)4587-9932 |  
shuhei.nakamura@gs.com  
GS Japan Co., Ltd.

Mitsuhiro Icho
+81(3)4587-9836 |
mitsuhiro.x.icho@gs.com
GS Japan Co., Ltd.

Kaho Otake  
+81(3)4587-7498 | kaho.otake@gs.com  
GS Japan Co., Ltd.

Makoto Takahara  
+81(3)4587-4270 |  
makoto.takahara@gs.com  
GS Japan Co., Ltd.

Yuji Hidaka
+81(3)4587-3656 | yuji.hidaka@gs.com
GS Japan Co., Ltd.

## Exhibit 1: HDD Quarterly/Yearly Shipment and TAM

HDD Quarterly/Yearly Shipment & TAM

<table><tr><td rowspan="2">mn units</td><td colspan="4">2025</td><td colspan="4">2026</td><td rowspan="2">2025</td><td rowspan="2">2026E</td></tr><tr><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1Q</td><td>2QE</td><td>3QE</td><td>4QE</td></tr><tr><td>Enterprise</td><td>0.82</td><td>0.81</td><td>0.73</td><td>0.79</td><td>0.76</td><td>0.63</td><td>0.64</td><td>0.60</td><td>3.15</td><td>2.62</td></tr><tr><td>NL</td><td>14.61</td><td>16.47</td><td>18.14</td><td>18.40</td><td>18.66</td><td>18.70</td><td>19.09</td><td>19.15</td><td>67.62</td><td>75.60</td></tr><tr><td>3.5&quot; ATA</td><td>7.57</td><td>7.85</td><td>7.17</td><td>8.35</td><td>8.27</td><td>7.76</td><td>7.50</td><td>7.30</td><td>30.94</td><td>30.83</td></tr><tr><td>2.5&quot; Mobile</td><td>5.70</td><td>5.27</td><td>5.57</td><td>5.50</td><td>5.32</td><td>5.16</td><td>4.85</td><td>4.73</td><td>22.04</td><td>20.06</td></tr><tr><td>Total</td><td>28.70</td><td>30.40</td><td>31.61</td><td>33.04</td><td>33.01</td><td>32.25</td><td>32.08</td><td>31.78</td><td>123.75</td><td>129.11</td></tr><tr><td>Rev (mn $)</td><td>4,717</td><td>5,416</td><td>5,898</td><td>6,260</td><td>6,981</td><td>7,465</td><td>7,901</td><td>8,131</td><td>22,291</td><td>30,478</td></tr><tr><td>ASP</td><td>164.4</td><td>178.2</td><td>186.6</td><td>189.5</td><td>211.5</td><td>231.5</td><td>246.3</td><td>255.9</td><td>180.1</td><td>236.0</td></tr></table>

Source: Techno Systems Research, Data compiled by GS Global Investment Research

## Exhibit 2: HDD Quarterly/Yearly Production

HDD Quarterly/Yearly Production

<table><tr><td rowspan="2">mn units</td><td colspan="4">2025</td><td colspan="4">2026</td><td rowspan="2">2025</td><td rowspan="2">2026E</td></tr><tr><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1Q</td><td>2QE</td><td>3QE</td><td>4QE</td></tr><tr><td>Enterprise</td><td>0.95</td><td>0.85</td><td>0.79</td><td>0.85</td><td>0.69</td><td>0.60</td><td>0.73</td><td>0.66</td><td>3.44</td><td>2.68</td></tr><tr><td>NL</td><td>17.32</td><td>18.37</td><td>18.96</td><td>20.12</td><td>20.77</td><td>20.97</td><td>21.28</td><td>21.35</td><td>74.77</td><td>84.37</td></tr><tr><td>3.5&quot; ATA</td><td>7.12</td><td>6.85</td><td>7.30</td><td>7.24</td><td>7.29</td><td>6.81</td><td>6.78</td><td>6.73</td><td>28.51</td><td>27.61</td></tr><tr><td>2.5&quot; Mobile</td><td>5.62</td><td>5.61</td><td>5.96</td><td>5.63</td><td>5.14</td><td>5.38</td><td>4.88</td><td>4.80</td><td>22.82</td><td>20.20</td></tr><tr><td>Total</td><td>31.01</td><td>31.68</td><td>33.01</td><td>33.84</td><td>33.89</td><td>33.76</td><td>33.67</td><td>33.54</td><td>129.54</td><td>134.86</td></tr></table>

Source: Techno Systems Research, Data compiled by GS Global Investment Research

## Price Target Risks and Methodology - TDK

Valuation methodology: We are Buy-rated on TDK with a 12-month price target of ¥4,600. Our target price is based on FY3/29E EV/GCI vs. CROCI/WACC, applying a 10% premium to our sector average EV/DACF multiple of 10X (implies FY3/28E P/E of 31X).

Key risks: Decline in smartphone production volume, higher input costs, and yen appreciation.

## Price Target Risks and Methodology - HOYA

Valuation methodology: Our 12-month target price of ¥33,000 is based on a sum-of-the-parts valuation methodology (FY26-27E EV/EBITDA-based, implies FY3/28E P/E of 35X and P/B of 11X), using different multiples for each of HOYA's two main segments – life care (FY3/27-3/28E EV/EBITDA of 15X/13X) and IT (FY3/27-FY3/28E EV/EBITDA of 35X/28X).

Key risks: Intensifying competition in core businesses, a weakening of demand, and large-scale capex or M&A deals.

## Disclosure Appendix

## Reg AC

We, Daiki Takayama, Shuhei Nakamura, Mitsuhiro Icho, Kaho Otake, Makoto Takahara and Yuji Hidaka, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Daiki Takayama GS Japan Co., Ltd., Shuhei Nakamura GS Japan Co., Ltd., Mitsuhiro Icho GS Japan Co., Ltd., Kaho Otake GS Japan Co., Ltd., Makoto Takahara GS Japan Co., Ltd., Yuji Hidaka GS Japan Co., Ltd..

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

The rating(s) for TDK is/are relative to the other companies in its/their coverage universe: Alps Alpine, Dai Nippon Printing, Hirose Electric, IRISO Electronics, Ibiden, Japan Aviation Electronics Industry, Kohoku Kogyo, Kyocera, MARUWA, Mabuchi Motor, Maxell Ltd., MinebeaMitsumi Inc., Murata Mfg., NGK Corp., Nichicon, Nidec, Nippon Ceramic, Niterra, Nitto Denko, Renesas Electronics, Rohm, TDK, TOPPAN Holdings, Taiyo Yuden

The rating(s) for HOYA is/are relative to the other companies in its/their coverage universe: Advantest, DISCO, Ebara, HOYA, JEOL, Kioxia Holdings, Kokusai Electric, Lasertec, SCREEN Holdings, Tokyo Electron, Tokyo Seimitsu, Ulvac

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the second most recent month end: TDK (\(¥3,302) and TDK (ADR) (\$45.24)

GS has received compensation for investment banking services in the past 12 months: TDK (¥3,302) and TDK (ADR) (\$45.24)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: HOYA (¥24,185), TDK (¥3,302) and TDK (ADR) (\$45.24)

GS had an investment banking services client relationship during the past 12 months with: HOYA (¥24,185), TDK (¥3,302) and TDK (ADR) (\$45.24)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: TDK (¥3,302) and TDK (ADR) (\$45.24)

GS had a non-securities services client relationship during the past 12 months with: TDK (¥3,302) and TDK (ADR) (\$45.24)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/20003749b2467b47014dd61fe8d75c001e709fcd9f1b9d0511a927c470592480.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/4dbd6851b9f53eca6aa5dcf9a9dd60a4bdd43bcc9465ea2970d91083e3856e92.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## HOYA (7741.T)

TDK (6762.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>31-May-26</td><td>33,000</td><td>27,080</td><td>08-Jun-26</td><td>4,600</td><td>3,715</td></tr><tr><td>30-Apr-26</td><td>32,000</td><td>29,100</td><td>28-Apr-26</td><td>3,000</td><td>2,677</td></tr><tr><td>09-Mar-26</td><td>31,000</td><td>26,765</td><td>23-Mar-26</td><td>2,900</td><td>2,043</td></tr><tr><td>30-Jan-26</td><td>28,500</td><td>25,870</td><td>12-Jan-26</td><td>2,800</td><td>2,142</td></tr><tr><td>31-Oct-25</td><td>26,500</td><td>25,085</td><td>31-Oct-25</td><td>2,700</td><td>2,673</td></tr><tr><td>08-Oct-25</td><td>24,000</td><td>22,155</td><td>02-Oct-25</td><td>2,400</td><td>2,154</td></tr><tr><td>23-Jul-25</td><td>22,000</td><td>18,590</td><td>01-Aug-25</td><td>2,100</td><td>1,876</td></tr><tr><td>24-Mar-25</td><td>20,000</td><td>17,490</td><td>28-Apr-25</td><td>2,000</td><td>1,460</td></tr><tr><td>18-Feb-25</td><td>22,000</td><td>19,040</td><td>31-Mar-25</td><td>2,100</td><td>1,546</td></tr><tr><td>03-Feb-25</td><td>22,500</td><td>19,625</td><td>01-Nov-24</td><td>2,300</td><td>1,848</td></tr><tr><td>22-Jan-25</td><td>23,000</td><td>21,500</td><td>01-Oct-24</td><td>2,230</td><td>1,948</td></tr><tr><td>02-Sep-24</td><td>22,000</td><td>20,760</td><td>02-Sep-24</td><td>11,300</td><td>2,023</td></tr><tr><td>01-Aug-24</td><td>23,000</td><td>18,680</td><td>30-Jul-24</td><td>11,500</td><td>2,029</td></tr><tr><td>24-Apr-24</td><td>22,000</td><td>18,685</td><td>02-Jul-24</td><td>11,200</td><td>2,004</td></tr><tr><td>13-Mar-24</td><td>21,000</td><td>18,925</td><td>26-Apr-24</td><td>8,300</td><td>1,462</td></tr><tr><td>01-Feb-24</td><td>20,000</td><td>18,550</td><td>03-Apr-24</td><td>8,700</td><td>1,488</td></tr><tr><td>04-Jan-24</td><td>19,000</td><td>16,995</td><td>31-Jan-24</td><td>7,800</td><td>1,488</td></tr><tr><td>05-Oct-23</td><td>18,000</td><td>15,135</td><td>06-Dec-23</td><td>7,500</td><td>1,338</td></tr><tr><td>19-Jul-23</td><td>19,000</td><td>16,350</td><td>01-Nov-23</td><td>6,500</td><td>1,158</td></tr><tr><td></td><td></td><td></td><td>04-Oct-23</td><td>6,400</td><td>1,052</td></tr><tr><td></td><td></td><td></td><td>02-Aug-23</td><td>6,500</td><td>1,089</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Aust

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
