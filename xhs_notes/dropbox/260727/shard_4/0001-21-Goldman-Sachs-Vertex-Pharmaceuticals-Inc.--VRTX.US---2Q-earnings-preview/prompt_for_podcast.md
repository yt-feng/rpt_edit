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
# Vertex Pharmaceuticals Inc. (VRTX): 2Q earnings preview: Facing an eventful 2H

VRTX shares have underperformed the sector and broader market YTD (-5% vs. DRG, vs. -2% vs. S&P 500), as SION's likely August Phase 2 data in cystic fibrosis (CF; evaluating an add-on to VRTX's standard-of-care Trikafta) has served as an overhang. While SION has framed the bar-for-success as a 10mmol/L reduction on key biomarker sweat chloride (SwCI), for VRTX shares the bar is higher and we will evaluate the data in the context of its portfolio and ongoing serial innovation in CF (see our note here). Post, we see it as attractively positioned into: 1) the povetacicept launch in IgA nephropathy, noting a November 30 PDUFA, a new product cycle – in our view, the totality of the data to-date (hematuria and monthly administration, key in the context of a chronic therapy) supports best-in-class potential, and 2) data from the CRNX assets given the proposed acquisition, including Phase 2 open-label extension atumelnant data in congenital adrenal hyperplasia (CAH) and Cushings syndrome potentially this year followed by Phase 3 data in 2027 – the acquisition has been debated by investors on valuation. We also expect Phase 1/2 CF data from next-generation CFTR modulator VX-828 and initial Phase 1/2 DM1 data in 2H and Phase 3 inaxaplin data in APOL1-mediated kidney disease (AMKD) in early-2027 (we also expect Phase 2 inaxaplin data in the co-morbid diabetes and moderate proteinuria populations in 2H, albeit are more cautious given less supporting data and following mixed data from MAZE).

We expect an in-line quarter (GSe/company-compiled total revenue of \$3,155mn/\$3,219mn; non-GAAP EPS of \$4.57/\$4.70) and note VRTX has historically raised revenue guidance on 2Q EPS, outside of 2Q25 (FY26 total revenue of \$12.95bn-\$13.1bn (+8.5% YoY at the midpoint); GSe/consensus of \$13.1bn/\$13.0bn) with revenue typically meeting consensus, and earnings per share either meeting or exceeding consensus. We model for 2Q Alyfrek revenue of \$490mn vs. company-compiled consensus of \$515mn. We expect questions on the call on: 1) the aforementioned SION data and VRTX's approach to further clinical innovation in CF, 2) povetacicept pre-launch activities, noting VRTX is building an initial salesforce covering nephrologists who see >90% of US patients (estimated at 120-150, larger than competitor VERA and Otsuka salesforces of 80/100, respectively), 3) the probability-of-success for inaxaplin in AMKD, where we see positive readthrough from the Phase 2 data published in the New England Journal of Medicine, and 4) the commercial outlook for the CRNX assets, Palsonify and atumelnant (VRTX sees a path to \$5bn+ in revenue). We also look for any potential updates on accounting for the proposed CRNX acquisition, which VRTX expects to close in 3Q and become accretive to non-GAAP operating income by FY29.

Salveen Richter, CFA
+1(212)934-4204 |
salveen.richter@gs.com
GS & Co. LLC

Elizabeth Webster, Ph.D.  
+1(212)357-9925 |  
elizabeth.webster@gs.com  
GS & Co. LLC

Lydia Erdman
+1(212)357-6383 |
lydia.erdman@gs.com
GS & Co. LLC

Matt Dellatorre, Ph.D.
+1(212)855-0830 |
matt.dellatorre@gs.com
GS & Co. LLC

Mark Aleynick, Ph.D.
+1(212)357-6820 |
mark.aleynick@gs.com
GS & Co. LLC

Tommie Reerink, CFA
+1(212)357-2470 |
tommie.reerink@gs.com
GS & Co. LLC

Shrunatra Mishra
+1(332)245-7673 |
shrunatra.mishra@gs.com
GS India SPL

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

We model for an in-line 2Q earnings report. We expect a mostly in-line quarter (GSe and company-compiled total revenue of \~\$3.2bn; non-GAAP EPS of \$4.57/\$4.70). VRTX historically raises revenue guidance on 2Q EPS, noting 2Q25 as the exception (FY26 total revenue of \$12.95bn-\$13.1bn (+8.5% YoY at the midpoint); GSe/consensus of \$13.1bn/\$13.0bn).

Exhibit 1: GSe vs. Consensus

<table><tr><td rowspan="9">VRTX</td><td rowspan="2"></td><td colspan="2">2Q26</td><td colspan="3">FY26</td><td colspan="2">FY27</td></tr><tr><td>GSe</td><td>Cons.</td><td>GSe</td><td>Cons.</td><td>Guidance</td><td>GSe</td><td>Cons.</td></tr><tr><td>Trikafta WW sales ($mn)</td><td>$2,440</td><td>$2,480</td><td>$9,985</td><td>$9,734</td><td></td><td>$9,650</td><td>$9,158</td></tr><tr><td>Alyftrek</td><td>$490</td><td>$515</td><td>$2,169</td><td>$2,280</td><td></td><td>$3,130</td><td>$3,378</td></tr><tr><td>Casgevy revenue ($mn)</td><td>$57</td><td>$60</td><td>$243</td><td>$242</td><td></td><td>$443</td><td>$411</td></tr><tr><td>Journavx (acute pain)</td><td>$45</td><td>$49</td><td>$234</td><td>$214</td><td></td><td>$553</td><td>$552</td></tr><tr><td>povetacicept (IgAN)</td><td>$0</td><td>$0</td><td>$0</td><td>$1</td><td></td><td>$174</td><td>$102</td></tr><tr><td>Total Product Revenue ($mn)</td><td>$3,155</td><td>$3,219</td><td>$13,099</td><td>$13,037</td><td>$12.95-$13.1bn</td><td>$14,338</td><td>$14,309</td></tr><tr><td>Non-GAAP EPS</td><td>$4.57</td><td>$4.70</td><td>$19.61</td><td>$19.16</td><td></td><td>$22.90</td><td>$21.33</td></tr></table>

Source: Company data, FactSet, Data compiled by GS Global Investment Research

Catalysts: Following the proposed acquisition of CRNX, investors look to understand the revenue outlook for CRNX's Palsonify and Ph3 atumelnant in addition to the catalyst path for atumelnant and other acquired pipeline assets in thyroid eye disease and Graves' disease. For atumelnant, the next anticipated catalysts are OLE data in congenital adrenal hyperplasia (CAH) in 2H26+, which could serve to assuage investor debates on prior liver toxicities (we are not concerned), and Ph3 data likely in 2027 per the primary completion date on clinicaltrials.gov. Outside of the CRNX assets, most focus continues to be on near-term catalysts in kidney disease/autoimmune indications, including: 1) Ph2 inaxaplin data in APOL1-mediated kidney disease (AMKD) in mid-2026, in the subset of patients with moderate proteinuria and Type 2 diabetes, 2) approval and launch of povetacicept in IgAN per the November 30 PDUFA and 3) Ph3 48-week interim analysis inaxaplin data in primary AMKD in early-2027. We also monitor VRTX's innovation cycle in CF in the context of the competitive landscape (SION's NBD1 stabilizers), with initial Ph1 data from VX-828, a next-generation 3.0 CFTR corrector, in people with CF (2H). In addition, Ph1/2 data from VX-670 in DM1 (muscle strength, splicing) serves as an upside lever.

Exhibit 2: Key catalysts into 2027

<table><tr><td>Company</td><td>Timing</td><td>Drug</td><td>Event</td></tr><tr><td rowspan="11">VRTX</td><td>-</td><td>povetacicept in gMG</td><td>Ph2 initiated in gMG, driving enrollment + dosing</td></tr><tr><td>-</td><td>povetacicept in pMN</td><td>Enrollment in Ph2 pivotal trial complete and Ph3 initiated; drive Ph3 advancement</td></tr><tr><td>2H26</td><td>VX-670 (DM1)</td><td>Ph1/2 data (splicing, muscle strength)</td></tr><tr><td>2H26</td><td>inaxaplin</td><td>Ph2 AMPLIFIED study data in AMKD with moderate proteinuria or diabetes</td></tr><tr><td>2H26</td><td>VX-828 (next-gen CFTR modulator)</td><td>Ph1/2 data in CF patients</td></tr><tr><td>2H26+</td><td>atulmelnant</td><td>OLE data in CAH (estimated)</td></tr><tr><td>November 30th</td><td>povetacicept</td><td>PDUFA in IgAN</td></tr><tr><td>early-2027</td><td>inaxaplin</td><td>Ph3 48-week interim analysis data in AMKD; potential AA filing thereafter</td></tr><tr><td>2Q27+</td><td>suzetrigine</td><td>Ph3 data in DPN</td></tr><tr><td>Mid-2027</td><td>atumelnant</td><td>Ph3 data in CAH (timing anticipated)</td></tr><tr><td>2027</td><td>atumelnant</td><td>Ph3 data in carcinoid syndrome (timing anticipated)</td></tr></table>

Source: Data compiled by GS Global Investment Research

## Valuation and Risks

VRTX (Buy): Our 12-month PT of \$652 is based on a 100% DCF value (8% WACC, 1%

TGR). Risks: Downside risks: Clinical/technology setbacks – Failure to execute across the earlier stage pipeline would present risk to VRTX's future growth outlook outside the CF franchise. Failure to secure reimbursement for CF therapies ex-US. Failure to obtain regulatory approval and lack of commercial success for later-stage pipeline assets would pose significant downside risks to our sales estimates. Competition — We note potential competitive threats to the CF franchise and gene editing technologies. Failure to protect IP portfolio — We assume IP coverage into the late 2030s, and failure to extend these patents would represent downside to our estimates. Pricing/reimbursement pressure — Similar to all large-cap biopharma companies, downward pressure on price and/or reimbursement challenges on recently launched or existing drugs would represent downside risk to product revenues.

<table><tr><td>VRTX</td><td>12m Price Target: $652.00</td><td colspan="2">Price: $477.36</td><td colspan="2">Upside: 36.6%</td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: $121.2bn</td><td>Revenue ($ mn)</td><td>12,001.3</td><td>13,098.8</td><td>14,338.3</td><td>16,448.6</td></tr><tr><td>Enterprise value: $111.2bn</td><td>EBITDA ($ mn)</td><td>4,383.1</td><td>5,144.3</td><td>5,833.9</td><td>7,408.1</td></tr><tr><td>3m ADTV: $703.2mn</td><td>EBIT ($ mn)</td><td>4,173.3</td><td>4,929.6</td><td>5,555.7</td><td>7,312.0</td></tr><tr><td>United States</td><td>EPS ($)</td><td>18.40</td><td>19.61</td><td>22.90</td><td>29.57</td></tr><tr><td>Americas Biotechnology</td><td>P/E (X)</td><td>24.1</td><td>24.3</td><td>20.8</td><td>16.1</td></tr><tr><td>M&amp;A Rank: 3</td><td>EV/EBITDA (X)</td><td>24.7</td><td>21.7</td><td>18.2</td><td>13.7</td></tr><tr><td></td><td>FCF yield (%)</td><td>2.8</td><td>4.0</td><td>5.2</td><td>4.3</td></tr><tr><td></td><td>Dividend yield (%)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td></td><td>Net debt/EBITDA (X)</td><td>(1.2)</td><td>(1.9)</td><td>(2.8)</td><td>(2.9)</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS ($)</td><td>4.47</td><td>4.57</td><td>5.18</td><td>5.39</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 24 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Salveen Richter, CFA, Elizabeth Webster, Ph.D., Lydia Erdman, Matt Dellatorre, Ph.D., Mark Aleynick, Ph.D., Tommie Reerink, CFA and Shrunatra Mishra, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Salveen Richter, CFA GS & Co. LLC, Elizabeth Webster, Ph.D. GS & Co. LLC, Lydia Erdman GS & Co. LLC, Matt Dellatorre, Ph.D. GS & Co. LLC, Mark Aleynick, Ph.D. GS & Co. LLC, Tommie Reerink, CFA GS & Co. LLC, Shrunatra Mishra GS India SPL.

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

The rating(s) for Vertex Pharmaceuticals Inc. is/are relative to the other companies in its/their coverage universe: 4D Molecular Therapeutics, Acadia Pharmaceuticals Inc., Agios Pharmaceuticals Inc., Alnylam Pharmaceuticals Inc., Amgen Inc., Annexon Biosciences, BioMarin Pharmaceutical Inc., Biogen Inc., CRISPR Therapeutics, Denali Therapeutics Inc., Enliven Therapeutics Inc., Generate Biomedicines Inc., Gilead Sciences Inc., Immunome Inc., Incyte Corp., Intellia Therapeutics, Ionis Pharmaceuticals Inc., Moderna Inc., Rapport Therapeutics, Regeneron Pharmaceuticals Inc., Relay Therapeutics, Sarepta Therapeutics Inc., Summit Therapeutics Inc., Taysha Gene Therapies Inc., Ultragenyx Pharmaceutical, Vertex Pharmaceuticals Inc., uniQure

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Vertex Pharmaceuticals Inc. (\$477.36)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Vertex Pharmaceuticals Inc. (\$477.36)

GS has received compensation for non-investment banking services during the past 12 months: Vertex Pharmaceuticals Inc. (\$477.36)

GS had an investment banking services client relationship during the past 12 months with: Vertex Pharmaceuticals Inc. (\$477.36)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Vertex Pharmaceuticals Inc. (\$477.36)

GS had a non-securities services client relationship during the past 12 months with: Vertex Pharmaceuticals Inc. (\$477.36)

GS makes a market in the securities or derivatives thereof: Vertex Pharmaceuticals Inc. (\$477.36)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/cedcef2933b2c40500c3e14385496cdb4581ddb2f758e38dbf9c8bbe830a9d5e.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Vertex Pharmaceuticals Inc. (VRTX)

<table><tr><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td></tr><tr><td>20-Jul-26</td><

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
