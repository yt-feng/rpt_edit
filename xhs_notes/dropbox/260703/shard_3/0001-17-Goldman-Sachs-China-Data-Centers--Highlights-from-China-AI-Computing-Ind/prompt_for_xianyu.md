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
# China Data Centers: Highlights from China AI Computing Industry Ecological Development Conference

We recently attended the China AI Computing Industry Ecological Development Conference, where representatives from a variety of industry players (e.g. data center operators, hyperscalers, token routing platforms) and independent research institutes (e.g. CAICT, KZ Consulting) delivered presentations. Key topics included national computing power network, GW-scale data center clusters, domestic chip ramp-up and limitations, token operations, etc.

GS takes: We think China's national computing power network may reshape the competitive landscape and geographic footprint of the China data center industry over the next 5 years; in other words, capital and technology are heavily shifting toward Western China hubs, while the value proposition of tier-1 city data centers is shifting toward ultra-low latency hot compute, edge nodes and AI inference. The emergence of GW-scale computing power clusters implies higher technology and resource barriers and provides differentiation among data center operators. Within our China data center coverage, we are Buy rated on VNET, GDS and Range Intelligent, Neutral rated on Shanghai Athub, and Sell rated on Beijing Sinnet.

We summarize key highlights from the conference below.

## Computing power network

Computing power network as part of China's core infrastructure construction project in 2026-30: China's "six major networks", including the water network, new-type power grid, computing power network, next-generation communication network, urban underground pipe network, and logistics network, will attract Rmb7tn investments in 2026 as per NDRC, and Bloomberg reported on Jun 9 that China is to spend c.Rmb2tn (US\$300bn) over the next 5 years in data center investments (GS note).

Computing power network architecture: 1) Computing-networking infrastructure layer that integrates heterogeneous compute with high-speed transmission via RDMA (Remote Direct Memory Access) and elastic networks; 2) Interconnection resource layer driven by a “1+M+N” node hierarchy i.e. 1 national public computing-networking service platform, M regional platforms, and N industry platforms; 3) Application service layer. Hence, wide-area data transmission and long-distance RDMA, and cross-domain orchestration platforms are key capabilities; currently, out of 1.1k+ computing nodes and 110+ scheduling platforms, only 10% possess cross-domain orchestration capabilities,

Timothy Zhao  
+852-2978-2673 |  
timothy.zhao@gs.com  
GS (Asia) L.L.C.

Ronald Keung, CFA +852-2978-0856 | ronald.keung@gs.com GS (Asia) L.L.C.

Eunice Liu  
+852-2978-7472 | eunice.liu@gs.com  
GS (Asia) L.L.C.

as per CAICT.

## GW-scale data center clusters

Foundation of a GW-scale data center clusters lies in network architecture as increasing switch port counts from 65 to 144 ports require higher individual network capacity. While there have been a number of operational GW-scale clusters in operation in the US (e.g. Project Rainier), computing clusters composed of $100\mathrm{k}+$ chips remain scarce in China.

Breakthrough of 200MW data centers in China: Range Intelligence (300442.SZ, Buy) has brought a 200MW, 100k chip-scale data center building operationally YTD, as part of its GW-scale computing cluster on a 500 mu (0.3 sqkm) land parcel, and sees a 400MW data center theoretically feasible to implement.

Computing power economics gap between domestic chips and imported chips remain big (Exhibit 1). While capex per IT power for domestic chips is $40 - 50\%$ lower than imported chips, computing power related efficiency metrics lag e.g. capex per computing power is 2-4x and computing power per IT power is $10 - 30\%$ vs. imported chips.

Exhibit 1: Capex per 200MW IT power data center based on different IT infrastructure

<table><tr><td>Capex per 200MW IT power data center</td><td>Nvidia B300</td><td>Huawei CM384</td><td>Panjiu 2.0</td></tr><tr><td>Computing power (EFLOPS, FP16)</td><td>250</td><td>80</td><td>40</td></tr><tr><td>Total IT power (kW)</td><td>187,500</td><td>208,800</td><td>234,600</td></tr><tr><td>Servers/supernodes</td><td>12,500</td><td>261</td><td>782</td></tr><tr><td>IT power per unit</td><td>15</td><td>800</td><td>300</td></tr><tr><td>Total capex (Rmb bn)</td><td>61.0</td><td>41.0</td><td>41.5</td></tr><tr><td>Land</td><td>0.05</td><td>0.05</td><td>0.05</td></tr><tr><td>Land area (mu)</td><td>100</td><td>100</td><td>100</td></tr><tr><td>Land cost (Rmb k/mu)</td><td>500</td><td>500</td><td>500</td></tr><tr><td>Building construction</td><td>0.90</td><td>0.90</td><td>0.90</td></tr><tr><td>GFA (k sqm)</td><td>200</td><td>200</td><td>200</td></tr><tr><td>Cost per GFA (Rmb k/sqm)</td><td>4.5</td><td>4.5</td><td>4.5</td></tr><tr><td>Electrical equipment</td><td>3.8</td><td>4.8</td><td>5.4</td></tr><tr><td>Cost per IT power (Rmb k/kW)</td><td>20</td><td>23</td><td>23</td></tr><tr><td>Servers/supernodes</td><td>56.3</td><td>35.2</td><td>35.2</td></tr><tr><td>Unit cost (Rmb mn)</td><td>4.5</td><td>135.0</td><td>45.0</td></tr><tr><td>Capex per IT power (Rmb bn/GW)</td><td>325</td><td>196</td><td>177</td></tr><tr><td>Capex per computing power (Rmb bn/EFLOPS)</td><td>0.24</td><td>0.51</td><td>1.04</td></tr><tr><td>Computing power per IT power (EFLOPS/GW)</td><td>1,333</td><td>383</td><td>171</td></tr></table>

Source: Company data

Exhibit 2: Typical workload distribution for a GW-level campus  
![](images/71ee8b20bbb981a52dad41e073b805d9da776078d8ee2cca9120afb4e02124e8.jpg)  
Source: Company data

## Domestic chips

\- Imported computing power remains dominant among CSPs: As per CAICT, 70-90% of outstanding computing power of major CSPs (each with operational computing power 2.2-4.5 PFLOPS) in China is based on imported chips.

Domestic AI accelerator chip ramp-up: As per KZ Consulting, domestic AI accelerator chip shipments may exceed $50\%$ market share in 2026 in China, with Huawei and T-Head leading the domestic market share. Internet companies and government entities appear to be the biggest customers of domestic chips, with internet companies accounting for $63\% / 23\% / 60\% / 30\%$ of

Huawei/T-Head/Cambricon/Hygon shipments in 2026, and government entities accounting for $15\% / 15\% / 35\%$ of Huawei/Cambricon/Hygon shipments in 2026.

Gap between domestic and imported chips on token efficiency and profitability: As per CAICT, domestic chips remain lagging behind foreign peers in performance, cost and ecosystem, which constrain token output efficiency (Exhibit 5) and efficiency (Exhibit 6).

Exhibit 3: Domestic AI accelerator chip shipments are expected to exceed 50% market share in 2026
China AI accelerator chip shipments: domestic vs. imported  
![](images/46220088ffaeeee3f84cd3ec11150972131178915ce7cf5be406f52a6706514b.jpg)  
Source: KZ Consulting

Exhibit 4: Huawei and T-Head are expected to lead domestic AI accelerator chip shipments in 2026 China AI accelerator chip shipment share in 2026  
![](images/1c563aebc9eac7d5c9b3e74b4dd56adbe250b1aa2f42aa8ab7f2084eb1e748ee.jpg)  
Source: KZ Consulting

Exhibit 5: Huawei 910B/910C token output volume is 1/6-1/3 of that of Nvidia H800 servers  
Average daily token output per server for typical tasks (mn)  
![](images/8c247acddce22bab07addd396aebf3bfb992f3f5d4153f9955e1b423d5a7c0fe.jpg)  
Source: CAICT

Exhibit 6: Profit margins of tokens/APIs based on Huawei 910B servers lag behind that on Nvidia H800
Illustration: Profit margin by IT infrastructure  
![](images/9cfdfc7a1e14d4bd62cd24ff77619e0d93004e36e6b5744ed8290e53a8b024ef.jpg)  
Source: CAICT

## Token operations

\- Token pricing divergence: Against the backdrop of the “impossible triangle” between intelligence, cost and quality (i.e. low latency, high concurrency, high availability), the token pricing trend appears to diverge. This is also related to business model variations as competition is evolving from single model breakthroughs to ecosystems.

\- Token export: 1) Shantou City is leveraging its “Inbound Data Processing” policy to build China’s first city-level practice for token export, with advantages in its submarine cable connectivity and abundant offshore wind power resources; 2) Key applications currently involve AI toys and AI short-form videos, while cross-border digital employee may represent a future business model.

## Disclosure Appendix

## Reg AC

I, Timothy Zhao, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Timothy Zhao GS (Asia) L.L.C., Ronald Keung, CFA GS (Asia) L.L.C., Eunice Liu GS (Asia) L.L.C..

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

## Pricing information

Beijing Sinnet Technology Co Ltd. (Rmb13.77), GDS Holdings (ADR) (\$31.61), Range Intelligent (Rmb90.06), Shanghai Athub (Rmb25.80) and VNET Group (\$8.81)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States
The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of i

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
