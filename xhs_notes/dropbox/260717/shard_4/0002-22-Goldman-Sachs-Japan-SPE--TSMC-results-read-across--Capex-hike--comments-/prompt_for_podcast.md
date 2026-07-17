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
# Japan SPE: TSMC results read-across: Capex hike, comments on inflation look positive for the SPE sector as a whole

TSMC (covered by our Asia technology analyst Evelyn Yu), the world's largest foundry, held its 2Q12/26 (Apr-Jun) earnings call from 15:00 JST on July 16. We summarize the key points below, focusing mainly on the current business environment, capex outlook, and read-across for Japanese SPE makers.

## Further tightness amid strong AI demand

While demand for consumer-use semiconductors remains weak, TSMC raised its full-year 2026 sales outlook from growth exceeding +30% yoy, to growth of slightly over +40% yoy as demand for AI grows even stronger. With further expansion in demand expected going forward, full-year capex guidance was also increased from the upper end of the \$52 bn-\$56 bn range, to \$60 bn-\$64 bn. The company also announced new investment (totaling \$100 bn) in fabs for advanced processes of N2 and below and advanced packaging in Arizona (commenting that there will likely be four fabs). Management intends to determine the investment timelines depending on market trends.

## Capex outlook

Of the total capex, the company said it would allocate 70-80% for advanced processes, 10% for specialty (mature) nodes, and 10-20% for advanced packaging, mask manufacturing, testing, and other applications (maintaining a flexible range as usual). It stated it will allocate resources dynamically based on where capacity bottlenecks arise. The capex guidance hike was driven by sustained strong customer demand, as well as rising procurement costs due to inflation. The company also noted that development of A14, the next node after N2, is progressing smoothly, and reconfirmed its schedule for mass production in 2028.

## Read-across for Japanese SPE makers

We view the upward revision to TSMC's capex outlook amid even stronger AI demand and the mention of inflation as a contributing factor as having positive implications for the sector as a whole, in that this suggests price hikes may be gaining traction in the SPE market. We reiterate our Buy ratings on Lasertec (on CL), Ebara, Disco, and Tokyo Electron.

+81(3)4587-9932 |
shuhei.nakamura@gs.com
GS Japan Co., Ltd.

Kaho Otake
+81(3)4587-7498 | kaho.otake@gs.com
GS Japan Co., Ltd.

Exhibit 1: Sales exposure to TSMC (based on FY25 results)  
![](images/ae1afd958d0439ed4080f101588b8c934ced2403b6a19f71123e306b8330f557.jpg)  
Lasertec and Ulvac figures are based on our estimates.  
Source: Company data, GS Global Investment Research

Exhibit 2: TP risks and methodology for companies mentioned

<table><tr><td>Company Name (rating)</td><td>Ticker</td><td>12-m TP (¥)</td><td>Methodology</td><td>Risks</td></tr><tr><td>DISCO (Buy)</td><td>6146.T</td><td>100,000</td><td>Based on the global SPE sector average multiple of 18X and our FY3/28E estimates. We then apply a sector-relative premium of 50%.</td><td>(-) slowdown or share loss in AI-related demand(-) slowdown in China demand or tightening of export controls(-) rapid yen appreciation against the USD</td></tr><tr><td>Ebara (Buy)</td><td>6361.T</td><td>7,800</td><td>Based on the correlation between P/B and our FY12/27E ROE estimates.</td><td>(-) Semiconductor capex enters a downcycle(-) Increasing competitiveness of Chinese CMP system makers(-) Slow adoption of new technology in semiconductor devices(-) Decline in crude oil/LNG prices, oil refining/petrochemical margins</td></tr><tr><td>Lasertec (Buy)*</td><td>6920.T</td><td>67,000</td><td>Based on the global SPE sector average multiple of 18X and the average of our FY6/28E estimates. We then apply a sector-relative premium of 50%.</td><td>(-) Decline in market share due to new entrants(-) Lack of progress in ACTIS adoption by wafer fabs(-) Weaker customer investment appetite for leading-edge process nodes(-) Rapid appreciation of the yen against the US dollar</td></tr><tr><td>Tokyo Electron (Buy)</td><td>8035.T</td><td>83,000</td><td>Based on the global SPE sector average multiple of 18X and our FY3/28E estimates. We then apply a sector-relative premium of 30%.</td><td>(-) prolonged inventory adjustment phase in the semiconductor industry(-) further strengthening of export restrictions(-) depressed valuation multiple amid upward pressure on interest rates and other factors</td></tr></table>

\*=on Conviction List

Source: GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Shuhei Nakamura and Kaho Otake, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Shuhei Nakamura GS Japan Co., Ltd., Kaho Otake GS Japan Co., Ltd..

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

DISCO (Buy, ¥70,430), Ebara (Buy, ¥5,869), Lasertec (Buy, ¥46,530) and Tokyo Electron (Buy, ¥70,940)

The rating(s) for DISCO, Ebara, Lasertec and Tokyo Electron is/are relative to the other companies in its/their coverage universe: Advantest, DISCO, Ebara, HOYA, JEOL, Kioxia Holdings, Kokusai Electric, Lasertec, SCREEN Holdings, Tokyo Electron, Tokyo Seimitsu, Ulvac

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Ebara (¥5,869) and Lasertec (¥46,530)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: DISCO (¥70,430), Ebara (¥5,869), Lasertec (¥46,530) and Tokyo Electron (¥70,940)

GS has received compensation for non-investment banking services during the past 12 months: Tokyo Electron (¥70,940)

GS had an investment banking services client relationship during the past 12 months with: DISCO (¥70,430), Ebara (¥5,869), Lasertec (¥46,530) and Tokyo Electron (¥70,940)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Tokyo Electron (¥70,940)

GS had a non-securities services client relationship during the past 12 months with: DISCO (¥70,430), Ebara (¥5,869) and Tokyo Electron (¥70,940)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

DISCO (6146.T)

<table><tr><td colspan="3">Rating Distribution</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>50%</td><td>34%</td><td>16%</td></tr></table>

<table><tr><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/89bda346c2b3a5ab13f6e45f84fb8abb00c95bd1f144df8329aa9f7a0db68772.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/ea15e04c286a1b17a794b067ddb7589af3caee08a610ac9a7e375a448b321cce.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/2a0c3988a07b9a1286eed3e598857a3ebfe1ef3d1299e6a7227c3b3d5e9a8232.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/25a0f9814c503995237f1d81d26e4e11cf5d6ef5fc5f4ad825a5ae592c910fba.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>06-Jul-26</td><td>100,000</td><td>78,000</td></tr><tr><td>30-Jun-26</td><td>95,000</td><td>81,260</td></tr><tr><td>31-May-26</td><td>87,000</td><td>65,090</td></tr><tr><td>22-Apr-26</td><td>86,000</td><td>74,830</td></tr><tr><td>09-Mar-26</td><td>83,000</td><td>66,500</td></tr><tr><td>21-Jan-26</td><td>68,000</td><td>58,570</td></tr><tr><td>08-Jan-26</td><td>64,000</td><td>55,590</td></tr><tr><td>06-Jan-26</td><td>62,000</td><td>54,200</td></tr><tr><td>29-Oct-25</td><td>61,000</td><td>56,390</td></tr><tr><td>08-Oct-25</td><td>60,000</td><td>52,140</td></tr><tr><td>06-Oct-25</td><td>56,000</td><td>54,000</td></tr><tr><td>09-Jul-25</td><td>51,000</td><td>41,290</td></tr><tr><td>30-Jun-25</td><td>47,000</td><td>42,630</td></tr></table>

## Tokyo Electron (8035.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>30-Jun-26</td><td>83,000</td><td>77,150</td></tr><tr><td>31-May-26</td><td>62,000</td><td>52,420</td></tr><tr><td>04-May-26</td><td>57,000</td><td>47,450</td></tr><tr><td>30-Apr-26</td><td>55,000</td><td>44,390</td></tr><tr><td>09-Mar-26</td><td>52,000</td><td>38,920</td></tr><tr><td>21-Feb-26</td><td>50,000</td><td>43,960</td></tr><tr><td>06-Feb-26</td><td>44,000</td><td>41,030</td></tr><tr><td>06-Jan-26</td><td>43,000</td><td>37,350</td></tr><tr><td>15-Dec-25</td><td>38,000</td><td>31,140</td></tr><tr><td>31-Oct-25</td><td>36,000</td><td>34,180</td></tr><tr><td>08-Oct-25</td><td>32,500</td><td>29,255</td></tr><tr><td>31-Jul-25</td><td>30,000</td><td>27,330</td></tr><tr><td>30-Jun-25</td><td>33,000</td><td>27,680</td></tr></table>

DISCO (6146.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>13-Apr-25</td><td>43,000</td><td>27,470</td></tr><tr><td>04-Apr-25</td><td>44,000</td><td>27,635</td></tr><tr><td>24-Mar-25</td><td>51,000</td><td>33,060</td></tr><tr><td>21-Nov-24</td><td>59,000</td><td>42,380</td></tr><tr><td>01-Nov-24</td><td>57,000</td><td>42,810</td></tr><tr><td>04-Oct-24</td><td>54,000</td><td>39,710</td></tr><tr><td>02-Oct-24</td><td>56,000</td><td>37,410</td></tr><tr><td>02-Sep-24</td><td>63,000</td><td>41,350</td></tr><tr><td>22-Aug-24</td><td>66,000</td><td>43,560</td></tr><tr><td>04-Jul-24</td><td>71,000</td><td>64,580</td></tr><tr><td>27-May-24</td><td>65,000</td><td>61,790</td></tr><tr><td>04-Apr-24</td><td>60,000</td><td>56,750</td></tr><tr><td>21-Mar-24</td><td>56,000</td><td>52,960</td></tr><tr><td>13-Mar-24</td><td>53,000</td><td>50,000</td></tr><tr><td>31-Jan-24</td><td>43,000</td><td>40,380</td></tr><tr><td>24-Jan-24</td><td>42,000</td><td>40,730</td></tr><tr><td>04-Jan-24</td><td>39,000</td><td>33,630</td></tr><tr><td>21-Nov-23</td><td>34,000</td><td>32,030</td></tr><tr><td>26-Oct-23</td><td>32,000</td><td>26,960</td></tr><tr><td>05-Oct-23</td><td>31,000</td><td>27,940</td></tr><tr><td>15-Aug-23</td><td>30,000</td><td>25,865</td></tr></table>

<table><tr><td colspan="3">Tokyo Electron (8035.T)</td></tr><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>07-Apr-25</td><td>30,000</td><td>17,060</td></tr><tr><td>24-Mar-25</td><td>32,500</td><td>22,190</td></tr><tr><td>10-Jan-25</td><td>35,000</td><td>27,025</td></tr><tr><td>02-Oct-24</td><td>38,500</td><td>25,080</td></tr><tr><td>02-May-24</td><td>43,000</td><td>35,010</td></tr><tr><td>21-Mar-24</td><td>41,000</td><td>39,340</td></tr><tr><td>13-Mar-24</td><td>40,000</td><td>37,390</td></tr><tr><td>09-Feb-24</td><td>33,000</td><td>29,755</td></tr><tr><td>04-Jan-24</td><td>30,000</td><td>24,005</td></tr><tr><td>25-Nov-23</td><td>27,000</td><td>24,005</td></tr><tr><td>19-Jul-23</td><td>24,000</td><td>20,725</td></tr></table>

Ebara (6361.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>30-Jun-26</td><td>7,800</td><td>6,256</td></tr><tr><td>31-May-26</td><td>7,100</td><td>5,683</td></tr><tr><td>04-May-26</td><td>7,000</td><td>5,242</td></tr><tr><td>15-Apr-26</td><td>6,800</td><td>5,004</td></tr><tr><td>21-Feb-26</td><td>6,600</td><td>5,638</td></tr><tr><td>13-Feb-26</td><td>5,900</td><td>5,303</td></tr><tr><td>06-Jan-26</td><td>5,200</td><td>4,050</td></tr><tr><td>10-Dec-25</td><td>5,000</td><td>3,942</td></tr></table>

Lasertec (6920.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>30-Jun-26</td><td>67,000</td><td>49,700</td></tr><tr><td>04-May-26</td><td>55,000</td><td>42,930</td></tr><tr><td>30-Apr-26</td><td>53,000</td><td>42,690</td></tr><tr><td>09-Mar-26</td><td>50,000</td><td>30,360</td></tr><tr><td>21-Feb-26</td><td>28,000</td><td>30,640</td></tr><tr><td>06-Jan-26</td><td>27,000</td><td>32,760</td></tr><tr><td>15-Dec-25</td><td>24,000</td><td>30,300</td></tr><tr><td>31-Oct-25</td><td>22,500</td><td>28,410</td></tr><tr><td>08-Oct-25</td><td>20,000</td><td>20,030</td></tr><tr><td>07-Aug-25</td><td>19,000</td><td>14,295</td></tr><tr><td>30-Jun-25</td><td>19,500</td><td>19,410</td></tr><tr><td>12-May-25</td><td>17,500</td><td>14,775</td></tr><tr><td>07-Apr-25</td><td>17,000</td><td>10,585</td></tr><tr><td>24-Mar-25</td><td>18,000</td><td>14,040</td></tr><tr><td>31-Jan-25</td><td>20,000</td><td>15,470</td></tr><tr><td>10-Jan-25</td><td>21,500</td><td>15,655</td></tr><tr><td>21-Nov-24</td><td>24,500</td><td>17,280</td></tr><tr><td>31-Oct-24</td><td>28,500</td><td>23,475</td></tr><tr><td>02-Oct-24</td><td>30,000</td><td>22,785</td></tr><tr><td>07-Aug-24</td><td>34,000</td><td>22,170</td></tr><tr><td>10-May-24</td><td>33,000</td><td>40,940</td></tr><tr><td>30-Apr-24</td><td>30,000</td><td>34,600</td></tr><tr><td>21-Mar-24</td><td>26,500</td><td>43,060</td></tr><tr><td>13-Mar-24</td><td>25,500</td><td>38,270</td></tr><tr><td>04-Jan-24</td><td>22,500</td><td>35,220</td></tr><tr><td>25-Nov-23</td><td>21,000</td><td>30,970</td></tr><tr><td>05-Oct-23</td><td>19,500</td><td>22,890</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global

Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
