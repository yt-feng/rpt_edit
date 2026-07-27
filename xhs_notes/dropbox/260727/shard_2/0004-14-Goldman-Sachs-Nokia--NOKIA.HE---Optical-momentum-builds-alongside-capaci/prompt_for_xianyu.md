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
# Nokia (NOKIA.HE): Optical momentum builds alongside capacity investment progress; Neutral on valuation

EUROPE TECHNOLOGY: HARDWARE

Analysing the role of European AI enablers and

updating our view on long-term upside potential

![](images/e6def58d67f609dacee719053f09a675b8d33a8cada82ba7fb0e1d80e205a337.jpg)

Nokia reported 2Q revenue was in-line but comparable EBIT was $16 \%$ above Infront consensus data. The company classified its Fixed Wireless Access CPE and Enterprise Campus Edge business as discontinued ops. We note that had NOK not treated these as discontinued ops, sales would have been higher by €66mn but comparable EBIT would have been €13mn lower. As such, Group net sales increased by $9 \%$ yoy in cc and portfolio, driven by growth in Networks Infrastructure with Optical/IP Networks growing $20 \% / 16 \%$ yoy, respectively. Key takeaways include 1) AI and Cloud demand continues to support Optical order momentum, 2) AI-RAN pilots on track as Nokia scales internal AI adoption, 3) Optical capacity expansion progresses across Indium Phosphide and packaging, and 4) Optical & IP design wins broaden customer engagement, with revenue contribution building.

AI and Cloud demand continues to support Optical order momentum: Nokia highlighted continued strength in Optical, booking €2.8bn of orders from AI and cloud customers during the quarter, up from €1.0bn in 1Q26, representing a meaningful acceleration in demand. Importantly, management expects around half of these orders to convert into revenue over the next 12 months, providing improved near-term revenue visibility. AI and cloud remained the strongest growth driver in Q2, with net sales more than doubling yoy, supported by robust demand for data centre interconnect and scale-out networking. Beyond hyperscalers, management also noted early signs of increasing investment from telecom operators as AI-driven data traffic begins to drive additional network upgrades. Meanwhile, ongoing supply constraints across leading-edge optical components, particularly indium phosphide wafers and memory, continue to extend lead times, with customers increasingly placing longer-term orders to secure supply.

AI-RAN pilots on track as Nokia scales internal AI adoption: Management reiterated that its AI-RAN platform remains on track for pilot deployments by the end of 2026, ahead of expected commercial availability in 2027. Developed with NVIDIA, the platform is open, programmable and O-RAN compliant, and is intended to improve spectral efficiency while giving operators greater flexibility

Alexander Duval  
+44(20)7552-2995 | alexander.duval@gs.com GS International

Anant Jakhar  
+1(332)245-7829 |  
anant.x.jakhar@gs.com  
GS India SPL

Ayo Odunaiya
+44(20)7051-5995 |
ayo.x.odunaiya@gs.com
GS International

over their hardware architecture. Nokia is also extending AI adoption internally, with broad uptake across its software developer base and early evidence of productivity benefits. Together, these initiatives reflect management's continued focus on embedding AI across both its product portfolio and internal operations.

Optical capacity expansion progresses across Indium Phosphide and packaging: Nokia continues to expand its optical manufacturing footprint, including the acquisition of an NXP site in Arizona to add indium phosphide capacity. The company's San Jose fab is now processing test wafers and remains on track to begin volume production by year-end, while the planned expansion of its Pennsylvania facility is expected to increase advanced test and packaging capacity for optical systems by around tenfold. These investments are intended to address current supply constraints and provide capacity for future optical demand. Alongside this expansion, Nokia continues to reshape its portfolio and cost base. Separately, the sale of its Fixed Wireless Access business to Inseego remains on track to close by year-end, while management expects approximately €800m of restructuring charges in 2026 as it completes the 2023–26 programme and implements further efficiency measures across China and Europe.

## ■ Optical & IP design wins broaden customer engagement, with revenue

contribution building: Nokia secured its first multi-rail ILA design win with a major customer, representing initial customer adoption of one of the optical products introduced at OFC in March. Management also noted that previously announced design wins across Optical and IP Networks are beginning to translate into revenue, while reiterating its focus on product areas where it believes it can maintain differentiation. The company also expanded several customer and technology partnerships during the quarter; these included integrating Google Cloud's Gemini-powered AI agents into its autonomous networks portfolio, extending its relationship with Indosat Ooredoo Hutchison to support network modernisation and a potential transition towards AI-RAN, and conducting trials with a US hyperscaler for an out-of-band management solution using passive optical technology (ultimately reflecting ongoing customer engagement across Nokia's core networking business).

## Changes to estimates

We revise our FY26-30 revenue estimates by $-2\%$ to $0\%$ reflecting our conservative view on the growth in NOK's Mobile Infrastructure business in the near term partially offset by stronger-than-expected growth opportunities in Nokia's Optical and IP network, underpinned by strong demand for AI infrastructure and robust order intake in NOK's AI and cloud business. Our gross profit estimates change between $-2\%$ to $+2\%$ , broadly reflecting the changes to top line and gross margins affected by product mix. For comparable EBIT, our FY26-30 forecasts change by c. $-3\%$ to $+1\%$ owing to our latest assumptions on the top line, GM and opex assumptions. Finally, our FY26-30 EPS forecast changes between $-2\%$ to $-1\%$ reflecting our latest EBIT assumptions.

## Valuation and key risks

We are Neutral rated on Nokia with a 12-month price target of €8.5 / ADR \$9.7 (vs €8.9 / ADR \$10.4 prior) based on a 12x 2HCY27+1HCY28E (vs 13x prior CY27E) EV/EBITDA (incl. restructuring) applied to our updated EBITDA estimates. Our updated multiple reflects a roll forward of our valuation period. Key risks to our view include faster/slower-than-expected growth in Optical and IP Networks; incremental profitability tailwinds/headwinds in the Radio Networks segment; and better/worse-than-expected cost control and planned investments related to capacity expansion, which could pose tailwinds/headwinds to absolute EBIT in a strong/weak top-line scenario.

<table><tr><td>NOKIA.HE</td><td>12m Price Target: €8.50</td><td>Price: €8.22</td><td>Upside: 3.4%</td></tr><tr><td>NOK</td><td>12m Price Target: $9.70</td><td>Price: $9.10</td><td>Upside: 6.6%</td></tr></table>

<table><tr><td>Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: €47.7bn / $54.3bn</td><td>Revenue (€ mn) New</td><td>19,904.0</td><td>20,453.9</td><td>21,508.1</td><td>22,829.4</td></tr><tr><td>Enterprise value:</td><td>Revenue (€ mn) Old</td><td>19,904.0</td><td>20,903.2</td><td>21,893.6</td><td>22,953.2</td></tr><tr><td>€44.6bn / $50.7bn</td><td>EBIT (€ mn)</td><td>1,950.0</td><td>2,332.5</td><td>2,783.7</td><td>3,282.7</td></tr><tr><td>3m ADTV: €219.8mn / $254.5mn</td><td>EPS (€) New</td><td>0.29</td><td>0.33</td><td>0.37</td><td>0.43</td></tr><tr><td>Finland</td><td>EPS (€) Old</td><td>0.29</td><td>0.33</td><td>0.38</td><td>0.44</td></tr><tr><td rowspan="3">European Semiconductors, Hardware and Gaming Tech M&amp;A Rank: 3</td><td>EV/sales (X)</td><td>1.1</td><td>2.2</td><td>2.0</td><td>1.8</td></tr><tr><td>EV/EBITDA (X)</td><td>7.3</td><td>13.8</td><td>11.7</td><td>9.8</td></tr><tr><td>P/E (X)</td><td>15.9</td><td>25.2</td><td>22.4</td><td>19.1</td></tr><tr><td>Leases incl. in net debt &amp; EV?: No</td><td>Org. sales grth (%)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (€)</td><td>0.05</td><td>0.07</td><td>0.05</td><td>0.15</td></tr></table>

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

The rating(s) for Nokia is/are relative to the other companies in its/their coverage universe: ASM International, ASML Holding, BE Semiconductor Industries, CD Projekt, Ericsson, Infineon, Logitech, Nebius Group, Nokia, STMicroelectronics, Stillfront, Technoprobe S.p.A.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Nokia (€8.22) and Nokia (\$9.10)

GS has received compensation for investment banking services in the past 12 months: Nokia (€8.22) and Nokia (\$9.10)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Nokia (€8.22) and Nokia (\$9.10)

GS has received compensation for non-investment banking services during the past 12 months: Nokia (€8.22) and Nokia (\$9.10)

GS had an investment banking services client relationship during the past 12 months with: Nokia (€8.22) and Nokia (\$9.10)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Nokia (€8.22) and Nokia (\$9.10)

GS had a non-securities services client relationship during the past 12 months with: Nokia (€8.22) and Nokia (\$9.10)

GS makes a market in the securities or derivatives thereof: Nokia (€8.22) and Nokia (\$9.10)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/0e9225de83caa197c9a5ec602dba986a5760f06793677ee4da9618ca729b902c.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/4468e52e3588208effb157fa0a6ae56a7a2b2832f3c57ade53ced370a952e525.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

Nokia (NOK)  
Nokia (NOKIA.HE)

<table><tr><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td><td>Date of report</td><td>Target price (€)</td><td>Closing price (€)</td></tr><tr><td>27-Apr-26</td><td>10.40</td><td>10.76</td><td>27-Apr-26</td><td>8.90</td><td>9.28</td></tr><tr><td>27-Mar-26</td><td>9.20<

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
