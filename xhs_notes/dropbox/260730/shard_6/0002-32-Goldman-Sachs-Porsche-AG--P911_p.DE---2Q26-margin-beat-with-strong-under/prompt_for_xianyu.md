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
# Porsche AG (P911\_p.DE): 2Q26 margin beat with strong underlying performance, auto cashflow above GSe

Porsche AG reported 2Q26 results today (29th July). Porsche 2026 consensus EPS is likely to move up LSD on stronger underlying business, driven by 911 model mix in-line with our thesis. We remain Buy rated.

2Q26 above expectations: Porsche AG reported 2Q group EBIT of €753mn, above company-compiled consensus (€713mn / GSe €785mn). Sales revenues were in line with consensus (€8.80bn / GSe €9.24bn) resulting in a 2Q margin of 8.5% (consensus 8.1%, GSe 8.5%). The quarter was burdened by GSe €300mn restructuring charges, which were fully offset by a provision release of GSe €300mn. Revenue per Vehicle for the quarter was above our expectations at €126k (GSe €125k) driven by strong share of top-end 911 models GTS, Turbo and GT models. Porsche reported 2Q EPS of €0.81 (consensus €0.57, GSe €0.64) benefiting from a lower tax rate of 17% vs GSe 30%.

Auto net cash flow above GSe, driven by better operating and working capital: Porsche reported 2Q auto net cash flow at €506mn, below consensus (consensus €608mn) but above our estimate (GSe €344mn), driven by better operating business, working capital but also burdened by a €0.3bn pension liabilities. For 2Q26, the company had lower spend on R&D €517mn (GSe €596mn) and lower capitalisation rate of 38.5% (GSe 43%), thus resulting in a P&L headwind of -€165mn (GSe -€131mn). This resulted in a net cash flow margin of 6.5%, above the full-year guidance of 3-5%.

Guidance maintained for 2026: Porsche AG maintained its full year guidance for 2026 expecting €35-36bn of revenue and a Group RoS of 5.5%-7.5%. On Auto EBITDA, the company continues to expect a margin of 15%-17%. For 2027, the company indicated that a three-digit million amount of restructuring would continue.

Key questions for the call: 1) Building blocks and timing of return to +10% margin with future steps towards mid-term guidance (up to 15%); 2) Key pillars of cash flow guidance and Bugatti stake sale inflows; 3) Update on restructuring and other special effects continuing into 2026; 4) Outlook on model launch pipeline and product portfolio in the near term; 5) Updates on tariff mitigation measures.

Christian Frenes  
+44(20)7051-8641 |  
christian.frenes@gs.com  
GS International

Robert Triulzi  
+44(20)7552-2281 | robert.triulzi@gs.com GS International

Shivam Kotecha
+1(332)245-7822 |
shivam.kotecha@gs.com
GS India SPL

Monika Mengting Liu, CFA
+44(20)7051-7601 | monika.liu@gs.com
GS International

# Porsche AG 2Q26 Results

## Reported vs estimates and consensus

Exhibit 1: Porsche AG 2Q26 vs. GSe and company-compiled consensus

<table><tr><td rowspan="2">€ Mn</td><td colspan="5">2Q26</td><td colspan="3">2026E</td></tr><tr><td>Reported</td><td>GSe</td><td>Cons</td><td>Reported vs. Gse</td><td>Reported vs. Cons</td><td>GSe</td><td>Cons</td><td>GSe vs. Cons</td></tr><tr><td>Revenue</td><td>8,829</td><td>9,236</td><td>8,804</td><td>-4.4%</td><td>0.3%</td><td>36,039</td><td>35,129</td><td>2.6%</td></tr><tr><td>Operating Profit</td><td>753</td><td>785</td><td>713</td><td>-4.1%</td><td>5.6%</td><td>2,284</td><td>2,252</td><td>1.4%</td></tr><tr><td>Operating Profit Margin, %</td><td>8.5%</td><td>8.5%</td><td>8.1%</td><td>0.0pp</td><td>0.4pp</td><td>6.3%</td><td>6.4%</td><td>-0.1pp</td></tr><tr><td>EPS</td><td>0.81</td><td>0.64</td><td>0.57</td><td>26.3%</td><td>42.5%</td><td>2.32</td><td>1.82</td><td>27.3%</td></tr><tr><td>DPS</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>1.20</td><td>1.04</td><td>15.4%</td></tr><tr><td colspan="9">Automotive</td></tr><tr><td>Auto Revenue</td><td>7,777</td><td>8,243</td><td>7,800</td><td>-5.7%</td><td>-0.3%</td><td>31,944</td><td>30,912</td><td>3.3%</td></tr><tr><td>Auto EBITDA</td><td>1,496</td><td>1,557</td><td>1,429</td><td>-3.9%</td><td>4.7%</td><td>5,353</td><td>5,232</td><td>2.3%</td></tr><tr><td>Auto EBITDA Margin, %</td><td>19.2%</td><td>18.9%</td><td>18.3%</td><td>0.3pp</td><td>0.9pp</td><td>16.8%</td><td>16.9%</td><td>-0.2pp</td></tr><tr><td>Auto Operating Profit</td><td>691</td><td>704</td><td>631</td><td>-1.8%</td><td>9.5%</td><td>2,005</td><td>1,923</td><td>4.2%</td></tr><tr><td>Auto Operating Profit Margin, %</td><td>8.9%</td><td>8.5%</td><td>8.1%</td><td>0.3pp</td><td>0.8pp</td><td>6.3%</td><td>6.2%</td><td>0.1pp</td></tr><tr><td>Auto Net Cash Flow</td><td>506</td><td>344</td><td>608</td><td>47.2%</td><td>-16.8%</td><td>1,020</td><td>1,352</td><td>-24.6%</td></tr><tr><td>Auto Net Cash Flow Margin, %</td><td>6.5%</td><td>4.2%</td><td>7.8%</td><td>2.3pp</td><td>-1.3pp</td><td>3.2%</td><td>4.4%</td><td>-1.2pp</td></tr><tr><td>Deliveries (in &#x27;000)</td><td>61</td><td>66</td><td>62</td><td>-6.8%</td><td>-1.1%</td><td>250</td><td>248</td><td>1.1%</td></tr></table>

Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

## Valuation & Key Risks

We continue to value Porsche on a forward P/E basis applying a target multiple of 20x on our blended FY27/28 EPS deriving a 12-month target price of €57.

## Downside risks:

Delays to new product launches and delivery timelines: Any further slippage in anticipated product launches, whether from regulatory, supplier or development setbacks, would extend the existing volume gap and delay the expected delivery/margin recovery.

■ Increase in competitive forces across key segments: Intensifying pressure from both traditional European performance peers and well-capitalized Chinese EV entrants moving upmarket could erode the pricing power and ASP growth assumptions central to our thesis.

■ Lower delivery growth and supply-demand mismatch across BEV and ICE models: A faster regulatory push toward electrification or slower consumer BEV adoption could create inventory imbalances, leading to margin-dilutive discounting on electric models alongside premature ICE run-off.

■ Lower profitability from delivery shortfalls or weaker-than-expected BEV gross margins: If BEV unit economics disappoint due to higher battery costs, unfavorable platform economics, or competitive pricing pressure, the offset from 911 mix normalization may prove insufficient to sustain group-level margin targets.

\- Ongoing deterioration of business in China: A sharper-than-expected decline driven by further luxury tax threshold adjustments, intensifying domestic

competition from premium Chinese OEMs, or broader macroeconomic weakness could push China deliveries meaningfully below our base case.

\- Failure to secure raw material supply: Supply disruptions from geopolitical tensions, export restrictions, or sourcing concentration risk could lead to production delays and higher input costs as Porsche scales BEV production toward its medium-term targets.

<table><tr><td>P911_p.DE</td><td>12m Price Target: €57.00</td><td colspan="2">Price: €44.86</td><td colspan="2">Upside: 27.1%</td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: €40.9bn / $46.5bn</td><td>Revenue (€ mn)</td><td>36,272.0</td><td>36,038.7</td><td>35,677.8</td><td>37,601.6</td></tr><tr><td>Enterprise value:</td><td>EBIT (€ mn)</td><td>413.0</td><td>2,284.4</td><td>3,034.9</td><td>4,036.0</td></tr><tr><td>€50.7bn / $57.9bn</td><td>EPS (€)</td><td>0.47</td><td>1.84</td><td>2.46</td><td>3.27</td></tr><tr><td>3m ADTV: €24.4mn / $28.2mn</td><td>EV/EBITDA (X)</td><td>8.5</td><td>7.3</td><td>6.3</td><td>5.4</td></tr><tr><td>Germany</td><td>P/E (X)</td><td>100.2</td><td>24.4</td><td>18.2</td><td>13.7</td></tr><tr><td>Europe Autos</td><td>Dividend yield (%)</td><td>2.1</td><td>2.7</td><td>2.9</td><td>3.3</td></tr><tr><td>M&amp;A Rank: 3</td><td>FCF yield (%)</td><td>0.8</td><td>1.5</td><td>5.0</td><td>7.0</td></tr><tr><td>Leases incl. in net debt &amp; EV?:</td><td>CROCI (%)</td><td>10.3</td><td>8.7</td><td>9.9</td><td>10.4</td></tr><tr><td>Yes</td><td>Net debt/EBITDA (X)</td><td>1.1</td><td>0.9</td><td>0.7</td><td>0.4</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (€)</td><td>0.44</td><td>0.64</td><td>0.28</td><td>0.96</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 28 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Christian Frenes, Robert Triulzi, Shivam Kotecha and Monika Mengting Liu, CFA, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Christian Frenes GS International, Robert Triulzi GS International, Shivam Kotecha GS India SPL, Monika Mengting Liu, CFA GS International.

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

The rating(s) for Porsche AG is/are relative to the other companies in its/their coverage universe: Aston Martin Lagonda Global Holdings, BMW, Ferrari NV, Mercedes-Benz Group AG, Porsche AG, Renault, Stellantis NV, Volkswagen

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Porsche AG (€44.86)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Porsche AG (€44.86)

GS had an investment banking services client relationship during the past 12 months with: Porsche AG (€44.86)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Porsche AG (€44.86)

GS had a non-securities services client relationship during the past 12 months with: Porsche AG (€44.86)

Distribution of ratings/investment banking relationships GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/01a84e416590063bbc2588dabafaf15e0df58787f82d5783c2bfa7c85dae4104.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Porsche AG (P911\_p.DE)

<table><tr><td>Date of report</td><td>Target price (€)</td><td>Closing price (€)</td></tr><tr><td>13-Jul-26</td><td>57.00</td><td>44.60</td></tr><tr><td>11-Jun-26</td><td>59.00</td><td>48.51</td></tr><tr><td>14-Apr-26</td><td>39.00</td><td>43.29</td></tr><tr><td>23-Mar-26</td><td>36.00</td><td>37.31</td></tr><tr><td>24-Feb-26</td><td>40.00</td><td>41.55</td></tr><tr><td>23-Nov-25</td><td>46.00</td><td>43.21</td></tr><tr><td>18-Feb-25</td><td>65.00</td><td>58.26</td></tr><tr><td>14-Jan-25</td><td>69.00</td><td>59.66</td></tr><tr><td>15-Oct-24</td><td>86.00</td><td>68.24</td></tr><tr><td>29-Jul-24</td><td>93.00</td><td>69.52</td></tr><tr><td>09-Jul-24</td><td>109.00</td><td>72.58</td></tr><tr><td>05-Apr-24</td><td>108.00</td><td>93.10</td></tr><tr><td>16-Jan-24</td><td>103.00</td><td>73.72</td></tr><tr><td>17-Nov-23</td><td>124.00</td><td>90.92</td></tr><tr><td>18-Oct-23</td><td>141.00</td><td>91.56</td></tr><tr><td>18-Sep-23</td><td>140.00</td><td>96.24</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by Uni

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
