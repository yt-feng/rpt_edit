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
# Mercedes-Benz Group AG (MBGn.DE): Production cost reduction in action - Takeaways from the Kecskemét plant extension trip

Mercedes-Benz opened the extension of its Kecskemét plant in Hungary, doubling annual capacity to c.400k units (with full ramp-up expected within 12 months) and making it its largest facility in Europe (and one of the largest globally). Backed by c.€1bn of investment, the extension adds two bodywork/assembly halls, a second press shop, a state-of-the-art paint shop, and a battery assembly facility. Attended by Hungary's Prime Minister and Economy Minister, the ceremony underscored the site's importance to the country's auto value chain. The start of production of the new all-electric C-Class marks the first BEV in Mercedes' Core segment built at the site, alongside the GLB and the exclusive production of the upcoming compact G-Class.

We attended the opening ceremony and an investor event alongside it on July 13, where senior management – the CEO, CFO, and Board Member for Production – laid out initiatives on production-cost reduction and humanoid robotics. Having cut global production cost per unit by c.10% in 2022-24, Mercedes targets a further 10% by 2027 (of which 4% was achieved in 2025), with potentially more beyond. The plan centres on raising best-cost-country, building a flexible production network, deepening local-for-local, and cutting structural dependency on Germany, supported by advanced robotics and AI. Additional key takeaways follow:

Streamlining global operations through rightsizing capacity and deepening local-for-local. On capacity, management is committed to a leaner footprint amid heightened demand volatility, targeting 2.4 million units in 2026 and 2.0–2.2 million over the mid term (c.2028), with the primary adjustments falling in China and Germany. In management's view, the world car concept may no longer be suitable for today's environment. Production is becoming increasingly regional, with local-for-local targets of over 85% in Europe and China, and a US ambition to exceed 50% (including the GLC localisation).

\- Moving East is the clear direction, yet Germany remains strategically important. Kecskemét offers roughly 70% lower factor costs than Germany (due to lower salaries, longer working hours, and markedly lower sick leave), a stable policy environment, EU proximity, and an established supplier base, with the eastward shift now extending beyond vehicle assembly to powertrain and component production (e.g., Romania). The eastward shift now extends beyond vehicle assembly to powertrain and component production (e.g., Romania). Even so, Kecskemét is closely integrated with its two German counterpart plants –

Christian Frenes +44(20)7051-8641 | christian.frenes@gs.com GS International

Monika Mengting Liu, CFA +44(20)7051-7601 | monika.liu@gs.com GS International

Shivam Kotecha +1(332)245-7822 | shivam.kotecha@gs.com GS India SPL

Robert Triulzi  
+44(20)7552-2281 | robert.triulzi@gs.com GS International

Rastatt (on the MMA platform) and Bremen (on the MB.EA platform) – forming a flexible production network in which volumes can be shifted between sites according to demand. Germany, for its part, retains a defined role for capability and heritage, particularly for Top-End vehicles, where customers pay a premium for the manufacturing location. It also offers the optionality to leverage Mercedes' industrial capabilities for a growing (but still minor) defence business, some of it with civil applications.

## Digitalisation underpins an AI-first production process at Kecskemét. A

significant portion of the tour and presentation centered on Mercedes' ambition to lead in next-generation manufacturing. Kecskemét is the first site to feature a complete Digital Factory Twin of an entire assembly hall, built in NVIDIA Omniverse and layered atop the MO360 ecosystem and MO360 Vision System for real-time, camera-based quality control. Management outlined an AI-first production process connecting procurement, production, and sales to detect demand shifts earlier and steer suppliers accordingly. Crucially, as automation and humanoids expand, every production step is captured as data – improving quality and enabling AI to scan the entire process and flag anomalies far earlier.

The humanoid partnership with Apptronik bears potential for Mercedes' assembly automation and further applications. The most forward-looking discussion concerned humanoid robots, developed in partnership with Apptronik (Apollo models). Management sees humanoids as essential to achieving high automation in assembly, where the rate of automation is low and flexible industrial robots fall short, with a roadmap of humanoid training today, production pilots at Sindelfingen by end-2026, and mid-term series integration (subject to safety, regulation, and works-council alignment). Apptronik's CEO Jeff Cardenas emphasised that the collaboration with Mercedes is built on its state-of-the-art industrial manufacturing. Mercedes framed its role as bringing real industrial knowledge and safety/regulatory rigor, while keeping optionality open beyond a single hardware or software provider. Both remain open to exploring commercialisation of the partnership.

Exhibit 1: Moving East - production volume is expected to grow at a +29% CAGR in 2025-30, while falling -4% in Germany, according to S&P Global.
Forecast as of Jun-26  
![](images/3cd444c46a1991cc224f7ad6fabbc5d14c19e7b165ae5aacf43dea9cbdd78ccb.jpg)  
Source: S&P Global, GS Global Investment Research

## Valuation and risks

Valuation: We value Mercedes on a hybrid P/E and Daimler Truck (DTG) investment stake framework to explicitly account for the value of the remaining DTG stake. Our 12m price target is €65 and comprises: (1) €55 per share from applying a 7.5x target multiple on a 50/50 blend of FY27/28E EPS; and (2) €10 per share from the NPV of MBG's DTG stake, assuming an orderly sell-down over five years with proceeds returned to shareholders via MBG share buybacks. We remain Buy rated.

Key downside risks: Deviation from luxury strategy/focus; slowdown and/or restrictions in key luxury markets; cost savings do not materialise; inability to reduce capex; DTG stake monetisation may be slower or at lower prices than assumed due to market conditions reducing distributable cash and buyback capacity.

<table><tr><td>MBGn.DE</td><td>12m Price Target: €65.00</td><td>Price: €45.11</td><td>Upside: 44.1%</td></tr></table>

<table><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: €43.4bn / $49.7bn</td><td>Revenue (€ mn)</td><td>132,214.0</td><td>129,414.6</td><td>132,545.6</td><td>135,794.7</td></tr><tr><td>Enterprise value:</td><td>EBIT (€ mn)</td><td>8,235.0</td><td>7,139.0</td><td>8,416.5</td><td>9,186.0</td></tr><tr><td>€66.0bn / $75.6bn</td><td>EPS (€)</td><td>5.34</td><td>5.57</td><td>6.85</td><td>7.94</td></tr><tr><td>3m ADTV: €137.2mn / $159.4mn</td><td>EV/EBITDA (X)</td><td>7.0</td><td>6.2</td><td>5.5</td><td>5.2</td></tr><tr><td>Germany</td><td>P/E (X)</td><td>10.2</td><td>8.1</td><td>6.6</td><td>5.7</td></tr><tr><td>Europe Autos</td><td>Dividend yield (%)</td><td>6.4</td><td>7.8</td><td>8.6</td><td>9.3</td></tr><tr><td>M&amp;A Rank: 3</td><td>FCF yield (%)</td><td>(13.1)</td><td>12.4</td><td>11.8</td><td>15.0</td></tr><tr><td>Leases incl. in net debt &amp; EV?:</td><td>CROCI (%)</td><td>(0.7)</td><td>16.6</td><td>15.7</td><td>16.8</td></tr><tr><td>Yes</td><td>Net debt/EBITDA (X)</td><td>2.2</td><td>2.0</td><td>2.0</td><td>2.0</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (€)</td><td>1.49</td><td>1.43</td><td>1.30</td><td>1.35</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 14 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Christian Frenes, Monika Mengting Liu, CFA, Shivam Kotecha and Robert Triulzi, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Christian Frenes GS International, Monika Mengting Liu, CFA GS International, Shivam Kotecha GS India SPL, Robert Triulzi GS International.

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

The rating(s) for Mercedes-Benz Group AG is/are relative to the other companies in its/their coverage universe: Aston Martin Lagonda Global Holdings, BMW, Ferrari NV, Mercedes-Benz Group AG, Porsche AG, Renault, Stellantis NV, Volkswagen

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Mercedes-Benz Group (ADR) (\$65.61) and Mercedes-Benz Group AG (€45.11)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Mercedes-Benz Group (ADR) (\$65.61) and Mercedes-Benz Group AG (€45.11)

GS has received compensation for non-investment banking services during the past 12 months: Mercedes-Benz Group (ADR) (\$65.61) and Mercedes-Benz Group AG (€45.11)

GS had an investment banking services client relationship during the past 12 months with: Mercedes-Benz Group (ADR) (\$65.61) and Mercedes-Benz Group AG (€45.11)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Mercedes-Benz Group (ADR) (\$65.61) and Mercedes-Benz Group AG (€45.11)

GS had a non-securities services client relationship during the past 12 months with: Mercedes-Benz Group (ADR) (\$65.61) and Mercedes-Benz Group AG (€45.11)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/ccc4a3a64c1f78c57e6be0b49ea83a9780e1c0b8babf301713c809cbeccf4de2.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Mercedes-Benz Group AG (MBGn.DE)

<table><tr><td>Date of report</td><td>Target price (€)</td><td>Closing price (€)</td></tr><tr><td>14-Jul-26</td><td>65.00</td><td>45.11</td></tr><tr><td>16-Apr-26</td><td>66.00</td><td>53.35</td></tr><tr><td>20-Feb-26</td><td>69.00</td><td>59.24</td></tr><tr><td>23-Jan-26</td><td>71.00</td><td>58.30</td></tr><tr><td>24-Nov-25</td><td>73.00</td><td>57.49</td></tr><tr><td>23-Nov-25</td><td>74.00</td><td>57.02</td></tr><tr><td>25-Feb-25</td><td>60.00</td><td>60.70</td></tr><tr><td>14-Jan-25</td><td>59.00</td><td>55.55</td></tr><tr><td>05-Nov-24</td><td>63.00</td><td>55.90</td></tr><tr><td>20-Sep-24</td><td>65.00</td><td>54.99</td></tr><tr><td>31-Jul-24</td><td>87.00</td><td>61.16</td></tr><tr><td>12-Jul-24</td><td>84.00</td><td>64.78</td></tr><tr><td>11-Apr-24</td><td>97.00</td><td>75.74</td></tr><tr><td>14-Feb-24</td><td>93.00</td><td>65.53</td></tr><tr><td>16-Jan-24</td><td>92.00</td><td>61.28</td></tr><tr><td>17-Nov-23</td><td>90.00</td><td>58.60</td></tr><tr><td>18-Sep-23</td><td>97.00</td><td>66.44</td></tr><tr><td>02-Aug-23</td><td>99.00</td><td>

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
