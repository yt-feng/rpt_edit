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
# StarPower (603290.SS): Product line diversification supporting growth ahead; 2Q26 NI guidance in line; Neutral

StarPower reported its 1H26 net income preliminary result (link), with 2Q26 net income mid-point -77% YoY / +48% QoQ to Rmb39m, in line with our estimate or 57% lower than Bloomberg consensus. Management attributes the net income YoY decline to (1) GM decline due to raw material price increase and (2) rising R&D spending on developing next-generation IGBT, SiC MOSFET, DrMOS, GaN power IC and module, which weighed on the company's profitability. Management mentioned that end customers acknowledge the rising raw material cost, but the product price adjustments must proceed according to established business processes. We remain positive on StarPower's product line expansion from IGBT to SiC MOSFET, GaN HEMT, and MCU, expanding end markets from EV to AI data center, industrial, robots, and home appliances to capture the rising end demand, and the company's GM would recover in the long run as new products' shipments ramp up. Maintain Neutral.

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Yifan Hu
+852-2978-0996 | yifan.hu@gs.com
GS (Asia) L.L.C.

Exhibit 1: StarPower 2Q26 net income guidance

<table><tr><td rowspan="2">Rmb m</td><td colspan="3">2Q26 pre-announcement</td><td rowspan="2">2Q26 G Se</td><td rowspan="2">Vs. Mid-point</td><td rowspan="2">2Q26 Consens us</td><td rowspan="2">Vs. Mid-point</td><td rowspan="2">2Q25</td><td rowspan="2">YoY</td><td rowspan="2">1Q26</td><td rowspan="2">QoQ</td></tr><tr><td>Low-end</td><td>High-end</td><td>Mid-point</td></tr><tr><td>Net income</td><td>29</td><td>49</td><td>39</td><td>39</td><td>1%</td><td>91</td><td>-57%</td><td>172</td><td>-77%</td><td>27</td><td>48%</td></tr></table>

Source: Company data, GS Global Investment Research, Bloomberg

Earnings revision: We factor in StarPower's 2Q26 net income guidance and revise down our 2026-28E net incomes by $13\%$ / $7\%$ / $6\%$ , mainly on lower GM and higher opex ratio. We cut our 2026-28E GMs by 1.0\~1.5ppts, reflecting the rising raw material cost weighing on the GM, while still modeling a GM uptrend in coming years as new products' shipments ramp up. We raise our 2026-28E opex ratios, mainly on higher R&D spending on developing next-generation products.

Exhibit 2: Earnings revision

<table><tr><td rowspan="2">(Rmb mn)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td></tr><tr><td>Revenue</td><td>4,615</td><td>4,615</td><td>0%</td><td>5,817</td><td>5,817</td><td>0%</td><td>6,351</td><td>6,351</td><td>0%</td></tr><tr><td>Gross profit</td><td>1,163</td><td>1,231</td><td>-6%</td><td>1,615</td><td>1,678</td><td>-4%</td><td>1,778</td><td>1,841</td><td>-3%</td></tr><tr><td>Operating income</td><td>463</td><td>540</td><td>-14%</td><td>829</td><td>893</td><td>-7%</td><td>918</td><td>983</td><td>-7%</td></tr><tr><td>Net income</td><td>501</td><td>577</td><td>-13%</td><td>855</td><td>918</td><td>-7%</td><td>941</td><td>1,005</td><td>-6%</td></tr><tr><td>Margins</td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td></tr><tr><td>Gross margin</td><td>25.2%</td><td>26.7%</td><td>-1.5ppts</td><td>27.8%</td><td>28.8%</td><td>-1.1ppts</td><td>28.0%</td><td>29.0%</td><td>-1ppts</td></tr><tr><td>Operating margin</td><td>10.0%</td><td>11.7%</td><td>-1.7ppts</td><td>14.2%</td><td>15.4%</td><td>-1.1ppts</td><td>14.5%</td><td>15.5%</td><td>-1ppts</td></tr><tr><td>Net margin</td><td>10.9%</td><td>12.5%</td><td>-1.6ppts</td><td>14.7%</td><td>15.8%</td><td>-1.1ppts</td><td>14.8%</td><td>15.8%</td><td>-1ppts</td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We continue to use near-term P/E to derive our 12M TP and our 2027E target P/E is updated to 33.8x (vs. 31.4 previously), mainly on higher avg. net income growth in 2027-28E, which is still derived from peers' forward trading P/E and net income growth. With the updated target multiple and earnings estimate, our 12M TP is unchanged at Rmb121.2. Maintain Neutral.

Exhibit 3: StarPower local and global peers' 2027 P/E and 27-28E earnings growth  
![](images/a132c9a693d049e7d51912cfdb8395a73d78d5b2cbbe5e573fe1fae827e71397.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 4: StarPower: 12m forward P/E  
![](images/66dfbb06143130ef7a1fc225ca549bada2506817784c8efe0e73fbd8a8e78924.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 5: StarPower P&L summary

<table><tr><td>(Rmb m)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenue</td><td>919</td><td>1,016</td><td>1,054</td><td>1,023</td><td>864</td><td>951</td><td>1,333</td><td>1,467</td><td>2,705</td><td>3,663</td><td>3,391</td><td>4,012</td><td>4,615</td><td>5,817</td><td>6,351</td></tr><tr><td>Gross profit</td><td>279</td><td>296</td><td>259</td><td>212</td><td>182</td><td>203</td><td>370</td><td>408</td><td>1,090</td><td>1,374</td><td>1,070</td><td>1,047</td><td>1,163</td><td>1,615</td><td>1,778</td></tr><tr><td>Operating income</td><td>99</td><td>158</td><td>92</td><td>6</td><td>18</td><td>27</td><td>192</td><td>226</td><td>788</td><td>956</td><td>563</td><td>356</td><td>463</td><td>829</td><td>918</td></tr><tr><td>Net income</td><td>104</td><td>172</td><td>106</td><td>23</td><td>27</td><td>39</td><td>200</td><td>235</td><td>818</td><td>911</td><td>508</td><td>405</td><td>501</td><td>855</td><td>941</td></tr><tr><td>EPS (Rmb)</td><td>0.43</td><td>0.72</td><td>0.44</td><td>0.10</td><td>0.11</td><td>0.16</td><td>0.84</td><td>0.98</td><td>4.79</td><td>5.33</td><td>2.12</td><td>1.69</td><td>2.09</td><td>3.57</td><td>3.93</td></tr><tr><td>Margins / ratio</td><td colspan="4"></td><td colspan="4"></td><td colspan="7"></td></tr><tr><td>Gross margin</td><td>30.4%</td><td>29.2%</td><td>24.5%</td><td>20.8%</td><td>21.1%</td><td>21.4%</td><td>27.7%</td><td>27.8%</td><td>40.3%</td><td>37.5%</td><td>31.6%</td><td>26.1%</td><td>25.2%</td><td>27.8%</td><td>28.0%</td></tr><tr><td>Opex ratio</td><td>-19.6%</td><td>-13.7%</td><td>-15.8%</td><td>-20.2%</td><td>-19.0%</td><td>-18.6%</td><td>-13.3%</td><td>-12.4%</td><td>-11.2%</td><td>-11.4%</td><td>-14.9%</td><td>-17.2%</td><td>-15.2%</td><td>-13.5%</td><td>-13.6%</td></tr><tr><td>Operating margin</td><td>10.8%</td><td>15.5%</td><td>8.8%</td><td>0.6%</td><td>2.0%</td><td>2.8%</td><td>14.4%</td><td>15.4%</td><td>29.1%</td><td>26.1%</td><td>16.6%</td><td>8.9%</td><td>10.0%</td><td>14.2%</td><td>14.5%</td></tr><tr><td>Net margin</td><td>13.7%</td><td>18.2%</td><td>10.7%</td><td>1.9%</td><td>3.2%</td><td>4.2%</td><td>15.4%</td><td>16.5%</td><td>34.3%</td><td>28.5%</td><td>17.9%</td><td>11.0%</td><td>11.1%</td><td>15.2%</td><td>15.4%</td></tr><tr><td>QoQ</td><td colspan="4"></td><td colspan="4"></td><td colspan="7"></td></tr><tr><td>Revenue</td><td>-6%</td><td>11%</td><td>4%</td><td>-3%</td><td>-16%</td><td>10%</td><td>40%</td><td>10%</td><td colspan="7"></td></tr><tr><td>Gross profit</td><td>-8%</td><td>6%</td><td>-13%</td><td>-18%</td><td>-14%</td><td>12%</td><td>82%</td><td>10%</td><td colspan="7"></td></tr><tr><td>Operating income</td><td>-20%</td><td>58%</td><td>-41%</td><td>-93%</td><td>182%</td><td>54%</td><td>614%</td><td>18%</td><td colspan="7"></td></tr><tr><td>Net income</td><td>23%</td><td>66%</td><td>-38%</td><td>-78%</td><td>14%</td><td>47%</td><td>411%</td><td>18%</td><td colspan="7"></td></tr><tr><td>EPS</td><td>23%</td><td>66%</td><td>-38%</td><td>-78%</td><td>14%</td><td>47%</td><td>411%</td><td>18%</td><td colspan="7"></td></tr><tr><td>YoY</td><td colspan="4"></td><td colspan="4"></td><td colspan="7"></td></tr><tr><td>Revenue</td><td>14%</td><td>40%</td><td>20%</td><td>5%</td><td>-6%</td><td>-6%</td><td>27%</td><td>43%</td><td>59%</td><td>35%</td><td>-7%</td><td>18%</td><td>15%</td><td>26%</td><td>9%</td></tr><tr><td>Gross profit</td><td>9%</td><td>30%</td><td>-8%</td><td>-30%</td><td>-35%</td><td>-31%</td><td>43%</td><td>92%</td><td>74%</td><td>26%</td><td>-22%</td><td>-2%</td><td>11%</td><td>39%</td><td>10%</td></tr><tr><td>Operating income</td><td>-40%</td><td>51%</td><td>-45%</td><td>-95%</td><td>-82%</td><td>-83%</td><td>108%</td><td>3537%</td><td>82%</td><td>21%</td><td>-41%</td><td>-37%</td><td>30%</td><td>79%</td><td>11%</td></tr><tr><td>Net income</td><td>-36%</td><td>53%</td><td>-28%</td><td>-72%</td><td>-74%</td><td>-77%</td><td>88%</td><td>906%</td><td>105%</td><td>11%</td><td>-44%</td><td>-20%</td><td>24%</td><td>70%</td><td>10%</td></tr><tr><td>EPS</td><td>-36%</td><td>53%</td><td>-28%</td><td>-72%</td><td>-74%</td><td>-77%</td><td>88%</td><td>906%</td><td>93%</td><td>11%</td><td>-60%</td><td>-20%</td><td>24%</td><td>70%</td><td>10%</td></tr></table>

Source: Company data, GS Global Investment Research

## Price Target Risks and Methodology - StarPower

Valuation methodology: We are Neutral rated on StarPower with a 12-month target price of Rmb121.2. We apply a 33.8x target P/E multiple to our 2027E EPS. Our target P/E multiple is derived from the sector's P/E-EPS YoY growth correlation.

## Key risks: 1) Stronger-/weaker-than-expected IGBT market growth, 2)

Faster-/slower-than-expected new design wins and market share gains, 3) new product development progressing faster/slower than expected, and 4) less/more competition.

<table><tr><td>603290.SS</td><td colspan="2">12m Price Target: Rmb121.20</td><td colspan="2">Price: Rmb84.84</td><td colspan="2">Upside: 42.9%</td></tr><tr><td colspan="2">Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11" colspan="2">Market cap: Rmb20.3bn / $3.0bnEnterprise value:Rmb20.8bn / $3.1bn3m ADTV: Rmb1.6bn / $229.8mnChinaGreater China TechnologyM&amp;A Rank: 3Leases incl. in net debt &amp; EV?: No</td><td>Revenue (Rmb mn) New</td><td>4,012.4</td><td>4,615.4</td><td>5,816.8</td><td>6,350.6</td></tr><tr><td>Revenue (Rmb mn) Old</td><td>4,012.4</td><td>4,615.4</td><td>5,816.8</td><td>6,350.6</td></tr><tr><td>EBITDA (Rmb mn)</td><td>805.7</td><td>1,425.2</td><td>1,778.1</td><td>1,861.6</td></tr><tr><td>EPS (Rmb) New</td><td>1.69</td><td>2.09</td><td>3.57</td><td>3.93</td></tr><tr><td>EPS (Rmb) Old</td><td>1.69</td><td>2.41</td><td>3.84</td><td>4.20</td></tr><tr><td>P/E (X)</td><td>54.4</td><td>40.5</td><td>23.8</td><td>21.6</td></tr><tr><td>P/B (X)</td><td>3.2</td><td>2.8</td><td>2.6</td><td>2.4</td></tr><tr><td>Dividend yield (%)</td><td>0.6</td><td>0.7</td><td>1.3</td><td>1.4</td></tr><tr><td>CROCI (%)</td><td>12.8</td><td>16.1</td><td>17.9</td><td>16.4</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>0.11</td><td>0.16</td><td>0.84</td><td>0.98</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 23 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng and Yifan Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C., Yifan Hu GS (Asia) L.L.C..

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

The rating(s) for StarPower is/are relative to the other companies in its/their coverage universe: AAC, ACM Research, AMEC, ASMPT, AVC, AccoTest, Anji Micro, Asus, Auras, BOE, BYDE, Biren, CR Micro, Cambricon, Chenbro, China Mobile (HK), China Telecom, China Tower Corp., China Unicom, Chinasoft Intl, Compal, Desay SV, E Ink, E-Town Semis, EHang, Empyrean, Eoptolink, FOCI, Fositek, Foxconn Industrial Internet, Gigabyte, Gigadevice, Glodon Co., HTC Corp., Hikvision, Hon Hai, Horizon Robotics, Hua Hong, Huace Navigation, Huaqin Co.(A), Huaqin Co.(H), Hwatsing, Iluvatar, InnoScience, Inspur, Insta360, Inventec, JCET, Kematek, King Slide, Kingdee, Kingsoft Office, LandMark, Largan, Lenovo, Lingyi, Maxscend, Meitu, MetaX, Mitac, Montage (A), Montage (H), NAURA, NSIG, Nexchip, OmniVision, Pegatron, Pony AI Inc. (ADR), Pony AI Inc. (H), Quanta, RoboTechnik, Ruijie Networks, SG Micro, SICC, SMIC (A), SMIC (H), SZS, Sangfor, SenseTime, Shengyi Tech, Shennan Circuits, StarPower, Sunny Optical, TFC Optical, Thundersoft, Tongyu Communication, Transsion, UMT, UNIS, VPEC, Vanchip, VeriSilicon, Victory Giant, WNC, WUS, WeRide, Wistron, Wiwynn, YJ Semitech, YOFC, Yonyou, ZTE (A), ZTE (H), iFlytek

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

There are no company-specific disclosures for: StarPower (Rmb84.84)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/57d26425ba915b53dac1671ab4b18e2996621475f4bfb79c5aa29515c716296f.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) StarPower (603290.SS)

<table><tr><td>Date of report</td><td>Target price (Rmb)</td><td>Closing price (Rmb)</td></tr><tr><td>02-Nov-25</td><td>121.20</td><td>104.58</td></tr><tr><td>28-Aug-25</td><td>105.90</td><td>108.04</td></tr><tr><td>05-Jun-25</td><td>92.50</td><td>81.30</td></tr><tr><td>08-Oct-24</td><td>101.50</td><td>100.38</td></tr><tr><td>11-Jul-24</td><td>88.96</td><td>80.32</td></tr><tr><td>07-Mar-24</td><td>183.00</td><td>104.71</td></tr><tr><td>27-Oct-23</td><td>2

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
