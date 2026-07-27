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
# STMicroelectronics (STMPA.PA): Improving demand visibility, with AI datacentres & optical connectivity the key growth drivers

EUROPE TECHNOLOGY: HARDWARE
Analysing the role of European AI enablers and updating our view on long-term upside potential

Explore >

![](images/cb28e3c761c3283c9d1dd51126c4cb8d18f9eaf338573df2a8e157dc6a152966.jpg)

Alexander Duval
+44(20)7552-2995 |
alexander.duval@gs.com
GS International

STM's 2Q26 revenue came 1% above Visible Alpha Consensus Data, primarily due to higher revenues from Automotive and CECP. Further, reported EBIT came in 20% below consensus, affected primarily by a \$58mn impairment, restructuring expenses and other related phase-out costs and a \$24mn headwind related to PPAs from the acquisition of NXP's MEMS business. Excluding the impact of these, the company's EBIT of \$269mn would have been 15% above consensus. Key takeaways include 1) Improving demand visibility and AI datacentre momentum underpin growth outlook, 2) Expected sequential margin improvement, though reshaping costs remain a near-term headwind, 3) Demand momentum broadens as inventory normalises and supply tightens, and 4) 300mm capacity ramp continues to support future MCU and AI growth against a tightening supply backdrop. Remain Neutral.

Improving demand visibility and AI datacentre momentum underpin growth outlook: STM guided 3Q26 revenues of \$3.7bn at the midpoint, c.2% below consensus, while indicating that 4Q26 revenue should exceed \$4bn (vs. consensus of \$4.03bn), implying FY26 revenue broadly in line with street expectations. Importantly, management highlighted a continued improvement in demand, with book-to-bill close to 2x overall and above 2x in optical interconnect. Customer visibility also continues to strengthen, with well over half of Q2 bookings scheduled for delivery next year and backlog now representing c.4.5–5 quarters of Q2 revenue. AI datacentres remain the primary growth driver, with STM raising its datacentre revenue outlook to >\$1bn in 2026 and well above \$2bn in 2027, supported by sustained demand across AI infrastructure. Growth is expected to be driven by 800G and 1.6T pluggable optics, where the company continues to benefit from leading positions in microcontrollers, increasing share in integrated circuits and the ramp of silicon photonics for optical interconnects. Management also highlighted meaningful manufacturing scalability in silicon photonics, while noting that FY26 datacentre revenues are already fully covered by backlog and FY27 expectations are supported by existing customer engagements. We note that the Datacentre business continues to be gross margin accretive to group topline; we see the aforementioned commentary on

Anant Jakhar  
+1(332)245-7829 |  
anant.x.jakhar@gs.com  
GS India SPL

Ayo Odunaiya
+44(20)7051-5995 |
ayo.x.odunaiya@gs.com
GS International

strong AI demand and strong booking as a positive for power semis peer IFX.

Expected sequential margin improvement, though reshaping costs remain a near-term headwind: Gross margin included a c.60bp headwind from non-recurring costs associated with STM's manufacturing reshaping programme, with management expecting a similar impact through the remainder of the year. The programme involves transferring silicon production from 200mm to 300mm and silicon carbide production from 150mm to 200mm, with completion not expected before the end of 2027. During the transition, gross margin will continue to be affected by costs related to technology transfers, product qualifications and mask redesigns. That said, the company guided to a 3Q26 non-GAAP gross margin of $37\%$ at the midpoint, representing a sequential improvement, and expects further progress in 4Q as revenue scales. The pace of recovery will be moderated by continued underloading charges, including start-up costs at new fabs, particularly in China, as well as ongoing expenses linked to the manufacturing transfer programme. Overall, management remains confident that gross margin will improve sequentially in 4Q, albeit with these headwinds continuing to constrain the extent of the uplift.

Demand momentum broadens as inventory normalises and supply tightens: STM highlighted a clear acceleration in demand, with improved visibility, signs of supply tightness across several product categories and distribution inventories now below normal target levels. The recovery is particularly evident in general-purpose microcontrollers and analog, supported by stronger POS (point-of-sale) trends, while SiC also continued to improve, with low-teens yoy growth, mid-30%s sequential growth and a book-to-bill well above one. By end market, communications equipment and computer peripherals remain the strongest growth drivers, with revenue expected to grow by c.60% yoy in 3Q and accelerate to c.90% in 4Q. Industrial growth should also strengthen from 32% in 2Q to close to 40% by 4Q, while automotive is tracking ahead of prior expectations at LDD% growth. Personal electronics remains the outlier, with management expecting a negative 2H yoy following the positive 1H, though full-year should remain in the LSD/MSD% range.

300mm capacity ramp continues to support future MCU and AI growth against a tightening supply backdrop: STM noted some lengthening in lead times and pockets of capacity constraint, including at OSAT partners, although management views these pressures as temporary and partly related to the ongoing manufacturing reshaping programme. The Agrate 300mm fab is expected to reach full build-out before 2028 and begin supporting microcontroller growth once 90nm and 40nm technologies are qualified, while Crolles is set to ramp towards 15,000 wafers per week and expand further in-line with AI datacentre demand. In China, qualification of 40nm technology with a local manufacturing partner should also increase available capacity for domestic industrial and optical transceiver customers.

## Changes to estimates

We raise our FY26-30 revenue estimates by 3-5% (in \$ terms) to reflect the continued strong growth in STM's AI business as well as in its ADAS exposure. Further, our FY26-30 GP estimates change between 1% to 5% due to our higher topline assumptions, but are partially offset by under utilisation charges as well as costs associated with manufacturing capacity transition. As such, our FY26-30E EBIT changes between -1% to +6% (in \$ terms) reflecting our latest topline, GMs and opex assumptions Finally, our EPS changes between -2% and +7% (in \$ terms) across our forecast period due to our EBIT and latest share count assumptions.

## Valuation and key risks

We are Neutral rated on STMicro, with our 12-month price targets of €53.0/ADR \$60.5 (vs €58.0/ADR \$67.5 prior) based on a 11x 2HCY27+1HCY28E (vs 13x CY27 prior) EV/EBITDA multiple applied to updated EBITDA estimates. As such our updated valuation multiple reflects a roll forward our valuation period. Key risks to our view and price targets include a quicker/slower-than-expected inventory correction trough in consumer semis, accelerating/slowing Silicon Carbide momentum at competitors and evidence that currently favourable pricing can be sustained.

<table><tr><td>STMPA.PA</td><td>12m Price Target: €53.00</td><td>Price: €46.77</td><td>Upside: 13.3%</td></tr><tr><td>STM</td><td>12m Price Target: $60.50</td><td>Price: $51.54</td><td>Upside: 17.4%</td></tr></table>

<table><tr><td>Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: €43.1bn / $49.0bn</td><td>Revenue (€ mn) New</td><td>10,171.6</td><td>12,341.3</td><td>14,353.1</td><td>16,164.7</td></tr><tr><td>Enterprise value:</td><td>Revenue (€ mn) Old</td><td>10,171.6</td><td>12,055.9</td><td>13,907.7</td><td>15,659.9</td></tr><tr><td>€44.4bn / $50.5bn</td><td>EBIT (€ mn)</td><td>150.9</td><td>1,034.9</td><td>2,054.4</td><td>2,970.5</td></tr><tr><td>3m ADTV: €198.3mn / $229.2mn</td><td>EPS (€) New</td><td>0.16</td><td>1.05</td><td>2.01</td><td>2.88</td></tr><tr><td>France</td><td>EPS (€) Old</td><td>0.16</td><td>0.98</td><td>2.05</td><td>2.90</td></tr><tr><td rowspan="3">European Semiconductors, Hardware and Gaming Tech M&amp;A Rank: 3</td><td>EV/sales (X)</td><td>2.1</td><td>3.5</td><td>3.1</td><td>2.6</td></tr><tr><td>EV/EBITDA (X)</td><td>11.9</td><td>16.2</td><td>11.5</td><td>8.8</td></tr><tr><td>P/E (X)</td><td>145.4</td><td>43.7</td><td>23.3</td><td>16.3</td></tr><tr><td>Leases incl. in net debt &amp; EV?: No</td><td>Org. sales grth (%)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td></td><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td></td><td>EPS (€)</td><td>0.21</td><td>0.34</td><td>0.47</td><td>-</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 24 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Alexander Duval, Anant Jakhar and Ayo Odunaiya, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Alexander Duval GS International, Anant Jakhar GS India SPL, Ayo Odunaiya GS International.

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

The rating(s) for STMicroelectronics is/are relative to the other companies in its/their coverage universe: ASM International, ASML Holding, BE Semiconductor Industries, CD Projekt, Ericsson, Infineon, Logitech, Nebius Group, Nokia, STMicroelectronics, Stillfront, Technoprobe S.p.A.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: STMicroelectronics (\$51.54) and STMicroelectronics (\€46.77)

GS has received compensation for investment banking services in the past 12 months: STMicroelectronics (\$51.54) and STMicroelectronics (€46.77)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: STMicroelectronics (\$51.54) and STMicroelectronics (€46.77)

GS had an investment banking services client relationship during the past 12 months with: STMicroelectronics (\$51.54) and STMicroelectronics (€46.77)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: STMicroelectronics (\$51.54) and STMicroelectronics (€46.77)

GS had a non-securities services client relationship during the past 12 months with: STMicroelectronics (\$51.54) and STMicroelectronics (€46.77)

GS makes a market in the securities or derivatives thereof: STMicroelectronics (\$51.54) and STMicroelectronics (€46.77)

Distribution of ratings/investment banking relationships GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/2d45e491022af2c56653eaac404e914b41e653bfd0dbd37f4799b57636d72d7b.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/e734f6e61ea6de

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
