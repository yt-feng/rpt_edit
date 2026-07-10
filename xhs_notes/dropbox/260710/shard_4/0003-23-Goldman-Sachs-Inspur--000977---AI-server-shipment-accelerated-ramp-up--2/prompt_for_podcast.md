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
# Inspur (000977.SZ): AI server shipment accelerated ramp up; 2Q26 NI guidance beat

2Q26 NI guidance beat: Inspur reported strong 1H26 NI guidance at Rmb2.6bn\~Rmb3.1bn (+226% \~288% YoY), suggesting 2Q26 NI at Rmb2.0bn\~Rmb2.5bn, and beating our previous NI estimates of Rmb1.0bn. Management attributes the NI growth to (1) strong demand for AI servers, on rising China CSP AI Capex, (2) comprehensive product offerings with value-added solutions, and (3) secure procurement of upstream materials. We expect the company's revenue to grow at 22% CAGR in 2026-28E on the ongoing China CSP AI Capex cycle, while valuations appear stretched (above 5-year avg. P/E).

Allen Chang  
+852-2978-2930 |  
allen.k.chang@gs.com  
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

AI server ramp up ahead: We forecast China CSP's capex growth of +42%/ +14%/ +10% YoY in 2026-28E (link), and view the company as a key beneficiary of CSP clients' transition from AI servers empowered by global-tier GPUs to local AI chips. The company's inventory remains at a high level of Rmb44bn/ Rmb47bn in 1Q26/ 4Q25, supporting its AI server shipment ramp up ahead. Meanwhile, Inspur is also expanding to the SuperPOD architectural solution to meet clients' demand for large-scale deployment.

Ting Song +852-2978-6466 | ting.song@gs.com GS (Asia) L.L.C.

Earnings revision: We factor in Inspur's 2Q26 guidance and revise up earnings by $12\% / 2\% / 3\%$ in 2026-28E mainly on higher revenues of AI servers, driven by strong local CSP client demand and the company's shipment ramp up. We raise 2026 GM to reflect better product mix, while keep 2027-28E GM largely unchanged.

Source: Company data, GS Global Investment Research

Exhibit 1: Earnings revision

<table><tr><td rowspan="2">Rmb mn</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Old</td><td>New</td><td>Chg</td><td>Old</td><td>New</td><td>Chg</td><td>Old</td><td>New</td><td>Chg</td></tr><tr><td>Revenue</td><td>204,164</td><td>214,123</td><td>5%</td><td>250,893</td><td>259,093</td><td>3%</td><td>304,859</td><td>318,729</td><td>5%</td></tr><tr><td>GP</td><td>11,290</td><td>12,208</td><td>8%</td><td>13,313</td><td>13,603</td><td>2%</td><td>15,966</td><td>16,235</td><td>2%</td></tr><tr><td>OP</td><td>3,841</td><td>4,219</td><td>10%</td><td>4,400</td><td>4,530</td><td>3%</td><td>5,727</td><td>5,818</td><td>2%</td></tr><tr><td>Net income</td><td>3,593</td><td>4,010</td><td>12%</td><td>4,348</td><td>4,425</td><td>2%</td><td>5,645</td><td>5,787</td><td>3%</td></tr><tr><td>Margins</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GM</td><td>5.5%</td><td>5.7%</td><td></td><td>5.3%</td><td>5.3%</td><td></td><td>5.2%</td><td>5.1%</td><td></td></tr><tr><td>OPM</td><td>1.9%</td><td>2.0%</td><td></td><td>1.8%</td><td>1.7%</td><td></td><td>1.9%</td><td>1.8%</td><td></td></tr><tr><td>NM</td><td>1.8%</td><td>1.9%</td><td></td><td>1.7%</td><td>1.7%</td><td></td><td>1.9%</td><td>1.8%</td><td></td></tr></table>

Valuation: We continue to use near-term P/E to derive our 12M TP and our target P/E is updated to 23.7x 2027E EPS (vs. 21.1x previously) on lower forward year earnings growth, which is still derived from peers' correlation between trading P/E and forward year NI YoY, supported by the industry's re-rate on rising AI capex in China and strong client demand. Our peer group includes global and China AI infrastructure (e.g. AI server, general server, storage, etc.) suppliers. Our new TP is

Rmb71.4 (vs. Rmb62.5 previously).  
Exhibit 2: Inspur P&L Summary

<table><tr><td>Rmb m</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="9">Income statement</td><td colspan="6"></td></tr><tr><td>Revenues</td><td>46,858</td><td>33,334</td><td>40,477</td><td>44,113</td><td>35,470</td><td>54,336</td><td>60,353</td><td>63,964</td><td>65,867</td><td>114,767</td><td>164,782</td><td>214,123</td><td>259,093</td><td>318,729</td></tr><tr><td>GP</td><td>1,616</td><td>2,030</td><td>2,273</td><td>2,128</td><td>2,355</td><td>3,661</td><td>3,091</td><td>3,102</td><td>6,612</td><td>7,859</td><td>8,047</td><td>12,208</td><td>13,603</td><td>16,235</td></tr><tr><td>OP</td><td>495</td><td>582</td><td>676</td><td>66</td><td>949</td><td>1,701</td><td>845</td><td>724</td><td>1,167</td><td>1,949</td><td>1,819</td><td>4,219</td><td>4,530</td><td>5,818</td></tr><tr><td>Net income</td><td>463</td><td>336</td><td>683</td><td>931</td><td>605</td><td>1,979</td><td>736</td><td>689</td><td>1,783</td><td>2,292</td><td>2,413</td><td>4,010</td><td>4,425</td><td>5,787</td></tr><tr><td>EPS (Rmb)</td><td>0.32</td><td>0.23</td><td>0.46</td><td>0.64</td><td>0.41</td><td>1.35</td><td>0.50</td><td>0.47</td><td>1.21</td><td>1.56</td><td>1.64</td><td>2.73</td><td>3.01</td><td>3.94</td></tr><tr><td colspan="9">Margins</td><td colspan="6"></td></tr><tr><td>GM</td><td>3.4%</td><td>6.1%</td><td>5.6%</td><td>4.8%</td><td>6.6%</td><td>6.7%</td><td>5.1%</td><td>4.8%</td><td>10.0%</td><td>6.8%</td><td>4.9%</td><td>5.7%</td><td>5.3%</td><td>5.1%</td></tr><tr><td>OPM</td><td>1.1%</td><td>1.7%</td><td>1.7%</td><td>0.2%</td><td>2.7%</td><td>3.1%</td><td>1.4%</td><td>1.1%</td><td>1.8%</td><td>1.7%</td><td>1.1%</td><td>2.0%</td><td>1.7%</td><td>1.8%</td></tr><tr><td>NM</td><td>1.0%</td><td>1.0%</td><td>1.7%</td><td>2.1%</td><td>1.7%</td><td>3.6%</td><td>1.2%</td><td>1.1%</td><td>2.7%</td><td>2.0%</td><td>1.5%</td><td>1.9%</td><td>1.7%</td><td>1.8%</td></tr><tr><td colspan="9">Ratios</td><td colspan="6"></td></tr><tr><td>Opex ratio</td><td>2.4%</td><td>4.3%</td><td>3.9%</td><td>4.7%</td><td>4.0%</td><td>3.6%</td><td>3.7%</td><td>3.7%</td><td>8.3%</td><td>5.1%</td><td>3.8%</td><td>3.7%</td><td>3.5%</td><td>3.3%</td></tr><tr><td>R&amp;D ratio</td><td>1.4%</td><td>2.5%</td><td>2.4%</td><td>3.0%</td><td>2.4%</td><td>2.1%</td><td>2.2%</td><td>2.2%</td><td>4.7%</td><td>3.1%</td><td>2.3%</td><td>2.2%</td><td>2.2%</td><td>2.0%</td></tr><tr><td>Tax rate</td><td>17.5%</td><td>7.3%</td><td>10.5%</td><td>6.0%</td><td>4.9%</td><td>1.7%</td><td>3.1%</td><td>2.4%</td><td>1.7%</td><td>3.1%</td><td>2.4%</td><td>5.7%</td><td>5.0%</td><td>5.0%</td></tr><tr><td colspan="9">YoY</td><td colspan="6"></td></tr><tr><td>Revenues</td><td>166%</td><td>36%</td><td>-1%</td><td>39%</td><td>-24%</td><td>63%</td><td>49%</td><td>45%</td><td>-5%</td><td>74%</td><td>44%</td><td>30%</td><td>21%</td><td>23%</td></tr><tr><td>GP</td><td>14%</td><td>11%</td><td>-2%</td><td>-7%</td><td>46%</td><td>80%</td><td>36%</td><td>46%</td><td>-15%</td><td>19%</td><td>2%</td><td>52%</td><td>11%</td><td>19%</td></tr><tr><td>OP</td><td>34%</td><td>25%</td><td>-14%</td><td>-80%</td><td>92%</td><td>192%</td><td>25%</td><td>990%</td><td>-48%</td><td>67%</td><td>-7%</td><td>132%</td><td>7%</td><td>28%</td></tr><tr><td>Pretax income</td><td>57%</td><td>24%</td><td>-3%</td><td>-11%</td><td>39%</td><td>487%</td><td>11%</td><td>-26%</td><td>-16%</td><td>29%</td><td>4%</td><td>72%</td><td>10%</td><td>31%</td></tr><tr><td>Net income</td><td>51%</td><td>16%</td><td>-2%</td><td>-7%</td><td>31%</td><td>489%</td><td>8%</td><td>-26%</td><td>-15%</td><td>29%</td><td>5%</td><td>66%</td><td>10%</td><td>31%</td></tr><tr><td colspan="9">QoQ</td><td colspan="6"></td></tr><tr><td>Revenues</td><td>48%</td><td>-29%</td><td>21%</td><td>9%</td><td>-20%</td><td>53%</td><td>11%</td><td>6%</td><td rowspan="4" colspan="6"></td></tr><tr><td>GP</td><td>-30%</td><td>26%</td><td>12%</td><td>-6%</td><td>11%</td><td>55%</td><td>-16%</td><td>0%</td></tr><tr><td>OP</td><td>51%</td><td>18%</td><td>16%</td><td>-90%</td><td>1329%</td><td>79%</td><td>-50%</td><td>-14%</td></tr><tr><td>Net income</td><td>-54%</td><td>-27%</td><td>103%</td><td>36%</td><td>-35%</td><td>227%</td><td>-63%</td><td>-6%</td></tr></table>

Source: Company data, GS Global Investment Research

## Price Target Risks and Methodology - Inspur

Valuation: We derive our 12-m TP of Rmb71.4 on a target P/E multiple of 23.7x our 2027E EPS. Our target P/E of 23.7x is derived from the correlation between P/E and net income growth of its peers, based on the company's 2027E-28E net income YoY growth. We are Sell rated on Inspur. Upside risks: Stronger-than-expected generative AI demand in China; Faster-than-expected AI servers transition from global-tier GPU to local AI chips; Healthier-than-expected competition in AI servers in China.

<table><tr><td>000977.SZ</td><td colspan="2">12m Price Target: Rmb71.40</td><td colspan="2">Price: Rmb85.99</td><td colspan="2">Downside: 17.0%</td></tr><tr><td colspan="2">Sell</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td></td><td>Market cap:</td><td>Revenue (Rmb mn) New</td><td>164,782.0</td><td>214,123.3</td><td>259,093.1</td><td>318,728.8</td></tr><tr><td></td><td>Rmb126.3bn / $18.6bn</td><td>Revenue (Rmb mn) Old</td><td>164,782.0</td><td>204,163.8</td><td>250,893.0</td><td>304,858.9</td></tr><tr><td></td><td>Enterprise value:</td><td>EBITDA (Rmb mn)</td><td>2,641.4</td><td>5,054.3</td><td>5,376.6</td><td>6,613.7</td></tr><tr><td></td><td>Rmb129.2bn / $19.0bn</td><td>EPS (Rmb) New</td><td>1.64</td><td>2.73</td><td>3.01</td><td>3.94</td></tr><tr><td></td><td>3m ADTV: Rmb5.8bn / $853.7mn</td><td>EPS (Rmb) Old</td><td>1.64</td><td>2.45</td><td>2.96</td><td>3.84</td></tr><tr><td></td><td>China</td><td>P/E (X)</td><td>35.0</td><td>31.5</td><td>28.5</td><td>21.8</td></tr><tr><td></td><td>Greater China Technology</td><td>P/B (X)</td><td>3.8</td><td>5.0</td><td>4.4</td><td>3.8</td></tr><tr><td></td><td>M&amp;A Rank: 3</td><td>Dividend yield (%)</td><td>0.7</td><td>0.8</td><td>0.9</td><td>1.1</td></tr><tr><td></td><td>Leases incl. in net debt &amp; EV?: Yes</td><td>CROCI (%)</td><td>50.0</td><td>18.3</td><td>17.7</td><td>19.1</td></tr><tr><td></td><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td></td><td>EPS (Rmb)</td><td>0.41</td><td>1.35</td><td>0.50</td><td>0.47</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 9 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng and Ting Song, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C., Ting Song GS (Asia) L.L.C..

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

The rating(s) for Inspur is/are relative to the other companies in its/their coverage universe: AAC, ACM Research, AMEC, ASMPT, AVC, AccoTest, Anji Micro, Asus, Auras, BOE, BYDE, Biren, CR Micro, Cambricon, Chenbro, China Mobile (HK), China Telecom, China Tower Corp., China Unicom, Chinasoft Intl, Compal, Desay SV, E Ink, E-Town Semis, EHang, Empyrean, Eoptolink, FOCI, Fositek, Foxconn Industrial Internet, Gigabyte, Gigadevice, Glodon Co., HTC Corp., Hikvision, Hon Hai, Horizon Robotics, Hua Hong, Huace Navigation, Huaqin Co.(A), Huaqin Co.(H), Hwatsing, InnoScience, Innolight, Inspur, Insta360, Inventec, JCET, Kematek, King Slide, Kingdee, Kingsoft Office, LandMark, Largan, Lenovo, Lingyi, Maxscend, Meitu, MetaX, Mitac, Montage (A), Montage (H), NAURA, NSIG, Nexchip, OmniVision, Pegatron, Pony AI Inc. (ADR), Pony AI Inc. (H), Quanta, RoboTechnik, Ruijie Networks, SG Micro, SICC, SMIC (A), SMIC (H), SZS, Sangfor, SenseTime, Shengyi Tech, Shennan Circuits, StarPower, Sunny Optical, TFC Optical, Thundersoft, Tongyu Communication, Transsion, UMT, UNIS, VPEC, Vanchip, VeriSilicon, Victory Giant, WNC, WUS, WeRide, Wistron, Wiwynn, YJ Semitech, YOFC, Yonyou, ZTE (A), ZTE (H), iFlytek

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

There are no company-specific disclosures for: Inspur (Rmb85.99)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/51ea9fd564eb472d12d84fa286403df7acde966ac06c2c38aa4b74fc25d313ca.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Inspur (000977.SZ)

<table><tr><td>Date of report</td><td>Target price (Rmb)</td><td>Closing price (Rmb)</td></tr><tr><td>23-Jun-26</td><td>62.50</td><td>64.00</td></tr><tr><td>04-May-26</td><td>76.50</td><td>69.75</td></tr><tr><td>02-Nov-25</td><td>86.50</td><td>65.23</td></tr><tr><td>28-Aug-25</td><td>88.30</td><td>67.90</td></tr><tr><td>16-Jul-25</td><td>77.80</td><td>54.52</td></tr><tr><td>01-May-25</td><td>55.00</td><td>50.85</td></tr><tr><td>13-Apr-25</td><td>53.00</td><td>47.78</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts 

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
