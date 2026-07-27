你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

GS has received compensation for investme

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

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
