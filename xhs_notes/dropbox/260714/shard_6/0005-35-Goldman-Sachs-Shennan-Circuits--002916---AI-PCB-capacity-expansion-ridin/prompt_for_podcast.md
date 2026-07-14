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
# Shennan Circuits (002916.SZ): AI PCB capacity expansion riding on strong demand; 2Q26 NI guided at 44%\~67% YoY, in line; Buy

2Q26 NI guidance in line: Shennan reported 1H26 NI growth of 54%\~69% YoY at Rmb2.1bn to Rmb2.3bn, reflecting 2Q26 NI at Rmb1.25bn to Rmb1.45bn. The NI midpoint at Rmb1.35bn is in line with our 2Q NI estimate of Rmb1.36bn. Management attributed the strong NI growth in 1H to (1) capacity ramp up of Guangzhou factory with improving efficiency, (2) rising demand from AI computing and memory market, and (3) mix upgrade driving improved margin. We remain positive on the company's growth ahead, riding on AI server/ switch PCB spec upgrade, 1.6T optical module PCB ramp up, strong momentum of memory BT substrate, and improving ABF business. Maintain Buy.

Share issuance plan to support AI PCB capacity expansion: The company announced a new share issuance plan of \~Rmb4.9bn in Jun 2026, with proceeds of Rmb3.6bn planned to use on AI PCB capacity expansion in Wuxi PCB factory. We expect the company's Capex spending to reach Rmb6bn in 2026E (vs. Rmb3.8bn in 2025), supporting accelerated AI PCB capacity expansion to fulfill clients' demand. We believe Shennan's diversified data center exposure to AI servers, high-speed switches, and optical modules could help diversify risks.

Ting Song +852-2978-6466 | ting.song@gs.com GS (Asia) L.L.C.

Earnings revision: We factor in Shennan's 2Q26 NI guidance and revise up 2027/28E NI by $2\%$ / $2\%$ mainly on higher revenues of AI PCB, riding on capacity expansion and strong demand on AI server and optical module PCB. GM was revised up by 0.1ppts/ 0.2ppts in 2027/ 28E to reflect product mix upgrade.

Source: Company data, GS Global Investment Research

Allen Chang  
+852-2978-2930 |  
allen.k.chang@gs.com  
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Valuation: Our 12m TP remains based on a 2027E P/E (methodology unchanged). Our target P/E is revised up to 39.7x (vs. at 36.9x previously), mainly based on the company's 2027E-28E EPS growth and still derived from peer correlation between peers' 2027 trading P/E vs. the sum of 2027-28 EPS YoY growth and 2027-28 OPM (the PEG&M ratio). We think the higher multiple reflects re-rating potential on a more positive outlook on rising AI demand and higher-than-expected PCB / optical dollar content. With our updated earnings estimate and target multiple, our 12m TP is raised to Rmb494 (vs. Rmb450 previously).

Exhibit 1: Earnings revision

<table><tr><td rowspan="2">Rmb m</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Old</td><td>New</td><td>Diff (%)</td><td>Old</td><td>New</td><td>Diff (%)</td><td>Old</td><td>New</td><td>Diff (%)</td></tr><tr><td>Revenue</td><td>31,327</td><td>31,339</td><td>0%</td><td>43,361</td><td>43,756</td><td>1%</td><td>51,030</td><td>51,529</td><td>1%</td></tr><tr><td>GP</td><td>9,253</td><td>9,258</td><td>0%</td><td>13,653</td><td>13,840</td><td>1%</td><td>16,092</td><td>16,328</td><td>1%</td></tr><tr><td>OP</td><td>5,771</td><td>5,777</td><td>0%</td><td>8,952</td><td>9,134</td><td>2%</td><td>11,315</td><td>11,544</td><td>2%</td></tr><tr><td>Net income</td><td>5,235</td><td>5,240</td><td>0%</td><td>8,299</td><td>8,468</td><td>2%</td><td>10,497</td><td>10,710</td><td>2%</td></tr><tr><td>Margins</td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td></tr><tr><td>GM</td><td>29.5%</td><td>29.5%</td><td>0ppts</td><td>31.5%</td><td>31.6%</td><td>0.1ppts</td><td>31.5%</td><td>31.7%</td><td>0.2ppts</td></tr><tr><td>OPM</td><td>18.4%</td><td>18.4%</td><td>0ppts</td><td>20.6%</td><td>20.9%</td><td>0.2ppts</td><td>22.2%</td><td>22.4%</td><td>0.2ppts</td></tr><tr><td>NM</td><td>16.7%</td><td>16.7%</td><td>0ppts</td><td>19.1%</td><td>19.4%</td><td>0.2ppts</td><td>20.6%</td><td>20.8%</td><td>0.2ppts</td></tr></table>

Exhibit 2: Shennan P&L Summary

<table><tr><td>P&amp;L (Rmb mn)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenues</td><td>4,783</td><td>5,671</td><td>6,301</td><td>6,893</td><td>6,596</td><td>7,538</td><td>8,429</td><td>8,776</td><td>13,992</td><td>13,526</td><td>17,907</td><td>23,647</td><td>31,339</td><td>43,756</td><td>51,529</td></tr><tr><td>GP</td><td>1,183</td><td>1,564</td><td>1,978</td><td>1,971</td><td>1,924</td><td>2,276</td><td>2,501</td><td>2,558</td><td>3,571</td><td>3,170</td><td>4,447</td><td>6,696</td><td>9,258</td><td>13,840</td><td>16,328</td></tr><tr><td>OP</td><td>540</td><td>858</td><td>1,077</td><td>1,058</td><td>1,085</td><td>1,452</td><td>1,634</td><td>1,606</td><td>1,738</td><td>1,124</td><td>2,015</td><td>3,533</td><td>5,777</td><td>9,134</td><td>11,544</td></tr><tr><td>Pretax income</td><td>523</td><td>976</td><td>1,060</td><td>1,065</td><td>941</td><td>1,445</td><td>1,627</td><td>1,599</td><td>1,720</td><td>1,398</td><td>2,023</td><td>3,624</td><td>5,611</td><td>9,106</td><td>11,516</td></tr><tr><td>Net income</td><td>491</td><td>869</td><td>966</td><td>950</td><td>850</td><td>1,358</td><td>1,529</td><td>1,503</td><td>1,640</td><td>1,398</td><td>1,878</td><td>3,276</td><td>5,240</td><td>8,468</td><td>10,710</td></tr><tr><td>Margins</td><td colspan="4"></td><td colspan="4"></td><td colspan="7"></td></tr><tr><td>GM</td><td>24.7%</td><td>27.6%</td><td>31.4%</td><td>28.6%</td><td>29.2%</td><td>30.2%</td><td>29.7%</td><td>29.1%</td><td>25.5%</td><td>23.4%</td><td>24.8%</td><td>28.3%</td><td>29.5%</td><td>31.6%</td><td>31.7%</td></tr><tr><td>OPM</td><td>11.3%</td><td>15.1%</td><td>17.1%</td><td>15.4%</td><td>16.5%</td><td>19.3%</td><td>19.4%</td><td>18.3%</td><td>12.4%</td><td>8.3%</td><td>11.3%</td><td>14.9%</td><td>18.4%</td><td>20.9%</td><td>22.4%</td></tr><tr><td>NM</td><td>10.3%</td><td>15.3%</td><td>15.3%</td><td>13.8%</td><td>12.9%</td><td>18.0%</td><td>18.1%</td><td>17.1%</td><td>11.7%</td><td>10.3%</td><td>10.5%</td><td>13.9%</td><td>16.7%</td><td>19.4%</td><td>20.8%</td></tr><tr><td>Ratios</td><td colspan="4"></td><td colspan="4"></td><td colspan="7"></td></tr><tr><td>Opex ratio</td><td>13.4%</td><td>12.5%</td><td>14.3%</td><td>13.2%</td><td>12.7%</td><td>10.9%</td><td>10.3%</td><td>10.8%</td><td>13.1%</td><td>15.1%</td><td>13.6%</td><td>13.4%</td><td>11.1%</td><td>10.8%</td><td>9.3%</td></tr><tr><td>Tax rate</td><td>6.0%</td><td>10.9%</td><td>8.8%</td><td>10.7%</td><td>9.5%</td><td>6.0%</td><td>6.0%</td><td>6.0%</td><td>4.7%</td><td>0.0%</td><td>7.1%</td><td>9.5%</td><td>6.6%</td><td>7.0%</td><td>7.0%</td></tr><tr><td>YoY</td><td colspan="4"></td><td colspan="4"></td><td colspan="7"></td></tr><tr><td>Revenues</td><td>21%</td><td>30%</td><td>33%</td><td>42%</td><td>38%</td><td>33%</td><td>34%</td><td>27%</td><td>0%</td><td>-3%</td><td>32%</td><td>32%</td><td>33%</td><td>40%</td><td>18%</td></tr><tr><td>GP</td><td>19%</td><td>32%</td><td>65%</td><td>85%</td><td>63%</td><td>45%</td><td>26%</td><td>30%</td><td>8%</td><td>-11%</td><td>40%</td><td>51%</td><td>38%</td><td>49%</td><td>18%</td></tr><tr><td>OP</td><td>30%</td><td>41%</td><td>73%</td><td>188%</td><td>101%</td><td>69%</td><td>52%</td><td>52%</td><td>5%</td><td>-35%</td><td>79%</td><td>75%</td><td>63%</td><td>58%</td><td>26%</td></tr><tr><td>Net income</td><td>29%</td><td>43%</td><td>93%</td><td>144%</td><td>73%</td><td>56%</td><td>58%</td><td>58%</td><td>11%</td><td>-15%</td><td>34%</td><td>74%</td><td>60%</td><td>62%</td><td>26%</td></tr><tr><td>QoQ</td><td colspan="4"></td><td colspan="4"></td><td colspan="7"></td></tr><tr><td>Revenues</td><td>-2%</td><td>19%</td><td>11%</td><td>9%</td><td>-4%</td><td>14%</td><td>12%</td><td>4%</td><td rowspan="4" colspan="7"></td></tr><tr><td>GP</td><td>11%</td><td>32%</td><td>26%</td><td>0%</td><td>-2%</td><td>18%</td><td>10%</td><td>2%</td></tr><tr><td>OP</td><td>47%</td><td>59%</td><td>25%</td><td>-2%</td><td>3%</td><td>34%</td><td>13%</td><td>-2%</td></tr><tr><td>Net income</td><td>26%</td><td>77%</td><td>11%</td><td>-2%</td><td>-10%</td><td>60%</td><td>13%</td><td>-2%</td></tr></table>

Source: Company data, GS Global Investment Research

## Price Target Risks and Methodology - Shennan Circuits

We are Buy rated on Shennan Circuits with a 12-month target price of Rmb494, which is based on a 39.7x target P/E multiple on our 2027E EPS.

Downside risks: 1) slower-than-expected expansion to AI PCB; 2) fiercer-than-expected competition, which could lead to ASP erosion and margin pressure; 3) customer concentration risk; and 4) slower-than-expected server/automotive PCB and IC substrate growth.

<table><tr><td>002916.SZ</td><td>12m Price Target: Rmb494.00</td><td colspan="2">Price: Rmb393.59</td><td colspan="2">Upside: 25.5%</td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap:</td><td>Revenue (Rmb mn) New</td><td>23,647.0</td><td>31,338.7</td><td>43,756.0</td><td>51,528.8</td></tr><tr><td>Rmb201.9bn / $29.8bn</td><td>Revenue (Rmb mn) Old</td><td>23,647.0</td><td>31,326.7</td><td>43,360.8</td><td>51,030.1</td></tr><tr><td>Enterprise value:</td><td>EBITDA (Rmb mn)</td><td>5,150.4</td><td>7,638.6</td><td>11,567.3</td><td>14,264.5</td></tr><tr><td>Rmb204.2bn / $30.1bn</td><td>EPS (Rmb) New</td><td>4.91</td><td>7.69</td><td>12.43</td><td>15.72</td></tr><tr><td>3m ADTV: Rmb5.1bn / $754.7mn</td><td>EPS (Rmb) Old</td><td>4.91</td><td>7.69</td><td>12.18</td><td>15.41</td></tr><tr><td>China</td><td>P/E (X)</td><td>28.6</td><td>51.2</td><td>31.7</td><td>25.0</td></tr><tr><td>Greater China Technology</td><td>P/B (X)</td><td>5.5</td><td>12.9</td><td>10.1</td><td>7.9</td></tr><tr><td>M&amp;A Rank: 3</td><td>Dividend yield (%)</td><td>1.7</td><td>0.6</td><td>1.0</td><td>1.3</td></tr><tr><td>Leases incl. in net debt &amp; EV?: No</td><td>CROCI (%)</td><td>24.4</td><td>25.3</td><td>32.1</td><td>33.7</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (Rmb)</td><td>1.25</td><td>1.99</td><td>2.24</td><td>2.21</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 13 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Ting Song, Allen Chang and Verena Jeng, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Ting Song GS (Asia) L.L.C., Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C..

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

The rating(s) for Shennan Circuits is/are relative to the other companies in its/their coverage universe: AAC, ACM Research, AMEC, ASMPT, AVC, AccoTest, Anji Micro, Asus, Auras, BOE, BYDE, Biren, CR Micro, Cambricon, Chenbro, China Mobile (HK), China Telecom, China Tower Corp., China Unicom, Chinasoft Intl, Compal, Desay SV, E Ink, E-Town Semis, EHang, Empyrean, Eoptolink, FOCI, Fositek, Foxconn Industrial Internet, Gigabyte, Gigadevice, Glodon Co., HTC Corp., Hikvision, Hon Hai, Horizon Robotics, Hua Hong, Huace Navigation, Huaqin Co.(A), Huaqin Co.(H), Hwatsing, InnoScience, Innolight, Inspur, Insta360, Inventec, JCET, Kematek, King Slide, Kingdee, Kingsoft Office, LandMark, Largan, Lenovo, Lingyi, Maxscend, Meitu, MetaX, Mitac, Montage (A), Montage (H), NAURA, NSIG, Nexchip, OmniVision, Pegatron, Pony AI Inc. (ADR), Pony AI Inc. (H), Quanta, RoboTechnik, Ruijie Networks, SG Micro, SICC, SMIC (A), SMIC (H), SZS, Sangfor, SenseTime, Shengyi Tech, Shennan Circuits, StarPower, Sunny Optical, TFC Optical, Thundersoft, Tongyu Communication, Transsion, UMT, UNIS, VPEC, Vanchip, VeriSilicon, Victory Giant, WNC, WUS, WeRide, Wistron, Wiwynn, YJ Semitech, YOFC, Yonyou, ZTE (A), ZTE (H), iFlytek

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Shennan Circuits (Rmb393.59)

GS had an investment banking services client relationship during the past 12 months with: Shennan Circuits (Rmb393.59)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment

banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/179344e4e01b7766684f6c8def0e2b1d76678a374198fd4a8c803b225471fdd3.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Shennan Circuits (002916.SZ)

Date of report Target price (Rmb) Closing price (Rmb)

<table><tr><td>25-May-26</td><td>450.00</td><td>400.00</td></tr><tr><td>06-May-26</td><td>394.00</td><td>318.75</td></tr><tr><td>09-Feb-26</td><td>290.00</td><td>246.05</td></tr><tr><td>20-Nov-25</td><td>254.00</td><td>197.88</td></tr><tr><td>19-Aug-25</td><td>150.00</td><td>145.00</td></tr><tr><td>14-Jul-25</td><td>132.00</td><td>123.98</td></tr><tr><td>24-Apr-25</td><td>152.00</td><td>81.75</td></tr><tr><td>13-Mar-25</td><td>150.00</td><td>98.46</td></tr><tr><td>17-Feb-25</td><td>162.00</td><td>113.83</td></tr><tr><td>26-Dec-24</td><td>143.00</td><td>98.89</td></tr><tr><td>17-Sep-24</td><td>135.00</td><td>73.53</td></tr><tr><td>29-Jul-24</td><td>98.00</td><td>85.71</td></tr><tr><td>18-Apr-24</td><td>94.00</td><td>68.64</td></tr><tr><td>18-Mar-24</td><td>86.00</td><td>70.58</td></tr><tr><td>20-Feb-24</td><td>76.00</td><td>44.14</td></tr><tr><td>20-Nov-23</td><td>88.00</td><td>59.29</td></tr><tr><td>24-Aug-23</td><td>79.00</td><td>49.01</td></tr><tr><td>25-Jul-23</td><td>91.00</td><td>61.35</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosur

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY

10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
