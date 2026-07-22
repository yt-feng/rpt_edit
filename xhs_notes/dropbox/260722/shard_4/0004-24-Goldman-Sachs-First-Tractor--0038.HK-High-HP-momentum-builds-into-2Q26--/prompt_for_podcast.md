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
# First Tractor (0038.HK): High-HP momentum builds into 2Q26; reiterate Buy

First Tractor is scheduled to report 2Q26 results on August 25. Latest industry data point to a sustained recovery in China's agricultural tractor market, with medium-to-high HP production up $22\%$ yoy and high-HP output up $41\%$ yoy, supported by resilient exports, improving domestic demand, and a record-high high-HP mix. We expect First Tractor to benefit from the demand rebound and product mix upgrade, forecasting $25\%$ yoy revenue growth and $40\%$ yoy core EBIT growth in 2Q26, while net profit growth is likely to be more modest at $6\%$ yoy due to a high base from one-off gains in 2Q25. We reiterate our Buy ratings on both A- and H-shares and raise our 12-m TPs to Rmb21.3 and HKD13.9, respectively.

Nick Zheng, CFA
+852-2978-1405 | nick.zheng@gs.com
GS (Asia) L.L.C.

Selina Yan
+852-2978-0178 | shuling.yan@gs.com
GS (Asia) L.L.C.

## Industry trends in 2Q26:

Industry production accelerated further in 2Q26 after the 1Q26 inflection. Medium-to-high HP tractor output has sustained $20\%+$ yoy growth since April, while high-HP tractors have maintained robust mid-double-digit yoy growth since May. As a result, 2Q26 medium-to-high HP tractor production increased $22\%$ yoy, driven by a strong $41\%$ yoy rebound in high-HP tractors, pushing second-quarter volumes to a record high.

■ Supported by strong high-HP expansion, the high-HP mix within the medium-to-high HP segment reached a historic high of 37% in 2Q26, nearly double the historical second-quarter average of 20%. By geography:

Despite ongoing geopolitical conflicts, exports maintained strong momentum in 2Q26, with medium-to-high HP tractor export volumes rising $40\%$ yoy and high-HP tractor exports surging $56\%$ yoy. By region, double-digit yoy growth was recorded across all key markets except Africa, where medium-HP tractor exports faced a high base last year.

☐ Implied domestic demand, measured as production minus exports, posted solid 16% yoy growth in 2Q26, led by a notable 38% yoy increase in the high-HP segment. A key driver was favorable crop pricing, with the average price of major crops up 5% YTD and 10% above last year's trough.

## First Tractor 2Q26 preview

■ Strong topline and core EBIT growth projected in 2Q26: We believe First Tractor is a key beneficiary of the industry demand rebound and product mix improvement. We expect revenue to grow 25% yoy in 2Q26, with GPM expanding to 16.8% (+0.5ppt yoy / +0.3ppt qoq). As a result, we forecast core EBIT growth of 40% yoy. Given the large one-off gain recorded in 2Q25, we expect 2Q26 net profit to increase 6% yoy.

Valuation: We maintain our 2026E–2028E full-year earnings forecasts, which remain 8%–18% above consensus. We roll forward our valuation base to mid-2027E, from end-2026E previously, leading to new 12-month target prices of Rmb21.3 / HKD13.9 for the A/H shares, up from Rmb19.5 / HKD13.0 previously.

Exhibit 1: First Tractor's share prices historically trade on tractor industry production volume

First Tractor's H/A share price performances (indexed) vs. monthly tractor industry production volume (12M-MA yoy chg%)

Exhibit 3: The high-HP mix within the medium-to-high HP segment reached a historic high of $37\%$ in 2Q26, almost doubling the historical 2Q average China quarter medium-to-high HP tractor production volume mix trends (1Q15-2Q26)  
![](images/aeeaa7bb562185cd18125d945702a5dff2b7e7c2b64fdd973dbbaa6170ce8264.jpg)  
Source: Wind, NBS, GS Global Investment Research

Exhibit 2: China's medium-to-high HP tractors production volume saw strong growth of $+22\%$ yoy in 2Q26, with high-HP tractors recording robust rebound of $+41\%$ yoy China quarter medium-to-high HP tractor production volume (k units) and $\%$ yoy (RHS)  
![](images/2f31fe704db58033b699a3c94d96a3758709629e82ef37c6737af5d74cd22be7.jpg)  
Source: NBS

![](images/af137939456b57dfc9f410c23b1b0591dc8e5438ab59f0bb3ffec4785f892ca4.jpg)  
Source: NBS

Exhibit 4: The average price of major crops saw solid growth of +5% YTD, up +10% vs. the low-end last year China M/H-HP tractor monthly production volume 12M-MA chg% yoy (RHS) vs. average price of major crops  
![](images/40d417ba3bb9c3674716d580a59b9b310ba7255359c94c83f5336837d8a7183c.jpg)  
Source: NBS

Exhibit 5: Earnings revision summary

<table><tr><td rowspan="2"></td><td rowspan="2">Target Price (RMB/share)</td><td colspan="3">Revenue</td><td colspan="3">Net profit</td><td colspan="3">EPS</td></tr><tr><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>First Tractor (601038.SS/0038.HK)</td><td></td><td colspan="3">Rmb mn</td><td colspan="3">Rmb mn</td><td colspan="3">Rmb</td></tr><tr><td>Gse (New)</td><td>RMB 21.30/HKD 13.90</td><td>12,591</td><td>14,857</td><td>17,134</td><td>947</td><td>1,163</td><td>1,471</td><td>0.84</td><td>1.04</td><td>1.31</td></tr><tr><td>Gse (Old)</td><td>RMB 19.50/HKD 13.00</td><td>12,591</td><td>14,857</td><td>17,134</td><td>947</td><td>1,163</td><td>1,471</td><td>0.84</td><td>1.04</td><td>1.31</td></tr><tr><td>% diff</td><td>9%/7%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Wind Consensus</td><td></td><td>11,662</td><td>12,614</td><td>14,222</td><td>904</td><td>1,057</td><td>1,203</td><td>0.80</td><td>0.94</td><td>1.07</td></tr><tr><td>% diff</td><td></td><td>8%</td><td>18%</td><td>20%</td><td>5%</td><td>10%</td><td>22%</td><td>5%</td><td>10%</td><td>22%</td></tr></table>

Source: Company data, Wind, GS Global Investment Research

## Price Target Risks and Methodology - First Tractor

Valuation: We derive our 12-m target price of HK\$13.9/share for First Tractor-H from an average of near- and long-term valuation. We apply a target P/E of 10.5x (in line with the long-term mid-cycle average) to 2026E/2027E average EPS to derive our near-term valuation, while applying a target P/E of 12x on 2030E EPS (referencing to the long-term mid-cycle average of its global peers), discounted back to mid-2027E using a CoE of 9.5% to arrive at our long-term valuation. Our 12-m target price of Rmb21.3/share for First Tractor-A incorporates a 67% A/H premium, consistent with the average A/H premium for First Tractor over the past 6 months.

Key downside risks: 1) weaker-than-expected crop prices; 2) unfavorable changes in gov't subsidy policy for agricultural equipment; 3) intensifying market competition; 4) execution risks relating product mix upgrade; 5) slower-than-expected localization of key components; 6) slower-than-expected progress in overseas market expansion.

## Investment Thesis - First Tractor

First Tractor is China's largest producer of agricultural tractors by sales revenue in 2024. We view First Tractor as well positioned to capture the structural growth opportunities brought by China's tractor upsizing (towards high-HP tractors) and upgrading (towards intelligent tractors) trend in light of China's transition towards agricultural modernization to achieve food security. Exports, presenting c.3x the TAM opportunity in EMs (c.US\$10bn) vs. the domestic market (2024), could add another leg of growth over the long term as First Tractor builds its global competitiveness. We believe these structural shifts should drive a gradual convergence of First Tractor's margin and return profiles towards its global peers and warrant a re-rating for the stock, which we view as undervalued. We are Buy rated on both A-share and H-share.

<table><tr><td>0038.HK</td><td>12m Price Target: HK$13.90</td><td>Price: HK$8.62</td><td>Upside: 61.3%</td></tr><tr><td>601038.SS</td><td>12m Price Target: Rmb21.30</td><td>Price: Rmb13.79</td><td>Upside: 54.5%</td></tr></table>

<table><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: HK$9.7bn / $1.2bn</td><td>Revenue (Rmb mn)</td><td>10,822.6</td><td>12,591.4</td><td>14,857.2</td><td>17,133.8</td></tr><tr><td rowspan="2">Enterprise value:HK$7.6bn / $970.1mn</td><td>EBITDA (Rmb mn)</td><td>815.3</td><td>997.4</td><td>1,285.6</td><td>1,646.4</td></tr><tr><td>EPS (Rmb)</td><td>0.72</td><td>0.84</td><td>1.04</td><td>1.31</td></tr><tr><td>3m ADTV: HK$33.6mn / $4.3mn</td><td>P/E (X)</td><td>9.1</td><td>8.8</td><td>7.2</td><td>5.7</td></tr><tr><td rowspan="3">China Battery, Machinery &amp; Advanced MaterialsM&amp;A Rank: 3</td><td>P/B (X)</td><td>0.9</td><td>0.9</td><td>0.9</td><td>0.8</td></tr><tr><td>Dividend yield (%)</td><td>4.1</td><td>4.2</td><td>5.1</td><td>6.5</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>(1.8)</td><td>(2.4)</td><td>(2.8)</td><td>(3.0)</td></tr><tr><td rowspan="2">Leases incl. in net debt &amp; EV?:Yes</td><td>CROCI (%)</td><td>11.6</td><td>13.1</td><td>15.5</td><td>19.0</td></tr><tr><td>FCF yield (%)</td><td>9.1</td><td>15.6</td><td>20.2</td><td>22.6</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (Rmb)</td><td>0.50</td><td>0.22</td><td>0.25</td><td>(0.13)</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 21 Jul 2026 close.

## Disclosure Appendix

## Reg AC

I, Nick Zheng, CFA, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Nick Zheng, CFA GS (Asia) L.L.C., Selina Yan GS (Asia) L.L.C..

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

The rating(s) for First Tractor (A) and First Tractor (H) is/are relative to the other companies in its/their coverage universe: Boqian New Materials, CALB Co., CATL (A), CATL (H), China Jushi, EVE Energy, Farasis Energy, First Tractor (A), First Tractor (H), Gotion High-Tech, Jiangsu Hengli Hydraulic Co., Lonking Holdings, Milkyway, NHU, REPT BATTERO Energy, Rianlon, Richful, Sany Heavy, Sinocera Functional Material, Sinotruk, Sunresin, Wanhua Chemical Group, Weichai Power (A), Weichai Power (H), Zenergy, Zhejiang Dingli Co Ltd.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

There are no company-specific disclosures for: First Tractor (A) (Rmb13.79) and First Tractor (H) (HK\$8.62)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/ce53adc88b44c51813cb82f0a2bfd412e5e7846a5042d9ff25d81a5096226661.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/71042220c0f4841009651b9365fda2b298741af7fe805ac9dcab8c42f92620f0.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## First Tractor (H) (0038.HK)

Date of report Target price (HK\$) Closing price (HK\$)

30-Mar-26 13.00 8.41

09-Dec-25 14.00 7.20

## First Tractor (A) (601038.SS)

Date of report Target price (Rmb) Closing price (Rmb)

30-Mar-26 19.50 12.75

09-Dec-25 21.00 12.69

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States
The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other 

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
