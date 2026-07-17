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
# UMT (3491.TWO): AI data center from LEO Satellite; High-speed interconnection end application in expansion; Buy

UMT announced its plan to acquire a majority stake in high-frequency and high-speed interconnect solution provider DYNAHZ Technology (private) for NT\$1.7bn (Link). The company plans to own over 51% of DYNAHZ total shares, and expects to complete the transaction in Aug 2026. DYNAHZ Technology provides products across RF/ microwave/ Millimeter wave solution, and high-speed signal module, targeting high-speed interconnection, LEO satellite and semi applications. Management notes the company is developing THz (Terahertz) products, and the DYNAHZ acquisition would bring synergies through the company’s customer gain and penetration of AI data center business. While we do not take a view on the likelihood of the proposed deal being completed, we are positive on the company’s potential strategic expansion towards AI data center space. Maintain Buy.

UMT provides rectangular waveguides, which are conducting pipes with a rectangular cross-section used to guide the propagation of microwave or mmwave signals. Different shapes and combinations of waveguides can form various RF passive components, such as filter / diplexer, coupler, isolator, antenna, power amplifiers (PAs), etc. The company serves leading global LEO satellite operators, and its waveguides can be seen in LEO satellites / payloads (main), and gateways in ground stations.

Synergies on AI data center business: DYNAHZ Technology mainly provides RF/microwave/ Millimeter wave solution, and high-speed signal modules for AI data center and satellite clients. DYNAHZ has penetrated AI data center clients, and UMT is also verifying its THz products with clients. Management expects to see synergies from the acquisition, and the company is able to provide different types of interconnection solutions for a larger client base. DYNAHZ is expanding its new factory in Kaohsiung, targeting to improve the capacity by 2-3x by 2028E to support rising client demand.

Expanding Terahertz products: Management is positive on the rising adoption of THz (Terahertz) on the next generation of architecture in AI data center and 6G applications, supported by high speed interconnection and high price-to-performance ratio. UMT has built its first THz Testing lab in the factory back to Aug 2022 (Link), and management notes the company is verifying its THz products with multiple clients. We would expect the proposed acquisition of a high-speed/high-frequency player to be complementary to company's Terahertz business.

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Ting Song
+852-2978-6466 | ting.song@gs.com
GS (Asia) L.L.C.

Exhibit 1: UMT P&L Summary

<table><tr><td>NT$ mn</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td rowspan="24"></td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td colspan="7">Income statement</td><td colspan="4"></td><td colspan="4"></td></tr><tr><td>Revenue</td><td>1,585</td><td>2,335</td><td>2,452</td><td>4,276</td><td>8,991</td><td>12,645</td><td>620</td><td>514</td><td>484</td><td>834</td><td>1,020</td><td>966</td><td>1,042</td><td>1,249</td></tr><tr><td>Gross profit</td><td>641</td><td>1,198</td><td>1,254</td><td>2,706</td><td>6,060</td><td>8,732</td><td>314</td><td>223</td><td>229</td><td>489</td><td>592</td><td>576</td><td>691</td><td>848</td></tr><tr><td>OP income</td><td>202</td><td>624</td><td>575</td><td>1,559</td><td>3,560</td><td>5,242</td><td>167</td><td>94</td><td>84</td><td>230</td><td>314</td><td>318</td><td>413</td><td>515</td></tr><tr><td>Net income</td><td>200</td><td>547</td><td>518</td><td>1,262</td><td>2,851</td><td>4,135</td><td>143</td><td>71</td><td>88</td><td>216</td><td>253</td><td>260</td><td>335</td><td>414</td></tr><tr><td>EPS (NT$)</td><td>3.12</td><td>8.27</td><td>7.60</td><td>18.39</td><td>41.55</td><td>60.27</td><td>2.09</td><td>1.07</td><td>1.29</td><td>3.15</td><td>3.69</td><td>3.79</td><td>4.88</td><td>6.03</td></tr><tr><td colspan="7">Ratios</td><td colspan="4"></td><td colspan="4"></td></tr><tr><td>Opex ratio</td><td>27.7%</td><td>24.6%</td><td>27.7%</td><td>26.8%</td><td>27.8%</td><td>27.6%</td><td>23.7%</td><td>25.1%</td><td>29.9%</td><td>31.0%</td><td>27.2%</td><td>26.7%</td><td>26.7%</td><td>26.7%</td></tr><tr><td>Tax rate</td><td>19.4%</td><td>21.7%</td><td>19.0%</td><td>21.7%</td><td>22.0%</td><td>22.0%</td><td>21.9%</td><td>7.7%</td><td>21.8%</td><td>19.1%</td><td>22.0%</td><td>22.0%</td><td>22.0%</td><td>22.0%</td></tr><tr><td colspan="7">Margins</td><td colspan="4"></td><td colspan="4"></td></tr><tr><td>Gross margin</td><td>40.4%</td><td>51.3%</td><td>51.1%</td><td>63.3%</td><td>67.4%</td><td>69.1%</td><td>50.6%</td><td>43.3%</td><td>47.3%</td><td>58.6%</td><td>58.0%</td><td>59.6%</td><td>66.3%</td><td>67.9%</td></tr><tr><td>Operating margin</td><td>12.8%</td><td>26.7%</td><td>23.4%</td><td>36.5%</td><td>39.6%</td><td>41.5%</td><td>26.9%</td><td>18.2%</td><td>17.4%</td><td>27.6%</td><td>30.7%</td><td>15.4%</td><td>39.6%</td><td>41.2%</td></tr><tr><td>Net margin</td><td>12.6%</td><td>23.4%</td><td>21.1%</td><td>29.5%</td><td>31.7%</td><td>32.7%</td><td>23.0%</td><td>13.8%</td><td>18.2%</td><td>25.9%</td><td>24.8%</td><td>150.0%</td><td>32.1%</td><td>33.2%</td></tr><tr><td colspan="7">YoY</td><td colspan="4"></td><td colspan="4"></td></tr><tr><td>Revenue</td><td>-14%</td><td>47%</td><td>5%</td><td>74%</td><td>110%</td><td>41%</td><td>43%</td><td>-21%</td><td>-24%</td><td>36%</td><td>65%</td><td>88%</td><td>115%</td><td>50%</td></tr><tr><td>Gross profit</td><td>-15%</td><td>87%</td><td>5%</td><td>116%</td><td>124%</td><td>44%</td><td>60%</td><td>-38%</td><td>-31%</td><td>56%</td><td>89%</td><td>159%</td><td>202%</td><td>74%</td></tr><tr><td>OP income</td><td>-31%</td><td>208%</td><td>-8%</td><td>171%</td><td>128%</td><td>47%</td><td>117%</td><td>-53%</td><td>-55%</td><td>40%</td><td>88%</td><td>240%</td><td>390%</td><td>124%</td></tr><tr><td>Net income</td><td>-26%</td><td>173%</td><td>-5%</td><td>143%</td><td>126%</td><td>45%</td><td>84%</td><td>-60%</td><td>-33%</td><td>36%</td><td>77%</td><td>266%</td><td>279%</td><td>92%</td></tr><tr><td colspan="7">QoQ</td><td colspan="4"></td><td colspan="4"></td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1%</td><td>-17%</td><td>-6%</td><td>72%</td><td>22%</td><td>-5%</td><td>8%</td><td>20%</td></tr><tr><td>Gross profit</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0%</td><td>-29%</td><td>3%</td><td>113%</td><td>21%</td><td>-3%</td><td>20%</td><td>23%</td></tr><tr><td>OP income</td><td></td><td></td><td></td><td></td><td></td><td></td><td>2%</td><td>-44%</td><td>-10%</td><td>173%</td><td>36%</td><td>1%</td><td>30%</td><td>25%</td></tr><tr><td>Net income</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-10%</td><td>-50%</td><td>24%</td><td>145%</td><td>17%</td><td>3%</td><td>28%</td><td>24%</td></tr></table>

Source: Company data, GS Global Investment Research

## Price target risks and methodology - UMT

Valuation: We use a discounted P/E methodology and apply a 37.0x target P/E multiple to UMT's 2029E EPS, discounting it back to 2027E at a COE of 7.8% (beta 1.2x, risk-free rate 1.6% and market risk premium at 5.1%), which leads to our 12-month target price of NT\$2,513. The target P/E is based on the average PEG&M ratio of peers in the satellite supply chain. We are Buy-rated on UMT.

Key Risks: Slower-than-expected LEO satellite deployment; Potential competition from new-entrant suppliers; LEO satellite operators manufacturing in-house components.

<table><tr><td>3491.TWO</td><td colspan="2">12m Price Target: NT$2,513.00</td><td colspan="2">Price: NT$1,310.00</td><td colspan="2">Upside: 91.8%</td></tr><tr><td colspan="2">Buy</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="9" colspan="2">Market cap: NT$86.8bn / $2.7bnEnterprise value:NT$86.1bn / $2.7bn3m ADTV: NT$3.4bn / $106.2mnTaiwanGreater China TechnologyM&amp;A Rank: 3Leases incl. in net debt &amp; EV?:Yes</td><td>Revenue (NT$ mn)</td><td>2,452.2</td><td>4,276.4</td><td>8,990.9</td><td>12,644.9</td></tr><tr><td>EBITDA (NT$ mn)</td><td>688.6</td><td>1,681.9</td><td>3,699.6</td><td>5,397.9</td></tr><tr><td>EPS (NT$)</td><td>7.60</td><td>18.39</td><td>41.55</td><td>60.27</td></tr><tr><td>P/E (X)</td><td>54.5</td><td>71.2</td><td>31.5</td><td>21.7</td></tr><tr><td>P/B (X)</td><td>9.0</td><td>26.7</td><td>22.6</td><td>18.4</td></tr><tr><td>Dividend yield (%)</td><td>1.4</td><td>1.1</td><td>2.5</td><td>3.6</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>(0.6)</td><td>(0.4)</td><td>(0.3)</td><td>(0.5)</td></tr><tr><td>CROCI (%)</td><td>21.5</td><td>45.3</td><td>90.1</td><td>136.1</td></tr><tr><td>FCF yield (%)</td><td>0.8</td><td>0.8</td><td>1.6</td><td>4.5</td></tr><tr><td colspan="2"></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td colspan="2"></td><td>EPS (NT$)</td><td>3.69</td><td>3.79</td><td>4.88</td><td>6.03</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 16 Jul 2026 close.

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

The rating(s) for UMT is/are relative to the other companies in its/their coverage universe: AAC, ACM Research, AMEC, ASMPT, AVC, AccoTest, Anji Micro, Asus, Auras, BOE, BYDE, Biren, CR Micro, Cambricon, Chenbro, China Mobile (HK), China Telecom, China Tower Corp., China Unicom, Chinasoft Intl, Compal, Desay SV, E Ink, E-Town Semis, EHang, Empyrean, Eoptolink, FOCI, Fositek, Foxconn Industrial Internet, Gigabyte, Gigadevice, Glodon Co., HTC Corp., Hikvision, Hon Hai, Horizon Robotics, Hua Hong, Huace Navigation, Huaqin Co.(A), Huaqin Co.(H), Hwatsing, InnoScience, Innolight, Inspur, Insta360, Inventec, JCET, Kematek, King Slide, Kingdee, Kingsoft Office, LandMark, Largan, Lenovo, Lingyi, Maxscend, Meitu, MetaX, Mitac, Montage (A), Montage (H), NAURA, NSIG, Nexchip, OmniVision, Pegatron, Pony AI Inc. (ADR), Pony AI Inc. (H), Quanta, RoboTechnik, Ruijie Networks, SG Micro, SICC, SMIC (A), SMIC (H), SZS, Sangfor, SenseTime, Shengyi Tech, Shennan Circuits, StarPower, Sunny Optical, TFC Optical, Thundersoft, Tongyu Communication, Transsion, UMT, UNIS, VPEC, Vanchip, VeriSilicon, Victory Giant, WNC, WUS, WeRide, Wistron, Wiwynn, YJ Semitech, YOFC, Yonyou, ZTE (A), ZTE (H), iFlytek

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

There are no company-specific disclosures for: UMT (NT\$1,310.00)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/7d0d7d0feb1e81a6d456799877acb8fc30fb07a97c92c28cb2f0293c5c52c7cf.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) UMT (3491.TWO)

<table><tr><td>Date of report</td><td>Target price (NT$)</td><td>Closing price (NT$)</td></tr><tr><td>29-May-26</td><td>2,513.00</td><td>2,200.00</td></tr><tr><td>10-May-26</td><td>2,208.00</td><td>1,655.00</td></tr><tr><td>16-Feb-26</td><td>2,007.00</td><td>1,400.00</td></tr><tr><td>22-Jan-26</td><td>1,333.00</td><td>986.00</td></tr><tr><td>15-Jan-26</td><td>992.00</td><td>890.00</td></tr><tr><td>05-Jan-26</td><td>863.00</td><td>766.00</td></tr><tr><td>22-Dec-25</td><td>751.00</td><td>635.00</td></tr><tr><td>07-Dec-25</td><td>655.00</td><td>529.00</td></tr><tr><td>30-Sep-25</td><td>581.00</td><td>447.50</td></tr><tr><td>03-Aug-25</td><td>510.00</td><td>344.50</td></tr><tr><td>09-Jul-25</td><td>592.00</td><td>335.00</td></tr><tr><td>04-May-25</td><td>626.00</td><td>379.00</td></tr><tr><td>06-Apr-25</td><td>588.00</td><td>415.00</td></tr><tr><td>17-Feb-25</td><td>591.00</td><td>391.50</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any

such system.
"""
