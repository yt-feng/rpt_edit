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
# MARUWA (5344.T): Results briefing: Prospects for upside to new guidance for AI/semiconductor applications; Buy

MARUWA held its 1Q3/27 results briefing at 10am JST on July 31 at which it explained 1Q results by application and the outlook from 2Q onward. Key points were: (1) Full-year sales guidance for AI applications was raised significantly to +110%, from +50% previously. The company expects the Seto No. 2 plant to start mass production and contribute to sales from 3Q. Given strong near-term demand, management intends to take steps to bring forward production at the No. 3 plant. (2) The company confirmed the launch of products for CPO applications from 4Q, and this was a factor behind the upward revision to AI applications. (3) Full-year sales growth (yoy) for semiconductor applications was revised up to +20%, from +14%, but the company's tone suggested upside is possible given the current strength of inquiries. In light of this strong demand, MARUWA plans to bring forward the start-up of two new buildings at the Miharu plant to 2Q, from the previously scheduled 2H.

We view the briefing as positive, reinforcing our view that there is potential upside to guidance for AI/semiconductor applications. We reiterate our Buy rating, based on a structural growth story centered on AI applications. For details on 1Q results by segment, new full-year guidance, our impressions, and key points from investor feedback, please refer to our reports published on the day of the earnings announcement (LINK, LINK).

Key points from the results briefing are as follows (company commentary unless otherwise noted)

(1) Telecommunications: 1Q sales were ¥9.2 bn. Full-year sales guidance for AI applications was raised substantially to +110%, from +50% previously. The upward revision was driven by improved visibility as strong forecasts at the start of the fiscal year translated into confirmed orders. Management's tone suggested that near-term inquiries are strong and it expects further sales growth. The company assumes mass production and a sales contribution from the Seto No. 2 plant from 3Q, and while the quarterly schedule for the No. 3 plant, which is scheduled for completion and start-up in FY3/28, is undecided, it intends to take steps to bring forward production given the strong demand. Guidance for full-year sales growth (yoy) for the segment was revised up to +48%, from +23%.

(2) CPO-related products: A launch from 4Q was confirmed, and was a factor behind the upward revision to AI applications. Orders are already large, with mass production scheduled for FY3/28.

Mitsuhiro Icho
+81(3)4587-9836 |
mitsuhiro.x.icho@gs.com
GS Japan Co., Ltd.

Daiki Takayama
+81(3)4587-9870 |
daiki.takayama@gs.com
GS Japan Co., Ltd.

(3) Automotive: 1Q sales were ¥3.5 bn. Sales for xEV applications remained solid. Inquiries from major existing customers are increasing, and MARUWA expects sales growth in differentiated products. Guidance for full-year sales growth (yoy) for the segment was revised up to +6%, from +2%.

(4) Semiconductors: 1Q sales were ¥2.2 bn. The company expects sales of c.¥3 bn in 2Q, and over ¥3 bn in 2H (3Q/4Q). Guidance for full-year sales growth (yoy) for the segment was revised up to +20%, from +14%, but management's tone suggested upside is possible given the current strength of inquiries. In light of this strong demand, MARUWA plans to bring forward the start-up of two new buildings at the Miharu plant to 2Q, from the previously scheduled 2H, increasing production capacity by (at least) +50% from the previous level. This will lead to a production system capable of meeting future increases in demand.

(5) 1Q operating profits: 1Q results were in line with company expectations. The main reason for the qoq decline in the operating margin was the 1Q shipment of work-in-progress inventory produced in 4Q, when yield issues occurred for new products. Shipments of this low-margin inventory were fully completed within 1Q, and thus management expects margins to improve from 2Q.

## Earnings revisions, target price

We leave our FY3/27-FY3/29 operating profit estimates unchanged, but revise our quarterly breakdown and make minor tweaks to our EPS and net profit estimates (less than 1%). We leave our 12-month target price unchanged at ¥89,000, and we maintain our Buy rating.

## MARUWA

## Investment Thesis - MARUWA

As a ceramics supplier, MARUWA's history dates back nearly 200 years. The company provides a wide range of ceramic products mainly for applications in fields such as (1) telecommunications, (2) autos, (3) semiconductors, and (4) industrial equipment. MARUWA has been transforming its business portfolio since the mid-2000s, shifting its focus from highly commoditized and cyclical products that face intense price-based competition to high-margin products for niche markets that require customization. Margins have improved sharply as a result, and MARUWA has won high share in niche markets with strong growth potential. It has established a structural competitive advantage enabling high growth, customization, margins, and market share. In FY3/27-FY3/29, we expect earnings growth to be driven mainly by heat-dissipation substrates for optical transceivers, as well as xEVs and quartz/SiC products for semiconductor production equipment. We are Buy rated on the stock, as we think earnings growth potential from FY3/27 is not fully factored into the current share price.

## Price Target Risks and Methodology - MARUWA

We are Buy rated on MARUWA. Our 12-month target price is ¥89,000 (implies FY27/28E P/E of 29x/23x). Our target price is based on FY28E EBITDA, and we derive the applied multiple of 12.5x from the historical correlation between the EBITDA margin and the

EV/EBITDA multiple. Key risks include lower investment in applications that support final demand (including AI/general-purpose servers, xEV, SPE), lower demand for end products due to supply chain disruptions and inventory adjustments, and the emergence of alternative technology.

<table><tr><td>5344.T</td><td>12m Price Target: ¥89,000</td><td colspan="2">Price: ¥52,860</td><td colspan="2">Upside: 68.4%</td></tr><tr><td>Buy</td><td>GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Market cap: ¥652.2bn / $4.1bn</td><td>Revenue (¥ bn)</td><td>74.5</td><td>93.3</td><td>114.0</td><td>132.5</td></tr><tr><td>Enterprise value: ¥567.3bn / $3.6bn</td><td>Op. profit (¥ bn) New</td><td>25.0</td><td>35.0</td><td>52.0</td><td>67.0</td></tr><tr><td>3m ADTV: ¥12.1bn / $75.8mn</td><td>Op. profit (¥ bn) Old</td><td>25.0</td><td>35.0</td><td>52.0</td><td>67.0</td></tr><tr><td>Japan</td><td>Op. profit CoE (¥ bn)</td><td>27.0</td><td>33.7</td><td>-</td><td>-</td></tr><tr><td rowspan="4">Japan Electronic Components/Semiconductors M&amp;A Rank: 3</td><td>EPS (¥) New</td><td>1,471.9</td><td>2,041.6</td><td>3,074.8</td><td>3,921.7</td></tr><tr><td>EPS (¥) Old</td><td>1,471.9</td><td>2,043.8</td><td>3,077.0</td><td>3,923.9</td></tr><tr><td>P/E (X)</td><td>29.0</td><td>25.9</td><td>17.2</td><td>13.5</td></tr><tr><td>P/B (X)</td><td>3.6</td><td>3.8</td><td>3.2</td><td>2.6</td></tr><tr><td>Leases incl. in net debt &amp; EV?: Yes</td><td>CROCI (%)</td><td>18.3</td><td>23.5</td><td>29.9</td><td>33.0</td></tr><tr><td></td><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td></td><td>EPS (¥)</td><td>361.9</td><td>456.6</td><td>558.7</td><td>629.0</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 30 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Mitsuhiro Icho and Daiki Takayama, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Mitsuhiro Icho GS Japan Co., Ltd., Daiki Takayama GS Japan Co., Ltd..

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

The rating(s) for MARUWA is/are relative to the other companies in its/their coverage universe: Alps Alpine, Dai Nippon Printing, Hirose Electric, IRISO Electronics, Ibiden, Japan Aviation Electronics Industry, Kohoku Kogyo, Kyocera, MARUWA, Mabuchi Motor, Maxell Ltd., MinebeaMitsumi Inc., Murata Mfg., NGK Corp., Nichicon, Nidec, Nippon Ceramic, Niterra, Nitto Denko, Renesas Electronics, Rohm, TDK, TOPPAN Holdings, Taiyo Yuden

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: MARUWA (¥52,860)

Distribution of ratings/investment banking relationships
GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/3a2ac2522a8e307db2bcaa02c7a7850f699326d256e7cbd98c6a7d107568abb9.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

Target price history table(s)
MARUWA (5344.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>08-Jun-26</td><td>89,000</td><td>67,750</td></tr><tr><td>08-May-26</td><td>70,000</td><td>68,930</td></tr><tr><td>16-Apr-26</td><td>72,000</td><td>69,200</td></tr><tr><td>23-Mar-26</td><td>67,000</td><td>53,790</td></tr><tr><td>03-Feb-26</td><td>55,000</td><td>51,620</td></tr><tr><td>12-Jan-26</td><td>54,000</td><td>44,550</td></tr><tr><td>02-Oct-25</td><td>48,000</td><td>38,170</td></tr><tr><td>24-Jul-25</td><td>45,000</td><td>46,930</td></tr><tr><td>07-Jul-25</td><td>46,000</td><td>40,020</td></tr><tr><td>08-May-25</td><td>44,000</td><td>32,210</td></tr><tr><td>25-Apr-25</td><td>42,000</td><td>29,375</td></tr><tr><td>31-Mar-25</td><td>47,000</td><td>30,320</td></tr><tr><td>01-Feb-25</td><td>55,000</td><td>38,320</td></tr><tr><td>31-Jan-25</td><td>54,000</td><td>38,320</td></tr><tr><td>29-Jan-25</td><td>55,000</td><td>40,900</td></tr><tr><td>22-Jan-25</td><td>58,000</td><td>50,150</td></tr><tr><td>29-Oct-24</td><td>51,000</td><td>41,650</td></tr><tr><td>01-Oct-24</td><td>53,000</td><td>43,300</td></tr><tr><td>29-Jul-24</td><td>49,000</td><td>40,500</td></tr><tr><td>02-Jul-24</td><td>45,000</td><td>38,300</td></tr><tr><td>25-Apr-24</td><td>39,000</td><td>33,300</td></tr><tr><td>03-Apr-24</td><td>40,000</td><td>32,350</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are addition

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
