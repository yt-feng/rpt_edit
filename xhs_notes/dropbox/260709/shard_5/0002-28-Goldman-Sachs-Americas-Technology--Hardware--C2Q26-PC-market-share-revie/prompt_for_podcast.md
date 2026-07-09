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
# Americas Technology: Hardware: C2Q26 PC market share review: Industry unit shipment declines driven by component availability

BOTTOM LINE: IDC released preliminary estimates for 2Q26 PC shipments (including workstations) of 68.2 mn, down -4.9% year-over-year, marking the first decline after 9 sequential quarters of positive growth. IDC attributes the decline to ongoing component shortages (memory, storage), as well as a challenging macro backdrop, which should not ease until early 2028. IDC reiterated its expectation for PC shipments to see sharp declines for 2H26 driven by higher ASPs and limited supply. Though units are down, IDC observes industry revenue growth from price increases. A prolonged supply shortage should benefit larger, scaled players with multiple product lines and sophisticated supply chain management capabilities like Apple, Dell, Lenovo; IDC expects these larger vendors should be able to consolidate market share from smaller players over time.

2Q26 vendor market share: Apple, ASUS, and Lenovo grew ahead of the market, DELL performed in-line, and HP lagged. Specifically, IDC estimates that Apple shipments grew +10% (9.9% share), ASUS shipments grew 0.2% (7.4% share), Lenovo shipments were down -2% (24.4% share), Dell shipments were down -5% (13.6% share), and HP units declined -9% (19.1% share).

Katherine Murphy +1(212)902-1151 | katherine.a.murphy@gs.com GS & Co. LLC

Michael Ng, CFA
+1(212)902-8618 | michael.ng@gs.com
GS & Co. LLC

Zorayda Montemayor +1(212)357-6403 | zorayda.montemayor@gs.com GS & Co. LLC

Exhibit 1: IDC estimates 2Q26 PC shipments (including workstations) of 68.2 mn, marking -5% decline YoY PC units by vendor (mn)

<table><tr><td>(in millions)</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td></tr><tr><td>Vendor, Global (Includes Workstations)</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Units</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Apple</td><td>4.8</td><td>5.1</td><td>6.0</td><td>7.1</td><td>5.7</td><td>6.1</td><td>6.7</td><td>7.2</td><td>6.3</td><td>6.7</td></tr><tr><td>ASUS</td><td>3.6</td><td>4.2</td><td>5.3</td><td>4.9</td><td>4.1</td><td>5.0</td><td>6.0</td><td>5.5</td><td>4.8</td><td>5.0</td></tr><tr><td>Dell Technologies</td><td>9.3</td><td>10.1</td><td>9.8</td><td>9.9</td><td>9.6</td><td>9.8</td><td>10.1</td><td>11.7</td><td>10.3</td><td>9.3</td></tr><tr><td>HP Inc</td><td>12.0</td><td>13.7</td><td>13.6</td><td>13.7</td><td>12.8</td><td>14.3</td><td>15.0</td><td>15.4</td><td>12.1</td><td>13.0</td></tr><tr><td>Lenovo</td><td>13.7</td><td>14.7</td><td>16.5</td><td>16.9</td><td>15.2</td><td>17.0</td><td>19.3</td><td>19.4</td><td>16.5</td><td>16.6</td></tr><tr><td>Acer</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Others</td><td>16.7</td><td>16.3</td><td>19.8</td><td>19.1</td><td>18.6</td><td>19.6</td><td>21.4</td><td>21.3</td><td>17.8</td><td>17.5</td></tr><tr><td>Total PC Units</td><td>60.2</td><td>64.2</td><td>71.0</td><td>71.6</td><td>65.9</td><td>71.7</td><td>78.5</td><td>80.5</td><td>67.9</td><td>68.2</td></tr><tr><td>Units market share</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Apple</td><td>8%</td><td>8%</td><td>8%</td><td>10%</td><td>9%</td><td>9%</td><td>9%</td><td>9%</td><td>9%</td><td>10%</td></tr><tr><td>ASUS</td><td>6%</td><td>7%</td><td>8%</td><td>7%</td><td>6%</td><td>7%</td><td>8%</td><td>7%</td><td>7%</td><td>7%</td></tr><tr><td>Dell Technologies</td><td>15%</td><td>16%</td><td>14%</td><td>14%</td><td>14%</td><td>14%</td><td>13%</td><td>15%</td><td>15%</td><td>14%</td></tr><tr><td>HP Inc</td><td>20%</td><td>21%</td><td>19%</td><td>19%</td><td>19%</td><td>20%</td><td>19%</td><td>19%</td><td>18%</td><td>19%</td></tr><tr><td>Lenovo</td><td>23%</td><td>23%</td><td>23%</td><td>24%</td><td>23%</td><td>24%</td><td>25%</td><td>24%</td><td>24%</td><td>24%</td></tr><tr><td>Acer</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Others</td><td>28%</td><td>25%</td><td>28%</td><td>27%</td><td>28%</td><td>27%</td><td>27%</td><td>26%</td><td>26%</td><td>26%</td></tr><tr><td>Year-over-year change</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Units</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Apple</td><td>14%</td><td>8%</td><td>-15%</td><td>19%</td><td>19%</td><td>19%</td><td>12%</td><td>1%</td><td>11%</td><td>10%</td></tr><tr><td>ASUS</td><td>-5%</td><td>10%</td><td>7%</td><td>15%</td><td>13%</td><td>19%</td><td>12%</td><td>12%</td><td>18%</td><td>0%</td></tr><tr><td>Dell Technologies</td><td>-2%</td><td>-2%</td><td>-4%</td><td>0%</td><td>3%</td><td>-3%</td><td>3%</td><td>18%</td><td>8%</td><td>-5%</td></tr><tr><td>HP Inc</td><td>0%</td><td>2%</td><td>0%</td><td>-2%</td><td>6%</td><td>4%</td><td>10%</td><td>12%</td><td>-5%</td><td>-9%</td></tr><tr><td>Lenovo</td><td>8%</td><td>4%</td><td>3%</td><td>5%</td><td>11%</td><td>15%</td><td>17%</td><td>15%</td><td>9%</td><td>-2%</td></tr><tr><td>Acer</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Others</td><td>26%</td><td>29%</td><td>6%</td><td>9%</td><td>11%</td><td>20%</td><td>8%</td><td>12%</td><td>-4%</td><td>-10%</td></tr><tr><td>Total PC Units</td><td>2%</td><td>2%</td><td>1%</td><td>6%</td><td>10%</td><td>12%</td><td>11%</td><td>12%</td><td>3%</td><td>-5%</td></tr><tr><td></td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Quarter-over-Quarter growth</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Units</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Apple</td><td>-19%</td><td>7%</td><td>17%</td><td>18%</td><td>-20%</td><td>7%</td><td>10%</td><td>7%</td><td>-12%</td><td>6%</td></tr><tr><td>ASUS</td><td>-15%</td><td>17%</td><td>26%</td><td>-8%</td><td>-17%</td><td>23%</td><td>19%</td><td>-8%</td><td>-13%</td><td>5%</td></tr><tr><td>Dell Technologies</td><td>-6%</td><td>9%</td><td>-2%</td><td>1%</td><td>-4%</td><td>2%</td><td>3%</td><td>16%</td><td>-12%</td><td>-10%</td></tr><tr><td>HP Inc</td><td>-14%</td><td>14%</td><td>-1%</td><td>1%</td><td>-7%</td><td>12%</td><td>5%</td><td>3%</td><td>-21%</td><td>7%</td></tr><tr><td>Lenovo</td><td>-15%</td><td>7%</td><td>12%</td><td>2%</td><td>-10%</td><td>11%</td><td>14%</td><td>0%</td><td>-15%</td><td>0%</td></tr><tr><td>Acer</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Total PC Units</td><td>-11%</td><td>7%</td><td>11%</td><td>1%</td><td>-8%</td><td>9%</td><td>9%</td><td>3%</td><td>-16%</td><td>0%</td></tr></table>

PC shipments include desktops, notebooks, and workstations. Totals may be affected by rounding.

<table><tr><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>18.6</td><td>19.0</td><td>18.1</td><td>17.9</td><td>22.8</td><td>27.8</td><td>27.9</td><td>21.9</td><td>23.0</td><td>25.7</td></tr><tr><td>19.1</td><td>17.1</td><td>15.4</td><td>14.9</td><td>18.2</td><td>21.8</td><td></td><td>16.8</td><td>18.0</td><td>20.5</td></tr><tr><td>39.2</td><td>40.1</td><td>42.2</td><td>44.3</td><td>48.0</td><td>56.3</td><td>48.1</td><td>40.0</td><td>39.1</td><td>41.1</td></tr><tr><td>52.7</td><td>57.1</td><td>58.2</td><td>60.8</td><td>66.0</td><td>71.5</td><td>53.9</td><td>52.9</td><td>53.0</td><td>57.5</td></tr><tr><td>54.9</td><td>54.1</td><td>58.0</td><td>63.6</td><td>70.6</td><td>79.9</td><td>67.0</td><td>59.1</td><td>61.8</td><td>70.9</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>24.0</td><td>18.2</td><td></td><td></td><td></td></tr><tr><td>256.2</td><td>255.4</td><td>254.7</td><td>262.1</td><td>298.8</td><td>353.6</td><td>297.4</td><td>260.1</td><td>267.0</td><td>296.6</td></tr><tr><td>7%</td><td>7%</td><td>7%</td><td>7%</td><td>8%</td><td>8%</td><td>9%</td><td>8%</td><td>9%</td><td>9%</td></tr><tr><td>7%</td><td>7%</td><td>6%</td><td>6%</td><td>6%</td><td>6%</td><td>0%</td><td>6%</td><td>7%</td><td>7%</td></tr><tr><td>15%</td><td>16%</td><td>17%</td><td>17%</td><td>16%</td><td>16%</td><td>16%</td><td>15%</td><td>15%</td><td>14%</td></tr><tr><td>21%</td><td>22%</td><td>23%</td><td>23%</td><td>22%</td><td>20%</td><td>18%</td><td>20%</td><td>20%</td><td>19%</td></tr><tr><td>21%</td><td>21%</td><td>23%</td><td>24%</td><td>24%</td><td>23%</td><td>23%</td><td>23%</td><td>23%</td><td>24%</td></tr><tr><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td colspan="10"></td></tr><tr><td></td><td>2%</td><td>-5%</td><td>-1%</td><td>27%</td><td>22%</td><td>0%</td><td>-21%</td><td>5%</td><td>12%</td></tr><tr><td></td><td></td><td></td><td>-3%</td><td>22%</td><td></td><td></td><td></td><td>7%</td><td>14%</td></tr><tr><td></td><td>2%</td><td>5%</td><td>5%</td><td>8%</td><td>17%</td><td>-15%</td><td>-17%</td><td>-2%</td><td>5%</td></tr><tr><td></td><td>8%</td><td>2%</td><td>5%</td><td>9%</td><td>8%</td><td>-25%</td><td>-2%</td><td>0%</td><td>8%</td></tr><tr><td></td><td>-1%</td><td>7%</td><td>10%</td><td>11%</td><td>13%</td><td>-16%</td><td>-12%</td><td>5%</td><td>15%</td></tr><tr><td></td><td>0%</td><td>0%</td><td>3%</td><td>14%</td><td>18%</td><td>-16%</td><td>-13%</td><td>3%</td><td>11%</td></tr><tr><td colspan="10"></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: IDC

## Disclosure Appendix

## Reg AC

I, Katherine Murphy, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Katherine Murphy GS & Co. LLC, Michael Ng, CFA GS & Co. LLC, Zorayda Montemayor GS & Co. LLC.

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

The rating(s) for Apple Inc., Dell Technologies Inc. and HP Inc. is/are relative to the other companies in its/their coverage universe: AT&T Inc., American Tower Corp., Apple Inc., Arista Networks Inc., Axon Enterprise Inc., Blend Labs, Celestica Inc., Charter Communications Inc., Cisco Systems Inc., Cogent Communications Holdings, Comcast Corp., Compass Inc., Crown Castle Inc., Dell Technologies Inc., Digital Realty Trust Inc., Equinix Inc., F5 Inc., HP Inc., Hewlett Packard Enterprise Co., IREN Ltd., Ingram Micro, Lumen Technologies Inc., NetApp Inc., Opendoor Technologies Inc., Optimum Communications Inc., Penguin Solutions Inc., SBA Communications Corp., Stagwell Inc., Super Micro Computer Inc., T-Mobile US Inc., TD SYNNEX Corp., Verizon Communications, Versant Media Group, Walt Disney Co., Zillow Group

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the second most recent month end: Dell Technologies Inc. (\$417.28)

GS has received compensation for investment banking services in the past 12 months: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

GS has received compensation for non-investment banking services during the past 12 months: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

GS had an investment banking services client relationship during the past 12 months with: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

GS had a non-securities services client relationship during the past 12 months with: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

A director and/or employee of GS is a director: Dell Technologies Inc. (\$417.28)

GS makes a market in the securities or derivatives thereof: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

Distribution of ratings/investment banking relationships GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/f03beb9a5b88c5ef281c8d8330133645445b4cd34b4f2b9c88313db4301aabbe.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/2caecc86d58d69fe7287cc26cc1f29941f5dcbe245163e4e928914779ea40ec1.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/be4f30a4c46e94cfb04f569b8037c62cfc87b67d5ac98d3996487cedea9876a5.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

Apple Inc. (AAPL)  
Dell Technologies Inc. (DELL)

<table><tr><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td></tr><tr><td>0

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
