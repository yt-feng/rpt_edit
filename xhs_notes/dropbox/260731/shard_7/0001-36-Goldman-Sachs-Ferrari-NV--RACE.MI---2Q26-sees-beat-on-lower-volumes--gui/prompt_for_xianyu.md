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
# Ferrari NV (RACE.MI): 2Q26 sees beat on lower volumes; guidance raised with room for further upgrades down the line; Our Buy thesis is in

Ferrari reported 2Q26 today (30th of July). We believe Ferrari 2026 consensus EPS to likely see mid-single-digit upgrades in the near term as new guidance is above current consensus, and in our view there is room for another raise in 3Q. We remain Buy rated.

2Q sees beat driven by outperformance in personalisation: Ferrari reported 2Q adj. EBIT 6.3% ahead of Visible Alpha Consensus Data (€569mn, GSe €590mn), with the quarter benefiting from strong price mix €122mn (GSe €82mn). Volumes came in -1.9% below cons at 3.37k (cons 3.43k, GSe 3.40k). Despite lower volumes, overall revenues benefited from a richer model mix and personalisation rates (20% vs mid-term guide of 18%), which led to a beat on revenues 4.3% above cons (€1.86bn) and in-line with GSe €1.90bn. Ferrari confirmed that its orderbook now covers the full of 2027. Special series mix for 2Q came in slightly below our estimates

Industrial FCF miss driven by inventory increase and lower D&A: Ferrari missed consensus ind. FCF expectations by -1.9%, which can largely be explained by negative working capital and provisions. Capex came in slightly below at -€236mn than we had anticipated (GSe -€247mn). Cash R&D was €267mn (GSe €255mn) with a capitalization ratio of c.45.7% (GSe 43%), leading to a slightly better P&L net benefit of €49mn (GSe €30mn).

2026 guidance upgrade with room for further upgrades: Ferrari upgraded its guidance for FY26 now expecting revenues of €7.60bn (previously \~€7.5bn, cons €7.55bn, GSe €7.84bn), adj. EBIT of >=€2.26bn (prev. >=€2.22bn, cons €2.25bn, GSe €2.32bn) and ind. FCF >=€1.55bn (prev. >€1.5bn, cons €1.61bn, GSe €1.73mn). We continue to see room for Ferrari to upgrade its guidance again in 3Q26 as we expect mix to continue to accelerate towards 2H26, supported by the ramp-up of the F80 supercar and the 296 Versione Speciale with personalisations remaining strong. We note that the upgraded guidance now implies a revenue growth rate of FY26-30 CAGR above the 5% guidance from CMD, thereby likely increasing investor confidence that the 5% CAGR target acts as a growth floor rather than a target.

Key questions for the call: 1) What explains the recent strong bounce-back in Luxury Residual Values particularly in the UK and Germany? 2) Outside of the UK, has the company taken any action in other markets to address declining residual values? 3) What volumes of the F80/499P were shipped in 2Q? 4) What was the personalisation rate in 2Q26, and what drove this positive development despite management expectations of lower uptake?

Christian Frenes +44(20)7051-8641 | christian.frenes@gs.com GS International

Robert Triulzi  
+44(20)7552-2281 | robert.triulzi@gs.com GS International

Shivam Kotecha
+1(332)245-7822 |
shivam.kotecha@gs.com
GS India SPL

Monika Mengting Liu, CFA
+44(20)7051-7601 | monika.liu@gs.com
GS International

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

Exhibit 1:

![](images/8a243d523dc12959c844895bcd4e26b88a00df2ffb372dc99fa612eed1b9edd6.jpg)

## 2Q26 results vs. GSe and consensus

Exhibit 2: Ferrari 2Q26 results vs. GSe and Visible Alpha consensus

<table><tr><td rowspan="2">(€ mn)</td><td colspan="5">2Q26</td><td colspan="3">2026E</td><td colspan="3">2027E</td></tr><tr><td>Reported</td><td>GSe</td><td>Cons</td><td>Reported vs GSe</td><td>Reported vs Cons</td><td>GSe</td><td>Cons</td><td>GSe vs cons</td><td>GSe</td><td>Cons</td><td>GSe vs cons</td></tr><tr><td>Shipments</td><td>3,366</td><td>3,397</td><td>3,433</td><td>-0.9%</td><td>-1.9%</td><td>13,519</td><td>13,655</td><td>-1.0%</td><td>13,940</td><td>13,849</td><td>0.7%</td></tr><tr><td>Revenues</td><td>1,938</td><td>1,903</td><td>1,857</td><td>1.8%</td><td>4.3%</td><td>7,837</td><td>7,551</td><td>3.8%</td><td>8,697</td><td>8,198</td><td>6.1%</td></tr><tr><td>of which Cars and Parts</td><td>1,629</td><td>1,587</td><td>1,554</td><td>2.7%</td><td>4.8%</td><td>6,565</td><td>6,331</td><td>3.7%</td><td>7,340</td><td>6,925</td><td>6.0%</td></tr><tr><td>Adj. EBITDA</td><td>755</td><td>757</td><td>732</td><td>-0.3%</td><td>3.1%</td><td>3,034</td><td>2,963</td><td>2.4%</td><td>3,337</td><td>3,235</td><td>3.1%</td></tr><tr><td>Adj. EBITDA Margin</td><td>39.0%</td><td>39.8%</td><td>39.4%</td><td>-0.8%</td><td>-0.5%</td><td>38.7%</td><td>39.2%</td><td>-0.5%</td><td>38.4%</td><td>39.5%</td><td>-1.1%</td></tr><tr><td>Adj. EBIT</td><td>605</td><td>590</td><td>569</td><td>2.6%</td><td>6.3%</td><td>2,317</td><td>2,250</td><td>2.9%</td><td>2,518</td><td>2,472</td><td>1.9%</td></tr><tr><td>Adj. EBIT Margin</td><td>31.2%</td><td>31.0%</td><td>30.6%</td><td>0.2%</td><td>0.6%</td><td>29.6%</td><td>29.8%</td><td>-0.2%</td><td>29.0%</td><td>30.1%</td><td>-1.2%</td></tr><tr><td>Adj. EPS</td><td>2.62</td><td>2.53</td><td>2.46</td><td>3.7%</td><td>6.6%</td><td>9.94</td><td>9.71</td><td>2.3%</td><td>10.89</td><td>10.83</td><td>0.5%</td></tr><tr><td>FCF</td><td>276</td><td>289</td><td>281</td><td>-4.4%</td><td>-1.9%</td><td>1,731</td><td>1,613</td><td>7.3%</td><td>1,641</td><td>1,704</td><td>-3.7%</td></tr></table>

Source: Visible Alpha Consensus Data, GS Global Investment Research, Company data

Exhibit 3: Ferrari FY26 guidance and FY30 targets vs GSe and Visible Alpha consensus

<table><tr><td></td><td>2025</td><td colspan="3">2026E</td><td colspan="3">vs FY25 Act</td><td colspan="3">2030E</td><td colspan="3">Implied 26-30 CAGR</td></tr><tr><td>(€ mn)</td><td>Actual</td><td>GSe</td><td>Guidance bottom</td><td>% diff</td><td>GSe</td><td>Guidance bottom</td><td>% diff</td><td>GSe</td><td>Guidance</td><td>% diff</td><td>Gse</td><td>Guidance</td><td>% diff</td></tr><tr><td>Revenues</td><td>7,146</td><td>7,837</td><td>7,600</td><td>3.1%</td><td>9.7%</td><td>6.4%</td><td>3.3%</td><td>10,044</td><td>9,000</td><td>11.6%</td><td>6%</td><td>4%</td><td>48.2%</td></tr><tr><td>Adj. EBITDA</td><td>2,772</td><td>3,034</td><td>2,970</td><td>2.1%</td><td>9.5%</td><td>7.2%</td><td>2.3%</td><td>3,823</td><td>3,600</td><td>6.2%</td><td>6%</td><td>5%</td><td>20.8%</td></tr><tr><td>Adj. EBITDA Margin</td><td>38.8%</td><td>38.7%</td><td>39.1%</td><td>-0.4%</td><td></td><td></td><td></td><td>38.1%</td><td>40.0%</td><td>-1.9%</td><td></td><td></td><td></td></tr><tr><td>Adj. EBIT</td><td>2,110</td><td>2,317</td><td>2,260</td><td>2.5%</td><td>9.8%</td><td>7.1%</td><td>2.7%</td><td>2,907</td><td>2,750</td><td>5.7%</td><td>6%</td><td>5%</td><td>16.1%</td></tr><tr><td>Adj. EBIT Margin</td><td>29.5%</td><td>29.6%</td><td>29.7%</td><td>-0.2%</td><td></td><td></td><td></td><td>28.9%</td><td>30.6%</td><td>-1.6%</td><td></td><td></td><td></td></tr><tr><td>Adj. EPS</td><td>8.96</td><td>9.94</td><td>9.68</td><td>2.6%</td><td>11.0%</td><td>8.1%</td><td>2.9%</td><td>13.13</td><td>11.50</td><td>14.2%</td><td>7%</td><td>4%</td><td>64.0%</td></tr><tr><td>FCF</td><td>1,538</td><td>1,731</td><td>1,550</td><td>11.7%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D&amp;A</td><td>662</td><td>717</td><td>710</td><td>1.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2025</td><td colspan="3">2026E</td><td colspan="3">vs FY25 Act</td><td colspan="3">2030E</td><td colspan="3">Implied 26-30 CAGR</td></tr><tr><td>(€ mn)</td><td>Actual</td><td>Cons</td><td>Guidance bottom</td><td>% diff</td><td>Cons</td><td>Guidance bottom</td><td>% diff</td><td>Cons</td><td>Guidance</td><td>% diff</td><td>Cons</td><td>Guidance*</td><td>FY26 Cons</td></tr><tr><td>Revenues</td><td>7,146</td><td>7,551</td><td>7,600</td><td>-0.6%</td><td>5.7%</td><td>6.4%</td><td>-0.7%</td><td>9,488</td><td>9,000</td><td>5.4%</td><td>6%</td><td>4%</td><td>36.0%</td></tr><tr><td>Adj. EBITDA</td><td>2,772</td><td>2,963</td><td>2,970</td><td>-0.2%</td><td>6.9%</td><td>7.2%</td><td>-0.3%</td><td>3,820</td><td>3,600</td><td>6.1%</td><td>7%</td><td>5%</td><td>33.2%</td></tr><tr><td>Adj. EBITDA Margin</td><td>38.8%</td><td>39.2%</td><td>39.1%</td><td>0.2%</td><td></td><td></td><td></td><td>40.3%</td><td>40.0%</td><td>0.3%</td><td></td><td></td><td></td></tr><tr><td>Adj. EBIT</td><td>2,110</td><td>2,250</td><td>2,260</td><td>-0.4%</td><td>6.7%</td><td>7.1%</td><td>-0.5%</td><td>2,931</td><td>2,750</td><td>6.6%</td><td>7%</td><td>5%</td><td>35.9%</td></tr><tr><td>Adj. EBIT Margin</td><td>29.5%</td><td>29.8%</td><td>29.7%</td><td>0.1%</td><td></td><td></td><td></td><td>30.9%</td><td>30.6%</td><td>0.3%</td><td></td><td></td><td></td></tr><tr><td>Adj. EPS</td><td>8.96</td><td>9.71</td><td>9.68</td><td>0.3%</td><td>8.4%</td><td>8.1%</td><td>0.3%</td><td>13.22</td><td>11.50</td><td>14.9%</td><td>8%</td><td>4%</td><td>82.3%</td></tr><tr><td>FCF</td><td>1,538</td><td>1,613</td><td>1,550</td><td>4.1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Visible Alpha Consensus Data, GS Global Investment Research, Company data

## Valuation & Key Risks

We are Buy-rated on Ferrari. We value Ferrari using a P/E approach and a target multiple of 35x, which we apply to our 2027E EPS of €10.92 to derive our 12-month price targets of €381/\$442.

Key downside risks include: 1) Material deterioration in car residual values challenges Ferrari's brand equity and orderbook 2) Ferrari's hybrid and BEVs are less well-received in the market than ICE product, reducing orderbook 3) Saturation of key markets prevents Ferrari from raising prices for successor models 4) Underestimating capex requirements for product innovation in outer years 5) Disruption to the supply chain or global trade inhibits Ferrari from shipping new products.

<table><tr><td>RACE.MI</td><td>12m Price Target: €381.00</td><td>Price: €339.80</td><td>Upside: 12.1%</td></tr><tr><td>RACE</td><td>12m Price Target: $442.00</td><td>Price: $385.69</td><td>Upside: 14.6%</td></tr></table>

<table><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: €60.6bn / $69.0bn</td><td>Revenue (€ mn)</td><td>7,145.8</td><td>7,837.5</td><td>8,697.1</td><td>9,044.3</td></tr><tr><td>Enterprise value:</td><td>EBIT (€ mn)</td><td>2,109.7</td><td>2,316.6</td><td>2,517.9</td><td>2,611.5</td></tr><tr><td>€60.4bn / $68.8bn</td><td>EPS (€)</td><td>8.96</td><td>9.94</td><td>10.89</td><td>11.45</td></tr><tr><td>3m ADTV: €180.5mn / $208.5mn</td><td>EV/EBITDA (X)</td><td>25.7</td><td>19.6</td><td>17.5</td><td>16.5</td></tr><tr><td>Italy</td><td>P/E (X)</td><td>44.5</td><td>34.2</td><td>31.2</td><td>29.7</td></tr><tr><td>Europe Autos</td><td>Dividend yield (%)</td><td>0.9</td><td>1.2</td><td>1.3</td><td>1.3</td></tr><tr><td>M&amp;A Rank: 3</td><td>FCF yield (%)</td><td>2.0</td><td>2.8</td><td>2.8</td><td>3.0</td></tr><tr><td>Leases incl. in net debt &amp; EV?:</td><td>CROCI (%)</td><td>21.6</td><td>19.6</td><td>20.3</td><td>19.7</td></tr><tr><td>Yes</td><td>Net debt/EBITDA (X)</td><td>0.0</td><td>(0.1)</td><td>(0.2)</td><td>(0.2)</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (€)</td><td>2.33</td><td>2.53</td><td>2.50</td><td>2.58</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 29 Jul 2026 close.

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

The rating(s) for Ferrari NV is/are relative 

[中间内容因长度限制已省略]

es, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

© 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
