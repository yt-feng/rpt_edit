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
# Foxconn Industrial Internet (601138.SS): Chairman & Vietnam factory tour: AI servers & switches with strong automated production; Buy

We visited FII factories during our Thailand / Vietnam Technology Tour (July 7 - 10). Management remains positive on AI capex upcycle, and highlighted their competitive advantages in strong R&D, fully automated production, comprehensive offerings (components, servers, switches), and diversified production sites. The company has been in Vietnam for over 15 years, with strong production experience, low depreciation costs, close networking across supply chain, customers, and authorities. The capacity expansion in Vietnam is ongoing, which is for AI infrastructure, requested by customers, echoing our positive view on FII's leading market position. We are positive on FII and expect it to ride on (1) AI servers ramp up: we recently raised global AI servers implied AI chips shipments by $14\%$ / $22\%$ / $14\%$ in 2026-28E, US CSP capex raised by $8\%$ / $27\%$ / $25\%$ in 2026-28E, and China CSP capex raised by $37\%$ / $44\%$ / $55\%$ in 2026-28E (Global Server TAM June updates), (2) AI server racks ongoing market share gains, with customers expansion toward NeoCloud, and rising ASIC AI servers, (3) AI servers and switch specification upgrades, along with new components opportunities, and (4) foldable iPhones: new form factor to bring new use cases, attracting consumers. Maintain Buy.

Verena Jeng  
+852-2978-1681 | verena.jeng@gs.com  
GS (Asia) L.L.C.

1. AI Capex sustainability: Management remains positive on the rising AI investments in coming years. CSP (cloud services providers), foundation model developers, Government, and Enterprise are the four types of customers who need computing power, while currently, the consumption is still mainly from CSPs, showing future upside from the other three types of customers, and the growing demand from NeoCloud is a positive signal of this expanding trend. Sovereign AI could facilitate national defense, smart city, smart transportation, smart administration, etc. and considering data security, each area would have their own data center to empower GenAI, enlarging AI data center demand. FII, as the global leader in AI servers, continue to receive strong demand from various customers, requesting for capacity. FII's capacity expansion continues, across mainland China, Vietnam, Mexico, etc.

## Key takeaways

Allen Chang  
+852-2978-2930 |  
allen.k.chang@gs.com  
GS (Asia) L.L.C.

2. Competitive advantages: Management highlights their value add is not assembly, but automated production for a customer's latest technology (NPI, new product introduction), for which FII self-designed automated production lines and equipment, facilitating customers to deliver the latest model in a timely manner with high yield rate. The NPI stage is the most difficult part, as it is from 0 to 1; however, once the fully automated production line is on, it is easy to duplicate and quickly

ramp up the production. Management highlights their focus: (1) R&D: focusing on latest technology / high-end models, leading global-tier clients relying on FII for every new product production, (2) automated production: fully automated production including testing and the final packaging and ship to warehouse, with digitalization / AI to control and monitor the quality, realizing light-off factories, (3) capacity expansion: fast duplication of the automated production lines for the latest models, to capture the strong AI infrastructure demand. FII would also continue to develop in-house components for AI servers / CPO switches to facilitate GM, and transit to consign business model to reduce working capital burden.

3. Vietnam production: Management highlights they have been in Vietnam for over 15 years, bringing them competitive production costs and rich experience of manufacturing in Vietnam. The company has five campuses in Vietnam and these production sites are the most profitable ones across the company's overseas production sites. Various products are produced in Vietnam, across consumer electronics and AI infrastructure (e.g. servers, switches), and both are in highly automated production. The high automation secures product quality, volume, and factory management, enhancing the yield rate and operation efficiency. FII also adopts generative AI and AR glasses for labour training and duplicating production lines, accelerating their capacity expansion, especially in overseas factories.

## Price Target Risks and Methodology - Foxconn Industrial Internet

Our 12M target price of Rmb107.2 is based on a 23x 2027E P/E. Our target P/E is set in line with peers' regression of P/E and forward year fundamentals (NI YoY and OPM).

Key downside risks: (1) Worse-than-expected demand and profit from the AI server business; (2) Worse-than-expected iPhone component business expansion due to strong competition; (3) Slower-than-expected capacity ramp-up in new factories; (4) Lower-than-expected iPhone shipment given FII provides components for iPhone.

<table><tr><td>601138.SS</td><td colspan="2">12m Price Target: Rmb107.20</td><td colspan="2">Price: Rmb66.27</td><td colspan="2">Upside: 61.8%</td></tr><tr><td colspan="2">Buy</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="9" colspan="2">Market cap: Rmb1.3tr / $194.0bn Enterprise value: Rmb1.3tr / $190.4bn 3m ADTV: Rmb16.3bn / $2.4bn China Greater China Technology M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: No</td><td>Revenue (Rmb mn)</td><td>902,887.2</td><td>1,575,387.0</td><td>2,530,626.1</td><td>3,852,806.9</td></tr><tr><td>EBITDA (Rmb mn)</td><td>50,575.0</td><td>84,990.7</td><td>116,021.8</td><td>155,385.3</td></tr><tr><td>EPS (Rmb)</td><td>1.78</td><td>3.18</td><td>4.66</td><td>6.34</td></tr><tr><td>P/E (X)</td><td>21.1</td><td>20.9</td><td>14.2</td><td>10.5</td></tr><tr><td>P/B (X)</td><td>4.4</td><td>6.7</td><td>5.5</td><td>4.5</td></tr><tr><td>Dividend yield (%)</td><td>2.6</td><td>2.6</td><td>3.9</td><td>5.3</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>(0.1)</td><td>(0.3)</td><td>(0.3)</td><td>(0.2)</td></tr><tr><td>CROCI (%)</td><td>21.5</td><td>35.2</td><td>40.1</td><td>44.0</td></tr><tr><td>FCF yield (%)</td><td>(1.6)</td><td>4.2</td><td>4.3</td><td>5.5</td></tr><tr><td colspan="2"></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td colspan="2"></td><td>EPS (Rmb)</td><td>0.53</td><td>0.75</td><td>0.90</td><td>1.00</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 10 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Verena Jeng and Allen Chang, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Verena Jeng GS (Asia) L.L.C., Allen Chang GS (Asia) L.L.C..

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

The rating(s) for Foxconn Industrial Internet is/are relative to the other companies in its/their coverage universe: AAC, ACM Research, AMEC, ASMPT, AVC, AccoTest, Anji Micro, Asus, Auras, BOE, BYDE, Biren, CR Micro, Cambricon, Chenbro, China Mobile (HK), China Telecom, China Tower Corp., China Unicom, Chinasoft Intl, Compal, Desay SV, E Ink, E-Town Semis, EHang, Empyrean, Eoptolink, FOCI, Fositek, Foxconn Industrial Internet, Gigabyte, Gigadevice, Glodon Co., HTC Corp., Hikvision, Hon Hai, Horizon Robotics, Hua Hong, Huace Navigation, Huaqin Co.(A), Huaqin Co.(H), Hwatsing, InnoScience, Innolight, Inspur, Insta360, Inventec, JCET, Kematek, King Slide, Kingdee, Kingsoft Office, LandMark, Largan, Lenovo, Lingyi, Maxscend, Meitu, MetaX, Mitac, Montage (A), Montage (H), NAURA, NSIG, Nexchip, OmniVision, Pegatron, Pony AI Inc. (ADR), Pony AI Inc. (H), Quanta, RoboTechnik, Ruijie Networks, SG Micro, SICC, SMIC (A), SMIC (H), SZS, Sangfor, SenseTime, Shengyi Tech, Shennan Circuits, StarPower, Sunny Optical, TFC Optical, Thundersoft, Tongyu Communication, Transsion, UMT, UNIS, VPEC, Vanchip, VeriSilicon, Victory Giant, WNC, WUS, WeRide, Wistron, Wiwynn, YJ Semitech, YOFC, Yonyou, ZTE (A), ZTE (H), iFlytek

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Foxconn Industrial Internet (Rmb66.27)

GS has received compensation for non-investment banking services during the past 12 months: Foxconn Industrial Internet (Rmb66.27)

GS had an investment banking services client relationship during the past 12 months with: Foxconn Industrial Internet (Rmb66.27)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Foxconn Industrial Internet (Rmb66.27)

GS had a non-securities services client relationship during the past 12 months with: Foxconn Industrial Internet (Rmb66.27)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/5720bf512c3fbc1c47513d18014f58fa18bc8a0cad4f4df619101b5c715aaed4.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Foxconn Industrial Internet (601138.SS)

Date of report Target price (Rmb) Closing price (Rmb)

<table><tr><td>23-Jun-26</td><td>107.20</td><td>74.10</td></tr><tr><td>16-Apr-26</td><td>93.90</td><td>59.32</td></tr><tr><td>30-Nov-25</td><td>92.90</td><td>60.72</td></tr><tr><td>29-Oct-25</td><td>95.50</td><td>80.80</td></tr><tr><td>15-Oct-25</td><td>83.80</td><td>63.38</td></tr><tr><td>18-Sep-25</td><td>77.20</td><td>64.36</td></tr><tr><td>05-Sep-25</td><td>68.30</td><td>55.83</td></tr><tr><td>17-Aug-25</td><td>59.50</td><td>44.86</td></tr><tr><td>09-Jul-25</td><td>31.11</td><td>26.60</td></tr><tr><td>28-Jun-25</td><td>27.20</td><td>21.35</td></tr><tr><td>28-Apr-25</td><td>23.80</td><td>18.00</td></tr><tr><td>06-Apr-25</td><td>24.70</td><td>19.05</td></tr><tr><td>24-Mar-25</td><td>25.00</td><td>20.84</td></tr><tr><td>23-Feb-25</td><td>28.61</td><td>23.20</td></tr><tr><td>09-Feb-25</td><td>25.84</td><td>21.55</td></tr><tr><td>31-Jan-25</td><td>26.49</td><td>21.45</td></tr><tr><td>13-Jan-25</td><td>28.52</td><td>19.72</td></tr><tr><td>03-Nov-24</td><td>29.95</td><td>23.68</td></tr><tr><td>05-Aug-24</td><td>34.20</td><td>20.42</td></tr><tr><td>28-May-24</td><td>36.54</td><td>24.12</td></tr><tr><td>15-Apr-24</td><td>32.33</td><td>22.24</td></tr><tr><td>15-Mar-24</td><td>32.13</td><td>23.08</td></tr><tr><td>08-Mar-24</td><td>32.44</td><td>24.87</td></tr><tr><td>05-Jan-24</td><td>29.03</td><td>13.30</td></tr><tr><td>30-Oct-23</td><td>31.61</td><td>14.60</td></tr><tr><td>15-Aug-23</td><td>31.61</td><td>21.39</td></tr><tr><td>09-Aug-23</td><td>31.61</td><td>22.25</td></tr><tr><td>01-Aug-23</td><td>31.35</td><td>22.67</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws an

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
